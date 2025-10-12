> Thanks. The next round will be about System Design for an Analytical Dashboard on applications like Uber eats or Netflix. Can you mimick this round for 
  me

✦ Of course. This is a great topic for a system design round, as it touches on data processing, real-time systems, and user-facing analytics.

  Let's begin.

  ---


  Interviewer: Hello, and welcome to the system design round. For this session, we're going to work through a high-level design problem. I'll be more
  interested in your thought process, how you handle trade-offs, and the major components of your system rather than minute details.

  The Problem:

  I want you to design a real-time analytics dashboard for our Uber Eats restaurant partners.


  Imagine you are a restaurant owner. You want to log in to your Uber Eats portal and see a dashboard that helps you understand your business's
  performance and make immediate operational decisions.


  Feel free to use a diagramming tool or just describe the components. Please start by asking any clarifying questions you have. The floor is yours.

> Thats a great questions to start with and with the description of the problem statement I understand that the end users of this dashboard will be 
  restaurant owners and similar clients to track their profits real-time. Hope I have completely understood the task.

✦ Yes, that's the core idea. The dashboard should empower restaurant owners to track their business health and make operational decisions.


  With that high-level goal understood, what specific questions do you have about the requirements before we dive into the architecture?

> Yes, I do have a question on the data availability. I believe that the data in the dashboard has to confirm on strong consistency rather than 
  availability of the numbers. Right?

✦ That's an excellent question, and it gets right to the heart of the system's architectural trade-offs.

  Let's think about it from the user's perspective. A restaurant manager is in the middle of a busy lunch rush. Which of these two scenarios do you think
  is worse for them?


   1. The dashboard is completely unavailable for two minutes.
   2. The dashboard is available, but the "Total Orders" count is off by one or two for a few seconds before it corrects itself.


  Which trade-off would you make?

> In this particular case, I would go with the option 2 where I would prefer that dashboard to be available but the "Total Orders" count is off.

✦ Exactly. That's the right trade-off for this system. A slightly stale number is far less disruptive than the entire dashboard being unavailable during a
  critical time.

  So, let's establish that as a core non-functional requirement: The system must prioritize High Availability, and we will design for Eventual Consistency.

  Great. Now that we've settled that, let's think about the features. What are the key functional requirements?


  Specifically, what metrics and data points do you think a restaurant owner would need to see on this dashboard to find it useful?

> Yes. Thank you for confirming. As far as metrics for dashboard are concerned, the restaurant manager would be interested in the food remaining in the 
  inventory to be served, what is the most ordered item on hourly basis, What are the total sales on daily basis. Does that suffice for the requierement?

