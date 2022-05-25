#!/usr/bin/env python
# coding=utf-8
import math
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

IMG_HT = 400
IMG_WIDTH = 500
BLACK_IMG = np.zeros((IMG_HT, IMG_WIDTH), dtype='uint8')
STAR_RADIUS = 165
EXO_RADIUS = 7
EXO_DX = 3
EXO_START_X = 40
EXO_START_Y = 230
NUM_FRAMES = 145


def main():
    intensity_simples = record_transit(EXO_START_X, EXO_START_Y)
    relative_brightness = calc_rel_brightness(intensity_simples)
    print('\nestimated exoplanet radius = {:.2f}\n'
          .format(STAR_RADIUS * math.sqrt(max(relative_brightness)
                                          - min(relative_brightness))))
    plot_light_curve(relative_brightness)


def record_transit(exo_x, exo_y):
    """draw planet transiting star and return list of intensity changes"""
    intensity_simples = []
    for _ in range(NUM_FRAMES):
        temp_img = BLACK_IMG.copy()
        # draw star
        cv.circle(temp_img, (int(IMG_WIDTH / 2), int(IMG_HT / 2)),
                  STAR_RADIUS, 255, -1)
        # draw exoplanets
        cv.circle(temp_img, (exo_x, exo_y), EXO_RADIUS, 0, -1)
        intensity = temp_img.mean()
        cv.putText(temp_img, 'Mean Intensity = {}'.format(intensity), (5, 390),
                   cv.FONT_HERSHEY_PLAIN, 1, 255)
        cv.imshow('Transit', temp_img)
        cv.waitKey(30)
        intensity_simples.append(intensity)
        exo_x += EXO_DX
    return intensity_simples


def calc_rel_brightness(intensity_simples):
    """return list of relative brightness from list of intensity values"""
    rel_brightness = []
    max_brightness = max(intensity_simples)
    for intensity in intensity_simples:
        rel_brightness.append(intensity / max_brightness)
    return rel_brightness


def plot_light_curve(rel_brightness):
    """plot changes in relative brightness vs. time"""
    plt.plot(rel_brightness, color='red', linestyle='dashed',
             linewidth=2, label='Relative Brightness')
    plt.legend(loc='upper center')
    plt.title('Relative Brightness vs. Time')
    plt.show()


if __name__ == '__main__':
    main()
