import media
import movie
import tv_show
import webbrowser
import fresh_tomatoes

__author__ = 'michaelmatias'

"""Creates instances of movie objects, adds them to a
list and calls the external rendering function"""

toy_story = movie.Movie(
    'Toy Story',
    '2:30',
    'Movie about toys coming alive',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc',
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg')

avatar = movie.Movie(
    'Avatar',
    '3:01',
    'A marine on an alien planet',
    'https://www.youtube.com/watch?v=cRdxXPV9GNQ',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCl00V9b7iQm7SjPWQ2ZKX6LL8KFj5t165LWsABIixjzmYrMk8qQ')  # noqa

harry_potter = movie.Movie(
    'Harry Potter',
    '2:45',
    'Rescued from the outrageous neglect of his aunt and uncle, '
    'a young boy with a great destiny proves his worth while attending '
    'Hogwarts School of Witchcraft and Wizardry.',
    'https://www.youtube.com/watch?v=PbdM1db3JbY',
    'http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1_SY317_CR8,0,214,317_AL_.jpg')  # noqa

forest_gump = movie.Movie(
    'Forest Gump',
    '2:22',
    'Forrest Gump, while not intelligent, has accidentally been '
    'present at many historic moments, '
    'but his true love, Jenny Curran, eludes him.',
    'https://www.youtube.com/watch?v=uPIEn0M8su0',
    'http://ia.media-imdb.com/images/M/MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@._V1_SX214_AL_.jpg')  # noqa

beethoven = movie.Movie(
    'Beethoven',
    '1:27',
    'Rescued from the outrageous neglect of his aunt and uncle, '
    'a young boy with a great destiny proves '
    'his worth while attending Hogwarts School of Witchcraft and Wizardry.',
    'https://www.youtube.com/watch?v=7eHgKg36xsY',
    'http://ia.media-imdb.com/images/M/MV5BMTIxOTUxMTY5M15BMl5BanBnXkFtZTcwNzI2NDAyMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg')  # noqa

up = movie.Movie(
    'Up',
    '1:36',
    'Seventy-eight year old Carl Fredricksen travels to Paradise Falls in '
    'his home equipped with balloons, '
    'inadvertently taking a young stowaway.',
    'https://www.youtube.com/watch?v=pkqzFUhGPJg',
    'http://ia.media-imdb.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_SX214_AL_.jpg')  # noqa


movies = [toy_story, avatar, harry_potter, forest_gump, beethoven, up]


def run():
    fresh_tomatoes.open_movies_page(movies)
