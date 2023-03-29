#!/usr/bin/env python
# coding: utf-8

# In[4]:


# i) Convert BGR and RGB to HSV and GRAY

# BGR TO HSV

import cv2
image =cv2.imread('bike.png')
cv2.imshow('original',image)
b_h=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR_HSV',b_h)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[6]:


# BGR TO GRAY

import cv2
image =cv2.imread('bike.png')
cv2.imshow('original',image)
b_g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR_GRAY',b_g)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[8]:


# RGB TO HSV

import cv2
image =cv2.imread('bike.png')
cv2.imshow('original',image)
r_h=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB_HSV',r_h)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[10]:


# RGB TO GRAY

import cv2
image =cv2.imread('bike.png')
cv2.imshow('original',image)
r_g=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB_GRAY',r_g)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[12]:


# ii)Convert HSV to RGB and BGR

# HSV TO RGB

import cv2
ori=cv2.imread('bgr_hsv.png')
cv2.imshow('hsvtorgb',ori)
h_r=cv2.cvtColor(ori,cv2.COLOR_HSV2RGB)
cv2.imshow('HSV_RGB',h_r)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[13]:


# HSV TO BGR

import cv2
ori=cv2.imread('bgr_hsv.png')
cv2.imshow('Original',ori)
h_b=cv2.cvtColor(ori,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV_BGR',h_b)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[16]:


# iii)Convert RGB and BGR to YCrCb

# RGB TO YCrCb

import cv2
ori=cv2.imread('hsv_rgb.png')
YCrCb_image = cv2.cvtColor(ori, cv2.COLOR_RGB2YCrCb)
cv2.imshow('RGB_YCRCB',YCrCb_image)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[18]:


# BGR TO YCrCb

import cv2
image1=cv2.imread('bike.png')
YCrCb_image = cv2.cvtColor(image1, cv2.COLOR_BGR2YCrCb)
cv2.imshow('BGR_YCRCB',YCrCb_image)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[ ]:


# iv)Split and Merge RGB Image

import cv2
img = cv2.imread("bike.png")
img1= cv2.resize(img, (270,180))
cv2
b,g,r = cv2.split(img1)
cv2.imshow("RED MODEL", r)
cv2.imshow("GREEN MODEL", g)
cv2.imshow("BLUE MODEL ", b)
merger = cv2.merge([b,g,r])
cv2.imshow("MERGED IMAGE", merger )
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


# v) Split and merge HSV Image

import cv2
img = cv2.imread("rgb_hsv.png")
img1= cv2.resize(img, (270,180))
cv2
r,g,b = cv2.split(img1)
cv2.imshow("RED MODEL", r)
cv2.imshow("GREEN MODEL", g)
cv2.imshow("BLUE MODEL ", b)
merger = cv2.merge([b,g,r])
cv2.imshow("MERGED IMAGE", merger )
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




