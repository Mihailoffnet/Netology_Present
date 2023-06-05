-- самый длинный трек и его название
SELECT track_name, track_duration FROM track 
WHERE track_duration = 
      (SELECT MAX(track_duration) from track);
      
-- Название треков, продолжительность которых не менее 3,5 минут
SELECT track_name, track_duration FROM track 
WHERE track_duration >= 210;
     
-- Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT collection_name, collection_years FROM collection 
WHERE collection_years BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова
SELECT singer_name FROM singer 
WHERE singer_name NOT LIKE '% %';

-- Название треков, которые содержат слово «мой» или «my»
SELECT track_name FROM track 
WHERE UPPER(track_name) 
      LIKE '%MY%' OR UPPER(track_name) LIKE '%МОЙ%';