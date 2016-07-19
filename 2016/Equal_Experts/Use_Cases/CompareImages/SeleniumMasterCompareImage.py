import cv2
class ImageCompare():

    def __init__(self):

        print "compare images in python"

    def compare(self,image1,image2):
        match=False
        img1 = cv2.imread(image1)
        img2 = cv2.imread(image2)
        row1, cols1, channel1 = img1.shape
        row2, cols2, channel2 = img2.shape
        print 'image 1 rows:', row1
        print 'image 2 rows:', row2
        print 'image 1 cols:', cols1
        print 'image 2 cols:', cols2
        print 'image 1 channel:', channel1
        print 'image 2 channel2:', channel2
        if (row1 != row2) or (cols1 != cols2) or (channel1 != channel2):
            print "two images are different"
            match=False
            return match
        else:
            mismatch = 0
            for i in range(1, row1):
                for j in range(1, cols1):
                    px1 = img1[i, j]
                    px2 = img2[i, j]
            ##print i,j,px1.sum(),px2.sum()
                    if (px1.sum() != px2.sum()):
                        mismatch = mismatch + 1
            print 'total mismatch is:', mismatch
            if(mismatch==0):
                match=True
            else:
                match=False
            return match