create database register;

use register;

create table credentials (
    id integer primary key auto_increment,
    email varchar(30) not null,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    street_name varchar(30) not null,
)

