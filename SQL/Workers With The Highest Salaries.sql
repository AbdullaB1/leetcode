-- https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1

select worker_title
from title t
join worker w on t.worker_ref_id = w.worker_id
where salary = (select max(salary) from worker)
