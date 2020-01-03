#Favorite Genres
#https://leetcode.com/discuss/interview-question/373006

def initialize():
    userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
    songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
    return userSongs, songGenres

def favGenres(userSongs, songGenres):
    genreSong = {}
    for genre in songGenres:
        for song in songGenres[genre]:
            genreSong[song] = genre
    
    userGenres = {}
    
    for user in userSongs:
        genres = {}
        for song in userSongs[user]:
            genre = genreSong[song]
            genres[genre] = True
        userGenres[user] = list(genres.keys())
            
    return userGenres

if __name__ == '__main__':
    userSongs, songGenres = initialize()
    print(favGenres(userSongs, songGenres))
