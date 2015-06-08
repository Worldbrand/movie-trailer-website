-------------------------------------------
June 2015
Kat-Phuong Nguyen
Udacity - Full Stack Development Nanodegree
Project #1: Movie Trailer Website
-------------------------------------------

INSTRUCTIONS:
This project was written for Python 2.79. Python 2 will be necessary to run the code.
In order to generate the website, open entertainment_center.py and execute the code in python.
If solanum_theatre.html already exists, it will be overwritten. 
A copy has been included in case anything goes wrong.
The generated website should open in a new browser window.



REMARKS:
freshtomatoes.py used outdated versions, so I updated the URIs to a newer CDN.
Most of the rewriting was done on the front-end side as opposed to in python;
implementing the new data turned out to be much more involved than passing it
through python.

I added functionality to the modal - before, it only displayed a movie trailer.

The script that was included in freshtomatoes.py was meant to remove data from the movie trailer container, but its trigger was the user clicking on the modal background, the close button, or (confusingly) the modal itself.

I thought a better way of doing that would be to call the function when the modal became hidden, which I have done, but it requires this line of code:
$(window).load(function(){

the site is named after the genus of plants that the tomato is found in.



CREDITS:
The HTML segments were written using jQuery and Bootstrap 3. 
Background image is a modified pattern by Pete Fecteau, found on subtlepatterns.com
YouTube trailer URLs were provided by the respective youtube channels in the links.
Movie data and posters comes from IMDb.net.