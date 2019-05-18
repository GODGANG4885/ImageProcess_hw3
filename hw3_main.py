from hw3 import *

# 5x5 stochastic mask
stochastic_x = np.array([
    [0.267, 0.364, 0, -0.364, -0.267],
    [0.373, 0.562, 0, -0.562, -0.373],
    [0.463, 1.000, 0, -1.000, -0.463],
    [0.373, 0.562, 0, -0.562, -0.373],
    [0.267, 0.364, 0, -0.364, -0.267]
])
stochastic_y = stochastic_x.T
# roberts mask
roberts_x = np.array([[1, 0, -1],
                      [0, 1, 0],
                      [0, 0, 0]])

roberts_y = np.array([[-1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]])
# prewitt mask
prewitt_x = np.array([[1, 0, -1],
                     [1, 0, -1],
                     [1, 0, -1]])

prewitt_y = np.array([[-1, -1, -1],
                     [0, 0, 0],
                     [1, 1, 1]])
# sobel mask
sobel_x = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

sobel_y = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])

img = cv2.imread('noise_9.bmp', 0)
width = img.shape[0]
height = img.shape[1]

# error_rate(img, roberts_x, roberts_y,'roberts')
# error_rate(img, sobel_x, sobel_y, 'sobel')
# error_rate(img, prewitt_x, prewitt_y, 'prewitt')
# error_rate(img, stochastic_x, stochastic_y, 'stochastic')

#  median filter
# median = cv2.medianBlur(img, 3)
#  low pass filter
# kernel = np.ones((3,3),np.float32)/9
# dst = cv2.filter2D(img, -1, kernel)

# median edge
# g, d = compute_gradient(median, img.shape[0], img.shape[1])
# img_edge = filter_out_non_maximum(g, d, img.shape[0], img.shape[1])
# save_image(img_edge,'median_edge')

# low pass edge
# g, d = compute_gradient(dst, img.shape[0], img.shape[1])
# img_edge = filter_out_non_maximum(g, d, img.shape[0], img.shape[1])
# save_image(img_edge,'low_pass_edge')

# print MSE
# print("MSE of Low-pass filter and Median filter : {0}".format(mse(median,dst)))