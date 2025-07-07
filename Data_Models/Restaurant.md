Of course. Here is a detailed data model for a Restaurant Management System, designed specifically for OLAP (Online Analytical Processing) to analyze sales and inventory.

The model will be based on the **Star Schema** methodology, which is the industry standard for OLAP and data warehousing. It consists of central **Fact tables** containing quantitative business measurements (the "facts") and is surrounded by **Dimension tables** that provide descriptive context (the "who, what, where, when, why").

This design separates the two core business processes—Sales and Inventory—into two distinct Star Schemas that share common dimensions. This is known as a **Galaxy Schema** or **Fact Constellation**.

---

### **High-Level Design Overview**

*   **Core Schemas:** We will design two primary star schemas:
    1.  **Sales Schema:** To analyze sales performance, profitability, staff performance, and customer ordering patterns.
    2.  **Inventory Schema:** To track the flow of ingredients, manage stock levels, analyze wastage, and forecast purchasing needs.
*   **Shared Dimensions:** Both schemas will share dimensions like `Dim_Date`, `Dim_Menu_Item`, and `Dim_Ingredient` to allow for integrated analysis (e.g., "How did the sales of a specific menu item impact our inventory of its key ingredients?").
*   **Granularity:**
    *   The grain of the `Fact_Sales` table will be **one line item per customer order**.
    *   The grain of the `Fact_Inventory_Transactions` table will be **one inventory event** (e.g., purchase, consumption, wastage).

---

### **1. The Sales Star Schema**

This schema is centered around the `Fact_Sales` table and is used to answer questions like:
*   What are our top-selling menu items by revenue and quantity?
*   Which waiter generates the most revenue?
*   What is the average order value during lunch vs. dinner?
*   How does a promotion on appetizers affect the sales of main courses?



#### **Fact Table: `Fact_Sales`**

This is the central table containing all the performance metrics for sales.

| Column Name            | Data Type      | Description                                                                                              | Example         |
| ---------------------- | -------------- | -------------------------------------------------------------------------------------------------------- | --------------- |
| **`Date_Key`**         | `INTEGER` (FK) | Foreign key to `Dim_Date`. The date of the sale.                                                         | `20231115`      |
| **`Time_Key`**         | `INTEGER` (FK) | Foreign key to `Dim_Time`. The time of the sale.                                                         | `1930`          |
| **`Menu_Item_Key`**    | `INTEGER` (FK) | Foreign key to `Dim_Menu_Item`. The item that was sold.                                                  | `101`           |
| **`Staff_Key`**        | `INTEGER` (FK) | Foreign key to `Dim_Staff`. The waiter/cashier who handled the order.                                    | `5`             |
| **`Table_Key`**        | `INTEGER` (FK) | Foreign key to `Dim_Table`. The table where the order was placed.                                        | `12`            |
| **`Payment_Method_Key`** | `INTEGER` (FK) | Foreign key to `Dim_Payment_Method`. How the final bill was paid.                                        | `2`             |
| `Order_ID`             | `VARCHAR(50)`  | **Degenerate Dimension**. The original order ID to group all line items from a single transaction.       | `ORD-2023-A45B` |
| `Quantity_Sold`        | `INTEGER`        | The number of units of this menu item sold in this line item.                                            | `2`             |
| `Unit_Price`           | `DECIMAL(10, 2)` | The price of a single unit of the menu item at the time of sale.                                         | `15.99`         |
| `Discount_Amount`      | `DECIMAL(10, 2)` | The total discount applied to this specific line item.                                                   | `3.20`          |
| `Line_Item_Total`      | `DECIMAL(10, 2)` | The final revenue for this line item. Calculated as `(Quantity * Unit_Price) - Discount_Amount`.         | `28.78`         |
| `Cost_Of_Goods_Sold`   | `DECIMAL(10, 2)` | The total cost of ingredients used for this line item. **Crucial for profitability analysis.**           | `7.50`          |

---

### **2. The Inventory Star Schema**

This schema is centered around `Fact_Inventory_Transactions` and is used to answer questions like:
*   What is our current stock level for each ingredient?
*   How much of each ingredient was wasted last month?
*   Which supplier provides the best-priced ingredients?
*   What is the consumption rate of flour, and when should we reorder?



