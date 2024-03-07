from moviepy.editor import VideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

clip = VideoFileClip("my_video.mp4")
clip = clip.subclip(0, 3)
clip.write_gif("my_gif.gif", fps=25)
gif = VideoClip("my_gif.gif")
gif.ipython_display()