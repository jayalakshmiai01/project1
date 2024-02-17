create database amazon;
show databases;
use amazon;
drop database ai_sample_db;
drop database ai_sample_dbs;
drop database ai_sample_db12;
create table customer(
id int not null primary key,
name varchar(50),
ph_no long,
location varchar(50),
product varchar(50)
);
select * from customer;

drop table customer;

describe customer;

alter table customer add otp long;

alter table customer drop otp;

insert into customer values( 123,'jaya',23456789,'trichy','headphones');
insert into customer values(124,'priya',234567809,'tanjore','laptop');

insert into customer values(125,'aki',9876543,'chennai','phone'),(126,'mala',5678234,'trichy','mobilecase');

insert into customer (id,name,ph_no,location,product)values(321,'kayal',6789234,'karur','battery'),(231,'surya',09876543,'cbe','tab');

select * from customer;

empty values


select id,name from customer;

SELECT id,name,location FROM customer
WHERE id=123;

SELECT id,name,location FROM customer
WHERE id>123;

SELECT id,name,ph_no FROM customer
WHERE id<125;

SELECT id,name,product FROM customer
WHERE id<125 AND location = 'trichy';



SELECT * FROM customer
WHERE location='trichy' OR location='tanjore';

SELECT * FROM customer
WHERE location IN ('chennai','trichy');

SELECT * FROM customer
WHERE location NOT IN ('chennai','trichy');

select * from customer limit 3;
select * from customer where id between 123 and 126 limit 2;


select * from customer where name like 'a%';
select * from customer where name like '%a';
select * from customer where name like 'S%a';
select * from customer where name like '__r%';
select * from customer where name like 'k\%';

error

update customer set product="charger";
update customer set product="charger" where product="battery";
update customer set product="charger" where id=123;
select * from customer;


error

delete from customer;
delete from customer where name="surya";

select distinct location from customer;

select * from customer order by id;
select * from customer order by id asc;
select * from customer order by id desc;
select * from customer where location="trichy" order by id;
select * from customer order by id,name;

select * from customer order by (case name
when 'priya' then 1
when 'kayal' then 2
when 'jaya' then 3
when 'aki' then 4
when 'mala' then 5
when 'surya' then 6
end);

