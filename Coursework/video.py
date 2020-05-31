import cv2
import glob


def generate_video(path, file_ext):
    img_array = []
    size = (0, 0)
    n = len(glob.glob(path + "*" + file_ext))

    for i in range(0, n):
        img = cv2.imread(path + str(i) + file_ext)
        height, width, layers = img.shape
        size = max(size, (width, height))
        img_array.append(img)

    out = cv2.VideoWriter("video.avi", 0, 50, size)

    for img in img_array:
        out.write(img)
    out.release()