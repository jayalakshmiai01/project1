create database rapido;
show databases;
use rapido;
drop database rapido;
select * from rapido_reg_tbl;

create table rapido_reg_tbl
(
user_id int not null primary key, first_name varchar(50)not null, middle_name varchar(50), last_name varchar(50)not null,dob date,ph_no long, user_name varchar(50) not null unique, password varchar(50) not null
);

create table rapido_login_tbl
(
login_id int not null primary key, user_name varchar(50) not null, password varchar(50) not null, new_password varchar(50) not null, user_id int not null,
 foreign key(user_id)references rapido_reg_tbl(user_id)
);

create table rapido_booking_tbl
(
booking_id int not null, booking_name varchar(50)not null, booking_vehicle varchar(50) not null, pickup_address varchar(50) not null, user_id int not null, login_id int not null,
foreign key(user_id)references rapido_reg_tbl(user_id),
foreign key(login_id)references rapido_login_tbl(login_id)
);

select * from rapido_reg_tbl;
select * from rapido_login_tbl;
select * from rapido_booking_tbl;


insert into rapido_reg_tbl values(1,'jaya','lakshmi','R',2001-2-6,1234566,'jayar','Jeevi'),
(2,'priya','pri','l',2002-6-7,24356789,'priyal','pril'),(3,'kayal','vizhi','k',2000-9-8,0987557,'kayalk','kayall');

insert into rapido_login_tbl values(123,'jayalakshmi','jaya','jayakavi',1);(321,'akila','akilav','aki',2),(231,'priya','priyal','priyaa',3);

insert into rapido_booking_tbl values(10,'kavi','enfield','trichy',100,200),(11,'sanjai','activa','tanjore',101,201),(12,'bharathi','splender','trichy',102,202);

12:55:33	insert into rapido_login_tbl values(123,'jayalakshmi','jaya','jayakavi',1),(321,'akila','akilav','aki',2),(231,'priya','priyal','priyaa',3)	Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`rapido`.`rapido_login_tbl`, CONSTRAINT `rapido_login_tbl_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `rapido_reg_tbl` (`user_id`))	0.000 sec
