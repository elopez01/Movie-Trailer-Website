import fresh_tomatoes
import media

'''
Adding information about the movie:
movie_title, movie_storyline, poster_image,
movie_trailer_url, movie_information, release_date
'''


don_juan = media.Movie("Don Juan DeMarco",
    "Have you ever loved a woman?",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/Don_juan_demarco.jpg",  # NOQA
    "https://www.youtube.com/watch?v=MCpLSvW5s-A",
    "https://en.wikipedia.org/wiki/Don_Juan_DeMarco",  # NOQA
    1994
    )

'''
Adding information about the movie:
movie_title, movie_storyline, poster_image,
movie_trailer_url, movie_information, release_date
'''
beauty_and_beast = media.Movie("Beauty and the Beast",
   "A tale about love",
   "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg",  # NOQA
   "https://www.youtube.com/watch?v=dGboC3UVvX8",
   "https://en.wikipedia.org/wiki/Beauty_and_the_Beast_(1991_film)",  # NOQA
   1991
   )


'''
Adding information about the movie:
movie_title, movie_storyline, poster_image,
movie_trailer_url, movie_information, release_date
'''
dark_knight = media.Movie("Dark Knight",
  "Batman goes against the Joker",
  "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
  "https://www.youtube.com/watch?v=EXeTwQWrcwY",
  "https://en.wikipedia.org/wiki/The_Dark_Knight_(film)",  # NOQA
  2008
  )

'''
Adding information about the movie:
movie_title, movie_storyline, poster_image,
movie_trailer_url, movie_information, release_date
'''
the_waterboy = media.Movie("The Waterboy",
   "Foosball is the Devil!",
   "https://upload.wikimedia.org/wikipedia/en/f/f3/Waterboy-poster-0.jpg",  # NOQA
   "https://www.youtube.com/watch?v=z8yv9eq5s14",
   "https://en.wikipedia.org/wiki/The_Waterboy",
   1998
   )

'''
Adding information about the movie:
movie_title, movie_storyline, poster_image,
movie_trailer_url, movie_information, release_date
'''
scarface = media.Movie("Scarface",
   "The world is yours and everything in it!",
   "https://upload.wikimedia.org/wikipedia/en/7/71/Scarface_-_1983_film.jpg",  # NOQA
   "https://www.youtube.com/watch?v=7pQQHnqBa2E",
   "https://en.wikipedia.org/wiki/Scarface_(1983_film)",  # NOQA
   1983
   )


'''
Adding information about the movie:
movie_title, movie_storyline, poster_image,
movie_trailer_url, movie_information, release_date
'''
independence_day = media.Movie("Independence Day",
   "Going back in time to meeet the authors",
   "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",  # NOQA
   "https://www.youtube.com/watch?v=kA2WzBi2grE",
   "https://en.wikipedia.org/wiki/Independence_Day_(1996_film)",  # NOQA
   1996
   )

'''
Adding Movies to array to be called by the
fresh_tomatoes.open_movies_page method
'''
movies = [
    don_juan,
    beauty_and_beast,
    dark_knight,
    the_waterboy,
    scarface,
    independence_day
    ]

'''
Passing the movies array as a parameter to
open_movies_page function
'''
fresh_tomatoes.open_movies_page(movies)
