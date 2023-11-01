DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS people CASCADE;
DROP TABLE IF EXISTS movie CASCADE;
DROP TABLE IF EXISTS people_movie CASCADE;
CREATE TABLE genre(id serial PRIMARY KEY, genre_name VARCHAR(255) NOT NULL UNIQUE);
CREATE TABLE people(id serial PRIMARY KEY,actor_name VARCHAR(255) NOT NULL UNIQUE,birth_day DATE NOT NULL UNIQUE);
CREATE TABLE movie(id serial PRIMARY KEY,title VARCHAR(255) NOT NULL UNIQUE,tagline TEXT NOT NULL UNIQUE, summary TEXT NOT NULL UNIQUE, release_year INT NOT NULL UNIQUE, genre_id INTEGER REFERENCES genre(id));
CREATE TABLE people_movie(people_id INTEGER REFERENCES people(id), movie_id INTEGER REFERENCES movie(id));
INSERT INTO genre (genre_name) VALUES ('horror'), ('comedy'), ('movie'), ('western'), ('fantasy');
INSERT INTO people (actor_name, birth_day) VALUES ('Leonardo DiCaprio ', '1978-05-07'), ('Will Smith','1975-05-07'), ('Jackie Chan','1976-05-07'), ('McDuck','1977-05-07'), ('Daniel Radcliffe', '1989-07-23'), ('Emma Watson', '1990-04-15');
INSERT INTO movie (title, tagline, summary, release_year, genre_id) VALUES ('Titanic', 'The story so few lived to tell', 'About ship accedent', '1997', 1), ('I Am Legend', 'The last man on Earth is not alone', 'About last man and a dog', '2007', 2), ('Rush Hour', 'The fastest hands of the east and the biggest mouth of the west', 'About stealing a person', '1998', 3), ('Duck stories', 'Money,money,money', 'About ducks', '1990', 4), ('Harry Potter', 'Draco dormiens nunquam titillandus!', 'The story about magic', '2001', 5); 
INSERT INTO people_movie VALUES (1,1),(2,2),(3,3),(4,4), (5,5), (6,5);
--select *from people_movie --Для просмотра
--select movie.*, genre.* FROM movie JOIN genre ON movie.genre_id = genre.id; --Проба JOIN в отношение 1 to N
--select a.actor_name, b.title from people a join people_movie on a.id = people_movie.people_id join movie b on people_movie.movie_id = b.id; --Проба JOIN в отношение N to N
