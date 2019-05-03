
import numpy as np
import imageio
import matplotlib.pyplot as plt
import random as rnd

def plot_image(img):
    fig = plt.figure(figsize=(5,27))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.show()
  

    
    
    
def make_picture_gray(pic):
    a = pic[:,:,:].max(axis=2)
    a = a.reshape((34,152,1))
    pic1 = a[:]
    pic1 = np.append(pic1, a, axis = 2)
    pic1 = np.append(pic1, a, axis = 2)  
    return pic1
    
    
def change_picture(pic1, nums, pixels_x, pixels_y, shade):
    '''Добавляет изменения в pic1 согласно
       nums, pixels_x, pixels_y и shade'''
    pic = np.array(pic1)
    E = pic.mean()
    #print(pic.shape[2])
    add_darkness = rnd.normalvariate(E / 2, 50)
    add_darkness = -int(add_darkness)
    pic = pic.astype(int)
    np.clip(add_darkness + pic, 0, 255, out=pic)

    pic[pixels_x, pixels_y] = [[shade[i],shade[i],shade[i]] for i in range(nums)]
    return pic
        
        
def choose_changes_for_picture(pic):
    '''choose noise to the picture
       return nums_pixels pixels_x pixels_y shade
       nums_pixels - number of pixels to change
       pixels_x - array of coordinates of pixels on x-axis
       pixels_y - array of coordinates of pixels on y-axis
       shade - array of shades'''
    '''Chosse numbers of pixels 
                        30-Math Expectation 
                        20-Dispersion'''
    nums_pixels = rnd.normalvariate (800, 20)
    nums_pixels = int(nums_pixels)
    if (nums_pixels < 0):
        nums_pixels = 0
    if (nums_pixels > (pic.shape[0] * pic.shape[1]) / 2):
        num_pixels = int((pic.shape[0] * pic.shape[1]) / 2)
    
    '''Add pixels on y - axis
                  Normal Distribution
                  Math Exp is the center of picture on y
                  Dispersion is 1/4 of numbers pixels on y'''
    
    pixels_x = (pic.shape[0] / 4) * np.random.randn(nums_pixels) + pic.shape[0] / 2
    pixels_x = np.clip(pixels_x, 0, pic.shape[0] - 1).astype(int)
    
    '''Add pixels on x - axis
                  Normal Distribution
                  Math Exp is the center of picture on x
                  Dispersion is 1/4 of numbers pixels on x'''
    pixels_y = (pic.shape[1] / 4) * np.random.randn(nums_pixels) + pic.shape[1] / 2
    pixels_y = np.clip(pixels_y, 0, pic.shape[1] - 1).astype(int)
    
    
    '''Choose shade of gray for every pixel'''
    
    shade = np.random.randn(nums_pixels) * (255 / 4) + 255/2
    np.clip(shade, 0, 255, out=shade)
    return nums_pixels, pixels_x.astype (int), pixels_y.astype (int), shade.astype (int)
    
