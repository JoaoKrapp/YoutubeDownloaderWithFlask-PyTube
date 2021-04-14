from pytube import YouTube

link = input("Url aqui: ")
yt = YouTube(link)

printada = yt.streams.filter(progressive="True")

for i in printada:
    print(i.resolution)
'''
video = yt.streams.get_by_resolution("360p")

print(video)
'''