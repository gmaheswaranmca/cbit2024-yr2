-- procedure / function : routines running in the SQL 

-- function : stored function
    -- function deals with data table 
        find_employee_age(id)
            -- returns age of the employee
    -- function deals not with data table 
        abs(x), square(x), find_add(a,b)

    -- deterministic - for input we should get always the same output 
-- procedure : stored procedure (SP)
    -- have CRUD ops procedures 
    -- complicated query - if possible via routine - we may use the SP 
    -- specilized reports / visualization / dashboard query

notes - crud ops 
1. sp_notes_create(title, notes)    insert      myself 
2. sp_notes_read_all()              query       assignment 
3. sp_notes_read_byid(id)           query       myself 
4. sp_notes_update(id, title, notes) update     assignment 
5. sp_notes_delete(id)               delete     assignment 

drop procedure if exists sp_notes_read_byid;
create procedure sp_notes_read_byid(p_id int) 
begin 
    select id, title, notes 
    from notes
    where (id = p_id);
end; 
call sp_notes_read_byid(2)

drop procedure if exists sp_notes_create;
create procedure sp_notes_create(p_title varchar(255), p_notes varchar(3500))
begin
    declare v_id int; 

    insert into notes(title, notes)
    values(p_title, p_notes);

    set v_id = last_insert_id();

    select id, title, notes 
    from notes
    where (id = v_id);
end;
call sp_notes_create('php','php is a web development framework');

drop procedure if exists sp_emp_exp;
create procedure sp_emp_exp( p_id int)
begin
    declare v_joining_date datetime;
    declare v_exp int;

    select joining_date into v_joining_date
    from employees where employee_id=p_id;

    set v_exp = timestampdiff(year, v_joining_date, now());
    
    select *, v_exp exp from employees where employee_id=p_id;
end;
call sp_emp_exp(3);


 ---
DROP FUNCTION if exists find_diff;
DELIMITER $$
CREATE FUNCTION find_diff(a int, b int) 
returns int deterministic
begin
    return a - b;
end$$
DELIMITER ;
select find_diff(10,4) as diff;