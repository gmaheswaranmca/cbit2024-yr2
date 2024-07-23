sample data sets from nimbus:  - mysql
    "employees"

select * from employees;
select * from departments;
select * from leaves;
select * from salaries;

selectors                               : columns, expressions, constant : operators + - * / 
tables selectors                        : table[s in join] 
filtering                               : where condition | operators: < > = <= >= <>   IN BETWEEN LIKE EXIST   AND OR NOT 
sorting                                 : asc / desc / | sort by  / sort by then by ... | column name or expression or ordinal number 
aggregations                            : MIN, MAX, COUNT, COUNT *, COUNT DISTINCT, SUM, AVG 
grouping | aggregations | filtering     : GROUP BY | aggregators | HAVING 
sub query - correlated sub query        : 
join                                    : inner, left outer, right outer, full outer
union                                   : to combine two query results of same output table structure 



select * from employees;

-- to display first name, last name of all employees
SELECT first_name, last_name
FROM employees;

-- to display first name, last name, date of birth of all employees
SELECT first_name, last_name, date_of_birth
FROM employees;

-- to display first name, last name, date of birth and age of all employees
/*
SELECT first_name, last_name, date_of_birth, ' ' age
FROM employees;
    -- solve
SELECT first_name, last_name, date_of_birth, now() as today, ' ' age
FROM employees;
    -- find year diff bt two dates
*/
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees;

-- to display first name, last name, date of birth, age, retires in years of all employees
-- assume 58 is max age to work 
SELECT first_name, last_name, date_of_birth, 
    timestampdiff(year,date_of_birth,now()) as age,
    58 - timestampdiff(year,date_of_birth,now()) as retires_in 
FROM employees;

-- to display first name, last name, joining_date, experience
SELECT first_name, last_name, joining_date, timestampdiff(year,joining_date,now()) as experience
FROM employees;

-- to display first name, last name, joining_date, experience, retires_in
-- percentage of experience wrt (sum of experience + retires_in)
-- select 10,3, (3/10)*100
    -- solution 1: 
    SELECT first_name, last_name, joining_date, timestampdiff(year,joining_date,now()) as experience,
    58-timestampdiff(year,date_of_birth,now()) as retires_in,
    (timestampdiff(year,joining_date,now()) / 
        ( timestampdiff(year,joining_date,now()) +  58 - timestampdiff(year,date_of_birth,now()))
    ) * 100 as experience_per
    FROM employees;

            -- OR ---

    -- STEP 1 view 1: all employees : all cols + age, experience :: employees_age_exp
        CREATE VIEW employees_age_exp as 
            SELECT e.*, 
                timestampdiff(year,e.date_of_birth,now()) as age, 
                timestampdiff(year,e.joining_date,now()) as experience FROM employees as e;
        -- view is named stored query | view can be seen as table
        SELECT * FROM employees_age_exp;

        -- STEP 2 view 2: all employees_age_exp : all cols + total_service, retires_in :: employees_service
        -- DROP VIEW employees_service;
        CREATE VIEW employees_service AS 
            SELECT e.*, 58-e.age+e.experience as total_service, 58-e.age as retires_in FROM employees_age_exp as e;

        
        SELECT e.* FROM employees_service as e;
    -- solution 2: to get the experience percentage:
    SELECT e.*, (e.experience / e.total_service)*100 as experience_per FROM employees_service as e;

-- selectors : column, expression, constant 
             : -> expression may be a function / arith operation or both 
             : -> expression and constant needs to be given alias name for the output table 
-- sorting   : sort by | sort by then by ...
             : A-Z 'ASC', Z-A 'DESC', ascending 'ASC', descending 'DESC' 
             : sort by col/expr/ordinal number 
             : what is ordinal number? 1-based number, each output table column is given an ordinal number
             : clause: ORDER BY 

-- display first_name, last_name, date_of_birth, age sort by first_name a-z
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
ORDER BY first_name;

-- display first_name, last_name, date_of_birth, age sort by first_name z-a
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
ORDER BY first_name DESC;

-- display first_name, last_name, date_of_birth, age sort by age ascending
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
ORDER BY timestampdiff(year,date_of_birth,now());
    -- OR use ordinal number
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
ORDER BY 4;

-- display first_name, last_name, date_of_birth, age sort by age descending
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
ORDER BY 4 DESC;

-- display first_name, last_name, date_of_birth, age sort by age ascending and then by first_name a-z
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
ORDER BY 4, first_name; 


                                --- filtering ----
-- filtering : relational ops =    <>    <=  >=  < >      |  IN BETWEEN LIKE EXIST | logical ops: AND OR NOT
            : where condition 
-- display first_name, last_name, date_of_birth, age where age less than 40
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) < 40;

