import pandas as pd
spotify = pd.read_csv('top_10000_1950-now.csv', index_col='Track URI')
spotify.head()
album = spotify[['Artist URI(s)','Album URI','Album Name','Album Artist Name(s)','Album Release Date','Album Genres']]
spotify = spotify.drop(columns=['Album URI','Album Name','Album Artist URI(s)','Album Artist Name(s)','Album Image URL','Copyrights'])
spotify
#checking for missing values
spotify.isnull().sum()
spotify = spotify.drop(columns='Album Genres')
album = album.drop(columns='Album Genres')
spotify = spotify.dropna(how='any')
album = album.dropna(how='any')
  spotify.isnull().sum()
album.isnull().sum()
spotify.drop(columns='ISRC')
spotify[spotify.duplicated()]
spotify.drop_duplicates(inplace=True)
album[album.duplicated()]
spotify['Album Release Date'] = spotify['Album Release Date'].str.split('-').str[0]
spotify['Track Duration (ms)']=spotify['Track Duration (ms)']//60000
