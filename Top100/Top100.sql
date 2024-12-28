sudo su -l postgres
psql
CREATE DATABASE peliculas;
\C peliculas
CREATE TABLE peliculas(
id INT,
Pelicula VARCHAR(70),
Anno estreno INT,
Director VARCHAR(30),
PRIMARY KEY (id) );
CREATE TABLE reparto(
id_peliculas INT ,
nombre VARCHAR(30),
FOREIGN KEY (id_pelicula) REFERENCES peliculas(id) );
\copy peliculas FROM '/home/victor/Escritorio/Top100/peliculas.csv' csv header;
\copy reparto FROM '/home/victor/Escritorio/Top100/reparto.csv';
SELECT id FROM peliculas where pelicula='Titanic';
SELECT  * from reparto where id_pelicula = 2;
SELECT COUNT(id_pelicula) FROM reparto WHERE  nombre = 'Harrison Ford';
SELECT * FROM peliculas where anno >=1990 and anno <=1999 ORDER BY pelicula;
SELECT * FROM peliculas where anno  BETWEEN 1990 and 1999 ORDER BY pelicula;
SELECT peliculas, LENGTH(pelicula) AS longitud_titulo FROM peliculas;
SELECT MAX (LENGTH(pelicula)) from peliculas;



