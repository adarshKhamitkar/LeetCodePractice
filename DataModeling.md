Prompt:
Consider yourself an expert in Data modeling curate a list of 30+ questions on all of concepts of Data Modeling along with Data warehouse to interview a 10 years of experience Data Engineer.  Make sure to include detailed solutions for each question.
---

### **Interviewer's Guide: Data Modeling & Warehousing for Senior Data Engineers**

**Philosophy:** For a candidate with a decade of experience, we are not looking for textbook definitions. We are looking for depth, trade-off analysis, and a proven ability to connect business requirements to robust, scalable, and maintainable data models. Their answers should be rich with examples from their past projects.

---

### **Category 1: Foundational & Strategic Concepts**

These questions set the stage and gauge the candidate's high-level understanding and philosophy.

**1. Compare and contrast the Kimball and Inmon approaches to data warehousing. In your experience, which have you used more and why?**

*   **Solution:** A strong candidate will go beyond the basic "top-down vs. bottom-up" explanation.
    *   **Bill Inmon (Top-down):** Proposes building a centralized, normalized Enterprise Data Warehouse (EDW) in 3rd Normal Form (3NF). Data marts for specific departments are then sourced from this EDW.
        *   **Pros:** High data integrity, single source of truth, low redundancy, very robust for enterprise-level reporting.
        *   **Cons:** High upfront effort and cost, slower to deliver initial value, less flexible to changing business requirements.
    *   **Ralph Kimball (Bottom-up):** Advocates for building business process-centric data marts first, using dimensional models (star schemas). These marts can then be integrated via conformed dimensions and facts to create an enterprise view.
        *   **Pros:** Faster time-to-value, more agile, intuitive for business users (optimized for queries).
        *   **Cons:** Can lead to data silos if not governed properly ("data swamp"), risk of multiple sources of truth if conformed dimensions are not managed.
    *   **What to look for:** The candidate should articulate the trade-offs clearly. They should provide a real-world example, e.g., "At my previous company, we used a Kimball approach because the business needed quick insights on sales performance. We built a sales data mart in 3 months. An Inmon approach would have taken over a year as we'd need to model the entire customer and product lifecycle first."

**2. How has the rise of the Modern Data Stack (e.g., Snowflake, BigQuery, dbt, ELT) changed the traditional principles of data modeling?**

*   **Solution:** This question tests if the candidate's knowledge is current.
    *   **Shift from ETL to ELT:** Raw data is loaded into the warehouse first. Transformation happens *in* the warehouse (e.g., using dbt). This makes the "staging area" conceptually different—it's often just raw tables in a dedicated schema.
    *   **Cheap Storage & Powerful Compute:** Cloud warehouses separate storage and compute. This reduces the pressure for perfect normalization to save space (a key driver for Snowflake schemas). Denormalization is now more common for performance, as compute can power through wider tables.
    *   **Rise of the "One Big Table" (OBT):** For some BI use cases, creating a single, wide, highly denormalized table with all necessary attributes is now feasible and often preferred for tools like Tableau/Looker. It simplifies the BI layer at the cost of pre-computation and storage.
    *   **Modeling as Code:** Tools like dbt have made data modeling an engineering discipline with version control (Git), testing, and CI/CD. The model is now documented and tested as part of the codebase.
    *   **What to look for:** Mention of specific tools (dbt), concepts (ELT vs. ETL), and an understanding of the trade-off shift (storage cost is down, so denormalization for query performance is up).

**3. Explain the difference between a Data Warehouse and a Data Lake. How does a Data Lakehouse attempt to bridge the gap?**

*   **Solution:**
    *   **Data Warehouse (DWH):** Stores structured, processed data. Schema-on-write. Optimized for fast BI queries and analytics. Expensive to store all data.
    *   **Data Lake:** Stores all types of data (structured, semi-structured, unstructured) in its raw format. Schema-on-read. Highly flexible and cost-effective for storage. Can become a "data swamp" without proper governance.
    *   **Data Lakehouse:** A modern architecture that combines the benefits of both. It implements data warehouse-like features (ACID transactions, data quality enforcement, versioning via formats like Delta Lake, Iceberg, Hudi) directly on top of low-cost data lake storage (like S3 or ADLS). This allows for both BI/reporting and ML/data science workloads on the same data repository.
    *   **What to look for:** Clarity on the "schema-on-write vs. schema-on-read" paradigm. The key insight for the Lakehouse is bringing DWH reliability features to Data Lake storage.

