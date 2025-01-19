-- 코드를 입력하세요
SELECT u.user_id, u.nickname, sum(g.price) as total_sales
from (select *
    from used_goods_board
    where status = "DONE") as g
    join used_goods_user as u
    on g.writer_id = u.user_id
    
group  by u.user_id, u.nickname
having sum(g.price)>=700000
order by total_sales
