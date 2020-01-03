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
        genres_count = {}
        max = 0
        for song in userSongs[user]:
            genre = genreSong[song]
            if genre in genres_count:
                genres_count[genre] += 1
            else:
                genres_count[genre] = 1
            if genres_count[genre] > max:
                max = genres_count[genre]
        userGenres[user] = [gen for gen,count in genres_count.items() if count == max]
        
            
    return userGenres

if __name__ == '__main__':
    userSongs, songGenres = initialize()
    print(favGenres(userSongs, songGenres))
