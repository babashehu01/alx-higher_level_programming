-- This script lists all rows with a name

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
