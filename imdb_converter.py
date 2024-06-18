import numpy as np
import pandas as pd
import os
import gzip
import shutil
def unzip_files(folder):

    out_files = []

    
    for file in os.listdir(folder):

        
        if file.endswith(".gz"):

            in_file_path = os.path.join(folder, file)

            out_file_path = os.path.join(folder,file.replace('.gz',''))

            out_files.append(out_file_path)

            print('\tUnzipping ',in_file_path,' to ',out_file_path)

            
            with gzip.open(in_file_path, 'rb') as f_in:
                with open(out_file_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

    return out_files

def make_Aliases(title_akas):
    
    
    

    print("\tMaking 'Aliases' table")

    
    Aliases = title_akas[['titleId','ordering','title','region','language',
    'isOriginalTitle']]

    
    Aliases = Aliases.rename(columns={
    'titleId':'title_id',
    'isOriginalTitle':'is_original_title'
    })

    
    Aliases.to_csv('Aliases.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Alias_types(title_akas):
    
    
    

    print("\tMaking 'Alias_types' table")

    
    Alias_types = title_akas[['titleId','ordering','types']]

    
    Alias_types = Alias_types.rename(columns={
    'titleId':'title_id',
    'types':'type'
    })

    
    
    
    
    
    
    Alias_types = Alias_types.dropna()

    
    Alias_types.to_csv('Alias_types.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Alias_attributes(title_akas):
    
    
    

    print("\tMaking 'Alias_attributes' table")

    
    Alias_attributes =  title_akas[['titleId','ordering','attributes']]

    
    Alias_attributes = Alias_attributes.rename(columns={
    'titleId':'title_id',
    'attributes':'attribute'
    })

    
    
    
    
    
    
    Alias_attributes = Alias_attributes.dropna()

    
    Alias_attributes.to_csv('Alias_attributes.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Directors_and_Writers(title_crew):
    
    

    print("\tMaking 'Directors' and 'Writers' tables")

    
    
    Directors = title_crew[['tconst','directors']]
    Writers = title_crew[['tconst','writers']]

    
    Directors = Directors.rename(columns={
    'tconst':'title_id',
    'directors':'name_id'
    })
    Writers = Writers.rename(columns={
    'tconst':'title_id',
    'writers':'name_id'
    })

    
    Directors = Directors.dropna()
    Writers = Writers.dropna()

    
    Directors = Directors.assign(name_id=Directors.name_id.str.split(',')).explode('name_id').reset_index(drop=True)
    Writers = Writers.assign(name_id=Writers.name_id.str.split(',')).explode('name_id').reset_index(drop=True)

    
    Directors.to_csv('Directors.tsv',index=False,na_rep=r'\N',sep='\t')
    Writers.to_csv('Writers.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Episode_belongs_to(title_episode):
    
    

    print("\tMaking 'Episode_belongs_to' table")

    

    
    Episode_belongs_to = title_episode.rename(columns={
    'tconst':'title_id',
    'parentTconst':'parent_tv_show_title_id',
    'seasonNumber':'season_number',
    'episodeNumber':'episode_number'
    })

    
    Episode_belongs_to.to_csv('Episode_belongs_to.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Names_(name_basics):
    
    
    

    print("\tMaking 'Names_' table")

    
    Names_ = name_basics[['nconst','primaryName','birthYear','deathYear']]

    
    Names_= Names_.rename(columns={
    'nconst':'name_id',
    'primaryName':'name_',
    'birthYear':'birth_year',
    'deathYear':'death_year'
    })

    
    Names_.to_csv('Names_.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Name_worked_as(name_basics):
    
    
    

    print("\tMaking 'Name_worked_as' table")

    
    Name_worked_as = name_basics[['nconst','primaryProfession']]

    
    Name_worked_as = Name_worked_as.dropna()

    
    Name_worked_as = Name_worked_as.rename(columns={
    'nconst':'name_id',
    'primaryProfession':'profession'
    })

    
    Name_worked_as = Name_worked_as.assign(profession=Name_worked_as.profession.str.split(',')).explode('profession').reset_index(drop=True)

    
    Name_worked_as.to_csv('Name_worked_as.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Known_for(name_basics):
    
    
    

    print("\tMaking 'Known_for' table")

    
    Known_for = name_basics[['nconst','knownForTitles']]

    
    Known_for = Known_for.dropna()

    
    Known_for = Known_for.rename(columns={
    'nconst':'name_id',
    'knownForTitles':'title_id'
    })

    
    Known_for = Known_for.assign(title_id=Known_for.title_id.str.split(',')).explode('title_id').reset_index(drop=True)

    
    Known_for.to_csv('Known_for.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Principals(title_principals):
    
    

    print("\tMaking 'Principals' table")

    
    Principals = title_principals[['tconst','ordering','nconst','category','job']]

    
    Principals = Principals.rename(columns={
    'tconst':'title_id',
    'nconst':'name_id',
    'category':'job_category',
    })

    
    Principals.to_csv('Principals.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Had_role(title_principals):
    
    

    print("\tMaking 'Had_role' table")

    
    Had_role = title_principals[['tconst','nconst','characters']]

    
    Had_role =  Had_role.rename(columns={
    'tconst':'title_id',
    'nconst':'name_id',
    'characters':'role_'
    })

    
    Had_role = Had_role.dropna()

    
    
    Had_role['role_'] = Had_role['role_'].str.replace('[\"\[\]]','',regex=True)
    
    Had_role['role_'] = Had_role['role_'].str.replace('\\','|')

    
    Had_role = Had_role.assign(role_=Had_role.role_.str.split(',')).explode('role_').reset_index(drop=True)

    
    
    
    
    
    
    
    
    
    
    
    
    
    Had_role['role_'] = Had_role['role_'].str.title()

    
    Had_role['role_'] = Had_role['role_'].str.replace('^ | $','',regex=True)

    
    Had_role.drop_duplicates(keep=False,inplace=True)

    
    Had_role.to_csv('Had_role.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Titles(title_basics):
    
    
    

    print("\tMaking 'Titles' table")

    
    Titles = title_basics[['tconst','titleType','primaryTitle',
    'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes']]

    
    Titles = Titles.rename(columns={
    'tconst':'title_id',
    'titleType':'title_type',
    'primaryTitle':'primary_title',
    'originalTitle':'original_title',
    'isAdult':'is_adult',
    'startYear':'start_year',
    'endYear':'end_year',
    'runtimeMinutes':'runtime_minutes'
    })

    
    Titles.to_csv('Titles.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Title_genres(title_basics):
    
    
    

    print("\tMaking 'Title_genres' table")

    
    Title_genres = title_basics[['tconst','genres']]

    
    Title_genres = Title_genres.rename(columns={
    'tconst':'title_id',
    'genres':'genre'
    })

    
    Title_genres = Title_genres.dropna()

    
    Title_genres = Title_genres.assign(genre=Title_genres.genre.str.split(',')).explode('genre').reset_index(drop=True)

    
    Title_genres.to_csv('Title_genres.tsv',index=False,na_rep=r'\N',sep='\t')




def make_Title_ratings(title_ratings):
    
    

    print("\tMaking 'Title_ratings' table")

    
    Title_ratings = title_ratings.rename(columns={
    'tconst':'title_id',
    'averageRating':'average_rating',
    'numVotes':'num_votes'
    })

    
    Title_ratings.to_csv('Title_ratings.tsv',index=False,na_rep=r'\N',sep='\t')







data_path = './imdb_data'
print('Looking for IMDb data in: ',data_path,'\n')




data_files = unzip_files(data_path)
print('\n','Reading title.akas.tsv ...','\n')
title_akas = pd.read_csv(os.path.join(data_path,'title.akas.tsv'),
    dtype = {'titleId':'str', 'ordering':'int', 'title':'str', 'region':'str',
    'language':'str', 'types':'str','attributes':'str',
    'isOriginalTitle':'Int64'},
    sep='\t',na_values='\\N',quoting=3)

make_Aliases(title_akas)
make_Alias_types(title_akas)
make_Alias_attributes(title_akas)

del title_akas
print('\n','Reading title.crew.tsv','\n')

title_crew = pd.read_csv(os.path.join(data_path,'title.crew.tsv'),sep='\t',na_values='\\N')

make_Directors_and_Writers(title_crew)

del title_crew




print('\n','Reading title.episode.tsv ...','\n')

title_episode = pd.read_csv(os.path.join(data_path,'title.episode.tsv'),
    dtype = {'tconst':'str', 'parentTconst':'str', 'seasonNumber':'Int64',
    'episodeNumber':'Int64'},
    sep='\t',na_values='\\N')

make_Episode_belongs_to(title_episode)

del title_episode





print('\n','Reading name.basics.tsv ...','\n')

name_basics  = pd.read_csv(os.path.join(data_path,'name.basics.tsv'),
    dtype = {'nconst':'str', 'primaryName':'str', 'birthYear':'Int64',
    'deathYear':'Int64', 'primaryProfession':'str', 'knownForTitles':'str'},
    sep='\t',na_values='\\N')

make_Names_(name_basics)
make_Name_worked_as(name_basics)
make_Known_for(name_basics)

del name_basics




print('\n','Reading title.principals.tsv ...','\n')

title_principals = pd.read_csv(os.path.join(data_path,'title.principals.tsv'),sep='\t',na_values='\\N')

make_Principals(title_principals)
make_Had_role(title_principals)

del title_principals







print('\n','Reading title.basics.tsv ...','\n')

title_basics = pd.read_csv(os.path.join(data_path,'title.basics.tsv'),
    dtype = {'tconst':'str', 'titleType':'str', 'primaryTitle':'str',
    'originalTitle':'str', 'isAdult':'int', 'startYear':'Int64',
    'endYear':'Int64', 'runtimeMinutes':'Int64', 'genres':'str'},
    sep='\t',na_values='\\N',quoting=3)

make_Titles(title_basics)
make_Title_genres(title_basics)

del title_basics




print('\n','Reading title.ratings.tsv ...','\n')

title_ratings = pd.read_csv(os.path.join(data_path,'title.ratings.tsv'),sep='\t',na_values='\\N')

make_Title_ratings(title_ratings)

del title_ratings
