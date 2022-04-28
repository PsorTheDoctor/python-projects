import cv2
from db import TEMPLATES, TITLES


class Matcher:

    def __init__(self, camera):
        self.camera = camera
        self.detector = cv2.ORB_create()
        self.matcher = cv2.BFMatcher()
        self.threshold = 0.75

    def capture(self):
        snap = self.camera.export_to_png('snap.jpg')
        return snap

    def compute(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        _, des = self.detector.detectAndCompute(img, None)
        return des

    def match(self):
        snap = self.capture()
        snap_des = self.compute(snap)

        best_score = 0
        best_img = 'Cannot recognize'

        for t in range(len(TEMPLATES)):
            template_des = self.compute(TEMPLATES[t])
            matches = self.matcher.knnMatch(snap_des, template_des, k=2)

            good = []
            for m, n in matches:
                if m.distance < self.threshold * n.distance:
                    good.append([m])

            score = len(good)
            if score > best_score:
                best_score = score
                best_img = TITLES[t]

        return best_score, best_img
