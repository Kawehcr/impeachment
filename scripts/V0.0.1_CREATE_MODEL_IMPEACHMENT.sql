CREATE TABLE impeachments(
	id INT NOT NULL,
    company_id INT NOT NULL,
	name_impeachment VARCHAR(60),
	description_impeachment TEXT
) CONSTRAINT pk_impeachments primary key(id)