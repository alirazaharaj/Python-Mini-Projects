'''from pytube import YouTube

link=input("Enter link: ")
YouTube_1=YouTube(link)
print(YouTube_1.title)

streaming=YouTube_1.streams.filter(only_video=True) # It will gave all avalibal formates in video which we can download 
stream=list(enumerate(streaming))
for i in stream:
    print(stream)
given_stream=int(input('Enter Formate: '))
streaming[given_stream].download()
print('Download Sucessfully.......')
'''

# For playlest 

'''from pytube import Playlist

link=input("Enter link: ")
py=Playlist(link)
print(f'Downloading {py.title}')

for video in py.videos:
    video.streams.first().download()'''
