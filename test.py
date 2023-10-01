from selenium import webdriver
from selenium.webdriver.common.by import By
import cv2
import web_check


img=cv2.imread("screenshot.png")
hash1=web_check.aHash(img)
img=cv2.imread("screenshot2.png")
hash2=web_check.aHash(img)

print(hash1==hash2)