BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `UPORABNIK` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`ime`	CHAR NOT NULL,
	`priimek`	CHAR NOT NULL,
	`email`	CHAR NOT NULL UNIQUE,
	`geslo`	CHAR NOT NULL
);
CREATE TABLE IF NOT EXISTS `SLIKE_NAKUPA` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`slika_id`	INTEGER,
	`nakup_id`	INTEGER,
	FOREIGN KEY(`slika_id`) REFERENCES `SLIKA`(`id`),
	FOREIGN KEY(`nakup_id`) REFERENCES `NAKUP`(`id`)
);
CREATE TABLE IF NOT EXISTS `SLIKA` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`dosegljivost`	BOOLEAN NOT NULL,
	`naslov`	CHAR NOT NULL,
	`vrsta`	CHAR NOT NULL,
	`cena`	DOUBLE NOT NULL
);
CREATE TABLE IF NOT EXISTS `RACUN` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`placan`	BOOLEAN NOT NULL,
	`datum`	DATE NOT NULL,
	`vrednost`	DOUBLE NOT NULL
);
CREATE TABLE IF NOT EXISTS `NAKUP` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`racun_id`	INTEGER,
	FOREIGN KEY(`racun_id`) REFERENCES `RACUN`(`id`)
);
CREATE TABLE IF NOT EXISTS `KOSARICA` (
	`id`	integer PRIMARY KEY AUTOINCREMENT,
	`uporabnik_id`	integer,
	`slika_id`	integer,
	`nakup_id`	integer,
	`datum_vstavljanja`	char NOT NULL,
	`datum_izbrisa`	char
);
COMMIT;
