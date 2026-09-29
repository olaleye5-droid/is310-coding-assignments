favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]
print(favorite_movies)

total_favorite_movies = len(favorite_movies)
print("How many total favorite movies do we have?", total_favorite_movies)

print(type(favorite_movies))
print(type(favorite_movies[0]))

print('Enter your favorite movie of the last year:')
recent_favorite_movie = input()
print('Your favorite movie is of the last year:', recent_favorite_movie)

favorite_movies[0]['long_description'] = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. The Waschowskis created a plot set in a dystopian future where humanity is unknowingly trapped inside a simulated reality, the Matrix, created by intelligent machines to distract humans while using their bodies as an energy source. In the movie, the main character, Neo, is a computer programmer who learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the Matrix."

print(favorite_movies[0])

favorite_movies[0]['long_description'] = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. The Waschowskis created a plot set in a dystopian future where humanity is unknowingly trapped inside a simulated reality, the Matrix, created by intelligent machines to distract humans while using their bodies as an energy source. In the movie, the main character, Neo, is a computer programmer who learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the Matrix."

print(favorite_movies[0])

split_description = favorite_movies[0]['long_description'].split(' ')
print(split_description)
print(len(split_description))

favorite_movies[0]['short_description'] = ' '.join(split_description[:10])
print(favorite_movies[0]['short_description'])

print(' '.join(split_description))

edited_description = favorite_movies[0]['long_description'].replace('the Wachowskis', 'Lana and Lilly Wachowski')
print(edited_description)

print(favorite_movies[0]['long_description'].lower())
print(favorite_movies[0]['long_description'].upper())
print(favorite_movies[0]['long_description'].title())
print(favorite_movies[0]['long_description'].strip())

for movie in favorite_movies:
    print(movie['name'])

def print_movie_name(movie):
    print(movie['name'])

print_movie_name(favorite_movies[0])

def print_movie_name_and_year(movie):
    movie_data = movie['name'] + ' was released in ' + str(movie['release_year'])
    return movie_data

new_movie_data = print_movie_name_and_year(favorite_movies[0])
print(new_movie_data)

if 'Matrix' in favorite_movies[0]['name']:
    print('Matrix')
else:
    print('No Matrix')

if favorite_movies[0]['release_year'] > favorite_movies[1]['release_year']:
    print('The Matrix')
else:
    print('Star Wars')


## Homework

def check_movie_release(movie):
    if movie['release_year'] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie['name']
recent_movies = []

for movie in favorite_movies:
    result = check_movie_release(movie)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)