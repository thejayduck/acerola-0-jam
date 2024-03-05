﻿define e = Character("Eileen")
default deviceInput = "FFFFFF"
default worldLine = "FFFFFF"
default canInput = False
define translocatorVisible = False
define currentScene = 1

define config.layers = [ 'master', 'film_grain', 'lightning', 'transient', 'screens', 'overlay']

label start:
    show film_grain onlayer film_grain
    show screen translocator_shortcut
    jump scene_1
    return

label show_chapter(idx):
    hide screen translocator with dissolve
    hide screen translocator_shortcut with dissolve
    $ quick_menu = False

    stop music fadeout 2.04
    play sound "audio/sfx/translocator.mp3"
    
    show lightning onlayer lightning
    pause 1
    
    $ renpy.pause(3, hard=True)
    scene black with dissolve

    $ renpy.pause(1.5, hard=True)
    hide lightning onlayer lightning with dissolve
    stop sound fadeout 1.0
    
    $ renpy.pause(1.5, hard=True)
    play sound "audio/sfx/warp.mp3" fadein 0.5
    scene space with dissolve 
    show screen chapterModal(idx) with dissolve
    
    $ renpy.pause(5, hard=True)
    hide screen chapterModal with dissolve
    $ quick_menu = True
    
    stop sound fadeout 15.0
    scene black with fade

screen chapterModal(idx):
    text "#[worldLine]":
        size 100
        xalign .5
        yalign .5

##
# Images & Effects
##

image space:
    "space_1" with dissolve
    pause 0.5
    "space_2" with dissolve
    pause 0.5
    "space_3" with dissolve
    pause 0.5
    "space_4" with dissolve
    pause 0.5
    "space_3" with dissolve
    pause 0.5
    "space_2" with dissolve
    pause 1.5
    repeat

image lightning:
    blend "add"
    "lightning_1" with dissolve
    pause 0.1
    "lightning_2" with dissolve
    pause 0.1
    "lightning_3" with dissolve
    pause 0.1
    "lightning_4" with dissolve
    pause 0.1
    repeat

image film_grain:
    blend "add"
    "grain_1"
    pause 0.1
    "grain_2"
    pause 0.1
    "grain_3"
    pause 0.1
    "grain_4"
    repeat

##
# Transitions
## 
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

##
# Scripts
##
init python:
    # Punctuation Pauses
    def punctuation_pause(input):
        punctuations = {
            ". " : ". {w=0.75}", 
            ", " : ", {w=0.45}",
            "? " : "? {w=0.75}",
            "! " : "! {w=0.75}", #? Add hpunch? (might distrub in some scenes)
            "...": "{cps=2}...{/cps} {w=0.1}"
        }
        for key in punctuations:
            input = input.replace(key, punctuations[key]) 
        return input
    config.say_menu_text_filter = punctuation_pause
    
    # Translocator
    def checkLength():
        global deviceInput
        if len(deviceInput) > 6:
            deviceInput = ""

    def updateInput(input):
        # Button Click SFX
        audioIndex = renpy.random.randint(1, 4)
        renpy.play(f"audio/sfx/numpad/key_{audioIndex}.mp3", "sound")

        # Update deviceInput on Input
        global deviceInput
        deviceInput = deviceInput + input

        if len(deviceInput) == 6 and canInput == True:
            confirmInput()
        else:
            checkLength()

    def confirmInput():
        global worldLine
        worldLine = deviceInput
        renpy.call("show_chapter", f"{currentScene + 1}") #? useful

    def toggleTranslocator():
        global translocatorVisible
        translocatorVisible = not translocatorVisible
        if translocatorVisible: #! Add SFX
            renpy.hide_screen("translocator")
        else:
            renpy.show_screen("translocator")

##
# Translocator Screen
##
style translocator_text:
    color "#000"
    insensitive_color "#08be4e"
    hover_color "#851400"
    selected_color "#930F00"
    size 64
    font "fonts/dot_matrix/DOTMATRI.TTF"

style translocator_shortcut_text:
    color "#000"
    hover_color "#5c5c5c"
    bold True

screen translocator_shortcut():
    textbutton "Toggle Translocator": #? Replace with imagebutton
        pos (1580,1020)
        text_style "translocator_shortcut_text"
        action [Function(toggleTranslocator)]

screen translocator():
    zorder 2
    frame:
        modal True
        xysize (460, 423)
        pos (1425, 576)
        background "images/translocator/translocator_numpad.png"

        # Number Grid
        grid 4 4:
            xalign 0.53
            yalign 0.35
            xspacing 20
            yspacing 5
            textbutton "1": 
                text_style "translocator_text"  
                action [Function(updateInput, "1")]
            textbutton "2":
                text_style "translocator_text"
                action [Function(updateInput, "2")]
            textbutton "3":
                text_style "translocator_text"
                action [Function(updateInput, "3")]
            textbutton "A":
                text_style "translocator_text"
                action [Function(updateInput, "A")]
            textbutton "4":
                text_style "translocator_text"
                action [Function(updateInput, "4")]
            textbutton "5":
                text_style "translocator_text"
                action [Function(updateInput, "5")]
            textbutton "6":
                text_style "translocator_text"
                action [Function(updateInput, "6")]
            textbutton "B":
                text_style "translocator_text"
                action [Function(updateInput, "B")]
            textbutton "7":
                text_style "translocator_text"
                action [Function(updateInput, "7")]
            textbutton "8":
                text_style "translocator_text"
                action [Function(updateInput, "8")]
            textbutton "9":
                text_style "translocator_text"
                action [Function(updateInput, "9")]
            textbutton "C":
                text_style "translocator_text"
                action [Function(updateInput, "C")]
            textbutton "*":
                text_style "translocator_text"
                action [Function(updateInput, "*")]
            textbutton "O":
                text_style "translocator_text"
                action [Function(updateInput, "O")]
            textbutton "#":
                text_style "translocator_text"
                action [Function(updateInput, "#")]
            textbutton "D":
                text_style "translocator_text"
                action [Function(updateInput, "D")]
    # Input Frame
    frame:
        xysize (560, 322)
        pos (1420, 336)
        padding (55, 130)
        background "translocator_screen"
        
        text "#[deviceInput]":
            id "worldLineText"
            font "fonts/dot_matrix/DOTMATRI.TTF"
            antialias True
            color "#000"
            size 72