CREATE SEQUENCE person_id_seq INCREMENT 1;

CREATE TABLE person(
id INT PRIMARY KEY NOT NULL DEFAULT nextval('person_id_seq'::regclass),
name VARCHAR(80)	
)


select * from person