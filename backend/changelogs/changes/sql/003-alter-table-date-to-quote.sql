ALTER TABLE date_to_quote 
ADD column movie VARCHAR(256),
ADD CONSTRAINT fk_movie FOREIGN KEY (movie) REFERENCES movie(title) ON DELETE SET null; 