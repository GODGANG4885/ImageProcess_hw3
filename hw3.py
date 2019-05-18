import cv2
import numpy as np
from math import sqrt, atan2, pi

def compute_blur(input_pixels, width, height, kernel):

    # Keep coordinate inside image
    clip = lambda x, l, u: l if x < l else u if x > u else x
    # Middle of the kernel
    offset = len(kernel) // 2

    # Compute the blurred image
    blurred = np.empty((width, height))
    for x in range(width):
        for y in range(height):
            acc = 0
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = clip(x + a - offset, 0, width - 1)
                    yn = clip(y + b - offset, 0, height - 1)
                    acc += input_pixels[xn, yn] * kernel[a, b]
            blurred[x, y] = int(abs(acc))
    return blurred


def compute_gradient(input_pixels, width, height):

    gradient = np.zeros((width, height))
    direction = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            if 0 < x < width - 1 and 0 < y < height - 1:
                mag_x = int(input_pixels[x + 1, y]) - int(input_pixels[x - 1, y])
                mag_y = int(input_pixels[x, y + 1]) - int(input_pixels[x, y - 1])
                gradient[x, y] = sqrt(mag_x**2 + mag_y**2)
                direction[x, y] = atan2(mag_y, mag_x)

    return gradient, direction


def filter_out_non_maximum(gradient, direction, width, height, THRESH=150):
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            angle = direction[x, y] if direction[x, y] >= 0 else direction[x, y] + pi
            rangle = round(angle / (pi / 4))
            mag = gradient[x, y]
            if ((rangle == 0 or rangle == 4) and (gradient[x - 1, y] > mag or gradient[x + 1, y] > mag)
                    or (rangle == 1 and (gradient[x - 1, y - 1] > mag or gradient[x + 1, y + 1] > mag))
                    or (rangle == 2 and (gradient[x, y - 1] > mag or gradient[x, y + 1] > mag))
                    or (rangle == 3 and (gradient[x + 1, y - 1] > mag or gradient[x - 1, y + 1] > mag))):
                gradient[x, y] = 0

            if gradient[x, y] <= THRESH:
                gradient[x, y] = 0
    return gradient


def gaussian_noisy(image, var):
    row, col = image.shape
    mean = 0
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    noisy = image + gauss
    return noisy


def save_image(image, name):
    cv2.imwrite('%s.bmp' % name, image)


def masked_edge(img, width, height, kernel_x, kernel_y):
    x = compute_blur(img, width, height, kernel_x)
    y = compute_blur(img, width, height, kernel_y)
    blur = x + y
    g, d = compute_gradient(blur, width, height)
    edge_img = filter_out_non_maximum(g, d, width, height)
    return edge_img


def error_rate(img, mask_x, mask_y, name):
    # 이미지 분산 구하기
    origin_var = np.var(img)
    SNR = 8
    # 노이즈 이미지의 분산 구하기
    noise_var = origin_var / 10 ** (SNR/10)
    # 노이즈 이미지 만들기
    noise_img = gaussian_noisy(img, noise_var)
    save_image(noise_img, 'noise_9')
    # edge image 만들기
    g, d = compute_gradient(noise_img, img.shape[0], img.shape[1])
    img_edge = filter_out_non_maximum(g, d, img.shape[0], img.shape[1])
    save_image(img_edge, 'noise_edge')
    masked_img = masked_edge(img, img.shape[0], img.shape[1], mask_x, mask_y)
    or_edge_count = 0
    # origin image edge count
    for i in range(img_edge.shape[0]):
        for j in range(img_edge.shape[1]):
            if img_edge[i][j] != 0:
                or_edge_count += 1
    # print(or_edge_count)
    # masked image edge count
    masked_edge_count = 0
    for i in range(masked_img.shape[0]):
        for j in range(masked_img.shape[1]):
            if(img_edge[i][j] == 0 and masked_img[i][j] != 0):
                masked_edge_count += 1
            elif(img_edge[i][j] != 0 and masked_img[i][j] == 0):
                masked_edge_count += 1
    # error rate 구하기
    print("{1} error rate : {0}".format(masked_edge_count / or_edge_count, name))
    save_image(masked_img, name)


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err