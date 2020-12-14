CREATE TABLE characters (
    name varchar(255),
    series integer,
    id integer
);
CREATE UNIQUE INDEX uidx_characters_id ON characters (id);
ALTER TABLE characters ADD PRIMARY KEY (id);
ALTER TABLE characters
ALTER COLUMN name SET NOT NULL, 
ALTER COLUMN series SET NOT NULL, 
ALTER COLUMN id SET NOT NULL;