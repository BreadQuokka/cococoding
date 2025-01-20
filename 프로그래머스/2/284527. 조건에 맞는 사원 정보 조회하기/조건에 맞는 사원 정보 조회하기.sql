-- 코드를 작성해주세요
select sum(distinct G.score) as score,
e.emp_no, e.emp_name, e.position, e.email
from HR_DEPARTMENT as D
join hr_employees as E on D.Dept_id= E.Dept_id
join hr_grade as G on E.Emp_no = G.emp_no and year="2022"
group by E.emp_NO
order by sum(G.score) desc
limit 1
