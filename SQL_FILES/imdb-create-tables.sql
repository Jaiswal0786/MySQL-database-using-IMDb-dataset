-- Delete IMDb database if necessary
DROP DATABASE IF EXISTS IMDb;

-- Create IMDb database

CREATE DATABASE IMDb;

-- Use IMDb database

USE IMDb;
ALTER DATABASE IMDb CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE Titles (
  title_id 			  VARCHAR(255) NOT NULL, -- not null bc PK
  title_type 			VARCHAR(50),
  primary_title 	TEXT, -- some are really long
  original_title 	TEXT, -- some are really long
  is_adult 			  BOOLEAN,
  start_year			INTEGER, -- add better domain here (>1800)
  end_year 			  INTEGER, -- add better domain here (>0)
  runtime_minutes	INTEGER -- add better domain here (>0)
);
CREATE TABLE Title_ratings (
  title_id 			  VARCHAR(255) NOT NULL, -- not null bc PK
  average_rating	FLOAT,
  num_votes			  INTEGER
);
CREATE TABLE Aliases (
  title_id          VARCHAR(255) NOT NULL, -- not null bc PK
  ordering          INTEGER NOT NULL, -- not null bc PK
  title             TEXT NOT NULL,
  region				    CHAR(4),
  language          CHAR(4),
  is_original_title	BOOLEAN
);
CREATE TABLE Alias_types (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  ordering			INTEGER NOT NULL, -- not null bc PK
  type				  VARCHAR(255) NOT NULL-- Only stored if not null
);
CREATE TABLE ALias_attributes (
  title_id			VARCHAR(255) NOT NULL, -- not null bc PK
  ordering			INTEGER NOT NULL, -- not null bc PK
  attribute			VARCHAR(255) NOT NULL -- only stored if not null
);
CREATE TABLE Episode_belongs_to (
  episode_title_id          VARCHAR(255) NOT NULL, -- not null bc PK
  parent_tv_show_title_id   VARCHAR(255) NOT NULL,
  season_number             INTEGER,
  episode_number            INTEGER
);
CREATE TABLE Title_genres (
  title_id    VARCHAR(255) NOT NULL, -- not null bc PK
  genre				VARCHAR(255) NOT NULL -- not null bc PK
);
CREATE TABLE Names_ (
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  name_         VARCHAR(255) NOT NULL, -- everybody has a name
  birth_year    SMALLINT, -- add a better domain here
  death_year    SMALLINT -- add a better domain here
);

CREATE TABLE Name_worked_as (
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  profession    VARCHAR(255) NOT NULL -- not null bc PK
);
CREATE TABLE Had_role (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  role_         TEXT NOT NULL -- not null bc PK
);

CREATE TABLE Known_for (
  name_id       VARCHAR(255) NOT NULL, -- not null bc PK
  title_id      VARCHAR(255) NOT NULL -- not null bc PK
);

CREATE TABLE Directors (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL -- not null bc PK
);

CREATE TABLE Writers (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL -- not null bc PK
);

CREATE TABLE Principals (
  title_id      VARCHAR(255) NOT NULL, -- not null bc PK
  ordering      TINYINT NOT NULL, -- not null bc PK
  name_id       VARCHAR(255) NOT NULL,
  job_category  VARCHAR(255),
  job           TEXT
);
