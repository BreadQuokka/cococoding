-- 코드를 입력하세요
SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth,"%Y-%m-%d") as date_of_birth
FROM member_profile
WHERE month(date_of_birth)=3 and TLNO is not null and gender = 'W'
order by member_id