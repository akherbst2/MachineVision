#############################<MY COMPLETE SOLUTION TO THE EDGE DETECTION PROBLEM>#############################
#==<BEGIN ImageFrame CLASS>==========================================================MachineVision==
class ImageFrame:
    def __init__(self, image):
        self.img = PhotoImage(width = WIDTH, height = HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num = (int)(image[row*WIDTH + col])
                if COLORFLAG == True:
                   kolor ='#%02x%02x%02x' % (num[0], num[1], num[2]) # = color
                else:
                   kolor ='#%02x%02x%02x' % (num, num, num)          # = gray-scale
                self.img.put(kolor, (col,row))
        c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
        c.create_image(0,0, image = self.img, anchor = NW)
        printElapsedTime ('displayed image')
#==<END OF ImageFrame CLASS>=========================================================MachineVision==

def confirmP3fileType(file1):
    stng = file1.readline().strip()  # read first line, print it, and then ignore it.
    print('--First line of file reads:', stng)
    if stng[0]+stng[1] != 'P3':
        print('+===================================================+')
        print('| ERROR: This file is NOT of type P3.               |')
        print('|        The first line of the file is shown below. |')
        print('+===================================================+')
        print ('-->', stng)
        file1.close()
        exit()
#------------------------------------------------------------------------------------MachineVision--

def printElapsedTime (msg = 'time'):
    length = 30
    msg = msg [:length]
    tab = '.'*(length-len(msg)) # <-- msg length truncated at 30 chars
    print('--' + msg.upper() + tab + ' ', end = '')
    time = round(clock() - START, 1) # START is global constant.
    print( '%2d'%int(time/60), ' min :', '%4.1f'%round(time%60, 1), \
           ' sec', sep = '')
#------------------------------------------------------------------------------------MachineVision--

def readFileNumbersIntoString(file1):
    nums = file1.read().split() # = a list of strings (e.g., '87') each separated by a space.
    file1.close()
    if len(nums)%3 != 0:
        print('---WARNING: Size of file(', len(nums) ,') % 3 != 0')
        exit()
    return nums
#------------------------------------------------------------------------------------MachineVision--

def convertStringRGBsToGrayIntegersOrColorTuples(nums):
    image = []
    if COLORFLAG == True:
       for pos in range(0, len(nums), 3):
           RGB = ( int(nums[pos+0]), int(nums[pos+1]),int(nums[pos+2]) )
           image.append(RGB) # a tuple of three integers
    else:
       for pos in range(0, len(nums), 3):
           RGB = ( int(nums[pos+0]), int(nums[pos+1]),int(nums[pos+2]) )
           image.append( int (0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]) ) # a single gray integer
    return image
#------------------------------------------------------------------------------------MachineVision--

#===========================ASSIGNMENT 2==========================================================
def testImageInts(image):
    stng = ''
    for n in range(WIDTH + 5, WIDTH + 20, 1):
        stng = stng + '  ' + str(image[n]) 
    print('--MY IMAGE = ', stng)


def smooth(image):
    print('--SMOOTHING IMAGE................')
    #pixel(row, col) --> image[row*WIDTH + col]
    #image[index]    --> pixel(index//WIDTH, index%WIDTH)
    image2 = image.copy()
    multiplier = [1, 2, 1, 2, 4, 2, 1, 2, 1]

    for row in range(1, HEIGHT - 1, 1):#given index, iterate from 1 to WIDTH - 1
        for col in range(1, WIDTH - 1, 1): #given index, iterate from 1 to HEIGHT - 1 to exclude edges, through every image pixel
        #-- for every surrounding pixel
            myAdjacentPixels = []
            for y in range(-1, 2, 1):#--collects myAdjacentPixels
                for x in range(-1, 2, 1):
                    myAdjacentPixels.append(image[(row + y)*WIDTH + (col + x)])

            myAdjacentPixels = [myAdjacentPixels[x] * multiplier[x] for x in range(9)]
            newValue = sum(myAdjacentPixels) * 0.0625
            image2[row*WIDTH + col] = newValue
    return image2

