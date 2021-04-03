
from pytube import YouTube
import os
import os.path
from pathlib import Path

link = str(input("URL do video vadia: "))
video = YouTube(link)
stream = video.streams.get_highest_resolution()
#Deixar o nome bunito
nm = stream.default_filename
newnm = nm
nop = '/\:*"<>|'
for i in range(0, len(nop)):
    newnm = newnm.replace(nop[i], "")
print(newnm)
newnm = newnm[:-4]
print(newnm)