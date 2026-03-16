# utils.py
import cv2 as cv

drawing = False
is_zoomed = False
ix, iy = -1, -1
fx, fy = -1, -1
zoom_rect = None

def mouse_handler(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, is_zoomed, zoom_rect

    if event == cv.EVENT_LBUTTONDOWN and not is_zoomed:
        drawing = True
        ix, iy = x, y
        fx, fy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            fx, fy = x, y
    elif event == cv.EVENT_LBUTTONUP and not is_zoomed:
        drawing = False
        fx, fy = x, y

        x1, y1 = min(ix, fx), min(iy, fy)
        x2, y2 = max(ix, fx), max(iy, fy)

        if x2 - x1 > 10 and y2 - y1 > 10:
            zoom_rect = (x1, y1, x2, y2)
            is_zoomed = True

    elif event == cv.EVENT_RBUTTONDOWN:
        is_zoomed = False
        zoom_rect = None