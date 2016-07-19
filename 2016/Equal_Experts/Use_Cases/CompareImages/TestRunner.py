#from Equal_Experts.Use_Cases.CompareImages.SeleniumMasterCompareImage import ImageCompare
from SeleniumMasterCompareImage import ImageCompare
import urllib
import unittest



class TestRunner(unittest.TestCase):
    def test_hide_real_name_user_settings(self):
        img_url1 = "https://www.google.co.in/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
        img_url2 = "https://www.google.co.in/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
        fileN = open('1.jpg','wb')
        fileN .write(urllib.request.urlopen(img_url).read())
        fileN .close()
        fileN = open('2.jpg','wb')
        fileN .write(urllib.request.urlopen(img_url).read())
        fileN .close()
        imageCompare=ImageCompare()
        a=imageCompare.compare('1.jpg','2.jpg')
        print 'Images Equal?',a

##run the main test
if __name__ == "__main__":
     unittest.main()