from pytube import YouTube

url = input("Enter Video Link : ")

video = YouTube(url)

video = video.streams.get_highest_resolution()

video.download()

print(video.title,"Downloaded")