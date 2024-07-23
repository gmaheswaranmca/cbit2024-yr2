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