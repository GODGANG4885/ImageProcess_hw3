# ImageProcess_hw3
imageProcess edge detection (roberts , sobel, prewitt,stochastic filter)

영상처리 HW #3

Due on 18 May

1. Edge detection operators can be compared in an objective way. The performance of an edge detection operator in noise can be measured quantitatively as follows: Let n0 be the number of edge pixels declared and n1 be number of missed or new edge pixels after adding noise. If n0 is held fixed for the noiseless as well as noisy images, then the edge detection error rate is
                        .
Compare the performance of the gradient operators of Roberts, Sobel, Prewitt and the 5x5 stochastic gradient on a noisy image with SNR= 8dB. 
Note that the pixel location (m,n) is declared an edge location if the magnitude gradient   exceeds a THRESH value of 150. The edge locations constitute an edge map. For this assignment, you can select 512x512 BMP or RAW grayscale image of Lena. 





2. Compare the performance between the 3x3 Low-pass and Median filters for a noisy image with SNR=9dB. For an objective comparison, obtain the MSE (mean square error) for each result. For this assignment, use 512x512 grayscale image of BOAT.raw.  









 (2) Method to compute an image power or variance

The signal variance can be represented as follows:
 
where  

Thus, the image power for MXN image can be obtained by using the following equation:

       .



(3) Edge Detection Masks

1) As for the Roberts, Sobel, and Prewitt mask, please use the masks as shown in Fig. 3.16 on page 109 of the text book.

2) As for the 5x5 stochastic gradient mask, please use the mask shown below.










