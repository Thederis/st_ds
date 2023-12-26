CREATE TABLE test_table(
    sometext VARCHAR(100));

SELECT sometext FROM test_table

insert into test_table(sometext)
values ('abc');

SELECT sometext
FROM test_table

insert into test_table(sometext)
values ('dif');

SELECT sometext
FROM test_table

insert into test_table(sometext)
values ('hej');

ALTER TABLE test_table
ADD Phone VARCHAR(100)

SELECT *
from test_table