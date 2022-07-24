import cv2
import os

image_folder = 'data'
video_name = 'AVG-TownCentre.avi'

height, width, layers = cv2.imread(os.path.abspath(image_folder + "/" + os.listdir(image_folder)[0])).shape

video = cv2.VideoWriter(video_name, 0, 7, (width, height))

for image in sorted(os.listdir(image_folder)):
    video.write(cv2.imread(os.path.abspath(image_folder) + '/' + str(image)))

cv2.destroyAllWindows()
video.release()