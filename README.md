

# Introduction

In this project we will build a MySQL database using the Internet Movie Database
(IMDb) dataset. The dataset consists of 7 compressed tab-separated-value
(\*.tsv) files, which are explained and available for download from
[here](https://www.imdb.com/interfaces/).


The purpose of this project is to do the following:

- Learn about and use the database management system MySQL.

- Learn the essentials of database design, e.g., Entity-Relationship diagrams,
logical schema, and database normalisation.

- Practice database querying by posing basic and more advanced queries using
MySQL directly and also indirectly using python.

The tangible steps we will take in this project are:

- Understand the data in the IMDb dataset.

- Design a relational database and store the IMDb data in it.

  - Model the database using an Entity-Relationship (ER) diagram.
  - Perform normalisation and restructure the IMDb data using python.
  - Create MySQL database.
  - Load data into the database.
  - Add primary and foreign key constraints.
  - Create database indexes.

- Ask questions of the IMDb data, so as to practice simple and more advanced SQL
queries.
- Add triggers and insertion,deletion functions via python.
- providing an authentication


- Throughout we will adhere to SQL style conventions, e.g., please see SQL Style
guide <https://www.sqlstyle.guide/>. In particular, underscores will be used in
attribute names rather than camel case, which is used in the IMDb data files.

## Dataset details

Each dataset is contained in a gzipped tab-separated-values (TSV) formatted
file in the UTF-8 character set. The first line in each file contains headers
that describe what is in each column. A "\\N" is used to denote that a
particular field is missing or has a NULL value for that title or name. It
should be noted that the data available for download from the IMDb website is
not the full dataset, but it will suffice for our purposes. The available IMDb
data files are as follows:

### name.basics.tsv.gz

Contains the following information for names:

  - nconst (string) - alphanumeric unique identifier of the name/person.
  - primaryName (string)– name by which the person is most often credited.
  - birthYear – in YYYY format.
  - deathYear – in YYYY format if applicable, else "\\N".
  - primaryProfession (array of strings) – the top-3 professions of the person.
  - knownForTitles (array of tconsts) – titles the person is known for.

### title.basics.tsv.gz

Contains the following information for titles:

  - tconst (string) - alphanumeric unique identifier of the title.
  - titleType (string) – the type/format of the title (e.g. movie, short,
    tvseries, tvepisode, video, etc).
  - primaryTitle (string) – the more popular title / the title used by the
  filmmakers on promotional materials at the point of release.
  - originalTitle (string) - original title, in the original language.
  - isAdult (boolean) - 0: non-adult title; 1: adult title.
  - startYear (YYYY) – represents the release year of a title. In the case of TV
  Series, it is the series start year.
  - endYear (YYYY) – TV Series end year. "\\N" for all other title types.
  - runtimeMinutes – primary runtime of the title, in minutes.
  - genres (string array) – includes up to three genres associated with the
  title.


### title.akas.tsv.gz

Contains the following information for titles:

  - titleId (string) - a tconst which is an alphanumeric unique identifier of
  the title.
  - ordering (integer) – a number to uniquely identify rows for a given titleId.
  - title (string) – the localised title.
  - region (string) - the region for this version of the title.
  - language (string) - the language of the title.
  - types (array) - Enumerated set of attributes for this alternative title. One
  or more of the following: "alternative", "dvd", "festival", "tv", "video",
  "working", "original", "imdbDisplay". New values may be added in the future
  without warning.
  **Please note that types is said to be an array. In the data we have this
  appears to not be true. There appears to be only one string for each pair of
  titleId and ordering values. Also, there are many NULL (\\N) values in this
  field (~95%).**

  - attributes (array) - Additional terms to describe this alternative title,
  not enumerated.
  **Please note that attributes is said to be an array. In the data we have this
  appears to not be true. There appears to be only one string for each pair of
  titleId and ordering values. There are many NULL (\\N) values in this field
  (~99%).**

  - isOriginalTitle (boolean) – 0: not original title; 1: original title.


### title.crew.tsv.gz

Contains the director and writer information for all the titles in IMDb. Fields
include:

  - tconst (string) - alphanumeric unique identifier of the title.
  - directors (array of nconsts) - director(s) of the given title.
  - writers (array of nconsts) – writer(s) of the given title.

### title.episode.tsv.gz

Contains the tv episode information. Fields include:

  - tconst (string) - alphanumeric identifier of episode.
  - parentTconst (string) - alphanumeric identifier of the parent TV Series.
  - seasonNumber (integer) – season number the episode belongs to.
  - episodeNumber (integer) – episode number of the tconst in the TV series.

### title.principals.tsv.gz

Contains the principal cast/crew for titles

  - tconst (string) - alphanumeric unique identifier of the title.
  - ordering (integer) – a number to uniquely identify rows for a given titleId.
  - nconst (string) - alphanumeric unique identifier of the name/person.
  - category (string) - the category of job that person was in.
  - job (string) - the specific job title if applicable, else "\\N".
  - characters (string) - the name of the character played if applicable, else
  "\\N" (It is really "[role1,role2,....]" or "\\N").

### title.ratings.tsv.gz

Contains the IMDb rating and votes information for titles

  - tconst (string) - alphanumeric unique identifier of the title.
  - averageRating – weighted average of all the individual user ratings.
  - numVotes - number of votes the title has received.


## Entity-Relationship (ER) diagram

The IMDb data as provided is not normalised. We first design an entity-relationship diagram for our IMDb relational database. This is shown below.  

![IMDb ER diagram.](images/imdb-er-diagram.png)

## Logical schema

We then normalise our ER diagram and obtain the logical schema illustrated below. Note the following:

- New tables were created for multi-valued attributes, such as Title_genres.

- We pulled the rating information attributes from the Titles entity, because many titles didn't have a rating. If we were to store them in the Titles table, then we would have stored many NULL values. Instead we decided to separate this information, by putting it into the table Title_ratings.

![IMDb logical schema diagram.](images/imdb-logical-schema.png)

## Prepare the IMDb data and build the IMDb database

### 1) Preprocess the IMDb dataset  

The IMDb data is preprocessed using python. The script  `imdb_converter.py`
reads in the 7 data files, cleans and normalises the IMDb data. After which, the
desired set of tables are output as tab-separate-value (tsv) files.

![Terminal screenshot imdb_converter.py](images/terminal_screenshots/Terminal_screenshot-imdb_converter.png)

### 2) Build MySQL database

The sequence of steps to build the database are as follows:

1. Open MySQL in terminal:

```bash
$ mysql -u root -p --local-infile
```

The SQL commands to build the database described above by the ER diagram and
logical schema are contained in 4 `*.sql scripts`:

- imdb-create-tables.sql
- imdb-load-data.sql
- imdb-add-constraints.sql
- imdb-index-tables.sql

2. Create IMDb data base in MySQL:

```sqlmysql  
mysql> SOURCE C:\Users\jaisw\Desktop\Final_touch\SQL_FILES\imdb-create-tables.sql
```

3. Load data using this script in MySQL:
```sqlmysql
mysql> SOURCE C:\Users\jaisw\Desktop\Final_touch\SQL_FILES\imdb-load-data.sql
```

4. Add constraints to the IMDb database in MySQL
```sqlmysql
mysql> SOURCE C:\Users\jaisw\Desktop\Final_touch\SQL_FILES\imdb-add-constraints.sql
```

5. Add indexes to the IMDb database in MySQL
```sqlmysql
mysql> SOURCE C:\Users\jaisw\Desktop\Final_touch\SQL_FILES\imdb-index-tables.sql
```


## SQL Queries using MySQL

After creating and loading data into the database, we can now pose queries to
it. In the file `SQL_Queries_1.sql` we consider many questions and answer them
by querying the IMDb database. This section is an on going piece of work. We
intend to add more questions and queries to the repository as we practice SQL.

For each query in the file `SQL_Queries_1.sql` we create a view by

```sqlmysql
CREATE OR REPLACE VIEW Q1(column_1,column_2)
AS
...
;
```

The result of the query which is stored in the view can be seen by
```sqlmysql
SELECT * FROM Q1;
```

To delete the view
```sqlmysql
DROP VIEW Q1;
```

The database is quite large, so for illustration purposes we will quite often
limit ourselves to the first few entries only.

### Example queries

We will consider a few queries for illustration purposes.

- Query 9: Who are the actors who played James Bond in a movie? How many times
did they play the role of James Bond?

```sqlmysql
CREATE OR REPLACE VIEW Q9(name_id,name_,number_of_films)
AS SELECT N.name_id, N.name_, COUNT(*) AS number_of_films
FROM Names_ AS N, Had_role AS H, Titles AS T
WHERE H.role_ LIKE 'James Bond'
AND T.title_type LIKE 'movie'
AND T.title_id = H.title_id
AND N.name_id = H.name_id
GROUP BY N.name_id;
```
To see the results of this query:

```sqlmysql
SELECT * FROM Q9;
```

- Query 10: How many actors played James Bond?

```sqlmysql
CREATE OR REPLACE VIEW Q10(number_of_JB_actors)
AS SELECT COUNT(DISTINCT name_id) AS number_of_JB_actors
FROM Q9;
```
To see the results of this query:
```sqlmysql
SELECT * FROM Q10;
```
- Query 11: I don't recognise some of these names lets look at them more closely

```sqlmysql
CREATE OR REPLACE VIEW Q11(name_,title_id,primary_title,start_year)
AS SELECT Q9.name_, T.title_id, T.primary_title, T.start_year
FROM Q9, Titles AS T, Had_role AS H
WHERE Q9.name_id = H.name_id
AND H.role_ LIKE 'James Bond'
AND T.title_id = H.title_id
AND T.title_type LIKE 'movie'
ORDER BY T.start_year DESC;
```

To see the results of this query:
```sqlmysql
SELECT * FROM Q11;
```

        
