-- 코드를 입력하세요
# DSD
SELECT WAREHOUSE_ID, WAREHOUSE_NAME,ADDRESS,IFNULL(FREEZER_YN,"N")AS FREEZER_YN
FROM FOOD_WAREHOUSE
where address LIKE("경기%")
ORDER BY WAREHOUSE_ID