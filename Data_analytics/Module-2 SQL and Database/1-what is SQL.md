# 1-what is SQL ?
    1. SQL stands for structered query language
    2. sql is used to a 
    3.

    **table stuctured**
    **users**
    |uid | uname | gender | address |
    |----|-------|--------|---------|
    |1   |A      | male   | rjt     |
    |2   |B      | female |amd      |

  4. sql is case-insensitive language
    ex:INSERT | insert | Insert (cammel case)
  5. sql is not conditional
  6. sql is used to provides relation between tables using normalization
  7. sql create some query or commnds to create database or tabke structured

  ## sql types of query or commnds 

    1. DDL : "data defination language"
    2. DML : "data manuplation language"
    3. DQL : "data query language"
    4. TCL : "transction control language" 


### DDL .... data defination language

    1. ddl stand for data defination language
    2. ddl is used to create database | create table | alter data | rename tables | changed table column name  | drop database & table structerd | truncate data
    - create
    - alter
    - drop
    - change 
    - rename
    - truncate

  ##  how create database ?

     **
      syntex : create database databasename;
      or 
      create database da_db; 
     **
    
  ## how create table ?
      **create a table chart for datatype size**
        ```
        | columnname             | datatype(size)        |
        |------------------------|-----------------------|
        |id(pk) auto_increment   | int (defualt size 11) |            
        |name ,email,password    | char|varchar(0-255)   |      
        |date,datetime           | date | datetime       |      
        |address ,message        | text                  |      
        |multiple choice         | enum                  |
        |image                   | blob ,varchar(255)    |
        |salary,price            | int,float,money       |
        |phone                   | int,bigInt(by default 20) |  
        |default datatime        |timestamp                 |   
        | boolean                | true / false          |
     ```
      syntex : create table tablename
      (
        id int auto_increment primary key,
        columnname datatype(size),
        .
        .
        .
        columnname datatype(size)
      );
    **example**
      create table users
      (
        id int auto_increment primary key,
        name varchar(255),
        email varchar(255),
        password varchar(255),
        pincode int,
        salary float,
        address text,
        phone bigint
      )

      or

      create table products
      (
        pid int auto_increment primary key,
        pname varchar(255),
        photo blob,
        oldprice int,
        newprice int,
        qty int,
        status enum ('active','deactive'),
        description text
      )

      
      create table feedback
      (
        fid int auto_increment primary key,
        uname varchar(100),
        email varchar(100),
        phone_number int(10),
        message text        
      )

      
      create table rating
      (
        rid int auto_increment primary key,
        uname varchar(100),
        email varchar(100),
        phone_number int(10),
        rating enum('1','2','3','4','5')
        rating_description text
      )

  # alter (alter change only column not raw)
   1. alter is used to change table columnname | add table new column alter is used
   2. alter is also update columnname of table and also add unique key in table
   3. alter is used to change or upadate or modify tables column name 

   syntax :

   alter table tablename add columnname datatypea(size)
   or
   alter  table users add gender varchar(255);

    ## add columnname specific column

      alter table tabelname add columnname datatype(255) after columnname  

    ## update any spicific column

      alter table users change photo mobile bigint;

    ## alter used to add unique key in tables (unique key never store duplicate values)

      alter table users add UNIQUE ('email');

  # rename : rename is used to change a table name

  ** syntex **

  '''
   RENAME table users to user; 
   '''
# truncate : truncate is use to ampty or delete all data once time
  ## note : after truncate we never rollback our data

    ** syntex **

    '''
    truncate table user;
    '''

# drop : drop is use to drop or delete databse sturcture or table structure
  ## note : after drop we never rollback

  ** syntex **
  '''
  drop table users;
  or
  drop database da_db;
  '''
## rename : 

    1. rename the table name

    **syntex**

    '''
    RENAME  table table_name TO new_tablename
    '''

  ### DML ... data manuplation language
    **there are three queries in dml**

    -insert
    -update
    -delete

  ## how to insert data 
     **SYNTEX**

     **single data insert**
     '''    
     insert into tablename (columnname) values('value');
     '''
    
     **multi-data insert**
      note :: multipul value insert kari tyre jo column name no lakho to null lakhvu padse or insert sathe column name lakho tyre aani value nakho to koy error no ave.

      insert into employee values (null,'deep','deep@gmail.com','deep123','26000','it')

  ## cretae a product tabke with  following fiels 


