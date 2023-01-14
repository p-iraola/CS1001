'''
Please write a function named find_movies(database: list, search_term: str), 
which processes the movie database created in the previous exercise. 
The function should formulate a new list, 
which contains only the movies whose title includes the word searched for. 
Capitalisation is irrelevant here. 
A search for ana should return a list containing both Anaconda and Management.
'''


def find_movies(database: list, search_term: str):
    new_list = []
    for movies in database:
        if search_term in movies['name'].lower():
            new_list.append(movies)
    return new_list