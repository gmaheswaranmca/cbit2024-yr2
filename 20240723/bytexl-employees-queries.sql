-- mysql version 
SELECT version();

-- All tables
show tables;

--show all departments
select * from departments;
-- total number of departments 
select count(*) from departments;
--query department by id
select * from departments where department_id=101;
--query department by name
select * from departments where department_name='Engineering';
-- show all employees
-- total number of employees
-- query employee by id 
-- query employee by name 
-- count by gender
select gender, count(*) from employees group by gender;
-- count by position
select position, count(*) from employees group by position;
-- employees with most leaves 
select e.first_name, count(*) leaves_count 
from employees e 
    inner join leaves v on(e.employee_id=v.employee_id)
group by e.employee_id
order by 2 desc
limit 1;
-- top salary 
select max(amount) top_sal from salaries;
-- top salaried  
select e.first_name, s.amount salary 
from employees e 
    inner join salaries s on(e.employee_id=s.employee_id)  
order by 2 desc 
limit 1;
-- second highest salary 
select e.first_name, s.amount salary 
from employees e 
    inner join salaries s on(e.employee_id=s.employee_id)  
order by 2 desc 
limit 2,1; -- firs 2 is the rows to be skipped, second 1 is number of rows to be displayed after skip


Host ocdb.app
Port 5051
Database db_42kvxh2ws
Username user_42kvxh2ws
Password p42kvxh2ws