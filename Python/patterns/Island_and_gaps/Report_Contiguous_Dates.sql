-- Table: Failed

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | fail_date    | date    |
-- +--------------+---------+
-- fail_date is the primary key (column with unique values) for this table.
-- This table contains the days of failed tasks.
 

-- Table: Succeeded

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | success_date | date    |
-- +--------------+---------+
-- success_date is the primary key (column with unique values) for this table.
-- This table contains the days of succeeded tasks.
 

-- A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

-- Write a solution to report the period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

-- period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

-- Return the result table ordered by start_date.



with cte as (
    select fail_date as date, "Failed" as status
    from Failed
    union
    select success_date date, "Success" as status
    from Succeeded
),
input_tab as (
    select *
    from cte
    where date between '2019-01-01' and '2019-12-31'
    order by date
),
gaps as (
    select date,
        status,
        date_sub(date, Interval row_number() over(partition by status order by date) day) as gap
    from input_tab
)
select case when status = "Success" then "succeeded" else "failed" end as period_state,
       start_date,
       end_date
from(
    select status,
        gap,
        min(date) as start_date,
        max(date) as end_date
    from gaps
    group by status, gap
)tab