✕ [API Error: request to https://oauth2.googleapis.com/token failed, reason: socket hang up]


> Yes. Thank you for confirming. As far as metrics for dashboard are concerned, the restaurant manager would be interested in the food remaining in the 
    inventory to be served, what is the most ordered item on hourly basis, What are the total sales on daily basis. Does that suffice for the 
  requierements?

✦ Those are three excellent starting points. Let's refine them and build on them.


   1. Inventory: The "food remaining in inventory" metric is a fantastic idea. However, that would require deep integration with each restaurant's private
      inventory system, which is a huge project on its own. For our V1 design, let's scope that out and focus only on metrics we can derive from the data
      Uber Eats already generates (orders, deliveries, ratings, etc.).


   2. Most Ordered Item & Total Sales: These are perfect. For a real-time dashboard, we can frame them as:
       * "Total Sales So Far Today" (updating with every completed order).
       * "Top 5 Trending Items" (updating every few minutes).


  Now, think about the operational side. If you're a manager during a busy dinner service, what else would you be anxious to know? What about the status
  of active orders, the delivery process, or customer satisfaction?

> Yes. Total sales on daily basis would be a fit requirement for daily aggregation dashboard. Top 5 Trending Items is more likely towards a near real time 
  requirement. Our requirements lean towards real_time data capture where metrics like active orders can be tracked seamlessly. This will also cater the 
  driver assignment to the orders for order pickup and delivery. Also, the rating by committed by the user for food and delivery.

✦ Excellent. You're thinking about the full lifecycle of an order, which is perfect.

  Let's consolidate that into a clear set of V1 functional requirements for our dashboard:


  Real-Time Metrics (latency < 5 seconds):
   * Active Order Funnel: A live count of orders in each stage: New, Confirmed, In the Kitchen, Ready for Pickup.
   * Courier Status: A count of couriers currently waiting at the restaurant for an order.
   * Live Customer Ratings: A feed of new ratings for recently completed orders.


  Near Real-Time Metrics (latency < 1 minute):
   * Top 5 Trending Items in the last hour.
   * Average Food Prep Time over the last hour.

  Daily Aggregates (updating with each order):
   * Total Sales So Far Today.
   * Total Completed Orders Today.


  One quick clarification: our dashboard will display the status of driver assignments (e.g., "Courier Assigned"), but the actual transactional system
  that assigns the driver is a separate service. Our job is to subscribe to the events from that system.


  This is a solid feature set. Now, before we draw any boxes and arrows, let's quickly define the non-functional requirements.

  What kind of scale and latency should we design for? Let's put some numbers on it to make it concrete. Let's assume:


   * Scale: A global service with 1 million restaurants. Peak traffic is 10,000 events per second across all restaurants.
   * Latency: As we said, real-time metrics must be reflected on the dashboard in under 5 seconds (p99).
   * Historical Data: The dashboard must also support querying analytical data from the past 6 months.


  With these functional and non-functional requirements, how would you approach the high-level architecture? What are the major components you would
  build?

> Yes, since we are clear with the metrics now, I would like to decide the architectural components to be used. For a scale of 10,000 events per second, it 
  becomes more clear to use Apache kafka as a continuous event streaming buffer. Most of the Event emmittor APIs can be plugged to Kafka to extract all the 
  events for orders, delivery assignmnet, delivery status. Apache kafka is the perfect message broker for this requirement as data within each topic are 
  partitioned and each partition maintains a continuous sequence of messages through offsets. With Kafka, Apache flink as a continuous streaming tool should
   be used for real time tracking as it can directly tap into the Kafka topics and extract information continuously. For Fault tolerance, Apache Flink 
  follows exactly-once failure semantics and guarantees the recovery from failure through checkpointing the state of ingestion through time-based barriers. 
  During the event of failures Flink is capabale enough to restart from the last successful checkpoint commit. What do you think about the design decision 
  for Extraction of the events?

✦ This is an excellent start. Your choice of Apache Kafka for ingestion and Apache Flink for stream processing is a very strong, industry-standard approach
  for this kind of low-latency, high-throughput problem.


  I'm particularly glad you brought up fault tolerance, checkpointing, and exactly-once semantics right away. Thinking about reliability from the start
  is critical, and your reasoning is spot on.

  So, let's follow the data's journey.


   1. Events (orders, status changes, etc.) are flowing into Kafka.
   2. Flink is consuming these events, performing stateful computations (like counting active orders or calculating rolling averages), and producing a
      stream of real-time analytical results.

  Now, where does this processed data go? What kind of database or storage system would you use to serve the dashboard queries?


  And keep in mind our dual requirement: we need to serve both real-time data (e.g., "active orders right now") and historical queries (e.g., "sales
  trend over the last 6 months"). How does that influence your choice of storage?

> Yes. Thank you for confirming on the extraction. For live-dashbaord, I would like to approach the lambda architecture having 2 forms of loading the data. 
  1) Fast Layer, aka, continuous streaming layer. We will utilize this layer for our continuous streaming requirement where the data from Apache Flink will 
  be feeding into a high performance NoSQL Columnar storage. We can consider Apache Pinot, Apache Cassandra for high performance NoSQL and both these 
  databases are tailor made for real-time dashboards. And since both of them support columnar data format, query performance is guarateed and also both the 
  DBs are high availabile databases which prioritize availability of the system more than the consistency of the data refresh. Could you please valuate 
  these choices and then I will move ahead with the batch layer of data architecture.

✦ Excellent. Using a Lambda architecture is a classic and very effective pattern for this problem, as it directly addresses our need to serve both
  real-time and historical data.

  You've suggested Apache Pinot or Apache Cassandra for the speed layer. Let's discuss those choices.


   * Apache Pinot (or its alternative, Apache Druid) is an outstanding choice. These are real-time OLAP datastores purpose-built for exactly this use case:
     powering user-facing analytics with sub-second query latency. They are designed to ingest directly from streaming sources like Kafka and are optimized
     for the types of filtering, aggregation, and group-by queries our dashboard needs.


   * Cassandra is an interesting choice. It has phenomenal write throughput and availability. However, it's generally considered an OLTP-style database.
     What challenges or trade-offs do you foresee if we were to run complex analytical queries on Cassandra, as opposed to a purpose-built OLAP datastore
     like Pinot?

  For the sake of moving forward, let's assume we've chosen Pinot for our speed layer.


  Now, please describe the second half of your architecture: the batch layer. What is its purpose, and what technologies would you use to build it?

> Sure. The real-time are more concerned about the current_day and current_moment metrics. Storing the entire data in the fast layer will lead to data 
  duplicacy at multiple data stores. Hence in this design I would like to propose an additional trait to analytics dashboard. Lets say that we will only 
  maintain the data in Pinot for last 6 months and we will purge all the data older than 6 months. The batch layer will be having a batch loading style, and
   particularly I would like to choose ELT style of loading the data. As in, I would like to use batch extractors like Kafka connect which will tap to kafka
   topic. The single Kafka instance will be acting like a portal to both continuous streaming and batch processing, hence with the help of Kafka connect I 
  will be loading this data to persistent cloud storage like GCS. That will actually give me an edge for replay/reconciliation of the data for historical 
  analysis, to ingest any missing data or also to debug the errors in past historical snapshot. This data in GCS can be in Parquet Format and all these 
  files will be stored in dated directories, as in, the raw data will be stored as per date partitions based on the extraction. I would like to schedule the
   extraction and loading through kafka connect for every hour. Now, this raw data has to be transformed in any required format and presented as Apache 
  Hudi-Hive format tables. These tables will be used purposefully for historical analysis. There will be no historical limit for data stored in Hive tables.
   Since we are using Hudi table format, we can guarantee the consistency of critical information like sales, chargebacks and refunds. The transformation 
  and final table upserts is completely goverened by the Spark - batch processing and scheduled thorough apache Airflow. This Job in airflow will be 
  scheduled for every hour. Since we are loading the batch data asynchronously, the spark will consider the raw-data stored in GCS as true-replayable source
   avoiding the dependency over Kafka retention completely. Alternatively we can have a reconciliation pipeline which can fix any descrepancies in Pinot db 
  as well for data older than 7 days and within 6 months. Apache Hudi-Hive tables act as perfect data warehouse for historical analysis. The Live dashboard 
  can be built and monitered over Apache Pinot and historical analysis dashboards can be built over Hive tables. To successful confirmity over job 
  completions and lag monitoring, we will also build a metrics dashboard using promethius-grafana which can also act as alerting mechanism when the lag 
  between kafka and flink goes over the threshold. I believe with this design we can assure low-latency, scalability, availability and also fault tolerance 
  of the entire system. Could you please validate on each of the points.

✦ This is an outstanding and comprehensive design. You've covered the entire data lifecycle from ingestion to processing, storage, and even monitoring.
  This is a very strong, senior-level answer.

  Let's quickly validate the key points you've made, because you've hit on many best practices:


   * Lambda Architecture: Your choice to use a Lambda architecture is a perfect fit for the requirements.
   * Unified Log (Kafka): Using Kafka as the single source of truth for both the speed and batch layers is excellent. It simplifies the architecture and
     ensures consistency.
   * Data Lake (GCS + Parquet): Your batch layer design is textbook-perfect. Storing raw, partitioned Parquet files in GCS creates a durable,
     cost-effective, and replayable data lake.
   * Lakehouse (Hudi): Choosing Hudi is a very modern and powerful choice. You correctly identified its key benefit: enabling transactional updates and
     deletes on your data lake, which is crucial for handling things like refunds and chargebacks accurately in the historical data.
   * Clear Separation of Concerns: You've clearly defined the roles: Pinot for low-latency queries on recent data, and the Hudi/Hive data lakehouse for
     deep historical analysis.
   * Proactive Features: Your inclusion of a reconciliation pipeline and a Prometheus/Grafana monitoring stack shows a high level of maturity. You aren't
     just designing a happy-path system; you're planning for real-world operational issues like data divergence and processing lags.


  The high-level design is solid. Now, let's dig into a few specific, challenging areas.

  Question 1: The "Lambda Seam"


  You've proposed two serving layers: Pinot for real-time data (last 6 months) and Hudi/Hive for deep history. How does the end-user experience this? If
  a restaurant owner wants to see a single chart showing "Daily Sales" for the last 7 months, how do you architect the query layer to present a unified
  view from these two separate systems?

  Question 2: End-to-End "Exactly-Once"


  You correctly mentioned Flink provides exactly-once semantics for its internal state. However, achieving this end-to-end is tricky. When your Flink job
  writes the processed results to Pinot, how do you prevent duplicates? For example, if the job fails and restarts, it might re-process some data from
  Kafka and try to write it to Pinot again. How do you ensure the final metrics in the dashboard are not double-counted?

  Question 3: Metric Implementation


  Let's talk about calculating the "Average Food Prep Time". An order's prep time is the duration between its status: 'Confirmed' event and its status: 
  'Ready for Pickup' event. How would you implement the logic for this in your Flink job? What state do you need to maintain? And how would you handle
  potential issues like out-of-order events?

> Cool. I would like to assess on my design based on the above points one-by-one. 1) The "Lambda Seam": Yes, the end-user can have requirements to have an 
  aggregated view for both real-time and data older than 7 months also. I would like to modify my design to include a catalyst query layer such as Apache 
  presto or Trino which has multiple integrations with various databases, both RDBMS and NoSQL. Hence it can run the queries on both Pinot and Hudi, 
  aggregate the result and present it to the end-user.

