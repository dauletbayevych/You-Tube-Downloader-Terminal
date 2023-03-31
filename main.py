import pytube
pytube.YouTube(input("URL: ")).streams.get_highest_resolution().download('.')