-- sqlite3 mpsu-db.sqlite < mpsu-db.sql

CREATE TABLE field (
	id integer primary key autoincrement NOT NULL,
	name nvarchar(20) NULL
);

CREATE TABLE test (
	id integer primary key autoincrement NOT NULL,
	field_id integer NOT NULL,
	foreign key(field_id) references field(id)
);

CREATE TABLE test_question (
	test_id integer NOT NULL,
	question_id integer NOT NULL,
	question_index integer NOT NULL
);

CREATE TABLE question (
	id integer primary key autoincrement NOT NULL,
	statement nvarchar(500) NULL,
	field_id integer NOT NULL,
	foreign key(field_id) references field(id)
);

CREATE TABLE question_alternative (
	question_id integer NOT NULL,
	alternative_index smallint NOT NULL,
	description nvarchar(500) NULL,
	foreign key(question_id) references question(id)
);

CREATE TABLE question_answer (
	question_id integer NOT NULL,
	answer_index smallint NULL,
	foreign key(question_id) references question(id)
);

INSERT INTO field (name) VALUES ("Matemática");