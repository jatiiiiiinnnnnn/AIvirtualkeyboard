import cv2
import numpy as np

class Key:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def drawKey(self, img, text_color=(255, 255, 255), bg_color=(0, 0, 0), alpha=0.5, fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.8, thickness=2):
        # Draw the background rectangle with alpha blending
        bg_rec = img[self.y: self.y + self.h, self.x: self.x + self.w]
        overlay = np.ones(bg_rec.shape, dtype=np.uint8) * np.array(bg_color, dtype=np.uint8)
        blended = cv2.addWeighted(bg_rec, alpha, overlay, 1 - alpha, 0)

        # Put the blended image back in place
        img[self.y: self.y + self.h, self.x: self.x + self.w] = blended

        # Calculate text size and position
        text_size = cv2.getTextSize(self.text, fontFace, fontScale, thickness)
        text_pos = (int(self.x + self.w / 2 - text_size[0][0] / 2), int(self.y + self.h / 2 + text_size[0][1] / 2))

        # Put the text on the image
        cv2.putText(img, self.text, text_pos, fontFace, fontScale, text_color, thickness)

    def isOver(self, x, y):
        if (self.x <= x <= self.x + self.w) and (self.y <= y <= self.y + self.h):
            return True
        return False
