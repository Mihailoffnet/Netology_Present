-- https://github.com/netology-code/py-homeworks-db/tree/SQLPY-76/04-dml


--Количество исполнителей в каждом жанре

SELECT jenre_id, singer_name FROM singer_jenre
LEFT JOIN singer on singer_jenre.singer_id = singer.singer_id;
--LEFT JOIN jenre on singer_jenre.jenre_id = jenre.jenre_id;
-- GROUP BY jenre_id;

SELECT jenre_id, singer_name FROM singer
LEFT join singer_jenre on singer_jenre.singer_id = singer.singer_id
LEFT join jenre on jenre.jenre_id = singer_jenre.jenre_id;
-- GROUP BY jenre_id;