✦ Excellent answer. Using a federated query engine like Presto or Trino is a perfect solution for bridging the "seam" in a Lambda architecture. It provides
  a single unified SQL interface for the application, which can then query both Pinot and the Hudi data lake and merge the results. This is a great way to
  provide those longer-range historical views without moving all the data into one system.

  That cleanly solves that problem. Let's move on to the second question.

  Question 2: End-to-End "Exactly-Once"


  You're writing data from your Flink job to Pinot. How do you avoid creating duplicate metrics in your dashboard if the job fails and has to re-process
  some of the data from Kafka? How do you make the writes to your serving layer idempotent?

> For End-to-End, exactly-once semantics, this works perfectly well if the sink supports transactional inserts.

✕ [API Error: request to https://cloudcode-pa.googleapis.com/v1internal:countTokens failed, reason: 40E18E0802000000:error:0A0003FC:SSL 
  routines:ssl3_read_bytes:ssl/tls alert bad record mac:ssl/record/rec_layer_s3.c:916:SSL alert number 20
  ]


> For End-to-End, exactly-once semantics, this works perfectly well if the sink supports transactional inserts. But since Apache Pinot does not support 
  updates on the basis of key, I would think of one way to handle this, i.e., delete the existing records based on the key and insert the fresh keys with 
  updated information for other columns. I chose this way because both inserts and deletes are quite fast in Pinot and we will not have any performance 
  bottle necks. How would you evaluate this solution.

