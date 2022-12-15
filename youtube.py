from pytube import YouTube

link = input('YouTube Link : ')
youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
vid= list(enumerate(videos))

for i in vid:
    print(i)

print()
strm = int(input("Enter videos stream number:"))

path = r"D:\Uvesh Details\dj songs"
videos[strm].download(path)

print('Download Successfully')