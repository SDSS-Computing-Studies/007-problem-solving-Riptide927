#!python3 

import time
import pyautogui as p 

p.mouseInfo()


def upgrades():
    if p.pixelMatchesColor(469, 550, (220,123,54))==True:
        p.click(469, 550)
        time.sleep(0.5)
        p.click (1170,700)
        time.sleep(0.5)
        p.moveTo (1380,330)
        p.click (1380,330)
def mangers():
    if p.pixelMatchesColor(464, 622, (220,123,54))==True:
        p.click(464, 622)
        time.sleep(0.5)
        p.click (1160,600)
        time.sleep(0.5)
        p.moveTo (1380,330)
        p.click (1380,330)
def buy():
    #Oil
    if p.pixelMatchesColor(1230, 810, (224,136,74)):
        p.moveTo(1230,810)
        p.click(1230,810)
    #Bank
    if p.pixelMatchesColor(1180, 710, (224,136,74)):
        p.moveTo(1180,710)
        p.click(1180,710)
    #Movie
    if p.pixelMatchesColor(1180, 610, (224,136,74)):
        p.moveTo(1180,610)
        p.click(1180,610)
    #Hockey
    if p.pixelMatchesColor(1180, 540, (224,136,74)):
        p.moveTo(1230,525)
        p.click(1230,525)
    #Shrimp
    if p.pixelMatchesColor(1230, 430, (224,136,74)):
        p.moveTo(1230,430)
        p.click(1230,430)
    #Donut
    if p.pixelMatchesColor(850, 810, (224,136,74)):
        p.moveTo(850,810)
        p.click(850,810)
    #Pizza
    if p.pixelMatchesColor(850, 710, (224,136,74)):
        p.moveTo(850,710)
        p.click(850,710)
    #Carwash
    if p.pixelMatchesColor(850, 630, (224,136,74)):
        p.moveTo(850,630)
        p.click(850,630)
    #NewsPaper
    if p.pixelMatchesColor(850, 530, (224,136,74)):
        p.moveTo(850,530)
        p.click(850,530)
    #lemonstand
    if p.pixelMatchesColor(815, 440, (224,136,74)):
        p.moveTo(815, 440)
        p.click(815, 440)

def click():
    for x in range (10):
        upgrades()
        mangers()
        #lemon
        if p.pixelMatchesColor(800, 382, (115,105,96)):
            p.click(740, 400)
        #News
        if p.pixelMatchesColor(800, 4574, (115,105,96)):
            p.click(740, 500)
        #car
        if p.pixelMatchesColor(800, 570, (115,105,96)):
            p.click(740, 600)
        #Pizza
        if p.pixelMatchesColor(800, 666, (115,105,96)):
            p.click(740, 700)
        #Donut
        if p.pixelMatchesColor(784, 775, (115,105,96)):
            p.click(740, 800)

        if p.pixelMatchesColor(1160, 400, (115,105,96)):
            p.click(1160, 400)
        if p.pixelMatchesColor(1160, 493, (115,105,96)):
            p.click(1160, 493)
        if p.pixelMatchesColor(1160, 587, (115,105,96)):
            p.click(1160, 587)
        if p.pixelMatchesColor(1160, 680, (115,105,96)):
            p.click(1160, 680)
        if p.pixelMatchesColor(1160, 775, (115,105,96)):
            p.click(1160, 775)
def main():
    while True:
       click()
       buy()
click()