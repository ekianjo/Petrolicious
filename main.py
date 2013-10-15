import urllib
import youtube-dl


    
def get_logo():
  try:
    logo=urllib('http://static.petrolicious.com/petrolicious/images/about_horizontallogo.png')
    #save logo locally
  
  except:
    print 'could not get logo'



    
#Start with simple application

#get logo online. Do not distribute it.
#title page with logo or simply text of petrolicious with cool font

#use pygame or mplayer to play music in menu - need to choose music.

#0. Please wait message : caching all info retrieved online. Can take a while - play music in parallel

#1. Logo
#2. fade in tagline below Logo

#get list and links of latest youtube videos in channel
#get pictures/thumbnails from each video


#3. fade out and fade on interface - it displays the liat of latest videos, along with small screenshot. 'Play' button appears on the right of videos already downloaded
#4. use D-pad to move up or down in the list.
#5. click on button -> fade out
#6. Fade in video page -> description and download button.
#7. Click on download -> launches download. 
#8. Bar fills up
#9. When downloaded, two options: erase or play back
#10. Playback stops menu music. 
#11. then starts video in full screen
#display list of latest videos. 

#https://github.com/np1/pafy to use

#controls are simple and intuitive - keyboard based
#use ytdl for downloading videos - display download status or bar
#use mplayer for video playback - once video downloaded. 
#detects the best video format/size for the system - for pandora it would be 480 webm. for desktop probably Full HD
#sync with online server for pictures - and videos list. 
#transition effects between scenes (fade in fade out, with slight movement).

#confirm performance of pygame libraries for this. Should be good enough, but need to check.