✦ That's a logical approach, thinking in terms of a delete-then-insert pattern, which is common in traditional transactional databases.


  However, in a distributed OLAP system like Pinot, that two-step process isn't atomic and can be risky. If a failure happens after the DELETE but before
  the INSERT, you could permanently lose that data. These systems are heavily optimized for high-volume appends, and deletes can be complex or
  non-existent in some configurations.


  A more common and safer pattern here is to achieve idempotency. The goal is to design the write operation so that executing it multiple times has the
  exact same effect as executing it once.


  Pinot's real-time tables support this. You can define a primary key on the table. When a new event arrives with the same primary key as an existing
  record, Pinot can be configured to simply replace the old record with the new one. This is effectively an "upsert."


  Knowing this "upsert" capability exists, how would you design the data being emitted from your Flink job and the schema of the Pinot table to guarantee
  correctness, even if Flink re-sends an event?

> Thats a great hint. Thank you for the help. The Flink will process the incoming data based on some defined keys, these keys should be shared with and as 
  same as the keys configured for loading the data to apache pinot. Since Pinot supports idempotency, any data with same key will be automatically updated 
  in apache pinot.

✦ Exactly. That's the key to making the pipeline resilient.

  The Flink job would emit a complete record for each metric based on a unique key (e.g., an order_id). We would then configure that same order_id as the
  primary key in the Pinot table.


  This way, if Flink restarts and re-sends a processed record, Pinot sees the primary key already exists and simply overwrites the old row with the
  identical new one. The final state remains correct, and we've achieved end-to-end idempotency.

  Great. Let's move to our final deep-dive question.

  Question 3: Metric Implementation

  Let's get specific on the "Average Food Prep Time" metric.


  The prep time for a single order is the duration between its status: 'Confirmed' event and its status: 'Ready for Pickup' event. We want to show a
  rolling average of this over the last hour on the dashboard.


  How would you implement the logic for this in your Flink job? What state do you need to maintain, and how would you handle potential issues like
  out-of-order events (e.g., the 'Ready for Pickup' event arriving before the 'Confirmed' event)?

