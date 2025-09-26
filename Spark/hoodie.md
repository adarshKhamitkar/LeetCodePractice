✦ Of course. Uber is a major contributor to and user of Apache Hudi, so they will have high standards. I will tailor my questions to reflect the challenges
  of large-scale, low-latency data lake management that a company like Uber faces.

  Let's begin.


  To start, what fundamental problem in the data lake ecosystem was Apache Hudi designed to solve? Describe its two core table types, Copy on Write (CoW)
  and Merge on Read (MoR), and explain the primary trade-offs you would consider when choosing between them.

> Okay. Unlike traditional RDBMS which supports Row-level record updates, Apache Hive was designed for File-level record updates in a Distributed File 
  system. As in, instead of one record, a bulk of records were supposed to be updated. Some of these records might needed an update and some of them did not
   expect any updates. Uber is a system which prioritizes Consistency of the data and low-latency. Hence a team in Uber designed Apache Hudi which 
  guaranteed ACID compliance along with file-based updates. Hudi does this by writing all the inserts and updates to an entirely different set of files 
  called as Delta files. Whereas, the files where the actual data for the table is stored are called as Base Files. With that feature, Hudi offers 2 kinds 
  of tables, Copy-on-Write tables and Merge-on-Read tables. Both of these kind serve a different use-case altogether. Copy-on-Write tables, merge the delta 
  files of every batch with base files during write operation. The CoW tables guarantee complete consistency of the data and also they offer low-latency for
   Analytical queries. CoW tables are preferred for read-intensive application. The Merge-on-Read table on the other hand are used for write intensive use 
  cases as the delta files will be merged with the base files through a separate process called compaction. Because of this nature, MoR tables focus on 
  eventual consistency and low latency for data writes.

✦ That's a solid start. You've correctly identified the core problem—enabling record-level updates and deletes in a data lake—and you have a good grasp of
  the fundamental difference between CoW and MoR.


  You mentioned that for CoW, Hudi merges the delta files with the base files during the write operation. Let's get more precise.


  For a Copy on Write table, if you have an update for a single record that resides in a 128MB Parquet base file, what does Hudi do under the hood to
  apply that update? What is the "copy" in "Copy on Write," and what are the performance implications of this process, especially for write-heavy
  workloads?

> Since the delta files are getting merged with the base files during the write operation itself, the performance of writes for CoW tables expects a 
  certain amount of Latency. Considering the example of a single record in the file of 128MB parquet base file having updates, during the merge, the 
  update/insert records will be copied from delta files to table base files during write operation, hence the name copy-on-write. During update, based on 
  the specified record-key and pre-combine fields, the records from delta files will be merged with base files. Once these 2 process are complete, a CLEAN 
  operation running in the background will clean-up all these used delta files marking the overall status from INFLIGHT to COMPLETED.

✦ You're on the right track with the merge process, but let's clarify the most critical detail of Copy on Write.


  You said, "the update/insert records will be copied from delta files to table base files." This is true for MoR, but not exactly for CoW. In CoW, there
  are no separate delta files for updates; the changes are applied directly during the write commit.


  Let me rephrase the question to be more specific: When an update for a record comes in for a CoW table, Hudi identifies the base file containing that
  record. What happens to that specific base file? Does Hudi modify it in place? What does it create?

> Thank you for identifying the flaw in my response. For CoW tables, the updates/inserts will be directly copied/applied to the base files while write 
  operation itself. The process is straight forward for inserts. But, for updates, Hudi does not modify the records in-place, instead it creates new base 
  files and file-groups also with previously existing un-touched records, newly inserted records and updated records. The previous base files are marked 
  DELETE and are cleaned-up by CLEAN operation.

✦ Exactly. You've nailed the critical concept. Hudi does not modify files in place. It finds the base file that contains the record to be updated, and
  rewrites the entire file with the updated record included. This is the "copy" in Copy on Write—copying all the old data plus the new change into a new
  version of the file.

  This mechanism has a significant "write amplification" cost, as a single 1KB update can cause 128MB of data to be rewritten.


  Now, this leads to a crucial performance question. In a petabyte-scale table at Uber with millions of Parquet files, how does Hudi efficiently find
  which of those millions of files contains the specific record you want to update? What mechanism does it use to avoid a full table scan for every
  incoming batch of updates, and can you describe a few different implementations of this mechanism?

