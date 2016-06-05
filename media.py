import webbrowser

class Movie():
    def __init__(self, movie_title=None, movie_storyline=None, poster_image=None, trailer_youtube=None):
    # '__init__' always takes a 'self' argument
    # 'self' refers to the instance of the class that has been initialized.
    # Added default 'none' values to instance variables.
    
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # simple method to open trailer video.
        webbrowser.open(self.trailer_youtube_url)
