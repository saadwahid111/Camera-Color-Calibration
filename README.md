# Camera Color Calibration
## Introduction
The spectral responses of a camera are the products of the transmittances of color filters and the spectral response of image sensor, such as CCD or CMOS. The raw signal vector is designated as S = (R, G, B), in which R, G, and B are signal components of red, green, and blue channels, respectively. If the spectral responses of a camera exactly fit the CIE color matching functions (CMFs), the camera signal vector S is linearly proportional to the tristimulus vector T = (X, Y, Z) of image color. However, such an ideal camera cannot be easily realized.

Color calibration is to find a mapping from camera signal vector to tristimulus vector. Such a mapping can be called the camera color device model or camera model for simplicity. To obtain an accurate mapping, it requires a set of color patches under an illuminant. Their tristimulus vectors are measured by a spectroradiometer. For an example, X-Rite ColorChecker Passport is a target chart comprising 24 color patches so that the calibrated camera captures the image of the chart and signal vectors corresponding to the color patches can be extracted from the captured image. Usually the irradiance on the chart is not uniform. The non-uniformity of irradiance can be compensated by taking the image of a gray card under the same illumination condition.

## Background
A device model can be written as

                                q=Mp                    (1)

Where, q and p are column matrixes comprising desired output values and camera responses, respectively. For LRM and PRM the matrix q = (X,Y,Z ) ^T. The terms in the matrix p depends on regression model, e.g.,
for Linear Regression Model;

                               p = (R,G,B)^T            (2)                 

for the third-order Polynomial Regression Model; 

                               p = (R,G,B,R^2  ,G^2  ,B^2  ,RG,GB,BR,R^3  ,G^3  ,B^3,RG^2  ,RB^2  ,GB^2  ,GR^2  ,BR^2  ,BG^2  ,RGB )^T                   (3)

The number of terms in p is denoted as L. In equation (3), L= 19 for the third order PRM.

M is a matrix relating q and p, which can be found by regression in least-square-fitting. Given a set of N known XYZs for a reflectance target chart and the corresponding camera responses, we may construct a (3 x N) matrix Q from N column matrixes q and an (L x N) matrix P from N column matrixes p. Using the Moore-Penrose inverse, we have

                               M = QP^T(P^T P)^{-1}



## Methodology
### Extraction of Color Patches from Xrite Color Chart

24 color patches of Xrite color checker passport are utilized as testing color samples. The color patches are extracted ny using Canny Edge Detection and are our smaples are more refined by extracting our region of interest(ROI) at the centre of each color patch.

Developed by John F. Canny in 1986, the Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in an images.

The Canny filter is a multi-stage edge detector. It uses a filter based on the derivative of a Gaussian in order to compute the intensity of the gradients.The Gaussian reduces the effect of noise present in the image. Then, potential edges are thinned down to 1-pixel curves by removing non-maximum pixels of the gradient magnitude. Finally, edge pixels are kept or removed using hysteresis thresholding on the gradient magnitude.

Since not all the rectangles contain our region of interest (ROI), the unwanted boxes are removed by an algorithm which classifies the boxes based on their sizes and our ROI are filtered out by assuming their approximate size.

The patches extracted and appended to matrix 'P' of size (9602,3).


The matrix 'C' of size (19,9602) is calculated using calculating

                      p = (R, G, B, R^2, G^2, B^2, RG, GB, BR, R^3, G^3, B^3, RG^2, RB^2, GB^2, GR^2, BR^2, BG^2, RGB)^T                              

The number of terms in p is denoted as L. In equation (3), L= 19 for the third order PRM.

and appending it into matrix 'C'