> There are few implementation mechanisms to avoid full table scans. Some of them are controlled/implemented by the developers, they are, Partitioning and 
  Bucketing. Hudi applies few search optimization metrics through indexing the data. The developers, while creating the tables can specify the efficient 
  single-level or multi-level partitions by using columns such as calendar_date, company_cd, etc.,. If such columns are not available in the table then the 
  developer apply bucketing, aka, range-partitioning through clustering the table based on any columns which has sequentially increasing numbers or 
  alpha-numeric characters. Hudi applies various indexing strategies such as Simple Index, Bloom Index, GLOBAL_BLOOM Index and Record_level_index.

✦ You've correctly listed several relevant concepts: partitioning, clustering (which Hudi calls bucketing in some contexts), and the different index types.
  That's a great overview.

  Let's focus on the indexing part, as it's the primary mechanism for locating records. You mentioned Bloom Index and Global Bloom Index.


  Could you explain how a Bloom Index works in Hudi? Then, describe the fundamental difference between a regular Bloom Index and a Global Bloom Index.
  What specific problem does the Global Bloom Index solve, and what is its primary drawback, especially at Uber's scale?

> I am not aware of how indexes work in Apache Hudi, can you put a detailed explanation and help prepare better for this question.

✦ Of course. This is a critical concept for Hudi, so let's walk through it in detail. It's essential for understanding Hudi's performance.


  The fundamental purpose of a Hudi index is to answer one question quickly: "For this incoming record key, which file group does it belong to?"

  Without an index, Hudi would have to scan every data file to find the location of records you want to update, which is impossible at scale.

  1. Bloom Index (The Default)


  A Bloom filter is a special, space-efficient data structure. You can ask it if an item is part of a set. It will tell you one of two things:
   * "No, this item is definitely not in the set."
   * "Yes, this item might be in the set." (It can have false positives).


  How Hudi Uses It:
   1. Hudi maintains a Bloom filter of all the record keys that exist within each individual data file. This small Bloom filter is stored in the footer of
      the Parquet file itself.
   2. When a batch of updates arrives, Hudi first uses the partition path to identify the specific folder to look in.
   3. Then, for each incoming record, Hudi reads the footers of all files within that partition and checks their Bloom filters.
   4. If a file's Bloom filter says the record key "might be" present, Hudi adds that file to a candidate list. If it says "definitely not," Hudi ignores
      that file completely.
   5. Finally, Hudi only needs to scan the small list of candidate files to find the exact location of the record.


  Limitation: This index is scoped to a partition. It only works if the partition value of a record never changes. If a record's partition key changes,
  Hudi will look in the new partition, won't find the old record, and will incorrectly create a duplicate.

  ---

  2. Global Bloom Index

  This is where the Global Bloom Index comes in.


  Problem it Solves: It handles cases where a record's partition value might change. For example, at Uber, maybe a trip's city_id (the partition key) is
  corrected from san_francisco to oakland. A standard Bloom index would fail here.


  How it Works:
   1. Instead of checking files within a partition, the Global Bloom Index maintains a single, table-wide index. This index maps every record key in the
      entire table to its corresponding partition path.
   2. This global index is itself stored as a separate Hudi Merge-on-Read table.
   3. When an update arrives, Hudi first does a lookup against this global index table to find the correct partition path for the record key.
   4. Once it has the correct partition path, it can proceed to find the specific file within that partition.


  Primary Drawback (Crucial for Uber's Scale):
  The global index is a single source of truth for the entire table. Every single write operation, no matter which partition it's for, must also update
  this centralized index. This creates a massive write bottleneck. As your ingest volume grows into billions of events per day, all writes have to
  contend for locks to update this one global index table, which is extremely difficult to scale.

  So, the trade-off is: Global Bloom gives you global uniqueness enforcement at the cost of significantly reduced write scalability. For this reason,
  it's often avoided in hyper-scale scenarios.


  Does this distinction between a partition-scoped index and a global index make sense?

> yes

✦ Excellent. Now let's apply this to a practical, large-scale problem.


  Imagine you are designing a core data lake table at Uber for driver location events.
   * Data: You receive billions of events per day from drivers' phones. Each event has a driver_id, timestamp, latitude, longitude, and event_type (e.g.,
     'online', 'offline', 'trip_accepted').
   * Workload: This is an extremely write-heavy workload.
   * Requirements:
       1. A near real-time 'snapshot' view is needed for an operational dashboard that shows the last known location of every active driver. This view must
          be queryable by data analysts with low latency (seconds to a few minutes).
       2. The raw event history for each driver must be preserved for historical analysis and machine learning model training.
       3. You must be able to efficiently handle data deletion requests for a specific driver_id to comply with privacy regulations (like GDPR), without
          impacting the entire system.


  How would you design this Hudi table? Please justify your choice of:
   1. Table Type (CoW vs. MoR).
   2. Partitioning Strategy.
   3. Indexing Strategy, keeping in mind the limitations we just discussed.
   4. How you would approach the GDPR deletion requirement.

