#!/usr/bin/env python
# coding=utf-8
import os
from pathlib import Path
import numpy as np
import cv2 as cv

MIN_NUM_KEYOINT_MATCHES = 50


def main():
    """loop through 2 folders with paired images, register and blink images"""
    night1_files = sorted(os.listdir('night_1'))
    night2_files = sorted(os.listdir('night_2'))
    path1 = Path.cwd() / 'night_1'
    path2 = Path.cwd() / 'night_2'
    path3 = Path.cwd() / 'night_1_registered'

    for i, _ in enumerate(night1_files):
        img1 = cv.imread(str(path1 / night1_files[i]), cv.IMREAD_GRAYSCALE)
        img2 = cv.imread(str(path2 / night2_files[i]), cv.IMREAD_GRAYSCALE)

        print("Comparing {} to {}.\n".format(night1_files[i], night2_files[i]))

        # find keypoints and best matches between them
        kp1, kp2, best_matches = find_best_matches(img1, img2)
        img_match = cv.drawMatches(img1, kp1, img2, kp2,
                                   best_matches, outImg=None)

        # draw a line between the two images
        height, width = img1.shape
        cv.line(img_match, (width, 0), (width, height), (255, 255, 255), 1)
        QC_best_matches(img_match)

        # register left-hand image using keypoints
        img1_registered = register_image(img1, img2, kp1, kp2, best_matches)

        # QC registration and save registered image (optional steps)
        blink(img1, img1_registered, 'Check Registeration', num_loop=5)
        out_filename = '{}_registered.png'.format(night1_files[i][:-4])
        cv.imwrite(str(path3 / out_filename), img1_registered)

        cv.destroyAllWindows()

        # run the blink comparator
        blink(img1_registered, img2, 'Blink Comparator', num_loop=15)


def find_best_matches(img1, img2):
    """return list of keypoints and list of best matches for two images"""
    orb = cv.ORB_create(nfeatures=100)

    # find the keypoints and descriptors with ORB
    kp1, desc1 = orb.detectAndCompute(img1, mask=None)
    kp2, desc2 = orb.detectAndCompute(img2, mask=None)

    # find keypoints matches using Brute Force Matcher
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)

    # sort matches in ascending order of distance and keep best n matches
    matches = sorted(matches, key=lambda x: x.distance)
    best_matches = matches[:MIN_NUM_KEYOINT_MATCHES]

    return kp1, kp2, best_matches


def QC_best_matches(img_match):
    """draw best keypoint matches connected by colored lines."""
    cv.imshow('Best {} Matches'.format(MIN_NUM_KEYOINT_MATCHES), img_match)
    cv.waitKey(2500)


def register_image(img1, img2, kp1, kp2, best_matches):
    """return first image registered to second image"""
    if len(best_matches) >= MIN_NUM_KEYOINT_MATCHES:
        src_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
        dst_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
        for i, match in enumerate(best_matches):
            src_pts[i, :] = kp1[match.queryIdx].pt
            dst_pts[i, :] = kp2[match.trainIdx].pt

        h_array, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC)
        height, width = img2.shape
        img1_warped = cv.warpPerspective(img1, h_array, (width, height))

        return img1_warped
    else:
        print("WARNING: Number of keypoint matches < {}\n".format
              (MIN_NUM_KEYOINT_MATCHES))
        return img1


def blink(image_1, image_2, window_name, num_loop):
    """replicate blink comparator with two images"""
    for _ in range(num_loop):
        cv.imshow(window_name, image_1)
        cv.waitKey(330)
        cv.imshow(window_name, image_2)
        cv.waitKey(330)


if __name__ == '__main__':
    main()
