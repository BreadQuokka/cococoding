-- 코드를 입력하세요
SELECT animal_type, count(distinct animal_id) as "count"
from animal_ins
where animal_type ="cat" or animal_type = "dog"
group by animal_type 
order by animal_type