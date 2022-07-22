--https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

with earliest as (
    select user_id, timestamp::date as dt, max(timestamp) as first_time
    from facebook_web_log
    where action = 'page_load'
    group by user_id, dt
),
latest as (
    select user_id, timestamp::date as dt, min(timestamp) as last_time
    from facebook_web_log
    where action = 'page_exit'
    group by user_id, dt
)
select latest.user_id as user_id, AVG(last_time - first_time)
from latest
join earliest on latest.user_id = earliest.user_id and latest.dt = earliest.dt
group by latest.user_id

-- решение без join
with diffTable as (
    select user_id, timestamp::date as day, 
    min(case when action = 'page_exit' then timestamp else null end) - max(case when action = 'page_load' then timestamp else null end) as interval
    from facebook_web_log
    group by user_id, day
)
select user_id, avg(interval) as avg_session_time
from diffTable
where interval is not null
group by user_id
