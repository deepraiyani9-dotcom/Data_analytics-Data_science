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
        |address ,message        | text                  |
     '''
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

      alter table tabelname add columnname datatype(00) after columnname  

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

  ## delete data from tablea.

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