```
  CREATE TABLE products 
(
    pid int AUTO_INCREMENT PRIMARY KEY,
    sku varchar(100) UNIQUE NOT null,
    product_name varchar(200),
    barcode varchar(200),
    description text,
    category_id int,
    subcategory_id int,
    brand_id int,
    cost_price decimal(10,2) not null defualt 0.00,
    selling_price decimal (10,2),
    discount_price decimal(10,2),
    tax_rate decimal(5,2) default 0.00,
    stock_quantity int default 0,
    minimum_stock int default 0,
    maximum_stock int default 0,
    recorder_level int default 0,
    weight decimal(10,2),
    length decimal(10,2),
    width decimal(10,2),
    height decimal(10,2),
    unit varchar(50),
    color varchar(100),
    size varchar(100),
    image_url varchar(200),
    thumbnail_url varchar(500),
    slug varchar(255) unique,
    meta_title varchar(255),
    meta_description text,
    meta_keywords text,
    status enum('active','inactive') default 'active',
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp on update current_timestamp,
    manufacture_date date,
)
```
  ## delete data from table.

  ** syntex**

  1. delete is used to delete all data from tables
  2. delete is used to delete particular  from tables
  3. delete is used to range of data from tables
  4. delete is used to delete alterate data

  delete all data...
  delete from tbl_country;

  or

  delete particular one data ...
  delete from tbl_country where cid=1;

  or

  delete 2 data at once time..
  delete from tbl_country where cid in (4,6,9);

  or

  delete range of data..
  delete from tbl_country where cid between 1 and 5;


  ## uopdate the data or row..

  **syntex**

  '''
  update table set columname ='value' where id='id';
  or
  update table set cname='bhutan' where cid=2;
  or
  update table set cname='japan',cwork='export',ccapital='tokyo' where cid=1;
  
  '''
## DQL : data query language

  1. dql is handle to select all data from tables
  2.dql is handle to fetch all data from tables
  3. dql is handle particular fetch data from tables
  4. dql is handle particular range of data from tables
  5. dql is handle particular fetch alternate data from tables
  6. dql is handle particular fetch limit or data from tables

  **query in DQL**

  select

  1. how to select all data 
    SELECT* FROM PRODUCTS;
  2. select paricular data from id or name
    select * from products where impid=1;
    or 
    select * from products where name='deep' ;

  3. select particular data from columns 
    select name,mail,phonenumber from employee;

  4. select praticular column of one data 
      select name,mail,phonenumber from employee WHERE  name ='deep' ;
 
  5. select paricu;ar range of data
      select * from employee where impid between 3 and 8 ;
  
  6. select particular or alternate data 
       select * from employee where impid in(3,5,7,8) ;
       or
       select * from employee where impid in('deep','astha','punit') ;
        or
        select * from employee where impid in('deep','astha','punit') order by name desc ;
        or
        select * from employee where impid in('deep','astha','punit') order by name ;
        or
        select * from employee where impid in('deep','astha','punit') order by name asc ;
        
  7. select data using limit
     
     select * from emloyee where impid limit 0,5 ;
     or
    select * from emloyee where impid limit 2,6 ; 
    (note: where 2 was off set which means start from next 3 and goes to next 6 it's print total empid 3,4,5,6,7,8)
  
8.select or filter data using **order by**

  select *  from employee  order by name desc ;
  select *  from employee  order by name asc ;  

9. group by

    select sum(salary) as sum_od_salary,department from employee group by department;

## sql function

1. sql function is used to pre-defiend function

types of function : function giving only temprory result when get out it's back

1.aggrigate function
2.scaler function

  # aggrigate function

    1. sum()
    2. avg()
    3. count()
    4. max()
    5. min()

  # scalar function 
  
    1. ucase()
    2. lcase()
    3. length()
    4. round()
    5. now()
    6. date() 
    7. first()
    8. last()
    9. concat()
    10. replace

  # replace() :

    select replace("shall pass","deep","jeet") from 
  
  # concat() :

    select concat(name,' ',address) as fullname from employees;  

  # sum() :

    select sum(salary) as sum_of_salary from employees;
    or
    select sum(salary),department from employees group by department;
  
  # avg() : 
  
    select avg(salary) as average_salary from employees;

  # count() :
  
    select count(name) as total_employee from employees;
    or
    select count(name),department from employees group by department;

  # max() : 
  
    select max(salary) as max_salary from employees;
    or
    select max(salary),department from employees group by department;

  # min () :
   
    select min(salary) as min_salary from employees;
    or
    select min(salary),department from employees group by department;
  
  # find ther second  highest salary  ** using subquery method **

    **subquery**
      1.subquery used within another query.

     select max(salary) from employees where salary < (select max(salary) from table employee);
     or
     select * from employees group by salary DESC limit 1,1;

  # first() : the row find first in column

    select first(empid) from employees;

# what is like operator in sql ?
# like operator :

  1. like operator is used to search data from tables with keyword.
  2. like operstor is using for search using its wildcard (%).

   ## start cheracter  with d

    select * from employees where name like '%d';
    or
    select * from employees where name like 'h%';

    ## find anywhere in name

    select * from employees where name like '%a%';


  ## key constraints in sql 

    1. key constraints provide limit on tables.
    2. key constraints used to set primary key | unique key | foriegn key on tables
    3. key constraints provides limitation on tables
    4. key constraints provides relationship b/w tables

    ## types of key constraints

    1. primary key
    2. unique key
    3. foreign key

    ## primary key ?

    1. A pk only provides one time in a column
    2. s pk nevers repetednmore than one times
    3. a pk stored unique values and never return null value
    4. a pk should always be auto_increment 

    **users** 

    | uid(pk)  |    uname   |    age  |    address |   compsnt |
    |----------|------------|---------|------------|-----------|
    |   1      |    brijesh |  40     | rjt        |   tops    |
    |   2      |    deep    |  20     | vadodara   |   abtik   |
    |   3      |    tejas   |  21     | ahm        |   shreeja |


     ## unique key ?

    1. A uk provides more than one time in tables 
    2. a uk repetaed more  than one times in tables
    3. a uk stored unique values and return one times a null value
    4. a uk never return dulpicte values

    **users** 
    
    | uid(pk)  |    uname   |    age  |    address |   compony | phone(uk)|
    |----------|------------|---------|------------|-----------|----------|
    |   1      |    brijesh |  40     | rjt        |   tops    |9876543210|
    |   2      |    deep    |  20     | vadodara   |   abtik   |123467890 |
    |   3      |    tejas   |  21     | ahm        |   shreeja |4569871233|


    ## foriegn key ?

    1. A fk provides more than one time in tables 
    2. a fk repetaed more  than one times in tables
    3. a fk  stored duplicate value also
    4. a fk provides relation b/w tables with common field

    **country**

    |cid(pk)|  cname  |
    |-------|---------|
    |  1    |  india  |
    |  2    |  japan  |
    |  3    |  usa    |
    |  4    | china   |
    **via sql**
    CREATE TABLE country (
    cid INT PRIMARY KEY AUTO_INCREMENT,
    cname VARCHAR(100) NOT NULL
);

    **users** 
    
    | uid(pk)  |    uname   |    age  |    address |   compony | phone(uk)|cid|
    |----------|------------|---------|------------|-----------|----------|---|
    |   1      |    brijesh |  40     | rjt        |   tops    |9876543210|1  |
    |   2      |    deep    |  20     | vadodara   |   abtik   |123467890 |2  |
    |   3      |    tejas   |  21     | ahm        |   shreeja |4569871233|3  |

    **via sql**
    CREATE TABLE tbl_users (
    uid INT PRIMARY KEY AUTO_INCREMENT,
    uname VARCHAR(100) NOT NULL,
    age INT,
    address VARCHAR(255),
    compony VARCHAR(100),
    phone VARCHAR(15),
    cid INT,
    FOREIGN KEY (cid) REFERENCES country(cid)
);


# sql join ?
  1. sql join are used to join more than one field with common field
  2. sql join are used to join table data from one tabes to anither tabkes with common field 

1. join
2. inner join
3. outer jion
    1. left outer join
    2. right outer join
    3.full outer join 
4. cross join


# what is SQL join  ?
1. join are used to join more than one tables with common field 
2. join are used to match data from one tables to another table if data matched join the tables otherwise return null values 

**syntax**

```
select tbl1.*, columname from tbl1 join tbl2 on tbl1.commonfield=tbl2.commfield;
or
select tbl_salesman.*, depname from tbl_salesman join tbl_department on tbl_salesman.depid=tbl_department.depid;
or

select salesid, name, address , mobile,email , depname from tbl_salesman join tbl_department on tbl_salesman.depid=tbl_department.depid;
``` 

# types of JOin ? 

1. join 
2. inner join 
3. outer join 
   1. left outer join 
   2. right outer join 
   3. full outer join 
4. cross join 
5. self join 
6. union join 

# join :

# inner join :

1. iner join are used to join more than one tables with common field 
2. inner join are used to match data from one tables to another table if data matched join the tables otherwise return null values 

**syntax**

```
select tbl1.*, columname from tbl1 inner join tbl2 on tbl1.commonfield=tbl2.commfield;
or
select tbl_salesman.*, depname from tbl_salesman inner join tbl_department on tbl_salesman.depid=tbl_department.depid;
or

select salesid, name, address , mobile,email , depname from tbl_salesman inner join tbl_department on tbl_salesman.depid=tbl_department.depid;

or
select salesid, name, address , mobile,email , depname, compname from tbl_salesman inner join tbl_department on tbl_salesman.depid=tbl_department.depid inner join tbl_company on tbl_salesman.compid=tbl_company.compid;
``` 


# left join :

1. left join are used to join more than one tables with common field 
2. left join are used to join first table of left rows with second table of left rows if data matched from first table of left rows return all data of first table and join otherwise return null values.

**syntax**

```
select tbl1.*, columname from tbl1 left join tbl2 on tbl1.commonfield=tbl2.commfield;
or
select tbl_salesman.*, depname from tbl_salesman left join tbl_department on tbl_salesman.depid=tbl_department.depid;
or

select salesid, name, address , mobile,email , depname from tbl_salesman left join tbl_department on tbl_salesman.depid=tbl_department.depid;

or
select salesid, name, address , mobile,email , depname, compname from tbl_salesman left join tbl_department on tbl_salesman.depid=tbl_department.depid left join tbl_company on tbl_salesman.compid=tbl_company.compid;

``` 

# right join :

1. right join are used to join more than one tables with common field 
2. right join are used to join second table of right rows with first table of right rows if data matched from second table of right rows return all data of second  table and join otherwise return null values.

**syntax**

```
select tbl1.*, columname from tbl1 right join tbl2 on tbl1.commonfield=tbl2.commfield;
or
select tbl_salesman.*, depname from tbl_salesman right join tbl_department on tbl_salesman.depid=tbl_department.depid;
or

select salesid, name, address , mobile,email , depname from tbl_salesman right join tbl_department on tbl_salesman.depid=tbl_department.depid;

or
select salesid, name, address , mobile,email , depname, compname from tbl_salesman right join tbl_department on tbl_salesman.depid=tbl_department.depid right join tbl_company on tbl_salesman.compid=tbl_company.compid;

``` 

# full join : not dupported in mysql


# cross join 

1. cross join are used to join table with cross of data 
2. cross join return dublicate data 

**examples**
```
select * from tbl_salesman cross join tbl_department
```

# self join :

1. self join are used to join itself 

**examples**

```
select e.empid, e.name as employee_name , m.name as manager_name  from tbl_employee e inner join tbl_employee m on e.manager_id=m.empid; 

```
# union join :
1. union join is combine of left join + right join 
2. this is a solution of full join 

**examples**

```
select tbl_salesman.*, depname from tbl_salesman left join tbl_department on tbl_salesman.depid=tbl_department.depid
union 
select tbl_salesman.*, depname from tbl_salesman right join tbl_department on tbl_salesman.depid=tbl_department.depid;

```
# what is SQL index or indexer ?

1. SQL index or indexer create or used to improved speed of tables 
2. SQL indexer is used to fast lookups or search data from tables 
3. SQL indexer is also create fast speed optimization of tables 

# types of indexer 
1. **single indexer**

  - when we create a indexer on single column that is called single indexer 
  
  **examples**
  ```
  create index tbl_products_index1 on tbl_products (pid);

  ```
2. **composit indexer** 
  
   
  - when we create a indexer on more than one  columns that is called composit indexer 
  
  **examples**
  ```
  create index tbl_products_index2 on tbl_products (pid, pname, qty, price);

  ```

# what is SQL view  ?
  
1. create a SQL views for clone of a tables 
2. create a SQL views for hide some data from some users there we create a clone of tables of view of table 
3. create a View and when we changed in view main tables are effected 

**examples**

```
create view view_tbl_customer as select * from tbl_customer;
or
create view view_tbl_customer as select * from tbl_customer where custid in (1,3,6);
or 
create view view_tbl_customer as select custid , name , password ,phone  from tbl_customer;
or
create view view_tbl_salesman as select * from tbl_salesman;
```
# what is SQL Case In or case when ?

1. check a multiple case using case when 
2. check a multiple case using case when and it is also check logic based case in tables
3. filter logic based case data from tables used **case when**

**examples**

```
select name , salary , case when salary >=75000 then 'Higher Earner'  when salary >=50000 then  'Medium Earner' else 'Lower salary' end as salary_earner from tbl_employee; 
or
select name , salary , case when salary >=75000 then 'Higher Earner'  when salary >=50000 then  'Medium Earner' else 'Lower salary' end as salary_earner from tbl_employee; 
```

# what is SQL trigger ?

# what is SQL store procedure ?

# what is SQL windows function  ?

# what is SQL CTE (common table expression)?

# connect sql when we udate data in my sql commnity or sql databse   and  when you get update and insert it will change into excel.

  -open excel blank workbook
  -data
  -get data
  -from databse
  -sql database 
  -select table you want

