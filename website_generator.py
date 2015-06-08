"""
This file generates a webpage in html based on 
data received from entertainment_center.py
The data comes in the form of several instances of 
the Movie class found in media.py
"""
import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Solanum Theatre</title>
    
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body{
            padding-top: 80px;
            background-image: url("images/BackgroundTile.png");
        }
        #header{
            align-content: center;
        }
        #trailer .modal-dialog{
            margin-top: 200px;
        }
        .modal-backdrop{
        opacity:0.75 !important;
        }
        .hanging-close{
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video{
            width: 100%;
            height: 100%;
        }
        .movie-tile{
            margin-bottom: 20px;
            padding-top: 30px;
            padding-bottom:10px;
            border-radius:10px;
        }
        .movie-tile:hover{
            background-color: #CCC;
            cursor: pointer;
        }
        .scale-media{
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe{
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie-info{
            background-color: #CCC;
            border-radius: 10px;
            margin: 20px;
            padding:20px;
        }
        .modal-content{
            border-radius:  10px;
            background-color: #202020;
        }
        #movie-list{
            padding: 20px;
        }
        #rating{
            font-size:20px;
            font-weight:bold;
        }
        #cast{
            font-weight:bold;
        }
        .movie_tile_title{
            color: #FF6347;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        

        //I've modified this function to not only play the trailer,
        //but also to display information about the movie that is clicked on,
        //within the same modal dialog
        $(document).on('click', '.movie-tile', function(event){
            var title = $(this).attr('data-title');
            var year = $(this).attr('data-year');
            var plot = $(this).attr('data-plot');
            var rating = $(this).attr('data-rating');
            var cast = $(this).attr('data-cast');
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>",{
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            
            //Emptying .movie-info before we append means 
            //having a blank slate every time we write to it
            $(".movie-info").empty().append('<h2 class="text-center">' + title + ' (' + year + ') <h2>');
            $(".movie-info").append('<p id="rating">' + rating + '</p>');
            $(".movie-info").append('<p id="cast"> Starring: ' + cast + '</p>');
            $(".movie-info").append('<p>' + plot + '</p>');
        });
        
        
        // Animate in the movies when the page loads
        $(document).ready(function(){
          $('.movie-tile').hide().first().show("fast", function showNext(){
            $(this).next("div").show("fast", showNext);
          });
        });
        
        
        //When the modal is hidden, stop the youtube player.
        //This needed to be wrapped as a loaded function, for whatever reason.
        $(window).load(function(){
            $("#trailer").on("hidden.bs.modal", function(){
                // Remove the src so the player itself gets removed, as this is the only
                // reliable way to ensure the video stops playing in IE
                $("#trailer-video-container").empty();
            });
        });

        
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
    <body>
        
        
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                    </a>
                    
                    <!-- Empty class to be filled with data in javascript when the modal is activated -->
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                    
                    <!-- Empty class to be filled with data in javascript when the modal is activated -->
                    <div class="movie-info">
                    </div>
                </div>
            </div>
        </div>
        
        
        <!-- Main Page Content -->
        <div class="center-block">
            <img src="images/SolanumTheatreLarge.png" class="img-responsive center-block" alt="Solanum Theatre">
        </div>
        <div class="container-fluid" id="movieList">
            {movie_tiles}
        </div>
        
        
    </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-3 movie-tile text-center"
data-toggle="modal" 
data-target="#trailer"

data-title="{movie_title}"
data-year="{movie_year}"
data-plot="{movie_plot}"
data-cast="{movie_cast}"
data-rating="{movie_rating}"
data-trailer-youtube-id="{trailer_youtube_id}">
    <img src="{poster_image_url}" width="220" height="342">
    <h2 class="movie_tile_title">{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_plot=movie.plot,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_cast = movie.cast,
            movie_rating = movie.rating,
            movie_year = movie.year
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('solanum_theatre.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible