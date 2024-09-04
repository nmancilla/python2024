-- 1) Crear una base de datos llamada películas.  OK

-- 2) Cargar ambos archivos a su tabla correspondiente. OK


create table peliculas (
	id serial primary key,
	pelicula varchar(255) not null,
	estreno int,
	director varchar(255)	
);

create table reparto (
	id_pelicula int not null,
	actor varchar(255) not null
);





--- 3) Obtener el ID de la película “Titanic”. OK

select id from peliculas 
	where pelicula = 'Titanic';




-- 4) Listar a todos los actores que aparecen en la película "Titanic". OK


select actor from 
	peliculas
	join 
	reparto 
	on peliculas.id = reparto.id_pelicula
	where pelicula = 'Titanic';



-- 5) Consultar en cuántas películas del top 100 participa Harrison Ford. OK




select count(pelicula) from
	peliculas
	join
	reparto
	on peliculas.id = reparto.id_pelicula
	where actor = 'Harrison Ford'



-- 6) Indicar las películas estrenadas entre los años 1990 y 1999 ordenadas por título de manera ascendente. OK
	
-- opción 1)
select pelicula, estreno from peliculas
	where estreno between 1990 and 1999
	order by pelicula asc;

-- opción 2)
select pelicula, estreno from peliculas
	where estreno >= 1990 and estreno <= 1999
	order by pelicula asc;



-- 7) Hacer una consulta SQL que muestre los títulos con su longitud, la longitud debe ser
--    nombrado para la consulta como “longitud_titulo”. OK

select pelicula, length(pelicula) as longitud_titulo from  peliculas;



-- 8) Consultar cual es la longitud más grande entre todos los títulos de las películas. OK

select length(pelicula) as longitud_titulo from peliculas
order by longitud_titulo desc
limit 1;

-- Opcional: Query con su título:
select pelicula, length(pelicula) as longitud_titulo from peliculas
order by longitud_titulo desc
limit 1;





