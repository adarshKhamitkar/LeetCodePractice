/*
Table: Teams

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| team_id       | int      |
| team_name     | varchar  |
+---------------+----------+
team_id is the column with unique values of this table.
Each row of this table represents a single football team.
 

Table: Matches

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| host_team     | int     |
| guest_team    | int     | 
| host_goals    | int     |
| guest_goals   | int     |
+---------------+---------+
match_id is the column of unique values of this table.
Each row is a record of a finished match between two different teams. 
Teams host_team and guest_team are represented by their IDs in the Teams table (team_id), and they scored host_goals and guest_goals goals, respectively.
 

You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

The result format is in the following example.

 

Example 1:

Input: 
Teams table:
+-----------+--------------+
| team_id   | team_name    |
+-----------+--------------+
| 10        | Leetcode FC  |
| 20        | NewYork FC   |
| 30        | Atlanta FC   |
| 40        | Chicago FC   |
| 50        | Toronto FC   |
+-----------+--------------+
Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | host_team    | guest_team    | host_goals  | guest_goals  |
+------------+--------------+---------------+-------------+--------------+
| 1          | 10           | 20            | 3           | 0            |
| 2          | 30           | 10            | 2           | 2            |
| 3          | 10           | 50            | 5           | 1            |
| 4          | 20           | 30            | 1           | 0            |
| 5          | 50           | 30            | 1           | 0            |
+------------+--------------+---------------+-------------+--------------+
Output: 
+------------+--------------+---------------+
| team_id    | team_name    | num_points    |
+------------+--------------+---------------+
| 10         | Leetcode FC  | 7             |
| 20         | NewYork FC   | 3             |
| 50         | Toronto FC   | 3             |
| 30         | Atlanta FC   | 1             |
| 40         | Chicago FC   | 0             |
+------------+--------------+---------------+
*/

with points_tab as (
select *,
       sum(host_points) over (partition by host_team) as host_score,
        sum(guest_points) over (partition by guest_team) as guest_score
from (select match_id,
       host_team,
       guest_team,
       host_goals,
       guest_goals,
       case when host_goals > guest_goals then 3 
            when host_goals = guest_goals then 1 else 0 end as host_points,
       case when guest_goals > host_goals then 3 
            when guest_goals = host_goals then 1 else 0 end as guest_points
        from Matches)tab
)
  
select h.team_id,h.team_name, (h.host_score + g.guest_score) as num_points
from (select distinct t.team_id,t.team_name,case when p.host_team is not null then p.host_score else 0 end host_score
from Teams t left join points_tab p on t.team_id = p.host_team
order by host_score desc)h join 
(select distinct t.team_id,t.team_name,case when p.guest_team is not null then p.guest_score else 0 end guest_score
from Teams t left join points_tab p on t.team_id = p.guest_team
order by host_score desc)g on h.team_id = g.team_id
order by num_points desc, h.team_id
