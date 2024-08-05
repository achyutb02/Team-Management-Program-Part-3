-- Drop the table if it already exists
DROP TABLE IF EXISTS Player;

-- Create the table
CREATE TABLE Player(
    playerID    INTEGER PRIMARY KEY     NOT NULL,
    batOrder    INTEGER                 NOT NULL,
    firstName   TEXT                    NOT NULL,
    lastName    TEXT                    NOT NULL,
    position    TEXT                    NOT NULL,
    atBats      INTEGER                 NULL,
    hits        INTEGER                 NULL
);

-- Populate the table
INSERT INTO Player VALUES
(1,1,'Dominick','Gilbert','1B',537,170),
(2,2,'Craig','Mitchel','CF',396,125),
(3,3,'Jack','Quinn','RF',545,99),
(4,4,'Simon','Harris','C',450,135),
(5,5,'Darryl','Moss','3B',501,120),
(6,6,'Grady','Guzman','SS',443,131),
(7,7,'Wallace','Cruz','LF',443,131),
(8,8,'Cedric','Cooper','2B',165,54),
(9,9,'Alberto','Gomez','P',72,19);