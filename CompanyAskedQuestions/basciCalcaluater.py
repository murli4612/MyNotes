select distinct employee from employee_manger  where employee 
not in (select distinct manager from emplyee_manager where manager is not null)