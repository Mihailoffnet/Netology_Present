CREATE table if not exists jenre (
	jenre_id SERIAL primary key, 
	name VARCHAR(50) NOT NULL
);

CREATE table if not exists singer (
	singer_id SERIAL primary key, 
	name VARCHAR(80) NOT null
);
	
CREATE TABLE IF NOT EXISTS singer_jenre (
	jenre_id INTEGER REFERENCES jenre(jenre_id),
	singer_id INTEGER REFERENCES singer(singer_id),
	CONSTRAINT j_s PRIMARY KEY (jenre_id, singer_id)
);

CREATE table if not exists albums (
	album_id SERIAL primary key, 
	name VARCHAR(80) NOT NULL,
	years INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS singer_albums (
	album_id INTEGER REFERENCES albums(album_id),
	singer_id INTEGER REFERENCES singer(singer_id),
	CONSTRAINT s_a PRIMARY KEY (album_id, singer_id)
);

CREATE table if not exists tracks (
	track_id SERIAL primary key,
	name VARCHAR(80) NOT null,
	album INTEGER NOT NULL REFERENCES albums(album_id), 
	duration TIME NOT NULL
);

CREATE table if not exists collection (
	collection_id SERIAL primary key, 
	name VARCHAR(60) NOT NULL,
	years INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS track_collection(
	track_id INTEGER REFERENCES tracks(track_id),
	collection_id INTEGER REFERENCES collection(collection_id),
	CONSTRAINT t_c PRIMARY KEY (track_id, collection_id)
);


-- Новая версия с ограничениями

CREATE table if not exists jenre (
	jenre_id SERIAL primary key, 
	name VARCHAR(50) unique NOT NULL
);

CREATE table if not exists singer (
	singer_id SERIAL primary key, 
	name VARCHAR(80) NOT null
);
	
CREATE TABLE IF NOT EXISTS singer_jenre (
	jenre_id INTEGER REFERENCES jenre(jenre_id),
	singer_id INTEGER REFERENCES singer(singer_id),
	CONSTRAINT j_s PRIMARY KEY (jenre_id, singer_id)
);

CREATE table if not exists album (
	album_id SERIAL primary key, 
	name VARCHAR(80) NOT NULL,
	years INTEGER NOT null check (years >= 1900 and years <= 2050)
);

CREATE TABLE IF NOT EXISTS singer_album (
	album_id INTEGER REFERENCES album(album_id),
	singer_id INTEGER REFERENCES singer(singer_id),
	CONSTRAINT s_a PRIMARY KEY (album_id, singer_id)
);

CREATE table if not exists track (
	track_id SERIAL primary key,
	name VARCHAR(80) NOT null,
	album INTEGER NOT NULL REFERENCES album (album_id), 
	duration INTEGER NOT null check (duration > 10 and duration <= 3600)
);

CREATE table if not exists collection (
	collection_id SERIAL primary key, 
	name VARCHAR(60) NOT NULL,
	years INTEGER NOT NULL check (years >= 1900 and years <= 2050)
);

CREATE TABLE IF NOT EXISTS track_collection(
	track_id INTEGER REFERENCES track(track_id),
	collection_id INTEGER REFERENCES collection(collection_id),
	CONSTRAINT t_c PRIMARY KEY (track_id, collection_id)
);
