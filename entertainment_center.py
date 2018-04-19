import fresh_tomatoes
import media


# This section is used to initialize the values for each movie

toy_story = media.Movie("Toy Story",
                        "A story of a body and his toys that come to life",
                        "http://upload.wikimedia.org"
                        "/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0"
                     "/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=5PSNL1qE6VY")


school_of_rock = media.Movie("School of Rock",
                             "Dewey Finn poses as a substitute teacher",
                             "http://upload.wikimedia.org/wikipedia/en/1/11"
                             "/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")


hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42"
                           "/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")


mad_max_fury_road = media.Movie("Mad Max Fury Road",
                                "IStory of Max and Furiosa",
                                "https://encrypted-tbn3.gstatic.com"
                                "/images?q=tbn:ANd9GcSY9szIPbtk1-hwxdEVRJIHT_"
                                "pgYGNnFkFSWsCjlKFGP3Pu77Oo",
                                "https://www.youtube.com/watch?v=YWNWi-ZWL3c")


ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50"
                          "/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Use the "open_movies_page" function to
# create and open an html webpage or website that shows those movies

movies = [toy_story, avatar, school_of_rock,
          hunger_games, mad_max_fury_road, ratatouille]
fresh_tomatoes.open_movies_page(movies)
