from pytube import YouTube

link = input("Enter URL of Video: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()
#stream = video.streams.filter(progressive=True, file_extension='mp4')
stream.download()
