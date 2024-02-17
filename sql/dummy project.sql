use dummy;
show databases;

CREATE TABLE employee (
emp_id INT PRIMARY KEY,
ename VARCHAR(30),
job_desc VARCHAR(20),
salary INT );

INSERT INTO employee VALUES(1,'Ram','ADMIN',1000000);
INSERT INTO employee VALUES(2,'Harini','MANAGER',2500000);
INSERT INTO employee VALUES(3,'George','SALES',2000000);
INSERT INTO employee VALUES(4,'Ramya','SALES',1300000);
INSERT INTO employee VALUES(5,'Meena','HR',2000000);
INSERT INTO employee VALUES(6,'Ashok','MANAGER',3000000);


INSERT INTO employee VALUES(7,'Abdul','HR',2000000);
INSERT INTO employee VALUES(8,'Ramya','ENGINEER',1000000);
INSERT INTO employee VALUES(9,'Raghu','CEO',8000000);
INSERT INTO employee VALUES(10,'Arvind','MANAGER',2800000);
INSERT INTO employee VALUES(11,'Akshay','ENGINEER',1000000);
INSERT INTO employee VALUES(12,'John','ADMIN',2200000);
INSERT INTO employee VALUES(13,'Abinaya','ENGINEER',2100000);

select * from employee where emp_id=2;
SELECT emp_id,ename,salary FROM employee
WHERE salary>2000000;

select emp_id,ename,salary from employee where salary<2000000;


SELECT emp_id,ename,salary FROM employee
WHERE salary<2600000 AND job_desc = 'MANAGER';

SELECT * FROM employee
WHERE job_desc='ADMIN' OR job_desc='HR';

SELECT * FROM employee
WHERE job_desc IN ('ADMIN','HR');

SELECT * FROM employee
WHERE job_desc NOT IN ('MANAGER','CEO');

SELECT * FROM employee
WHERE salary BETWEEN 2000000 AND 3000000
LIMIT 5;

SELECT * FROM employee
LIMIT 5;  