################STOPPED HERE 3/17/15, 10:02 AM#####################
#Next, use myAdjacentPixels to multiply by 1/16, and set that new number to an index in image2.
#print that image to see if it works.
#For more info, check page 4 in machinevision packet
    
            #print(myAdjacentPixels)
            
            
            
    
    testImageInts(image2)    

#====================================================================================MachineVision==
def printTitleAndSizeOfImageInPixels(image):
    print('         ==<RUN TIME INFORMATION>==')
    if len(image) != WIDTH * HEIGHT:
        print('--ERROR: Stated file size not equal to number of pixels')
        print ('file length:', len(image))
        print ('width:', WIDTH, 'height:', HEIGHT)
        exit()
    print('--NUMBER OF PIXELS.............. ', len(image))
    printElapsedTime ('image extracted from file')
#------------------------------------------------------------------------------------MachineVision--

def readPixelColorsFromImageFile(IMAGE_FILE_NAME):
    imageFile     = open(IMAGE_FILE_NAME, 'r')
    confirmP3fileType(imageFile)
    nums  = readFileNumbersIntoString(imageFile)
    image = convertStringRGBsToGrayIntegersOrColorTuples(nums)
    printTitleAndSizeOfImageInPixels(image)
    return image
#------------------------------------------------------------------------------------MachineVision--

def displayImageInWindow(image):
    global x # This line is necessary.
    x = ImageFrame(image)
#------------------------------------------------------------------------------------MachineVision-

def saveImageNumbersToFile(image,  FILE_NAME):
    file1 = open (FILE_NAME, 'w')
    for elt in image:
        file1.write (str(elt) + ' ' )
    printElapsedTime ('saved file numbers')
    file1.close()
#------------------------------------------------------------------------------------MachineVision--

def extractTheImageGrayScaleNumbersFromFile(GRAY_SCALE_NUMBERS_FILE_NAME = 'g:\\grayScale.ppm'):
    file1    = open(GRAY_SCALE_NUMBERS_FILE_NAME, 'r')
    nums = file1.read().split()
    file1.close()
    image = []
    for elt in nums:
        image.append( int(elt) )
    printElapsedTime ('Extracted gray-scale nums from file')
    return image
#------------------------------------------------------------------------------------MachineVision--
#===================================================================================================
#===================================================================================================
#--<IMPORTS>-------------------------------------------------------------------------MachineVision--

from tkinter import *
from time    import clock
from sys import setrecursionlimit
setrecursionlimit(3000) # default = 1000
#--<GLOBALS>-------------------------------------------------------------------------MachineVision--

root      = Tk()
START     = clock()
WIDTH     = 512   # This value was obtained by looking at the file.
HEIGHT    = 512   # This value was obtained by looking at the file.
COLORFLAG = False # True = color image; False = Gray-scale image
HIGH      =  45   # found by experimenting (45 = best)
LOW       =  10   # found by experimenting (10 = best)
NUMBER_OF_TIMES_TO_SMOOTH_IMAGE = 6
#======================================= MAIN =======================================MachineVision==

def main():
#---Pull image data from PPM graphics file into a list of string-type numbers (nums).
#   the string function split, returns the different words
    file1 = open ('lena_rgb_p3.ppm', 'r') # This is the name and location on my personal computer.
    stng = file1.readline().strip()  # strip seems optional, here.
    nums  = file1.read().split()     # split is REQUIRED or all numbers run together.
    file1.close()

#---Create list of gray-values from the file numbers (cast from strings to ints).
    image = []
    for pos in range(0, len(nums), 3):
        RGB = ( int(nums[pos+0]), int(nums[pos+1]),int(nums[pos+2]) )
        image.append( int (0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]) ) # a single gray integer
    printElapsedTime ('Gray numbers are now created.')

    image2 = image.copy()
    testImageInts(image)
    for x in range(NUMBER_OF_TIMES_TO_SMOOTH_IMAGE):
        image2 = smooth(image2)
    testImageInts(image2)
    #image2 = extractTheImageGrayScaleNumbersFromFile ('grayScale.ppm')  # Optional check part 1
    displayImageInWindow (image2)                                           # Optional check part 2
    root.mainloop()
#------------------------------------------------------------------------------------MachineVision--
if __name__ == '__main__':  main()