> I have few questions on this requirement, before I start the actual design

✦ Excellent. Asking clarifying questions is a critical part of any design process. Please, go ahead.

> Can you explain me what exactly is GDPR and how is it related to this requirement

✦ Of course.

  GDPR (General Data Protection Regulation) is a data privacy law from the European Union. For the purpose of this technical discussion, the most important
  part of it is the "right to be forgotten."


  This means that a user (in our case, a driver) can request that a company delete all of their personal data.


  How it relates to this requirement:
  Technically, this means we need a reliable and efficient way to execute deletion requests. If we receive a list of driver_ids that have requested to be
  forgotten, our system must be able to go into the Hudi table and permanently delete all records associated with those specific driver_ids.


  The challenge is to do this without, for example, scanning the entire multi-petabyte table, which would be too slow and expensive. Your design needs to
  support fast, targeted deletions.

> Okay, so, is it guranteed that the GDPR ids will be not be a part of active incoming data and is handled separately through execlusive requests?

✦ That's a fantastic question, and it shows you're thinking about real-world race conditions.


  You should assume that you cannot guarantee this. A driver could submit a deletion request while their app is still online and sending a few final
  location events. The deletion request might come through a separate channel, but it will operate on the same data table that the live event stream is
  writing to.


  Therefore, your design must be robust enough to handle this. For example, if you process a batch of updates that contains both a final location event
  for driver_123 and a separate "delete" instruction for that same driver_123, the delete must win.


  This brings up a key concept: conflict resolution. How would you design your Hudi write operation to ensure that a 'delete' event for a driver always
  takes precedence over a regular 'location update' event for that same driver, especially if they are processed in the same batch?

> Okay. Since the question correctly specifies that this is a near-real time requirement, I will be using tools like Apache Kafka, Spark Structured 
  Streaming, Apache Hudi as a Lakehouse layer and Apache Hive as Data warehouse. For any Event-Driven Architecture, Apache Kafka acts as a perfect buffer 
  for all the incoming events. I would like to go with an assumption that the events will be flagged with "Active" and "Delete" tags for the separate 
  identification of records.

✦ Okay, a stack of Kafka, Spark Streaming, and Hudi is a solid choice. And assuming the incoming data can be flagged with an operation type (like "upsert"
  or "delete") is a great way to model this.


  Now, let's translate that into the specific Hudi table design. Based on your chosen stack and that assumption, please justify your choices for the
  following:


   1. Table Type: Given the extreme write-heavy workload (billions of events/day) but also the need for a low-latency analyst query view, would you choose
      Copy on Write or Merge on Read? Why?

   2. Conflict Resolution: How would you use your "delete" flag and Hudi's precombine key feature to ensure deletes are handled correctly, as we discussed?


   3. Partitioning and Indexing: How would you partition this table? And what indexing strategy would you use to make both the high-volume writes and the
      targeted GDPR deletions fast and scalable?

> For Table Type, I would like to go ahead with Merge-On-Read table type. Since I am using Strcutured streaming, a CoW table does not support the case well.
   If CoW table type is chosen then the batch size has to be lowered to cater to the write performance, this will add the latency and defeats the purpose of
   building a near-real time pipeline. The events seem to be high on inserts and very less amount of updates and deletes are expected. Hence merge on read 
  will be a best strategy as it supports quick writes in a micro-batch without adjusting the batch-size. The delta files are merged with base files on 
  querying the table or through compaction and since this is a micro batch, the merge can perform faster than expected as most of the records are 
  insert-only. For conflicts, I would like handle the case in transformation logic. Since the in-coming data has a delete flag with it, I will separate out 
  those records into a different dataframe, separate from the dataframe for inserts. Before loading to the base tables, first the records of delete flag 
  will be filtered from the base data frame and a separate delete operation will be queried to delete all the records matching the delete flag from base 
  files. This will ensure that the records with delete flag will be deleted from everywhere. For raw retention, I would like to write a separate batch flow 
  which will extract the raw-messages from kafka-topic on once in every 4 hours. This will complete the implementation of a full-scale Lambda Architecture. 
  For Partitioning and Indexing, Since we are getting timestamps in the events, I will create a new column extracting the date-part from the timestamp and 
  this will act as a parition key which will be applied day-wise for the table. The table-type is Merge-on-Read, Global_Bloom will be the right choice of 
  index to update the parquet file footers with record and pre-combine key and same is updated in the table-wide index as well. The deletes are less 
  frequent so we can expect that the record marked for delete is already indexed and the right file-group will be fetched for delete operation.

