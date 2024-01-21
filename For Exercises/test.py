import os
import random
from pytube import YouTube

url = input()
video = YouTube(url = url).streams.first().download()
