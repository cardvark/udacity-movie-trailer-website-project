import media
import fresh_tomatoes
# Note - good practice to create Class in separate file, import file.

toy_story = media.Movie(
    'Toy Story', 
    'A story of a boy and his toys come to life',
    'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://www.youtube.com/watch?v=vwyZH85NQC4')

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet',
    'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

star_wars_force_awakens = media.Movie(
    'Star Wars: The Force Awakens',
    'The Empire has fallen, but a new order threatens the Republic',
    'https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg', # NOQA
    'https://www.youtube.com/watch?v=sGbxmsDFVnE')

school_of_rock = media.Movie(
    'School of Rock',
    'Jack Black pretends to be a teacher and starts a band with his students',
    'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg', # NOQA
    'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie(
    'Ratatouille',
    'A rat puppeteers a goof in order to become a 5-star chef',
    'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
    'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie(
    'Midnight in Paris',
    'A screenwriter spends a groundhog day in Paris',
    'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg', # NOQA
    'https://www.youtube.com/watch?v=FAfR8omt-CY')

hunger_games = media.Movie(
    'The Hunger Games',
    'Young kids fight in an arena for food',
    'https://upload.wikimedia.org/wikipedia/en/a/ab/Hunger_games.jpg',
    'https://www.youtube.com/watch?v=mfmrPu43DF8')

# print toy_story.storyline
# avatar.show_trailer()

moviesList = [
    toy_story,
    avatar,
    star_wars_force_awakens,
    school_of_rock,
    ratatouille,
    midnight_in_paris,
    hunger_games
]

# Calling open_movies_page method to create the web page and open in browser.
fresh_tomatoes.open_movies_page(moviesList)