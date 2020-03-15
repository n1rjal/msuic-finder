import webbrowser,os
import random
from tkinter.filedialog import askdirectory

def music():
     try:
          path=open('path.dat','r')
          path=path.read()
          if (path==""):
              raise Exception
     except:
          pathf=open('path.dat','w')
          path=askdirectory(title="Music folder?")
          pathf.write(path)
          pathf.close()
     b=os.listdir(path)

     i=0
     while i==0:
          music_to_play=b[random.randrange(-1,(len(b)+1))]
          ext= os.path.splitext(music_to_play)[1]
          print (ext)
          if (ext==".mp3" or ext==".MP3" or ext==".MP4" or ext==".mp4" or ext==".MKV" or ext==".mkv"):
               print (music_to_play)
               a=os.path.join(path,music_to_play)
               print (a)
               webbrowser.open(a,'new')
               break

music()