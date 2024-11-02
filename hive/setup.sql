
-- After composing Docker Container,
-- Run "beeline -u jdbc:hive2://localhost:10000" 
-- For running Hive Database inside the terminal

USE vdt;

CREATE TABLE IF NOT EXISTS customers
(
    customerNumber         INT,
    customerName           STRING,
    contactLastName        STRING,
    contactFirstName       STRING,
    phone                  STRING,
    addressLine1           STRING,
    addressLine2           STRING,
    city                   STRING,
    state                  STRING,
    postalCode             STRING,
    country                STRING,
    salesRepEmployeeNumber INT,
    creditLimit            STRING
)
    STORED AS PARQUET;

ALTER TABLE customers
    SET LOCATION 'hdfs://namenode:8020/user/hive/warehouse/customers/';


CREATE TABLE IF NOT EXISTS products
(
    productCode        STRING,
    productName        STRING,
    productLine        STRING,
    productScale       STRING,
    productVendor      STRING,
    productDescription STRING,
    quantityInStock    INT,
    buyPrice           STRING,
    MSRP               STRING
)
    STORED AS PARQUET;


ALTER TABLE products
    SET LOCATION 'hdfs://namenode:8020/user/hive/warehouse/products/';


CREATE TABLE IF NOT EXISTS orders
(
    orderNumber    INT,
    orderDate      STRING,
    requiredDate   STRING,
    shippedDate    STRING,
    status         STRING,
    comments       STRING,
    customerNumber INT
)
    STORED AS PARQUET;


ALTER TABLE orders
    SET LOCATION 'hdfs://namenode:8020/user/hive/warehouse/orders/';

CREATE TABLE IF NOT EXISTS orderdetails
(
    orderNumber     INT,
    productCode     STRING,
    quantityOrdered INT,
    priceEach       STRING,
    orderLineNumber INT
)
    STORED AS PARQUET;

ALTER TABLE orderdetails
    SET LOCATION 'hdfs://namenode:8020/user/hive/warehouse/orderdetails/';

