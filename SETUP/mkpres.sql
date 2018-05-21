
begin;

create table presidents (
    num int primary key,
    lname varchar(32),
    fname varchar(64),
    dstart date,
    dend date,
    birthplace varchar(128),
    birthstate varchar(32),
    dbirth date,
    ddeath date,
    party varchar(32)
);


INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (1,'Washington','George','1789-04-30','1797-03-04','Westmoreland County','Virginia','1732-02-22','1799-12-14','no party');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (2,'Adams','John','1797-03-04','1801-03-04','Braintree, Norfolk','Massachusetts','1735-10-30','1826-07-04','Federalist');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (3,'Jefferson','Thomas','1801-03-04','1809-03-04','Albermarle County','Virginia','1743-04-13','1826-07-04','Democratic - Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (4,'Madison','James','1809-03-04','1817-03-04','Port Conway','Virginia','1751-03-16','1836-06-28','Democratic - Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (5,'Monroe','James','1817-03-04','1825-03-04','Westmoreland County','Virginia','1758-04-28','1831-07-04','Democratic - Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (6,'Adams','John Quincy','1825-03-04','1829-03-04','Braintree, Norfolk','Massachusetts','1767-07-11','1848-02-23','Democratic - Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (7,'Jackson','Andrew','1829-03-04','1837-03-04','Waxhaw','South Carolina','1767-03-15','1845-06-08','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (8,'Van Buren','Martin','1837-03-04','1841-03-04','Kinderhook','New York','1782-12-05','1862-07-24','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (9,'Harrison','William Henry','1841-03-04','1841-04-04','Berkeley','Virginia','1773-02-09','1841-04-04','Whig');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (10,'Tyler','John','1841-04-04','1845-03-04','Charles City County','Virginia','1790-03-29','1862-01-18','Whig');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (11,'Polk','James Knox','1845-03-04','1849-03-03','Mecklenburg County','North Carolina','1795-11-02','1849-06-15','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (12,'Taylor','Zachary','1849-03-05','1850-07-09','Orange County','Virginia','1784-11-24','1850-07-09','Whig');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (13,'Fillmore','Millard','1850-07-09','1853-03-04','Cayuga County','New York','1800-01-07','1874-03-08','Whig');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (14,'Pierce','Franklin','1853-03-04','1857-03-04','Hillsboro','New Hampshire','1804-11-23','1869-10-08','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (15,'Buchanan','James','1857-03-04','1861-03-04','Cove Gap','Pennsylvania','1791-04-23','1868-06-01','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (16,'Lincoln','Abraham','1861-03-04','1865-04-15','Hodgenville, Hardin County','Kentucky','1809-02-12','1865-04-15','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (17,'Johnson','Andrew','1865-04-15','1869-03-04','Raleigh','North Carolina','1808-12-29','1875-07-31','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (18,'Grant','Ulysses Simpson','1869-03-04','1877-03-04','Point Pleasant','Ohio','1822-04-27','1885-07-23','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (19,'Hayes','Rutherford Birchard','1877-03-04','1881-03-04','Delaware','Ohio','1822-10-04','1893-01-17','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (20,'Garfield','James Abram','1881-03-04','1881-09-19','Orange, Cuyahoga County','Ohio','1831-11-19','1881-09-19','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (21,'Arthur','Chester Alan','1881-09-20','1885-03-04','Fairfield','Vermont','1829-10-05','1886-11-18','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (22,'Cleveland','Grover','1885-03-04','1889-03-04','Caldwell','New Jersey','1837-03-18','1908-06-24','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (23,'Harrison','Benjamin','1889-03-04','1893-03-04','North Bend','Ohio','1833-08-20','1901-03-13','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (24,'Cleveland','Grover','1893-03-04','1897-03-04','Caldwell','New Jersey','1837-03-18','1908-06-24','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (25,'McKinley','William','1897-03-04','1901-09-14','Niles','Ohio','1843-01-29','1901-09-14','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (26,'Roosevelt','Theodore','1901-09-14','1909-03-04','New York City','New York','1858-10-27','1919-01-06','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (27,'Taft','William Howard','1909-03-04','1913-03-04','Cincinnati','Ohio','1857-09-15','1930-03-08','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (28,'Wilson','Woodrow','1913-03-04','1921-03-04','Staunton','Virginia','1856-12-28','1924-02-03','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (29,'Harding','Warren Gamaliel','1921-03-04','1923-08-02','Blooming Grove','Ohio','1865-11-02','1923-08-02','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (30,'Coolidge','Calvin','1923-08-03','1929-03-04','Plymouth','Vermont','1872-07-04','1933-01-05','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (31,'Hoover','Herbert Clark','1929-03-04','1933-03-04','West Branch','Iowa','1874-08-10','1964-10-20','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (32,'Roosevelt','Franklin Delano','1933-03-04','1945-04-12','Hyde Park','New York','1882-01-30','1945-04-12','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (33,'Truman','Harry S.','1945-04-12','1953-01-20','Lamar','Missouri','1884-05-08','1972-12-26','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (34,'Eisenhower','Dwight David','1953-01-20','1961-01-20','Denison','Texas','1890-10-14','1969-03-28','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (35,'Kennedy','John Fitzgerald','1961-01-20','1963-11-22','Brookline','Massachusetts','1917-05-29','1963-11-22','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (36,'Johnson','Lyndon Baines','1963-11-22','1969-01-20','near Stonewall','Texas','1908-08-27','1973-01-22','Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (37,'Nixon','Richard Milhous','1969-01-20','1974-08-09','Yorba Linda','California','1913-01-09','1994-04-22','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (38,'Ford','Gerald Rudolph','1974-08-09','1977-01-20','Omaha','Nebraska','1913-07-14','2006-12-26','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (39,'Carter','James Earl ''Jimmy''','1977-01-20','1981-01-20','Plains','Georgia','1924-10-01',NULL,'Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (40,'Reagan','Ronald Wilson','1981-01-20','1989-01-20','Tampico','Illinois','1911-02-06','2004-06-05','Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (41,'Bush','George Herbert Walker','1989-01-20','1993-01-20','Milton','Massachusetts','1924-06-12',NULL,'Republican');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (42,'Clinton','William Jefferson ''Bill''','1993-01-20','2001-01-20','Hope','Arkansas','1946-08-19',NULL,'Democratic');
        

INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (43,'Bush','George Walker','2001-01-20','2009-01-20','New Haven','Connecticut','1946-07-06',NULL,'Republican');
        
INSERT INTO presidents
(num,lname,fname,dstart,dend,birthplace,birthstate,dbirth,ddeath,party)
VALUES (44,'Obama','Barack Hussein','2009-01-20',NULL,'Honolulu','Hawaii','1961-08-04',NULL,'Democratic');
        
commit;