---

### **Category 2: Dimensional Modeling Deep Dive**

This is the core of most BI-focused data warehousing.

**4. What are the three types of Fact tables? Provide a business scenario for each.**

*   **Solution:**
    *   **Transactional:** Records a single event or transaction. It's the most common type. The grain is "one row per event."
        *   *Scenario:* An e-commerce sale. A row exists for each line item on an order (`order_id`, `product_id`, `quantity_sold`, `price`).
    *   **Periodic Snapshot:** Measures state at the end of a specific, regular time period (e.g., day, week, month). The grain is "one row per entity per period."
        *   *Scenario:* A monthly bank account summary. It would capture `account_id`, `month_end_date`, and the `closing_balance`. You can't sum the balances across months.
    *   **Accumulating Snapshot:** Tracks the progress of an entity through a well-defined lifecycle. The table has multiple date columns, one for each major milestone. A single row is updated as the entity progresses.
        *   *Scenario:* An order fulfillment pipeline. A single row for an `order_id` might have columns like `date_ordered`, `date_shipped`, `date_delivered`, and metrics like `shipping_duration`.
    *   **What to look for:** The ability to provide clear, distinct business examples.

**5. You need to model customer attributes, but some of them (like address or marital status) can change over time. Describe SCD Type 1, Type 2, and Type 3, and explain the trade-offs.**

*   **Solution:** This is a classic, but a senior should know it inside and out.
    *   **SCD Type 1 (Overwrite):** The new value overwrites the old value. No historical record is kept.
        *   *Use Case:* Correcting a typo in a name.
        *   *Trade-off:* Simple, but loses all history. Historical reports will reflect the *current* state.
    *   **SCD Type 2 (Add New Row):** A new row is added for the changed attribute. The old row is marked as "inactive" or "expired." This is the most common approach for historical tracking. It requires surrogate keys and effective date columns (`start_date`, `end_date`, `is_current_flag`).
        *   *Use Case:* Tracking a customer's address changes to analyze sales by their historical location.
        *   *Trade-off:* Preserves full history, but the dimension table grows larger and queries become more complex (e.g., `WHERE is_current_flag = true`).
    *   **SCD Type 3 (Add New Attribute):** A new column is added to store a limited amount of history (e.g., `current_address` and `previous_address`).
        *   *Use Case:* Tracking a salesperson's current vs. previous territory for a limited time.
        *   *Trade-off:* Simple to query, but history is limited and not scalable. The model must be changed if you need to track more than the predefined number of changes.
    *   **What to look for:** A follow-up question could be: "Describe SCD Type 6 (1+2+3 hybrid)." A senior candidate might have encountered this.

**6. What is the grain of a fact table, and why is it the single most important decision in dimensional model design?**

*   **Solution:**
    *   **Definition:** The grain defines what a single row in the fact table represents. It is the business definition of the lowest level of detail being recorded. For example, "one row per order line item" or "one row per daily web session per visitor."
    *   **Importance:**
        1.  **Determines Dimensionality:** The grain dictates which dimensions can be linked to the fact table. If the grain is "daily sales per store," you can't have a `product` dimension.
        2.  **Governs Measurements:** It defines what the facts (the numeric measures) actually mean and ensures they are additive.
        3.  **Prevents Misinterpretation:** A clearly stated grain prevents analysts from making incorrect assumptions. For example, if the grain is "per order" and a fact is `total_order_amount`, an analyst won't try to sum it by product.
    *   **What to look for:** The candidate must emphasize that *everything* flows from this decision. It must be declared upfront and agreed upon by business stakeholders.

**7. Explain degenerate dimensions. Provide a real-world example.**

