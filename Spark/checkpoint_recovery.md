## Problem Statement

Whenever there is a Failure in the structured streaming app, the developer fixes the issue by getting into the checkpoint directory, picks the checkpoint at CURRENT-3 position from offsets, feeds the offsets as app starting offset and restarts the application. Automate this process.

## Premise

### How does a structured streaming start when triggered.
1. Based on the trigger time, the application, at the start, checks the checkpoint directory for any previously committed offsets.
2. If there are any offsets, the application will try to start the stream from that offset.
3. If the checkpoint directory is empty, then it proves the this is fresh start of the application and the streaming will start from either "latest" or "earliest" offset as specified by the developer.

### What happens when the app fails.
1. While the application is running, the committed offsets will be written to the checkpoint directory.
2. If the application has failed and the restart is attempted within the threshold time (say <= 10 mins), the application can start from last committed offset with a simple app restart. This can work since the data has not started leaking out from last committed offset.
3. If the application has failed and the restart is attempted after the threshold time (say >= 1hour), then a simple restart will not work as the data will has started to leak out from the last committed offset.
4. Lets say that the offsets are not available at the topic due to expiry of retention policy then the entire data has to be replayed at the source from earliest offset.

### Understanding the Issue with Restarting from the Last Committed Offset
In Spark Structured Streaming, the checkpoint directory maintains fault tolerance by storing offset logs (write-ahead logs) and commit logs. Offsets are written at the start of a micro-batch to record the data range to process, while commits are written only after successful processing and output. Normally, on failure and restart, the query resumes from the last committed batch (e.g., batch N-1 if batch N failed mid-way). However, your described behavior—repeated failures from the last committed offset (N), requiring manual rollback to N-2 or N-3—typically stems from orphaned offset files after a partial failure.
Root Cause

During a micro-batch (e.g., batch N), Spark writes an offset file to the offsets/ subdirectory in the checkpoint, capturing the input data range and metadata like maxFilesPerTrigger or spark.sql.shuffle.partitions.
If the batch fails after this write but before completion (e.g., due to task failure, output sink error, or data volume exceeding limits), the offset file persists, but no corresponding commit file is created in the commits/ subdirectory.
On restart, Spark detects the uncommitted offset for batch N and retries it automatically using the stale metadata in that offset file (e.g., old batch size limits). If the retry fails again—often because the data volume is too large for the retained config, or external factors like source unavailability—the loop continues, causing the restart to "fail" from what appears to be the last committed point.
This creates a mismatch: the offsets/ folder is ahead of commits/ (e.g., offsets up to N, commits up to N-1), and retries ignore new configs or changes, forcing manual intervention.

This is a known behavior in Spark (observed in versions like 3.x), especially in environments like Databricks or when using file-based sources/sinks.
Why Manual Rollback Works
By manually deleting the orphaned offset file(s) for batch N (and sometimes N-1 if chained failures occur), you allow Spark to fall back to the last valid commit (e.g., N-2 or N-3). This starts a fresh micro-batch from the committed position, applying current configs and avoiding retry loops.
Solutions and Workarounds

# Immediate Recovery:

Stop the query.
Inspect the checkpoint: Use dbutils.fs.ls("<checkpoint-path>/offsets") (in Databricks) or hdfs dfs -ls <path>/offsets to list files. Identify the highest-numbered offset file (e.g., 42.json) without a matching commit in <checkpoint-path>/commits.
Backup the file externally.
Delete the orphaned offset file(s).
Restart the query—it will resume from the last commit.


# Preventive Measures:

Tune Batch Sizes Proactively: Set conservative maxFilesPerTrigger or maxBytesPerTrigger to reduce failure likelihood during retries. Monitor via query progress logs.
Use Idempotent Sinks: Ensure outputs (e.g., Delta, Kafka) support exactly-once semantics to minimize retry impacts.
Automate Cleanup: Script checks for offset-commit mismatches (e.g., via cron jobs scanning the checkpoint) and delete orphans before restarts.
Separate Checkpoints: Avoid reusing checkpoints across environments or major code changes—delete and recreate if upgrading Spark/configs, using startingOffsets for precise control.
Capture Offsets Externally: Implement a StreamingQueryListener to log starting/ending offsets to a DB/file, allowing manual startingOffsets overrides on restart if checkpoints corrupt.


## Solution

### Restart within the threshold.
   When prompted about the failure, restart the application immediately before leak.

### Auto-Restart after the threshold.
1. Since the app first checks for previously committed offsets before the application starts, the previously committed offsets have to backed up.
2. Programmatically pick the latest offset at current-3 position and save it in the app start config. This is necessary to ensure that the right offset is chosen to avoid data leak.
3. Set the kafka.start.offset property with the saved offsets from the config.
4. Now clean the checkpoint directory to ensure that the application considers this as a fresh start with the previously fed offsets.
5. The app will now start the streaming with the stable offsets ensuring 0 data loss.



