-- Table: Stadium

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | visit_date    | date    |
-- | people        | int     |
-- +---------------+---------+
-- visit_date is the column with unique values for this table.
-- Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
-- As the id increases, the date increases as well.
 

-- Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

-- Return the result table ordered by visit_date in ascending order.

with filtered as (
    select id,
        visit_date,
        people
    from Stadium
    where people >= 100
),
gaps as (
    select id,
        visit_date,
        people,
        id - row_number() over(order by id) as gap
    from filtered
),
consec as (
    select gap
    from gaps
    group by gap
    having count(*) >= 3
)
select  a.id,
        a.visit_date,
        a.people
from gaps a join consec b
on a.gap = b.gap
