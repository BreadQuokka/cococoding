-- 코드를 입력하세요
SELECT fo.product_id, fp.product_name , sum(fo.amount)*fp.price as total_sales
FROM FOOD_PRODUCT AS FP
JOIN FOOD_ORDER AS FO
ON FP.PRODUCT_ID = FO.PRODUCT_ID
where fo.produce_date like("2022-05%")
group by fo.product_id, fp.product_name 
order by total_sales desc, fo.product_id