*   **Solution:** A degenerate dimension is a dimension key in the fact table that has no corresponding dimension table. It's typically a transactional identifier like an order number, invoice number, or ticket number.
    *   **Example:** In a `fact_sales` table with a grain of "per order line," you would have keys for `dim_date`, `dim_customer`, `dim_product`, etc. You would also have the `order_number`. Instead of creating a `dim_order` table with just one attribute (the order number itself), you place `order_number` directly in the fact table.
    *   **Purpose:** It allows for grouping and filtering on that identifier (e.g., "show me all line items for order #12345") without the overhead of a join to a dimension table that would contain no other useful information.
    *   **What to look for:** A clear understanding that it's an attribute that *acts* like a dimension for slicing but doesn't warrant its own table.

**8. When would you use a Junk Dimension?**

*   **Solution:**
    *   A Junk Dimension is a dimension table that combines several low-cardinality flags and indicators that don't belong in a larger dimension.
    *   **Scenario:** Imagine a fact table with several boolean flags or simple text codes (e.g., `is_gift`, `payment_method_code`, `order_status`). Instead of adding each of these as a degenerate dimension or a separate mini-dimension (which would clutter the fact table schema), we can create a single Junk Dimension.
    *   **Implementation:** The Junk Dimension would contain the Cartesian product of all possible values of these indicators. For example, a row in `dim_order_flags` might look like: `(flag_key: 1, is_gift: 'Yes', payment_method: 'Credit Card', status: 'Shipped')`. The fact table then only needs a single foreign key (`flag_key`).
    *   **What to look for:** The main driver is to clean up the fact table schema and reduce its width by consolidating many low-cardinality, unrelated attributes.

**9. Explain the concept of conformed dimensions and why they are crucial for an enterprise-wide BI strategy.**

*   **Solution:**
    *   A conformed dimension is a dimension that is shared across multiple fact tables or data marts. It has a consistent structure, keys, and attribute values. For example, a single `dim_customer` table should be used by both the `fact_sales` and `fact_support_tickets` tables.
    *   **Crucial Importance:** They are the cornerstone of the Kimball architecture and integration.
        1.  **Single Source of Truth:** Ensures everyone in the organization is analyzing customer data using the same definitions and attributes.
        2.  **Cross-Process Analysis:** Allows for drilling across different business processes. An analyst can select a customer segment from the `dim_customer` table and see both their sales history and their support ticket history side-by-side. Without a conformed dimension, this is impossible.
        3.  **Consistency and Reusability:** Reduces development effort and ensures reports are consistent across different departments.
    *   **What to look for:** The candidate must highlight the "integration" and "drilling across" aspect. That's the key business value.

**10. How would you model a many-to-many relationship in a dimensional model? For example, patients and diagnoses, where a patient can have multiple diagnoses, and a diagnosis can apply to many patients.**

*   **Solution:** This requires a "bridge" or "linking" table.
    *   **The Problem:** You can't put a `diagnosis_key` in the `fact_encounters` table if a single encounter has multiple diagnoses. You also can't put `patient_key` in a `dim_diagnosis` table.
    *   **The Solution:**
        1.  Create a standard `dim_patient` and `dim_diagnosis` table.
        2.  Create a **bridge table**, e.g., `bridge_patient_diagnosis`, with at least two columns: `patient_key` and `diagnosis_key`. If you want to group patients by their combination of diagnoses, you create a `diagnosis_group_key` for each unique combination in the bridge table.
        3.  The fact table (`fact_encounters`) would then contain the `patient_key` and potentially the `diagnosis_group_key`.
    *   **What to look for:** The key term is "bridge table." A senior candidate might also discuss the "weighting factor" concept for allocating facts across the many-to-many relationship if needed.

**11. Differentiate between a Star Schema and a Snowflake Schema. When would you intentionally choose a Snowflake Schema?**

