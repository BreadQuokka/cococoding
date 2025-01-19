-- 코드를 입력하세요
SELECT mcdp_cd as '진료과 코드',count(distinct APNT_NO) as '5월예약건수'
from appointment as a
where apnt_ymd like "2022-05%"
group by mcdp_cd
order by count(distinct APNT_NO), mcdp_cd