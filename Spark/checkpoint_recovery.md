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

## Solution

### Restart within the threshold.
   When prompted about the failure, restart the application immediately before leak.

### Auto-Restart after the threshold.
1. Since the app first checks for previously committed offsets before the application starts, the previously committed offsets have to backed up.
2. Programmatically pick the latest offset at current-3 position and save it in the app start config. This is necessary to ensure that the right offset is chosen to avoid data leak.
3. Set the kafka.start.offset property with the saved offsets from the config.
4. Now clean the checkpoint directory to ensure that the application considers this as a fresh start with the previously fed offsets.
5. The app will now start the streaming with the stable offsets ensuring 0 data loss.



