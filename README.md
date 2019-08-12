# Basic Imageprocessing-algorithms

# Log Transformation
Log transformation means replacing each pixel value with its logarithm
the General form of log transformation is   S= T(r)=c*log(1+r) where s&r-output & input pixels respectively, c-scsling constant represented by following expression for 8-bit
where, c=255/log(1+ max_input_pixel_value)
       value of 'c' is chosen such that we get a maximum output value corosponding to bit size used
# applications of log transformation 
1. Expands the dark pixels in the image while corosponding the brighter pixels
2. Compresses the dynanmic range

# principle of log transformation
Dynamic range refers to the ratio of max & min intensity values. When the dynamic range of image is greater than that of displaying device (like in fourier transform),the lower values are supressed to overcome this issue, we use log transform.
log transformation first compresses the dynamic range and then upscales the image to a dynamic range of display devices. In other words, lower values are enhanced and thus the image show more details