-- display first_name, last_name, date_of_birth, age where age above or equal 40
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) >= 40;

-- display first_name, last_name, date_of_birth, age where age is either 35 or 38 or 44
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) IN (35, 38, 44);

-- display first_name, last_name, date_of_birth, age where age is not either 35 or 38 or 44
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) NOT IN (35, 38, 44);

-- display first_name, last_name, date_of_birth, age where age is between 33 and 38
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) BETWEEN 33 AND 38;

-- display first_name, last_name, date_of_birth, age where age is not between 33 and 38
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) NOT BETWEEN 33 AND 38;

-- display first_name, last_name, date_of_birth, age where first_name starts with 'a'
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE first_name LIKE 'a%';

-- display first_name, last_name, date_of_birth, age where first_name ends with 'a'
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE first_name LIKE '%a';

-- display first_name, last_name, date_of_birth, age where first_name contains 'ra'
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE first_name LIKE '%ra%';

-- display first_name, last_name, date_of_birth, age where first_name contains 'ar'
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE first_name LIKE '%ar%';

-- display first_name, last_name, date_of_birth, age where second_letter is a and last_letter is a
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE first_name LIKE 'a%a';

-- display first_name, last_name, date_of_birth, age where age is 34 and sort by first_name a-z
SELECT first_name, last_name, date_of_birth, timestampdiff(year,date_of_birth,now()) as age
FROM employees
WHERE timestampdiff(year,date_of_birth,now()) = 33
ORDER BY first_name;

-- sofar
-- -SQL
-- - -- selectors: column, expression: ops/fns, constant
-- - -- filtering: where cond: relational op / in between like / logical ops
-- - -- sorting: text, number | asc desc 

-- -- today
-- - --: join (cross join), inner join 
-- - --: aggregators: min, max, count(*),count(col),count(distinct col), sum, avg
-- - --: sub query
-- - --: group by | aggregators | having
-- - --: correlated sub query
-- - --: types of joins : inne join, left join, right join, full join 

-- - --: revisit byteXL queries statements - we are solving....

-- -
select * from employees;
select * from departments;
select * from salaries;
select * from leaves;
-- - aggregators
-- number of employees
select count(*) from employees
-- number of departments
select count(*) from departments
-- count the number of rows of joined employees with salaries by matching rows 
-- !!!
select count(*) 
from employees as e 
    inner join salaries as s on (e.employee_id = s.employee_id)
-- count the number of rows of joined employees with salaries without cond 
-- !!!
select count(*) 
from employees as e 
    inner join salaries as s on (1=1)
    -- -> cross join (cartesian product)
    -- -> each emp row joined to every salaries row 
-- display name and his/her salary 
select e.first_name, e.last_name, s.amount as salary 
from employees as e 
    inner join salaries as s on (e.employee_id = s.employee_id)

-- aggregators min / max / sum / avg salary
select min(s.amount) as min_salary, max(s.amount) as max_salary,
    sum(s.amount) as total_salary, 
    count(*) as number_of_emps, sum(s.amount) / count(*) as salary_avg,
    avg(s.amount) as avg_sal
from employees as e 
    inner join salaries as s on (e.employee_id = s.employee_id)

-- top salaried
select e.first_name, e.last_name, s.amount as salary 
from employees as e 
    inner join salaries as s on (e.employee_id = s.employee_id)
order by s.amount desc
limit 1
        -- OR 
select e.first_name, e.last_name, s.amount as salary 
from employees as e 
    inner join salaries as s on (e.employee_id = s.employee_id)
where s.amount = (select max(amount) from salaries)

-- display positions
select position from employees;
-- display distinct positions : distinct - no duplicates
select distinct position from employees;
-- count positions - count of all values in col position
select count(position) from employees;
-- count disticnt positions - count of values where duplicated values counted only once
select count(distinct position) from employees;

-- excercise 
-- - 1. display emp name, dept'name            join 
-- - 2. display emp name, dept name, salary    join 

-- group by
    -- categroize rows into groups, each group we will do aggregator
    -- fix participating columns for grouping - decide aggregator column

-- distinct genders using group by
select gender 
from employees 
group by gender 
-- gender's total employees 
--      here, group by column: gender, aggregator column: *
select gender, count(*) 
from employees 
group by gender 
-- gender's total salary and avg salary for the gender
--      here, group by column: gender, aggregator column: amount
select e.gender, sum(s.amount) as total_salary, avg(s.amount) as avg_salary 
from employees as e 
    inner join salaries as s on(e.employee_id = s.employee_id)
group by e.gender

-- position's total salary 
--      here, group by column: position, aggregator column: amount / sum
select e.position, sum(s.amount) as total_salary
from employees as e 
    inner join salaries as s on(e.employee_id = s.employee_id)
