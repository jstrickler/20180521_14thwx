
begin;

create table knights (
    id serial primary key,
    name varchar(32),
    title varchar(32),
    color varchar(32),
    quest varchar(32),
    comment varchar(128)
);

INSERT INTO knights(name, title, color, quest, comment)
VALUES ('Arthur', 'King', 'blue', 'The Grail', 'King of all the Britons');
        
INSERT INTO knights(name, title, color, quest, comment)
VALUES ('Lancelot', 'Sir', 'red', 'The Grail', '"I could handle some more peril"');

INSERT INTO knights(name, title, color, quest, comment)
VALUES ('Robin', 'Sir', 'yellow', 'not sure', 'He boldly ran away');

INSERT INTO knights(name, title, color, quest, comment)
VALUES ('Bedevere', 'Sir', 'red, no blue!', 'The Grail', 'AAAAARRRRGGGGHHHHH');

INSERT INTO knights(name, title, color, quest, comment)
VALUES ('Gawain', 'Sir', 'red', 'The Grail', 'none');

commit;