use ai_jayalakshmi;
create table spread_sheets
(
user_id int not null primary key auto_increment,
user_name varchar(50),
password varchar(50)
);

delimiter &&
create procedure s_table(
in user_nameparameter varchar(50),
in passwordparameter varchar(50)
)
begin
insert into spread_sheet(user_name,password)values(user_nameparameter,passwordparameter);
end &&
delimiter ;
call s_table('aki','aki@1');

select * from spread_sheet;
---------------------------------------------------------------------------
insert another method---------------------------------------------------------

delimiter &&
drop procedure if exists inserttbl;&&
create procedure inserttbl(
in tablename varchar(50),
in 


update-----------------------------------------------------------

delimiter &&
drop procedure if exists s_table;&&

create procedure sys_details(
in idparameter int,
in user_nameparameter varchar(50),
in passwordparameter varchar(50)
)
begin
update spread_sheet set user_name=user_nameparameter, password=passwordparameter where user_id=idparameter;
end &&
delimiter ;
call sys_details(1,'uhfgh','hchgcvgh');
------------------------------------------------------------------------------------------------
delimiter &&
drop procedure if exists update_cmt;&&
create procedure update_cmt(
in tablename varchar(50),
in columnname varchar(50),
in columnvalue varchar(50),
in idname varchar(50),
in idvalue varchar(50)
)
begin
set @cmt_update = concat('update ', tablename, ' set ', columnname, '=\'', columnvalue , '\'', 'where ', idname, '=', idvalue);
prepare cmt  from @cmt_update;
execute cmt;
end &&
delimiter ;

call update_cmt(' spread_sheet','user_name','santho','password','aki@1');

select * from spread_sheet;

alter -----------------------------------------------------------------

delimiter &&
drop procedure if exists cmt_alter1;&&
create procedure cmt_alter1(
in tablename varchar(50),
in columnname varchar(50)
)
begin
set @alter_cmt=concat('alter table ',tablename ,' drop column ',columnname);
prepare cmt  from  @alter_cmt;
execute cmt;
end &&
delimiter ;
call cmt_alter1('spread_sheet','user_name');
select * from spread_sheet;

delete--------------------------------------------------------------------


delimiter &&
drop procedure if exists cmt_delete;&&
create procedure cmt_delete(
in tablename varchar(50),
in idname varchar(50),
in idvalue varchar(50)
)
begin
set @delete_cmt=concat('delete ','from ',tablename ,'where ',idname, '=',idvalue);
prepare cmt  from @delete_cmt;
execute cmt;
end &&
delimiter ;
call cmt_delete('spread_sheet',user_name,gv);


add-------------------------------------------------------------------------------

delimiter &&
drop procedure if exists add_cmt;&&
create procedure add_cmt(
in tablename varchar(50),
in idname varchar(50)
)
begin

set @statement = concat(' alter table ',tablename, ' add column ',columnname ,' varchar\(50\)');
prepare stmt from @statement;
execute stmt;
end &&
delimiter ;
call add_cmt('spread_sheet','idname');
--------------------------------------------------------------------------------------------

delete------------------------------------------------------------


delimiter &&
drop procedure if exists cmt_delete;&&
create procedure cmt_delete(
in tablename varchar(50),
in idname varchar(50),
in idvalue varchar(50)
)
begin
set @delete_cmt=concat('delete from ',tablename,' where ',idname,'=\'',idvalue,'\'');
prepare cmt  from @delete_cmt;
execute cmt;
end &&
delimiter ;

call cmt_delete('spread_sheet','user_name','gv');



add---------------------------------------------------------------------------

delimiter &&
drop procedure if exists cmt_add;&&
create procedure cmt_add(
in tablename varchar(50),
in idname varchar(50),
in idvalue varchar(50))
begin
set @delete_cmt=concat('alter table ',tablename,' add column ',columnname, ' varchar\(50\)',columnvalue, 
' varchar\(50\)');
prepare cmt  from @delete_cmt;
execute cmt;
end &&
delimiter ;

call cmt_add('spread_sheet','user_name','user_id');
select * from spread_sheet;
------------------------------------------------------------------------------------
delimiter &&
drop procedure if exists value_insert;&&

create procedure value_insert(
in idname varchar(50),
in idvalue varchar(50));
begin
update spread_sheet set idname=idnameparameter, idvalue=idvalueparameter where user_id=idparameter;
end &&
delimiter ;
call sys_details(1,'uhfgh','hchgcvgh');