group by e.position
-- department_id's total salary 
--      here, group by column: department_id, aggregator column: amount / sum
select e.department_id, sum(s.amount) as total_salary
from employees as e 
    inner join salaries as s on(e.employee_id = s.employee_id)
group by e.department_id

-- Note:
-- 'group by' will be run in the database after 'where' clause
-- assume: filtering employees towards 'active' then find department wise total salary

-- from the 'group by' result table, to filter we use the 'having' clause
-- 'having' clause is like 'where' clause but 'having' clause will use only 'group by' column, or aggregated value

-- display department's total salary where total salary should not exceed 3.6lack
select e.department_id, sum(s.amount) as total_salary 
from employees as e 
    inner join salaries as s on ( e.employee_id = s.employee_id )
group by e.department_id
having sum(s.amount) <= 360000

-- join + aggregators
-- group by | aggregators | having 

-- correlated sub query : interview qn 
-- types of the joins : interview qn 

                        -- example for correlated sub query 
-- department's max salary 
select e.department_id, max(s.amount) as max_salary
from employees as e 
    inner join salaries as s on(e.employee_id = s.employee_id)
group by e.department_id

-- department's 2nd max salary : sub query - correlated
-- parent e and s are correlated to f and t becuase f.department_id is matched with e.department_id
select e.department_id, max(s.amount) as max_salary
from employees as e 
    inner join salaries as s on(e.employee_id = s.employee_id)
where s.amount < (select max(t.amount) 
            from salaries t 
                inner join employees f on(f.employee_id=t.employee_id) 
            where f.department_id = e.department_id)
group by e.department_id

-- find department 101 2nd max sal <-- to conclude we found for pervious query result is each dept's 2nd max sal
select max(s.amount) max_salary
from employees as e 
    inner join salaries as s on(e.employee_id = s.employee_id)
where e.department_id=101 and 
    s.amount < (select max(s.amount) max_salary
                    from employees as e 
                        inner join salaries as s on(e.employee_id = s.employee_id)
                    where e.department_id=101) 

-- difference between sub query and correlated sub query?
--  in sub query, main query will run based on result of the sub query 
--  in correlated sub query, each time sub query depends on each row of the main query
        -- so, parellelly sub query and main query will run wrt correlated sub query



-- inner join           -> matched rows 
-- left outer join      -> matched rows + left side table extra rows 
-- right outer join     -> matched rows + right side table extra rows 
-- full outer join      -> matched rows + left side table extra rows + right side table extra rows 

 -- to learn "left outer join", example: introduce no-employee account department and 
    -- find department's total salary 
-- -----------1. introduce account department
insert into departments(department_id, department_name) values(106,'account');
-- -----------2. find emp name and dept name 
select e.first_name, d.department_name 
from employees e inner join departments d on (e.department_id=d.department_id)
-- -----------3. find emp name and dept name; even no emp, print dept name
select ifnull(e.first_name,'--no emp--') first_name, d.department_name  
from employees e right join departments d on (e.department_id=d.department_id)
-- -----------3b. find emp name and dept name; even no emp, print dept name via left join
select ifnull(e.first_name,'--no emp--') first_name, d.department_name  
from departments d left join employees e on (e.department_id=d.department_id)
-- -----------4a. find department's total salary
select d.department_id, sum(ifnull(s.amount,0)) total_salary  
from employees e 
    inner join salaries s on (e.employee_id=s.employee_id)
    right join departments d on(e.department_id=d.department_id)
group by d.department_id
-- -----------4b. find department's total salary via left join
select d.department_id, sum(ifnull(s.amount,0)) total_salary  
from departments d
    left join ( employees e 
                    inner join salaries s on (e.employee_id=s.employee_id) 
                ) 
            on(e.department_id=d.department_id)
group by d.department_id

                -- trying full outer join in mysql

alter table employees 
drop constraint employees_ibfk_1;

insert into employees(employee_id, first_name, last_name, date_of_birth, 
gender, email, phone, address, department_id, 
position, joining_date) values(21,'rahul','dravid','1977-05-17',
'Male','dravid@example.com','222 222 2222','101 new street bangalore', 107,
'Senior Coach', '2022-01-27');

select ifnull(e.first_name,'--no emp--') first_name, d.department_id, d.department_name  
from employees e full outer join departments d on (e.department_id=d.department_id)


-- full outer join is not supported in mysql 
-- we can form the full outer using 'union' of left and right joins output
select ifnull(e.first_name,'--no emp--') first_name, d.department_id, d.department_name  
from employees e right join departments d on (e.department_id=d.department_id)
union 
select e.first_name, ifnull(d.department_id, e.department_id) department_id, 
    ifnull(d.department_name,'--no dept--')   department_name
from employees e left join departments d on (e.department_id=d.department_id)