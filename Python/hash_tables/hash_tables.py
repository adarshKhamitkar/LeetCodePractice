# Hash Tables in Python
# Usage of Dictionaries in Python

movies = {
    "marvel":["Caption America: The First Avenger","Shang-Chi and the Legend of the Ten Rings","Thor: Ragnarok","Doctor Strange in the Multiverse of Madness"],
    "dc":["Batman v Superman: Dawn of Justice","Aquaman","Man of Steel"],
    "star_wars":["A new Hope","The Empire Strikes Back","Return of the Jedi","The Phantom Menace","Attack of the Clones","Revenge of the Sith"],
    "harry_potter":["Harry Potter and the Philosopher's Stone","Harry Potter and the Chamber of Secrets","Harry Potter and the Prisoner of Azkaban","Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix","Harry Potter and the Half-Blood Prince","Harry Potter and the Deathly Hallows: Part 1","Harry Potter and the Deathly Hallows: Part 2"]
}

# Mutation: Adding new movies to the dictionary
movies["marvel"].append("Avengers: Infinity War")
movies["dc"].append("Wonder Woman:1984")

movies["Brahmastra"] = ["Part 1: Shiva","Part 2:Dev","Part 3: Brahmastra"]

def get_genre_list():
    for genre in movies.keys():
        print("---> "+genre+"\n")


def get_movies_by_genre(genre):
    if genre in movies:
        if genre == "harry_potter".lower():
            print("All the movies in this genre are: \n")
        else:
            print("Best movies in the genre "+genre+" are: \n")
        print(movies.get(genre))
    else: print("genre "+genre+" not found!\n")

def remove_movie(genre, movie):
    if genre in movies:
        if movie in movies[genre]:
            movies[genre].remove(movie)
            print("Movie "+movie+" removed from the genre "+genre+"\n")
        else: print("Movie "+movie+" not found in the genre "+genre+"\n")
    else: print("Genre "+genre+" not found!\n")

def remove_genre(genre):
    if genre in movies:
        del movies[genre]
        print("Genre "+genre+" removed from the list of genres\n")
    else: print("Genre "+genre+" not found!\n")

statement = "Harry Potter and the Philosopher's Stone, Harry Potter and the Chamber of Secrets, Harry Potter and the Prisoner of Azkaban, Harry Potter and the Goblet of Fire, Harry Potter and the Order of the Phoenix, Harry Potter and the Half-Blood Prince, Harry Potter and the Deathly Hallows: Part 1, Harry Potter and the Deathly Hallows: Part 2"

def main():
    get_genre_list()
    get_movies_by_genre("marvel")

if __name__ == "__main__":
    #main()
    word_counts = dict()
    for word in statement.split():
        word_counts[word] = word_counts.get(word,0) + 1
    print(word_counts)
