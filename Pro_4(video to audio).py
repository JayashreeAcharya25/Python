import moviepy.editor
# import csv
#
# data = open(r"C:\Users\Admin\Videos\MyVideo.mp4")
# data = csv.reader(data)

video = moviepy.editor.VideoFileClip("MyVideo.mp4")

audio = video.audio

audio.write_audiofile("result.mp3")