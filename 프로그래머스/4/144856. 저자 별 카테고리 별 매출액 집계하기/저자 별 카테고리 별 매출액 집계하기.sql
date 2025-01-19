-- 코드를 입력하세요
SELECT BOOK.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY, sum(book.price*book_sales.sales) as total_sales
FROM BOOK
JOIN AUTHOR 
ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
JOIN BOOK_SALES
ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID 
where book_sales.sales_date like "2022-01%"
GROUP BY BOOK.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY
order by book.author_id, book.category desc