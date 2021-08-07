#youtube video downloader
from pytube import YouTube
link = input("Enter Video link: ")
yt = YouTube(link)
print("Video title : ",yt.title)
print("Video Duration : "+str(yt.length)+"s")
print("Video views : ",yt.views)
print("Video ratings : ",yt.rating)
userinput = input("Do you want to download.[y/n]")
if userinput == "y":
	video = yt.streams.filter(file_extension="mp4").get_highest_resolution()
	print("Downloading video...")
	video.download()
	print("Complete.")
else:
	exit()