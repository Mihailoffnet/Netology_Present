-- Добавляем жанры
INSERT INTO jenre VALUES (1, 'Rock'); 
INSERT INTO jenre VALUES (2, 'Metall');
INSERT INTO jenre VALUES (3, 'POP');
INSERT INTO jenre VALUES (4, 'Hip-Hop');
INSERT INTO jenre VALUES (5, 'RAP');

-- Добавляем исполнителей
INSERT INTO singer VALUES (1, 'Metallica');
INSERT INTO singer VALUES (2, 'Eminem');
INSERT INTO singer VALUES (3, 'Kurt Cobain');
INSERT INTO singer VALUES (4, 'Morgenstern');
INSERT INTO singer VALUES (5, 'Britney Spears');


-- Делаем связку исполнителей с жанрами
INSERT INTO singer_jenre VALUES (1, 3);
INSERT INTO singer_jenre VALUES (2, 1);
INSERT INTO singer_jenre VALUES (3, 5);
INSERT INTO singer_jenre VALUES (4, 2);
INSERT INTO singer_jenre VALUES (5, 4);

-- Добавляем альбомы
INSERT INTO album VALUES (1, 'Cadillac', 2021); -- Морген
INSERT INTO album VALUES (2, 'Circus', 2008); -- Спирс
INSERT INTO album VALUES (3, 'In the Zone', 2003); -- Спирс
INSERT INTO album VALUES (4, 'Ride the Lightning', 1986); -- Металлика
INSERT INTO album VALUES (5, 'Kill Em All', 1983); -- Металлика
INSERT INTO album VALUES (6, 'The Slim Shady LP', 1991); -- Эминем
INSERT INTO album VALUES (7, 'Nevermind', 1991); --Кобейн 

-- Делаем связку исполнителей с альбомами
INSERT INTO singer_album VALUES (1, 4);
INSERT INTO singer_album VALUES (2, 5);
INSERT INTO singer_album VALUES (3, 5);
INSERT INTO singer_album VALUES (4, 1);
INSERT INTO singer_album VALUES (5, 1);
INSERT INTO singer_album VALUES (6, 2);
INSERT INTO singer_album VALUES (7, 3);

-- Добавляем треки
INSERT INTO track VALUES (1, 'Мой Cadillac', 1, 192); -- Морген
INSERT INTO track VALUES (2, 'In Bloom', 7, 255); -- Кобейн
INSERT INTO track VALUES (3, 'Hold It Against Me', 3, 310); -- Спирс
INSERT INTO track VALUES (4, 'Escape', 4, 261); -- Металлика
INSERT INTO track VALUES (5, 'My Name Is', 6, 268); -- Эминем
INSERT INTO track VALUES (6, 'Jump In The Fire', 5, 281); -- Металлика
INSERT INTO track VALUES (7, 'Love Story (Taylor Swift)', 2, 207); -- Спирс
INSERT INTO track VALUES (8, 'Stay Away', 7, 211); -- Кобейн

-- Добавляем сборники
INSERT INTO collection VALUES (1, 'TOP 100 2023', 2023); -- Морген
INSERT INTO collection VALUES (2, 'Rock Ballads', 2002); -- Металлика
INSERT INTO collection VALUES (3, 'Disco 2000', 2018); -- Спирс
INSERT INTO collection VALUES (4, 'RAPsody', 2020); -- Эминем

-- Делаем связку сборника с треком
INSERT INTO track_collection VALUES (1, 1);
INSERT INTO track_collection VALUES (6, 2);
INSERT INTO track_collection VALUES (7, 3);
INSERT INTO track_collection VALUES (5, 4);