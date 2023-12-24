select *
from shipping.shipment -- отправка (ship_id, cust_id, weight, truck_id, driver_id, city_id, ship_date)

select *
from shipping.city -- город (city_id, city_name, state, population, area)

select *
from shipping.customer -- клиент (cust_id, cust_name, annual_revenue, cust_type, address, zip, phone, city_id)


select *
from shipping.driver -- водитель (driver_id, first_name, last_name, address, zip_code, phone, city_id)


select *
from shipping.truck -- грезовик (truck_id, make, model_year)


Напишите запрос, который выдаёт сводную статистику по городам: количество клиентов (обозначьте как customers), заказов (обозначьте как shipments) и водителей (обозначьте как drivers).
Оставьте города, в которых хотя бы один из этих показателей ненулевой, и отсортируйте по первому столбцу.
Используйте left join для таблицы с городами.
В результате должна быть выведена таблица со следующими полями: 
city_name, customers, shipments, drivers (именно в таком порядке).

select c.city_name, count(distinct cu.cust_id) customers, count(s.ship_id) shipments, count(distinct d.driver_id) drivers
from shipping.shipment s
    left join shipping.customer cu on s.city_id = cu.city_id
    left join shipping.city c on s.city_id = c.city_id
    left join shipping.driver d ON s.driver_id = d.driver_id
group by c.city_name
having (COUNT(DISTINCT cu.cust_id) + COUNT(s.ship_id) + COUNT(DISTINCT d.driver_id)) != 0 
order by c.city_name


select 
        c.zip,
        count(distinct c.cust_id) customers,
        count(distinct d.driver_id) drivers
    from 
        shipping.customer c
            FULL join shipping.driver d on c.zip = d.zip_code
    group by 1
    having count(distinct c.cust_id) + count(distinct d.driver_id) >0
    order by  count(distinct c.cust_id) + count(distinct d.driver_id)  desc
    
    
select 
        count(*)
    from shipping.customer c
        left join  shipping.driver d on c.zip = d.zip_code
    where d.zip_code is null 
    
    
    select 
        count(*)
    from  shipping.driver d
        left join  shipping.customer c on c.zip = d.zip_code
    where c.zip is null
    
    
    select 
        coalesce(c.zip,d.zip_code) zip,
        count(distinct c.cust_id) customers,
        count(distinct d.driver_id) drivers
    from 
        shipping.customer c
            full outer join shipping.driver d on c.zip = d.zip_code
    group by 1
    having count(distinct c.cust_id) + count(distinct d.driver_id) >0
    order by  count(distinct c.cust_id) + count(distinct d.driver_id)  desc
    
    
    Напишите запрос, который выведет имена всех водителей и их телефоны. 
    В случае, если телефон не заполнен, укажите номер из одних девяток в том же формате. 
    Отсортируйте по имени водителя в алфавитном порядке. 
    В результате выполнения запроса должна быть выведена таблица со следующими полями: 
    first_name, phone (именно в таком порядке).
    
    select 
        d.first_name,
        coalesce(c.phone,d.phone,'(999)999-9999') phone
    from 
        shipping.customer c
            right join shipping.driver d on c.zip = d.zip_code
    group by 1, 2
    -- having count(distinct c.cust_id) + count(distinct d.driver_id) > 0
    order by d.first_name;

Напишите запрос, который выдаёт сводную статистику по городам (для идентификации используйте city_id):
количество клиентов (обозначьте как customers), заказов (обозначьте как shipments) и водителей (обозначьте как drivers). 
Не используйте таблицу shipping.city. 
Оставьте города, в которых хотя бы один из этих показателей ненулевой, отсортируйте по столбцу с id города. 
В результате должна быть выведена таблица со следующими полями: 
city_id, customers, shipments, drivers (именно в таком порядке).

    select 
        coalesce(s.city_id, c.city_id, d.city_id) city_id,
        count(distinct c.cust_id) customers,
        count(distinct s.ship_id) shipments,
        count(distinct d.driver_id) drivers
    from 
        shipping.shipment s
            full outer join shipping.customer c on c.city_id = s.city_id
            full outer join shipping.driver d on c.city_id = d.city_id
    group by 1
    having count(distinct c.cust_id) + count(distinct s.ship_id) + count(distinct d.driver_id) > 0
    order by  coalesce(s.city_id, c.city_id, d.city_id)
    
    
   Этим запросом мы присоединим все записи с клиентами к каждой записи водителя: 
    select 
            *
        from 
            shipping.driver 
                cross join shipping.customer
                
Альтернативный синтаксис для CROSS JOIN — указание всех таблиц в разделе from через запятую. 
Это устаревший формат, так как он менее читабельный. 
Тем не менее, такой синтаксис поддерживается большинством СУБД.

select 
            *
        from 
            shipping.driver,shipping.customer
            
Также обычный JOIN может перемножить строки, если вместо условия соединения указать логическое true.

select 
            *
        from 
            shipping.driver join shipping.customer on true
            
            
Напишите запрос, который выводит все возможные уникальные пары даты доставки и имени водителя, 
упорядоченные по дате и имени по возрастанию. 
В результате работы запроса должна быть выведена таблица со следующими полями: 
ship_date, first_name (именно в таком порядке).

select distinct s.ship_date, d.first_name
    from 
        shipping.driver d
            cross join shipping.shipment s
order by s.ship_date, d.first_name



CROSS JOIN иногда используют вместо INNER JOIN. 
Для этого нужно поместить условие объединения в where. 
Первый пример из блока INNER JOIN можно записать вот так:

select 
	count(*) -- раздел select остаётся неизменным
from 
	information_schema."tables" t -- указываем первую таблицу, не забываем дать alias
		cross join information_schema.columns c -- пишем join на вторую таблицу 
where  t.table_name = c.table_name 
			and t.table_schema = c.table_schema 
-- в разделе where пишется логическое условие любой сложности