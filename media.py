import webbrowser 

class Movie():
    '''
    This is the init function (constructor) for the movie class
    which takes 6 arguments and those arguments are initialized
    '''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 movie_trailer_url, movie_information, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image_url = poster_image
        self.trailer_url = movie_trailer_url
        self.info = movie_information        
        self.release_date = release_date        


