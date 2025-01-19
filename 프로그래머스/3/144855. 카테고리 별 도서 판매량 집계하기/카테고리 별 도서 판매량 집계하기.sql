-- 코드를 입력하세요
SELECT b.category, sum(bs.sales) as total_sales
from book as b
join (select *
      from book_sales
      where sales_date like "2022-01%") as bs
on b.book_id = bs.book_id
group by b.category
order by category