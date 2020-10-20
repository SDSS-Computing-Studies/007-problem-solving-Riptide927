#!python3 

import time
import pyautogui as p 

p.mouseInfo()

mang=0 
def upgrades():
    if p.pixelMatchesColor(469, 550, (224,136,74)):
        p.click(469, 550)
        time.sleep(1)
        p.click (1170,700)
        p.click (1380,330)
def mangers():
    if p.pixelMatchesColor(464, 622, (224,136,74)):
        p.click(464, 622)
        time.sleep(1)
        p.click (1160,600)
        p.click (1380,330)
        mang + 1
def buy():
    #Oil
    p.moveTo(1230,810)
    if p.pixelMatchesColor(1230, 810, (220,123,54)):
        p.click(1230,810)
    #Bank
    p.moveTo(1230,710)
    if p.pixelMatchesColor(1230, 710, (220,123,54)):
        p.click(1230,710)
    #Movie
    p.moveTo(1230,610)
    if p.pixelMatchesColor(1230, 610, (220,123,54)):
        p.click(1230,610)
    #Hockey
    p.moveTo(1230,530)
    if p.pixelMatchesColor(1230, 530, (220,123,54)):
        p.click(1230,430)
    #Shrimp
    p.moveTo(1230,430)
    if p.pixelMatchesColor(1230, 430, (220,123,54)):
        p.click(1230,430)
    #Donut
    p.moveTo(850,810)
    if p.pixelMatchesColor(850, 810, (220,123,54)):
        p.click(850,810)
    #Pizza
    p.moveTo(850,710)
    if p.pixelMatchesColor(850, 710, (220,123,54)):
        p.click(850,710)
    #Carwash
    p.moveTo(850,630)
    if p.pixelMatchesColor(850, 630, (220,123,54)):
        p.click(850,630)
    #NewsPaper
    p.moveTo(850,530)
    if p.pixelMatchesColor(850, 530, (220,123,54)):
        p.click(850,530)
    #lemonstand
    p.moveTo(850,430)
    if p.pixelMatchesColor(850, 430, (220,123,54)):
        p.click(850,430)
def click():
    if mang!=1:
         p.click(740, 400)
    if mang!=1 or 2:
         p.click(740, 500)
    if mang!=1 or 2 or 3:
         p.click(740, 600)
    if mang!=1 or 2 or 3 or 4:
         p.click(740, 700)
    if mang!=1 or 2 or 3 or 4 or 5:
         p.click(740, 800)
    if mang!=1 or 2 or 3 or 4 or 5 or 6:
         p.click(1100, 400)
    if mang!=1 or 2 or 3 or 4 or 5 or 6 or 7:
         p.click(1100, 500)
    if mang!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
         p.click(1100, 600)
    if mang!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
         p.click(1100, 700)
    if mang!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
         p.click(1100, 800)
def main():
    while True:
       upgrades()
       mangers()
       click()
       buy()
       time.sleep(60)
main()