"""
This file stores all of the movie data
The data is formatted by the class Movie found in media.py
It creates an array and sends the information to website_generator.py
"""

import media
import website_generator


BigHero6 = media.Movie("Big Hero 6",
                       "The special bond that develops between plus-sized inflatable robot "
                       "Baymax, and prodigy Hiro Hamada, who team up with a group of friends "
                       "to form a band of high-tech heroes.",
                       "http://ia.media-imdb.com/images/M/MV5BMjI4MTIzODU2NV5BMl5BanBnXkFtZTgwMjE0"
                       "NDAwMjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ",
                       "Ryan Potter, Scott Adsit, Jamie Chung",
                       "7.9 on IMDb",
                       "2014")

Interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in "
                           "an attempt to ensure humanity's survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4OD"
                           "I3MjE@._V1__SX887_SY928_.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw",
                           "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
                           "8.7 on IMDb",
                           "2014")

Gravity = media.Movie("Gravity",
                      "A medical engineer and an astronaut work together to survive after a "
                      "catastrophe destroys their shuttle and leaves them adrift in orbit.",
                      "http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOT"
                      "k4MTk0OQ@@._V1__SX887_SY928_.jpg",
                      "https://www.youtube.com/watch?v=ufsrgE0BYf0",
                      "Sandra Bullock, George Clooney, Ed Harris",
                      "7.9 on IMDb",
                      "2013")

PacificRim = media.Movie("Pacific Rim",
                        "As a war between humankind and monstrous sea creatures wages on, a "
                        "former pilot and a trainee are paired up to drive a seemingly "
                        "obsolete special weapon in a desperate effort to save the "
                        "world from the apocalypse.",
                        "http://ia.media-imdb.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5B"
                        "anBnXkFtZTcwOTU1OTU0OQ@@._V1__SX887_SY928_.jpg",
                        "https://www.youtube.com/watch?v=5guMumPFBag",
                        "Idris Elba, Charlie Hunnam, Rinko Kikuchi",
                        "7.0 on IMDb",
                        "2013")

FindingNemo = media.Movie("Finding Nemo",
                          "After his son is captured in the Great Barrier Reef and taken to "
                          "Sydney, a timid clownfish sets out on a journey to bring him home.",
                          "http://ia.media-imdb.com/images/M/MV5BMTY1MTg1NDAxOV"
                          "5BMl5BanBnXkFtZTcwMjg1MDI5Nw@@._V1__SX887_SY928_.jpg",
                          "https://www.youtube.com/watch?v=AXoZdTe9YFs",
                          "Albert Brooks, Ellen DeGeneres, Alexander Gould",
                          "8.2 on IMDb",
                          "2003")

CloudAtlas = media.Movie("Cloud Atlas",
                         "An exploration of how the actions of individual lives impact one "
                         "another in the past, present and future, as one soul is shaped "
                         "from a killer into a hero, and an act of kindness ripples across "
                         "centuries to inspire a revolution.",
                         "http://ia.media-imdb.com/images/M/MV5BMTczMTgxMjc4NF5BMl5BanBnXkFt"
                         "ZTcwNjM5MTA2OA@@._V1__SX887_SY928_.jpg",
                         "https://www.youtube.com/watch?v=ByehYal_cCs",
                         "Tom Hanks, Halle Berry, Hugh Grant",
                         "7.5 on IMDb",
                         "2012")

InTime = media.Movie("In Time",
                     "In a future where people stop aging at 25, but are engineered to "
                     "live only one more year, having the means to buy your way out of "
                     "the situation is a shot at immortal youth. Here, Will Salas finds "
                     "himself accused of murder and on the run with a hostage "
                     "- a connection that becomes an important part of the way "
                     "against the system.",
                     "http://ia.media-imdb.com/images/M/MV5BMjA3NzI1ODc1MV5BMl5B"
                     "anBnXkFtZTcwMzI5NjQwNg@@._V1__SX887_SY928_.jpg",
                     "https://www.youtube.com/watch?v=fdadZ_KrZVw",
                     "Justin Timberlake, Amanda Seyfried, Cillian Murphy",
                     "6.7 on IMDb",
                     "2011")

Alien = media.Movie("Alien",
                    "The commercial vessel Nostromo receives a distress call from an "
                    "unexplored planet. After searching for survivors, the crew heads "
                    "home only to realize that a deadly bioform has joined them.",
                    "http://ia.media-imdb.com/images/M/MV5BMTU1ODQ4NjQyOV5BMl"
                    "5BanBnXkFtZTgwOTQ3NDU2MTE@._V1__SX887_SY928_.jpg",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8",
                    "Sigourney Weaver, Tom Skerritt, John Hurt",
                    "8.5 on IMDb",
                    "1979")

Serenity = media.Movie("Serenity",
                       "The crew of the ship Serenity tries to evade an assassin sent "
                       "to recapture one of their number who is telepathic.",
                       "http://ia.media-imdb.com/images/M/MV5BMTI0NTY1MzY4NV"
                       "5BMl5BanBnXkFtZTcwNTczODAzMQ@@._V1__SX887_SY928_.jpg",
                       "https://www.youtube.com/watch?v=6nEAlpTb4tk",
                       "Nathan Fillion, Gina Torres, Chiwetel Ejiofor",
                       "8.0 on IMDb",
                       "2005")

GoneGirl = media.Movie("Gone Girl",
                       "With his wife's disappearance having become the focus of an intense "
                       "media circus, a man sees the spotlight turned on him when it's "
                       "suspected that he may not be innocent.",
                       "http://ia.media-imdb.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5"
                       "BanBnXkFtZTgwNzU1NzE3MjE@._V1__SX887_SY928_.jpg",
                       "https://www.youtube.com/watch?v=esGn-xKFZdU",
                       "Ben Affleck, Rosamund Pike, Neil Patrick Harris",
                       "8.2 on IMDb",
                       "2014")


movies = [BigHero6, Interstellar, Gravity, PacificRim, FindingNemo,
          CloudAtlas, InTime, Alien, Serenity, GoneGirl]

#Pass the data to website_generator in the function open_movies_page
website_generator.open_movies_page(movies)