#### **Fact Table: `Fact_Inventory_Transactions`**

This table tracks every movement of an ingredient.

| Column Name                   | Data Type      | Description                                                                                                   | Example           |
| ----------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------- | ----------------- |
| **`Transaction_Date_Key`**    | `INTEGER` (FK) | Foreign key to `Dim_Date`. The date the inventory transaction occurred.                                       | `20231114`        |
| **`Ingredient_Key`**          | `INTEGER` (FK) | Foreign key to `Dim_Ingredient`. The ingredient being tracked.                                                | `502`             |
| **`Transaction_Type_Key`**    | `INTEGER` (FK) | Foreign key to `Dim_Inventory_Transaction_Type`. Describes the event (Purchase, Consumption, Wastage).        | `1`               |
| **`Supplier_Key`**            | `INTEGER` (FK) | Foreign key to `Dim_Supplier`. The supplier for purchase transactions (nullable for others).                  | `25`              |
| **`Menu_Item_Key`**           | `INTEGER` (FK) | Foreign key to `Dim_Menu_Item`. Links consumption to a specific menu item sale (nullable for others).         | `101`             |
| `Quantity_Change`             | `DECIMAL(10, 3)` | The amount of ingredient affected. **Positive for additions (purchase), negative for reductions (consumption, wastage).** | `-0.150` (kg)     |
| `Unit_Cost`                   | `DECIMAL(10, 2)` | The cost per unit of the ingredient for this transaction.                                                     | `9.50` (per kg)   |
| `Transaction_Total_Cost`      | `DECIMAL(10, 2)` | The total cost of this transaction. Calculated as `Quantity_Change * Unit_Cost`.                              | `-1.43`           |

---

### **3. Dimension Tables (Shared and Specific)**

These tables provide the descriptive context for the facts.

#### `Dim_Date` (Conformed/Shared Dimension)
*   **`Date_Key` (PK)** `INTEGER` - e.g., `20231115`
*   `Full_Date` `DATE` - e.g., `2023-11-15`
*   `Day_Of_Week` `VARCHAR(10)` - e.g., 'Wednesday'
*   `Day_Number_In_Month` `INTEGER` - e.g., `15`
*   `Month_Name` `VARCHAR(10)` - e.g., 'November'
*   `Month_Number_In_Year` `INTEGER` - e.g., `11`
*   `Calendar_Quarter` `INTEGER` - e.g., `4`
*   `Calendar_Year` `INTEGER` - e.g., `2023`
*   `Is_Weekend` `BOOLEAN`
*   `Is_Holiday` `BOOLEAN`

#### `Dim_Time`
*   **`Time_Key` (PK)** `INTEGER` - e.g., `1930`
*   `Full_Time` `TIME` - e.g., `19:30:00`
*   `Hour` `INTEGER` - e.g., `19`
*   `Minute` `INTEGER` - e.g., `30`
*   `Time_Period` `VARCHAR(20)` - e.g., 'Dinner', 'Lunch Rush', 'Late Night'

#### `Dim_Menu_Item` (Conformed/Shared Dimension)
*   **`Menu_Item_Key` (PK)** `INTEGER` - e.g., `101`
*   `Item_Name` `VARCHAR(100)` - e.g., 'Classic Beef Burger'
*   `Item_Description` `TEXT`
*   `Category` `VARCHAR(50)` - e.g., 'Main Course'
*   `Sub_Category` `VARCHAR(50)` - e.g., 'Burgers'
*   `Is_Vegetarian` `BOOLEAN`
*   `Is_Gluten_Free` `BOOLEAN`
*   `Current_Price` `DECIMAL(10, 2)`

#### `Dim_Ingredient` (Conformed/Shared Dimension)
*   **`Ingredient_Key` (PK)** `INTEGER` - e.g., `502`
*   `Ingredient_Name` `VARCHAR(100)` - e.g., 'Ground Beef (80/20)'
*   `Category` `VARCHAR(50)` - e.g., 'Meat'
*   `Unit_Of_Measure` `VARCHAR(10)` - e.g., 'kg', 'litre', 'each'

