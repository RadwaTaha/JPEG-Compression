import  cv2
import matplotlib.pyplot as plt
import numpy

from PIL import Image

#1.1 Colorspace Conversion
#1. Convert the given image from RGB to YCbCr colorspace.
img = plt.imread('mandrill_30189.jpg')
img = img[..., ::-1]
ConvImg = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imwrite('Convertedimage.png', ConvImg)

#2. Display the three components of the image in three separate figures (include it in the report)
img2=Image.open('Convertedimage.png')
ConvImgY= img2.getchannel(2)
ConvImgY.save('ConvertedimageY.png')
ConvImgCb= img2.getchannel(1)
ConvImgCb.save('ConvertedimageCb.png')
ConvImgCr= img2.getchannel(0)
ConvImgCr.save('ConvertedimageCr.png')

#1.2 Chroma Subsampling
#1. Apply a 4:2:2 subsampling to the YCbCr components above.
img3=cv2.imread('ConvertedimageCb.png')
img4=cv2.imread('ConvertedimageCr.png')
resCB = cv2.resize(img3, None, fx=0.5, fy=1, interpolation = cv2.INTER_CUBIC)
plt.imshow(resCB,cmap = 'gray')
CbHeight , CbWidth , channels  = resCB.shape
print(CbHeight,CbWidth)
#plt.show()
resCr = cv2.resize(img4, None, fx=0.5, fy=1, interpolation = cv2.INTER_CUBIC)
plt.imshow(resCr,cmap = 'gray')
CrHeight , CrWidth , channels  = resCr.shape
print(CrHeight,CrWidth)                                                         
#plt.show()
























