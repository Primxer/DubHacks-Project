#!/usr/bin/env python3
import cv2


def testermain():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()

    if ret:
        cv2.imshow('SnapshotTest', image)
        cv2.waitKey(0)


if __name__ == '__main__':
    testermain()
