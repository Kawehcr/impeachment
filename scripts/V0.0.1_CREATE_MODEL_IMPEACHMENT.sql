CREATE TABLE impeachments(
	id INT NOT NULL,
    company_id INT NOT NULL,
	name_impeachment VARCHAR(60) NULL,
	description_impeachment TEXT NULL
) CONSTRAINT pk_Impeachment primary key(id)