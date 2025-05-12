# Hash Tables in Python
# Usage of Dictionaries in Python

movies = {
    "marvel":["Caption America: The First Avenger","Shang-Chi and the Legend of the Ten Rings","Thor: Ragnarok","Doctor Strange in the Multiverse of Madness"],
    "dc":["Batman v Superman: Dawn of Justice","Aquaman","Man of Steel"],
    "star_wars":["A new Hope","The Empire Strikes Back","Return of the Jedi","The Phantom Menace","Attack of the Clones","Revenge of the Sith"],
    "harry_potter":["Harry Potter and the Philosopher's Stone","Harry Potter and the Chamber of Secrets","Harry Potter and the Prisoner of Azkaban","Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix","Harry Potter and the Half-Blood Prince","Harry Potter and the Deathly Hallows: Part 1","Harry Potter and the Deathly Hallows: Part 2"],
    "fast_and_furious":["The Fast and the Furious","2 Fast 2 Furious","The Fast and the Furious: Tokyo Drift","Fast & Furious","Fast Five","Fast & Furious 6","Furious 7","The Fate of the Furious"],
    "transformers":["Transformers","Transformers: Revenge of the Fallen","Transformers: Dark of the Moon","Transformers: Age of Extinction","Transformers: The Last Knight"],
    "marvel_spider_man":["Spider: Homecoming","Spider: Far From Home","Spider: No Way Home"],
    "star_trek":["Star Trek: The Motion Picture","Star Trek II: The Wrath of Khan","Star Trek III: The Search for Spock","Star Trek IV: The Voyage Home","Star Trek V: The Final Frontier","Star Trek VI: The Undiscovered Country","Star Trek: Generations","Star Trek: First Contact","Star Trek: Insurrection","Star Trek: Nemesis"],
    "sonic_the_hedgehog":["Sonic the Hedgehog","Sonic the Hedgehog 2"],
    "ice_age":["Ice Age","Ice Age: The Meltdown","Ice Age: Dawn of the Dinosaurs","Ice Age: Continental Drift","Ice Age: Collision Course"],
    "despicable_me":["Despicable Me","Despicable Me 2","Minions","Despicable Me 3"]
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

def hash_function(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value

def hash_table(dictionary):
    hash_table = dict()
    for i in range(0,6):
        hash_table[i] = []

    for key in dictionary.keys():
        hash_key = hash_function(key) % 5
        hash_table[hash_key].append(key)

    return hash_table


def main():
    get_genre_list()
    get_movies_by_genre("marvel")

if __name__ == "__main__":
    main()
    print("Hash table: ",hash_table(movies))
