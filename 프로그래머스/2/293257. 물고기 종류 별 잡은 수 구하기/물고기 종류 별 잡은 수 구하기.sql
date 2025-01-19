-- 코드를 작성해주세요
select count(i.fish_type) as fish_count,n.fish_name
from fish_info as i
join fish_name_info as n
on i.fish_type = n.fish_type
group by i.fish_type,n.fish_name
order by fish_count desc