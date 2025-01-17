-- 코드를 입력하세요
SELECT distinct r.rest_id, r.rest_name,r.food_type, r.favorites, r.address,sr.avgs
from rest_info as r
join(select rest_id, round(avg(review_score),2) as avgs
    from rest_review sR 
    group by rest_id) as sr
on r.rest_id = sr.rest_id
join rest_review as rr
on rr.rest_id = r.rest_id
where r.address like "서울%"
order by avgs desc, favorites desc
