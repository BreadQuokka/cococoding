# -- 코드를 입력하세요
# ANIMAL_ID 기준으로 join. 근데 이름이 널값이 있을수도 있으니 full outer join 시행. 
# 이후 out 테이블의 datetime 과 in 테이블의 datetime 을 비교해서 만약 in 보다 out 데이트타임이 앞섰다면 오입력으로 간주하고 이를 where절에서 서브쿼리로 조회

SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS as INS
inner join ANIMAL_OUTS AS OUTS
on ins.animal_id = outs.animal_id
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME

