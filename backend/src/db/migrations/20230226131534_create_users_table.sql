-- migrate:up
create table users (
  id SERIAL PRIMARY KEY,
  name varchar(30) not null,
  password varchar(128) not null,
  email varchar(254) not null
);

-- migrate:down
drop table users;
