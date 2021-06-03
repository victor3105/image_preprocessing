import cv2 as cv
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename


#  TO-DO: add 'save image' feature for applying different algorithms sequentially
# global res
# res = None
# def saveResult():
#     global res
#     if res:
#         img = res

#  check image presence before algorithm visualization
global imgTk
imgTk = None
def noImage():
    if not imgTk:
        message = 'Please open an image first'
        popup = Tk()
        popup.wm_title('Error')
        label = Label(popup, text=message)
        label.pack(side='top', fill='x', pady=10)
        popupButton = Button(popup, text='OK', command=popup.destroy)
        popupButton.pack()
        popup.mainloop()
        return False


#  describe functions to be visualized
#  binarization
def thresholding():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Binarization')

        cv.createTrackbar('Lower val', 'Binarization', 0, 255, nothing)
        cv.createTrackbar('Upper val', 'Binarization', 0, 255, nothing)

        global res

        while True:
            thr1 = cv.getTrackbarPos('Lower val', 'Binarization')
            thr2 = cv.getTrackbarPos('Upper val', 'Binarization')

            # res, thr = cv.threshold(img, thr1, thr2, cv.THRESH_BINARY)
            thr, res = cv.threshold(img, thr1, thr2, cv.THRESH_BINARY)

            cv.imshow('Binarization', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


#  smoothing
def averaging():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Averaging')

        cv.createTrackbar('Kernel', 'Averaging', 1, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Averaging')

            if window < 1:
                window = 1

            res = cv.blur(img, (window, window))

            cv.imshow('Averaging', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


#  Gaussian blurring
def gaussian():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Gaussian blurring')

        cv.createTrackbar('Kernel', 'Gaussian blurring', 3, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Gaussian blurring')

            if window < 1:
                window = 1

            if window % 2 > 0:
                res = cv.GaussianBlur(img, (window, window), 0)

            cv.imshow('Gaussian blurring', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


#  median blurring
def median():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Median blurring')

        cv.createTrackbar('Kernel', 'Median blurring', 3, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Median blurring')

            if window < 1:
                window = 1

            if window % 2 > 0:
                res = cv.medianBlur(img, window)
            cv.imshow('Median blurring', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


def erosion():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Erosion')

        cv.createTrackbar('Kernel', 'Erosion', 1, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Erosion')

            kernel = np.ones((window, window), np.uint8)
            res = cv.erode(img, kernel, iterations=1)

            cv.imshow('Erosion', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


def dilation():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Dilation')

        cv.createTrackbar('Kernel', 'Dilation', 1, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Dilation')

            kernel = np.ones((window, window), np.uint8)
            res = cv.dilate(img, kernel, iterations=1)

            cv.imshow('Dilation', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


def opening():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Opening')

        cv.createTrackbar('Kernel', 'Opening', 1, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Opening')

            kernel = np.ones((window, window), np.uint8)
            res = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

            cv.imshow('Opening', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


def closing():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Closing')

        cv.createTrackbar('Kernel', 'Closing', 1, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Closing')

            kernel = np.ones((window, window), np.uint8)
            res = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

            cv.imshow('Closing', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


def sobel():
    def nothing(x):
        pass

    if not noImage():
        cv.namedWindow('Sobel edge detection')

        cv.createTrackbar('Kernel', 'image', 1, 25, nothing)

        global res

        while True:
            window = cv.getTrackbarPos('Kernel', 'Sobel edge detection')

            if window % 2 > 0:
                sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=window)
                sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=window)

            res = sobelx + sobely

            cv.imshow('Sobel edge detection', res)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

        cv.destroyAllWindows()


algorithms = {'Binarization': thresholding, 'Averaging': averaging, 'Gaussian Blurring': gaussian,
              'Median Blurring': median, 'Erosion': erosion, 'Dilation': dilation,
              'Opening': opening, 'Closing': closing, 'Sobel Edge Detection': sobel}

buttons = []

root = Tk()
root.title('Image Pre-processing')

f1 = Frame(root)
f1.pack(anchor=NW, side=LEFT)
f2 = Frame(root)
f2.pack(anchor=E, side=RIGHT, fill=Y)

l = Label(f2, image=None)
l.pack(anchor=S, side=BOTTOM)


def open_file():
    path = askopenfilename()
    if path:
        global img
        img = cv.imread(path, 0)
        global imgTk
        im = Image.fromarray(img)
        imgTk = ImageTk.PhotoImage(im)
        l.configure(image=imgTk)


open_file_b = Button(f2, text='Open image', command=open_file)
open_file_b.pack(anchor=NW)

for key, val in algorithms.items():
    buttons.append(Button(f1, text=key, bg='white', command=val))
    buttons[-1].pack(anchor=NW, fill=X)

root.mainloop()