> This the requirement for aggregated data and this has to be implemented as a transformation step through Apache Flink. Since Flink supports both 
  DataFrame and SQL API, the rolling average queries are evaluated on the incoming data. These aggregations has to be stateful operations, as in window 
  aggregations which can be configured through stateful processing. And, personally I do not have much practical experince on handling stateful 
  aggregations with Flink. I am more experienced in handling near-real time stateless processing. I provided response based on some theoritical knowledge. 
  Could you please valuate and provide me the exact response for this scenario.

✦ Thank you for being transparent about your practical experience with this specific feature. That honesty and self-awareness are highly valued.

  Your theoretical approach is exactly right. This is a classic stateful stream processing problem that requires windowing. Let me walk you through how it
  would be implemented in detail, as you asked.


  Here is the complete solution:

  1. The Core Logic: Joining Two Events

  The fundamental challenge is that the information we need (the Confirmed timestamp and the Ready for Pickup timestamp) arrives in two separate events
  at different times. We need to join them.

  2. State Management

  To do this, our Flink job must maintain state. We would use Flink's MapState where the key is the order_id.


   * When a `'Confirmed'` event arrives for `order_id: 123`: We access the state and store the event's timestamp. The state for that key now looks like
     {'123': confirmed_timestamp}.
   * When a `'Ready for Pickup'` event arrives for `order_id: 123`: We access the state, find the stored confirmed_timestamp, calculate the prep duration
     (ready_timestamp - confirmed_timestamp), and emit this duration as a new event downstream. We can then clear the state for order_id: 123 to conserve
     resources.

  3. Handling Out-of-Order Events


  This is the tricky part. What if the 'Ready for Pickup' event arrives before the 'Confirmed' event due to network latency?

  This is solved using Event Time Processing and Watermarks.


   * Event Time: We configure Flink to operate in "Event Time," meaning it processes data based on the timestamp embedded in the event, not the time the
     event arrives at the processor.
   * Watermarks: Flink uses watermarks as a mechanism to understand the progress of time. A watermark for time T is a declaration that the system doesn't
     expect any more events with a timestamp older than T. This allows Flink to know when it's "safe" to finalize calculations for a given time window.
   * Allowed Lateness: We can configure our Flink job to handle a certain amount of lateness. If the 'Confirmed' event is late but arrives before the
     watermark has passed its window, Flink can still process it correctly by holding the 'Ready for Pickup' event in state until its partner arrives.

  4. The Final Aggregation (Windowing)


  Once our job is successfully emitting a stream of individual prep time durations (e.g., 300 seconds, 450 seconds, etc.), we feed this stream into a
  final windowed aggregation operator.


   * We would use a sliding window to calculate a rolling average. For example: ...keyBy(restaurant_id).window(SlidingEventTimeWindows.of(Time.hours(1), 
     Time.minutes(1))).
   * This tells Flink to group events by restaurant_id and, every 1 minute, calculate the average prep time over the last 1 hour's worth of data.
   * This final aggregated result is what gets written to Pinot to be displayed on the dashboard.

  ---


  That covers the end-to-end logic. Your initial instincts were correct, and this detailed walkthrough just fills in the implementation specifics.


  This concludes the system design round. Overall, you did an excellent job. You started with great clarifying questions, built a very strong and
  comprehensive high-level architecture, and reasoned through complex trade-offs effectively. This was a very strong performance.

> Thank you for the evaluation