✦ Thank you for that detailed design. Let's break it down, because you've made some good choices and some that I'd like to challenge, which is common in a
  real design review.

  Table Type: Merge-on-Read


  Your choice of Merge-on-Read is excellent. For an extremely write-heavy workload, MoR is the correct path as it optimizes for fast ingestion by writing
  changes to delta files and deferring the expensive merging process. This is a solid decision.


  One small clarification: CoW tables are supported in Structured Streaming. The challenge, as you hinted at, is the high write amplification, which can
  lead to very large micro-batches taking a long time to commit, thus increasing end-to-end latency. But it is a supported combination.

  Deletion Logic and Indexing: A Major Challenge

  This is the area I want to push back on most.


  You proposed a complex, multi-step process for deletes and chose the Global Bloom Index. Let's connect this back to our earlier discussion. We
  established that the Global Bloom Index creates a massive write bottleneck because every write to the table must also update a single, centralized
  index.


  Given a workload of billions of events per day, how would a single global index handle that concurrent write pressure? And is there a simpler way to
  handle deletes without manually splitting your DataFrame?


  Let's rethink this.
   1. How can you handle inserts, updates, and deletes in a single, atomic write operation using Hudi's built-in capabilities? Think about the precombine
      key.
   2. Given that a driver_id will always be present in a single date partition (a driver can't be in two dates at once), is a global index even necessary?
      What would be a more scalable index choice?

> Thank you for both the challenges. You pointed out the flaw correctly for indexing. Chosing the GLOBAL_BLOOM for an exponentially increasing data is not 
  a good choice, GLOBAL_BLOOM is more suited for a low-write (once-in-a-day) refresh and read heavy tables. Since I have chosen date as my partition key 
  which is highly unlikely to change in our scenario, I would like to change my indexing strategy from GLOBAL_BLOOM to BLOOM index. Since Bloom index 
  maintains index for every partition, only the partition writes are required for indexing and hence it avoids the WRITE bottleneck. Coming to Upserts and 
  Deletes, every Hudi job will be configured with record key and pre-combine key which usually takes partition column and category flags to handle updates 
  and deletes for the existing records. I beleive irrespective of when the records with delete flag arrives, a query in the job to delete all the records 
  matching the delete flag will handle our case to delete all the driver_id for GDPR.

✦ Excellent correction. Moving from Global Bloom to a standard Bloom index is exactly the right decision for this workload. You've correctly identified
  that since the partition key (date) is stable for a given record, a partition-scoped index avoids the global bottleneck and is much more scalable.


  Now, let's zero in on your second point about deletes. You're right that the recordKey and precombine key are the answer. You said, "...a query in the
  job to delete all the records matching the delete flag will handle our case..."


  This still sounds like you are thinking of a separate action. The beauty of Hudi is that you don't need a separate "delete query." You can handle
  inserts, updates, and deletes all in one single data stream.

  Let's get very specific. Imagine your incoming DataFrame from Kafka has been processed and contains two records for the same driver:


   * Record 1 (Location Update): {"driver_id": "abc", "event_ts": 1677657600, "op_type": "upsert"}
   * Record 2 (GDPR Request): {"driver_id": "abc", "event_ts": 1677657601, "op_type": "delete"}

  You pass this single DataFrame containing both records to your spark.write.format("hudi")... call.


   1. What field would you set as the Record Key?
   2. What field would you set as the Precombine Key?
   3. How does Hudi use the value in the precombine field to automatically ensure the "delete" record wins and the driver's data is removed?
   4. Finally, to make this work, you need to tell Hudi how to perform the delete. What configuration or payload class would you use to handle records where
      op_type is "delete"?

> Thats a good hint. In this case, my Record Key will be driver_id and my pre-combine key will be a combination of event_ts and op_type.

✦ You've got the Record Key perfect. `driver_id` is the correct choice.

  You're very close on the pre-combine key. It must be a single field that Hudi can order to determine which record is "newer". You can't directly combine
  two fields in the configuration.

  Given your two fields, event_ts and op_type, the correct choice for the pre-combine key is `event_ts`.


  Here's how it works:
   1. Hudi sees two records for the same record key (driver_id: "abc").
   2. It compares them based on the pre-combine key (event_ts).
   3. It sees that 1677657601 (the delete record) is greater than 1677657600 (the update record).
   4. Therefore, Hudi picks the delete record as the "winner" and discards the location update.


  Now for the final, critical piece of the puzzle. Hudi has selected the winning record: {"driver_id": "abc", "event_ts": 1677657601, "op_type": 
  "delete"}.


  By default, Hudi would try to insert or update this record. How do you tell Hudi that when it sees a record with "op_type": "delete", it should
  interpret that as a delete instruction instead of an upsert? What configuration do you set?

> Can you answer this question as I might have not handled this scenario in my experience.

✦ Of course. This is a crucial piece of the puzzle for handling soft deletes, and it showcases Hudi's flexibility.


  You tell Hudi how to interpret records by using a specific Payload class. The default payload class (OverwriteWithLatestAvroPayload) just overwrites an
  old record with the new one. To handle deletes, you need a different approach.

  The most common and idiomatic way to do this is to use the `EmptyHoodieRecordPayload`.

  Here's the complete two-step process:

  Step 1: Flag the record in your Spark transformation.


  In your Spark job, before you write to Hudi, you add a step. When you see a record with "op_type": "delete", you replace its data with null. The record
  key must remain, but the data payload becomes empty.

  A simplified Spark expression would look like this:



   1 // df is your DataFrame with the "op_type" column
   2 val payloadDF = df.withColumn("hudi_payload",
   3   when(col("op_type") === "delete", lit(null))
   4   .otherwise(to_avro(struct(df.columns.map(col):_*))) // Convert the row to Avro otherwise
   5 )

  Note: The actual implementation might vary, but the concept is to make the payload empty for delete records.

  Step 2: Configure the Hudi writer.


  You don't actually need to change the payload class configuration. The default OverwriteWithLatestAvroPayload has a built-in feature: if it sees a
  record with an empty or null payload after pre-combining, it interprets it as a delete.


  So, the full sequence for your driver_id: "abc" is:
   1. Pre-combine: Hudi picks the record with the higher event_ts, which is the one with "op_type": "delete".
   2. Payload: The payload for this winning record is now null because of your transformation logic in Step 1.
   3. Write: The Hudi writer sees the null payload for the existing record key "abc" and proceeds to delete it from the table (by removing its entry from
      the index and no longer carrying it forward in future file versions).


  This allows you to mix inserts, updates, and deletes in a single stream, and Hudi handles them atomically and correctly. This is a core pattern for
  building transactional data lakes.


  That concludes the main part of the interview. You did very well. You started with a foundational understanding and, through our discussion, were able
  to correct your course on complex topics like indexing and delete handling. That ability to reason through trade-offs and adapt your design is exactly
  what's needed for a role at a company like Uber.

> Thank you for the great questions. Do you think you have missed some more corner cases like the delete scenario above? If Yes, then could you please post 
  those questions and detailed explanations as well.

✦ Of course. That's a great mindset to have. The scenarios that truly test a candidate's depth are often around operational issues and failure modes. Here
  are a few more corner-case questions and explanations that would be common in a high-level Hudi interview.

  ---


  Question 1: The Small File Problem and Table Maintenance


  Scenario: Your Merge-on-Read table for driver locations is ingesting data 24/7. After a few weeks, data analysts start complaining that their queries,
  which used to be fast, are now taking 10x longer, even for the same date range. You investigate and see that each partition folder contains thousands
  of small Avro "log" files and a growing number of small Parquet "base" files.


  Question:
  a) Why, specifically, do thousands of small files degrade query performance for engines like Presto or Spark SQL?
  b) What two distinct Hudi "table services" would you use to solve this problem? Explain what each service does and how they differ.
  c) What are the pros and cons of running these services inline versus asynchronously, and which approach is non-negotiable at Uber's scale?

  Detailed Explanation:


  a) Why Small Files are Bad: Query engines like Spark and Presto are optimized for reading large, columnar files. They incur significant overhead for
  each file they have to open. This overhead includes:
       * File System Operations: Interacting with the distributed file system (like HDFS or S3) to list, open, and seek each file is a slow, high-latency
         operation. Listing thousands of files can take seconds to minutes before any data is even read.
       * Reader Initialization: For each file, the Parquet/Avro reader has to be initialized, and the file's footer/metadata must be read and parsed.
       * Lack of Columnar Efficiency: With very small files, the benefits of columnar compression and predicate pushdown are greatly diminished.


  b) The Two Table Services:
       1. Compaction: This service is specific to Merge-on-Read tables. Its job is to take the Avro-based row-oriented delta "log files" and merge them with
          the corresponding columnar Parquet "base file" to produce a new, up-to-date base file. This process makes the data available in a columnar,
          read-optimized format.
       2. Clustering: This service works on the base files themselves (for both MoR and CoW). Its job is to take small base files and rewrite them into a
          smaller number of larger base files (e.g., taking 10 files of 12MB each and rewriting them into one 120MB file). This directly reduces the number
          of files a query engine needs to scan.


  c) Inline vs. Asynchronous:
       * Inline: This means the service (e.g., compaction) runs as part of the main data ingestion write job. The write commit is blocked until the service
         is complete.
           * Pro: Simple to manage. It's either done or not.
           * Con: It adds significant latency to your ingestion pipeline. For a continuous streaming job, this is often unacceptable as it can cause lag to
             build up.
       * Asynchronous: This means the service runs as a separate, dedicated Spark job that scans the table for work to do (e.g., compactions or clusterings
         to be performed) and executes it independently of the ingestion job.
           * Pro: It completely decouples table maintenance from data ingestion. Your streaming writers can continue to ingest data at low latency without
             being blocked.
           * Con: It requires more operational overhead. You have to schedule and monitor a separate Spark job for these services.


  At Uber's scale, the asynchronous approach is non-negotiable. You cannot afford to halt or delay your primary ingestion pipelines for minutes or hours
  to perform table maintenance. You must run dedicated, asynchronous compaction and clustering jobs to continuously optimize the table structure in the
  background.

  ---

  Question 2: Concurrency and Locking


  Scenario: You have the main streaming job writing to your Hudi table every 5 minutes. A separate, high-priority batch job also needs to run every hour
  to backfill corrected data for the past day. Both jobs will be writing to the same partitions.


  Question: What happens by default if both jobs try to write to the same table at the same time? How does Hudi prevent data corruption, and what
  configurations must you enable to make this concurrent writing possible and safe?

  Detailed Explanation:


  By default, Hudi operates with a single-writer assumption. It does not use any locking. If two jobs write to the same table concurrently, they will be
  unaware of each other. Both will read the table's state, write new files, and then try to update the timeline by committing their changes. The last one
  to commit will overwrite the other's changes on the timeline, leading to data loss and a corrupted table state.

  To solve this, you must enable Hudi's Optimistic Concurrency Control (OCC).


  How it Works:
   1. Acquire Lock (Optional but Recommended): Before writing, a writer can try to acquire a lock to signal its intent.
   2. Read State: The writer reads the table's timeline state at the beginning of its operation (e.g., "the last successful commit was C10").
   3. Write Data: It performs the write, creating new data files.
   4. Check for Conflicts: Before making its final commit to the timeline, the writer checks the timeline again. If the latest commit is still C10, there is
      no conflict. It can proceed. However, if another writer has successfully committed in the meantime (e.g., the latest commit is now C11), this writer
      has a conflict.
   5. Commit or Fail: If there's no conflict, the writer commits its changes (e.g., creating commit C12). If there is a conflict, the writer's commit fails,
      and the job must be configured to retry the entire process (re-read state, re-write data, etc.).


  Key Configurations:
   * hoodie.write.concurrency.mode: Must be set to optimistic_concurrency_control.
   * hoodie.cleaner.policy.failed.writes: Should be set to LAZY to ensure failed partial writes are eventually cleaned up.
   * hoodie.write.lock.provider: You must configure a distributed lock provider to make this robust. Common choices are
     org.apache.hudi.common.lock.ZookeeperBasedLockProvider (requires a Zookeeper cluster) or org.apache.hudi.hive.HiveMetastoreBasedLockProvider (uses the
     Hive Metastore).


  Enabling OCC makes concurrent writes safe, but the trade-off is that jobs can fail due to conflicts and must have retry logic, which can increase
  overall job duration and latency.


  ---
  These scenarios probe the practical, operational knowledge required to run Hudi reliably at a massive scale, which is exactly what companies like Uber
  look for.

