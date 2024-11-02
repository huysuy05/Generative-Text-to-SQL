USE test;

CREATE TABLE IF NOT EXISTS test_table
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