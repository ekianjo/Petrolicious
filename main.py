import urllib #to download some specific elements
import youtube-dl #for downloading youtube videos
import subprocess #for mplayer

requestapi="https://gdata.youtube.com/feeds/api/users/petroliciousCo/uploads/?alt=json"

#make a generic JSON loading function for X parameters. 


json_data=open('json_data')
#command to get json data from request api
jstr = json.loads(json_data)
print data["feed"]["entry"]["link"][0]

if jstr.get('attributetolookfor'):
    pass

#find free music to use for this application
    
def get_logo():
  try:
    if logoispresent:
        return True
    else:
        logo=urllib('http://static.petrolicious.com/petrolicious/images/about_horizontallogo.png')
        #save logo locally
        return True
  
  except:
    print 'could not get logo'
    return False



#how to control mplyaer
import subprocess
player = subprocess.Popen(["mplayer", "song.mp3", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#to stop mplayer
player.stdin.write("q")


#to play without border decorations
mplayer -noborder my_video.ogg

    
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
