-- 코드를 입력하세요
SELECT hour(datetime) as hour, count( distinct animal_id) as count
from animal_outs as a
where hour(datetime)>=9 and hour(datetime)<20
group by hour(datetime)
order by hour(datetime) asc
