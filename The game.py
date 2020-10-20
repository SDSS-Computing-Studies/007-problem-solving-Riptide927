#!python3 

import time
import pyautogui as p 

p.mouseInfo()


def upgrades():
    if p.pixelMatchesColor(469, 550, (220,123,54))==True:
        p.click(469, 550)
        time.sleep(1)
        p.click (1170,700)
        time.sleep(1)
        p.moveTo (1380,330)
        p.click (1380,330)
def mangers():
    if p.pixelMatchesColor(464, 622, (220,123,54))==True:
        p.click(464, 622)
        time.sleep(1)
        p.click (1160,600)
        time.sleep(1)
        p.moveTo (1380,330)
        p.click (1380,330)
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
            p.click(1100, 400)
        if p.pixelMatchesColor(1160, 493, (115,105,96)):
            p.click(1100, 500)
        if p.pixelMatchesColor(1160, 587, (115,105,96)):
            p.click(1100, 600)
        if p.pixelMatchesColor(1160, 680, (115,105,96)):
            p.click(1100, 700)
        if p.pixelMatchesColor(1160, 775, (115,105,96)):
            p.click(1100, 800)
def main():
    while True:
       click()
       buy()
main()