#### `Dim_Staff`
*   **`Staff_Key` (PK)** `INTEGER` - e.g., `5`
*   `Staff_ID` `VARCHAR(20)` - Natural key from the HR system.
*   `Staff_Name` `VARCHAR(100)`
*   `Role` `VARCHAR(50)` - e.g., 'Waiter', 'Chef', 'Manager'
*   `Hire_Date` `DATE`
*   `Row_Effective_Date` `DATE` - For Slowly Changing Dimensions (SCD Type 2)
*   `Row_Expiration_Date` `DATE` - For SCD Type 2
*   `Is_Current` `BOOLEAN` - For SCD Type 2

#### `Dim_Table`
*   **`Table_Key` (PK)** `INTEGER` - e.g., `12`
*   `Table_Number` `VARCHAR(10)` - e.g., '12' or 'Patio-3'
*   `Location` `VARCHAR(50)` - e.g., 'Main Dining Room', 'Patio', 'Bar'
*   `Capacity` `INTEGER`

#### `Dim_Supplier`
*   **`Supplier_Key` (PK)** `INTEGER` - e.g., `25`
*   `Supplier_Name` `VARCHAR(100)` - e.g., 'City Fresh Produce'
*   `Contact_Person` `VARCHAR(100)`
*   `City` `VARCHAR(50)`
*   `Country` `VARCHAR(50)`

#### `Dim_Payment_Method`
*   **`Payment_Method_Key` (PK)** `INTEGER` - e.g., `2`
*   `Method_Name` `VARCHAR(50)` - e.g., 'Credit Card', 'Cash', 'Mobile Pay'
*   `Card_Type` `VARCHAR(50)` - e.g., 'Visa', 'Mastercard', 'AMEX', `NULL`

#### `Dim_Inventory_Transaction_Type`
*   **`Transaction_Type_Key` (PK)** `INTEGER` - e.g., `1`
*   `Transaction_Type_Name` `VARCHAR(50)` - e.g., 'Purchase', 'Consumption - Sale', 'Wastage - Spoilage', 'Manual Adjustment'
*   `Type_Multiplier` `INTEGER` - `1` for additions, `-1` for subtractions.

---

### **4. The Bridge Table: Linking Recipes**

To connect menu items with the ingredients they consume, a **bridge table** is essential. This table defines the recipe for each menu item.

#### `Bridge_Menu_Item_Ingredient`
This is a factless fact table that holds the many-to-many relationship between menu items and ingredients.

| Column Name         | Data Type      | Description                                                 |
| ------------------- | -------------- | ----------------------------------------------------------- |
| **`Menu_Item_Key`** | `INTEGER` (FK) | Foreign key to `Dim_Menu_Item`.                             |
| **`Ingredient_Key`**| `INTEGER` (FK) | Foreign key to `Dim_Ingredient`.                            |
| `Quantity_Required` | `DECIMAL(10, 3)` | The standard quantity of the ingredient needed for one menu item. |

**Example Rows:**
| Menu_Item_Key | Ingredient_Key | Quantity_Required |
|---------------|----------------|-------------------|
| 101           | 502            | 0.150 (kg beef)   |
| 101           | 610            | 1.000 (each bun)  |
| 101           | 704            | 0.020 (kg cheese) |

This bridge table is used during the ETL (Extract, Transform, Load) process to:
1.  **Calculate `Cost_Of_Goods_Sold`** for `Fact_Sales` by summing the costs of all required ingredients.
2.  **Generate `Consumption` rows** in `Fact_Inventory_Transactions` every time a menu item is sold.

---

### **Design Considerations & Best Practices**

*   **Slowly Changing Dimensions (SCD):** The `Dim_Staff` table is a prime candidate for SCD Type 2. If a waiter is promoted to a manager, you would expire their old "Waiter" record and create a new "Manager" record with the same `Staff_ID`. This ensures that historical sales reports correctly attribute sales to their role at that time.
*   **Degenerate Dimensions:** `Order_ID` in `Fact_Sales` is a degenerate dimension. It’s a transactional ID that has no attributes of its own but is useful for grouping fact rows (e.g., to calculate the total value of a single order).
*   **ETL Process:** A robust ETL process is critical. It will be responsible for reading data from the transactional (OLTP) restaurant system, looking up keys in the dimension tables, performing calculations (like `Cost_Of_Goods_Sold`), and loading the data into the fact tables.