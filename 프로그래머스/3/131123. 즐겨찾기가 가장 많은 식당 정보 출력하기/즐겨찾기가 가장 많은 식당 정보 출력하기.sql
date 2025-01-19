-- 코드를 입력하세요
SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
from rest_info as r
join (select food_type, max(favorites) as ma
     from rest_info
     group by food_type) as j 
on r.food_type = j.food_type
where r.favorites = j.ma
order by r.food_type desc