*   **Solution:**
    *   **Star Schema:** A central fact table is directly connected to several denormalized dimension tables. It looks like a star. Queries are simple (usually one join per dimension).
    *   **Snowflake Schema:** An extension of a star schema where dimension tables are normalized into multiple related tables. For example, `dim_product` might be snowflaked into `dim_product`, `dim_product_subcategory`, and `dim_product_category`.
    *   **When to Snowflake (the trade-offs):**
        *   **Massive Dimensions:** If a dimension table is extremely large (e.g., a customer dimension with hundreds of millions of rows), snowflaking out a frequently-changing or large attribute set into a separate table can save a significant amount of space.
        *   **Clear Hierarchies:** When there are fixed, multi-level hierarchies (like Geography: Country -> State -> City) that are used independently, snowflaking can enforce data integrity.
        *   **Outrigger Dimensions:** When an attribute in one dimension is itself a fully-featured dimension (e.g., a customer's `account_manager` in `dim_customer`).
    *   **What to look for:** The candidate should emphasize that Star Schemas are the default and preferred choice for simplicity and query performance. Snowflaking is a deliberate exception made for specific reasons, and they should be able to articulate those reasons with the associated costs (more complex queries, more joins).

---

### **Category 3: Advanced Modeling & Alternative Approaches**

**12. Explain the core components of a Data Vault 2.0 model (Hubs, Links, Satellites). What are its primary advantages over a dimensional model?**

*   **Solution:** This question probes knowledge beyond Kimball.
    *   **Core Components:**
        *   **Hubs:** Contain the business keys (e.g., `customer_id`, `product_number`). They define the core business entities. Hubs do not change.
        *   **Links:** Represent the relationships or transactions between Hubs. They are essentially many-to-many join tables.
        *   **Satellites:** Contain the descriptive, contextual, and historical attributes of the Hubs and Links. This is where all the change tracking happens (like SCD Type 2).
    *   **Primary Advantages:**
        1.  **Auditability & Traceability:** The model inherently tracks the source and load date of every piece of data, making it highly auditable.
        2.  **Flexibility & Scalability:** It's much easier to add new data sources or business entities without re-engineering the existing model. You simply add new Hubs, Links, or Satellites. This makes it ideal for agile environments with evolving data sources.
        3.  **Parallel Loading:** The decoupled nature of Hubs, Links, and Satellites allows for massive parallel data loading, which is a huge advantage in large-scale environments.
    *   **Where it fits:** Data Vault is excellent for the raw/integrated layer of the data warehouse (the Inmon-style EDW). Dimensional models are then often built *on top* of the Data Vault for reporting and analytics.
    *   **What to look for:** Understanding that Data Vault is not typically a replacement for dimensional models for BI, but rather a more robust and flexible way to build the foundational enterprise data layer.

**13. What is a Factless Fact table? Provide two different business use cases.**

*   **Solution:** A factless fact table is a fact table that contains no numeric measures (no facts). It only contains foreign keys to dimensions.
    *   **Use Case 1: Tracking Events:** To record an event that occurred. For example, a `fact_student_attendance` table might contain `student_key`, `class_key`, and `date_key`. Its existence signifies that a student attended a particular class on a particular day. You can answer questions like "How many students attended the Data Science 101 class in October?" by doing a `COUNT(*)` on this table.
    *   **Use Case 2: Coverage or Eligibility:** To model the conditions under which an event *could* happen. For example, a `fact_promotion_coverage` table could list all the products (`product_key`) that were part of a promotion on a given day (`date_key`). This allows you to compare which products were on sale vs. which products actually sold (from the `fact_sales` table).
    *   **What to look for:** The key insight is that the existence of a row in the table is the "fact" itself.

**14. When would you use surrogate keys versus natural keys in a data warehouse dimension, and why?**

*   **Solution:**
    *   **Natural Key:** A key that has business meaning and exists in the source system (e.g., Employee ID, Social Security Number, Product SKU).
    *   **Surrogate Key:** An integer key with no business meaning, generated by the data warehouse load process (e.g., an auto-incrementing integer).
    *   **Why Surrogate Keys are Preferred in a DWH:**
        1.  **Handles SCDs:** They are essential for implementing SCD Type 2. The natural key (e.g., Employee ID) would be repeated for each historical version, but the surrogate key (`employee_sk`) would be unique for each row.
        2.  **Decoupling:** They insulate the warehouse from changes in source systems. If the source system decides to change its key format (e.g., `employee_id` changes from integer to string), the DWH is unaffected as all joins are on the stable surrogate key.
        3.  **Performance:** Integer joins are almost always faster than joins on strings or composite keys.
        4.  **Integration:** Allows for integrating data from multiple source systems that may have conflicting natural keys.
    *   **When to use Natural Keys:** While surrogate keys are the standard, the natural key should always be kept in the dimension table as an attribute for user reference and traceability back to the source.
    *   **What to look for:** A clear, strong advocacy for surrogate keys in dimensions, with multiple valid reasons.

---

### **Category 4: Physical Modeling, Performance & Implementation**

**15. Your star schema query is slow. The `JOIN` between a 2-billion-row fact table and a 50-million-row dimension table is the bottleneck. How would you diagnose and solve this?**

*   **Solution:** This tests practical troubleshooting skills.
    1.  **Analyze the Query Plan:** The first step is always to look at the `EXPLAIN` plan. Is it using the correct join algorithm (e.g., Hash Join vs. Nested Loop)? Are full table scans happening where an index seek would be better?
    2.  **Check Physical Design:**
        *   **Partitioning:** Is the fact table partitioned, typically by date? This can dramatically reduce the amount of data scanned if queries have a date filter (which most BI queries do).
        *   **Indexing:** Are the foreign key columns in the fact table and the primary/surrogate key column in the dimension table indexed?
        *   **Distribution/Clustering (Cloud DWH):** In a distributed system like Snowflake or Redshift, is the data distributed/clustered on the right keys? Both tables should be distributed on their join keys for co-location, or the fact table should be clustered on its most frequently filtered columns (like date).
    3.  **Check Statistics:** Are table statistics up to date? Out-of-date statistics can lead the query optimizer to make very poor decisions.
    4.  **Model Denormalization (if necessary):** If the join is still slow, and a few key attributes from the large dimension are frequently queried, consider denormalizing those specific attributes directly into the fact table. This is a trade-off: it increases storage but can eliminate a costly join.
    5.  **Materialized Views:** Consider creating a pre-aggregated or pre-joined materialized view if the query patterns are predictable.

**16. Explain data partitioning. What is a common partitioning strategy for a large `fact_sales` table?**

*   **Solution:**
    *   **Data Partitioning:** The process of dividing a large table into smaller, more manageable pieces (partitions) based on a column's value, while still being able to query it as a single table. The database optimizer is aware of the partitions.
    *   **Benefit (Partition Pruning):** When a query includes a filter on the partitioning key, the database can "prune" or ignore all partitions that don't match the filter. This drastically reduces the I/O and the amount of data that needs to be scanned.
    *   **Common Strategy:** For a `fact_sales` table, the most common and effective strategy is to partition by a date key (e.g., `date_key` or `order_date`). This is usually done by `RANGE` on a monthly or daily basis. Most analytical queries will have a date range filter (e.g., "last month's sales," "Q4 sales"), which allows the query engine to scan only the relevant partitions.
    *   **What to look for:** Mention of "partition pruning" is key.

**17. How do you handle late-arriving facts? Describe a technical implementation.**

*   **Solution:** This is a classic, difficult data engineering problem.
    *   **The Problem:** Data from source systems can be delayed. A sales transaction from January 31st might not arrive in the data pipeline until February 2nd. If our nightly load for Jan 31st has already run, this fact will be missed.
    *   **Solution Approach:**
        1.  **Timestamping:** The fact record *must* have two date/timestamps: the event date (when the transaction occurred) and the load date (when it was loaded into the warehouse).
        2.  **Updatable Load Process:** The ETL/ELT process needs to be able to handle this. When loading data for "today," it should also look back a certain window (e.g., 7 days) for records with an event date in that window but a load date of "today."
        3.  **For Snapshot Tables:** This is more complex. If an aggregate or snapshot table has already been built for Jan 31st, it needs to be updated or re-calculated. This can be done by:
            *   **Re-running the aggregation** for the affected periods (e.g., re-calculate all of January's summaries). This is simple but can be expensive.
            *   **Using deltas:** Calculate the impact of the late-arriving fact and apply an update to the aggregate table (e.g., `UPDATE daily_sales SET total_revenue = total_revenue + new_sale_amount WHERE date = '2023-01-31'`). This is more efficient but requires more complex logic.
    *   **What to look for:** Acknowledgment of the problem's difficulty and a clear distinction between handling late-arriving transactional facts vs. updating pre-built aggregates.

**18. Describe a situation where you had to manage schema evolution. A business user wants to add a new reporting attribute to a key dimension. What is your process?**

*   **Solution:** This tests their process and understanding of impact.
    1.  **Impact Analysis (Discovery):**
        *   Where is this new attribute coming from? Is the source data available?
        *   What downstream processes, reports, or dashboards use this dimension? I need to identify everything that could potentially break or be affected.
        *   Talk to the business user: What is the historical requirement? If we add the attribute today, should it be null for all old dimension records? Or do we need to backfill it? This determines the complexity.
    2.  **Development & Testing (in a non-prod environment):**
        *   Modify the ETL/ELT script to pull the new attribute.
        *   Add the new column to the dimension table in the development environment. The `ALTER TABLE` statement is straightforward. Decide on a default value for existing rows (usually `NULL` or `'N/A'`).
        *   If backfilling is required, write and test the backfilling script carefully. This can be resource-intensive.
        *   Run all associated data tests (dbt tests, etc.) to ensure no existing logic has broken. Validate the data in the new column.
    3.  **Deployment:**
        *   Create a deployment plan. This often involves running the `ALTER TABLE` script first, followed by deploying the updated ETL/ELT code.
        *   Communicate the change to all downstream consumers (BI analysts, data scientists).
    4.  **Post-Deployment:** Monitor the next few ETL/ELT runs and check the downstream reports to ensure everything is working as expected.
    *   **What to look for:** A structured, careful process. A cowboy who says "I'll just add the column" is a red flag. The emphasis on impact analysis, communication, and backfilling strategy is crucial for a senior role.

---

### **Category 5: Scenario-Based Design Questions**

These questions require the candidate to synthesize all their knowledge to solve a business problem.

**19. You are tasked with designing a data model for an e-commerce platform to analyze sales and customer behavior. Whiteboard the star schema. Identify the business process, the grain, the facts, and the dimensions.**

*   **Solution:** The candidate should be able to sketch this out.
    *   **Business Process:** Online Sales / Order Fulfillment.
    *   **Grain:** One row per product line item per order.
    *   **Fact Table:** `fact_sales`
        *   **Facts (Measures):** `quantity_ordered`, `unit_price`, `total_line_amount`, `discount_amount`. (Measures should be numeric and additive/semi-additive).
        *   **Foreign Keys:** `date_key`, `customer_key`, `product_key`, `shipping_address_key`, `order_status_key` (foreign key to a junk dimension), and a degenerate dimension `order_number`.
    *   **Dimensions:**
        *   `dim_date`: Standard date dimension with attributes like day, week, month, quarter, year, day_of_week, is_holiday.
        *   `dim_customer`: Customer attributes like `customer_name`, `email`, `sign_up_date`, `customer_segment`. This would likely be an SCD Type 2 dimension.
        *   `dim_product`: Product attributes like `product_name`, `SKU`, `brand`, `category`, `subcategory`.
        *   `dim_shipping_address`: `address_line_1`, `city`, `state`, `zip_code`. This could be part of `dim_customer` but is often broken out for efficiency if customers have many addresses (an outrigger).
    *   **What to look for:** A clear definition of the grain. Identification of additive facts. A logical set of dimensions that support common business questions. Mentioning a degenerate dimension like `order_number` shows deeper understanding.

**20. Now, extend the previous model. The business wants to track user web-clickstream activity to understand the customer journey leading to a sale. How would you model this? Would you use the same data mart?**

*   **Solution:** This tests their ability to model different processes.
    *   This is a **separate business process** (Website Navigation) and requires its own star schema. Trying to force this into the sales fact table would be a mistake because they have different grains.
    *   **Business Process:** Web Clickstream Events.
    *   **Grain:** One row per page view/click event.
    *   **Fact Table:** `fact_web_events`
        *   **Facts:** `duration_on_page_seconds` (semi-additive), `event_count` (always 1).
        *   **Foreign Keys:** `event_date_key`, `event_time_key`, `customer_key` (if logged in), `session_key`, `page_key`. A degenerate dimension would be `session_id`.
    *   **New Dimensions:**
        *   `dim_session`: Attributes of the browsing session, e.g., `device_type`, `browser`, `referral_source`, `landing_page`.
        *   `dim_page`: Attributes of the web page, e.g., `page_url`, `page_type` ('product', 'checkout', 'search').
    *   **Integration:** The key is that `fact_web_events` and `fact_sales` share the **conformed dimension `dim_customer`**. This allows an analyst to select a group of customers who bought a certain product and then "drill across" to see their web journey *before* the purchase.
    *   **What to look for:** The immediate recognition that this needs a separate fact table due to a different grain. The crucial point is explaining how `dim_customer` acts as the conformed dimension to link the two business processes.

---

### **Bonus Rapid-Fire Questions (30+ Total)**

21. What is a "Bus Matrix" and how is it used in requirements gathering?
    *   **A:** A planning tool that maps business processes (rows) to dimensions (columns), showing how they are shared (conformed).

22. What are semi-additive facts? Give an example.
    *   **A:** Facts that can be summed across some dimensions but not others. Example: Account Balance (can't be summed over time, but can be summed across customers).

23. What are non-additive facts?
    *   **A:** Facts that cannot be summed across any dimension, like ratios or percentages. They must be calculated at the BI layer.

24. Why is a dedicated `dim_date` table better than using a `DATE` or `TIMESTAMP` column in the fact table?
    *   **A:** It allows for storing rich business context (fiscal periods, holidays, etc.) without cluttering the fact table. It ensures consistency and simplifies queries.

25. What's the purpose of a staging area in a traditional ETL pipeline?
    *   **A:** An intermediate storage area between data sources and the DWH. Used for data cleansing, transformation, and consolidation before loading.

26. You are designing a DWH for a global company. How do you handle multiple currencies?
    *   **A:** Store all monetary facts in a standard currency (e.g., USD). Provide a separate `dim_currency` table with daily exchange rates to allow conversion to local currencies at query time.

27. What is a "Chasm Trap" in dimensional modeling?
    *   **A:** A query that incorrectly double-counts or misinterprets results when joining two fact tables that don't share a common dimension at the same grain. Bridge tables can help solve this.

28. How would you model recursive hierarchies, like an employee/manager relationship?
    *   **A:** In the `dim_employee` table, add a `manager_key` column that is a foreign key to the same table's `employee_key`. This is hard for standard SQL, so often a flattened hierarchy or bridge table is used for BI tools.

29. What is the role of metadata in a data warehouse?
    *   **A:** It's "data about data." It describes table schemas, ETL job logs, data lineage, business definitions, and quality rules. It's critical for governance and usability.

30. In dbt, what is the difference between a `view`, a `table`, and an `incremental` materialization?
    *   **A:** Tests modern tooling. `view` = a view in the DB. `table` = recreated on every run. `incremental` = only new/updated rows are processed, which is efficient for large tables.

31. If you saw a fact table with a string column in it, what would be your immediate concern?
    *   **A:** High cardinality descriptive attributes don't belong in fact tables. They should be in a dimension. It massively inflates the size of the fact table and slows down queries. The exception is a very low-cardinality code that is part of a junk dimension.

32. What's the difference between a "measure" and an "attribute"?
    *   **A:** A fundamental concept. Measures are the numeric, quantitative data in a fact table (e.g., `sale_amount`). Attributes are the descriptive, contextual data in a dimension table (e.g., `customer_name`). We measure "measures" across "attributes."
