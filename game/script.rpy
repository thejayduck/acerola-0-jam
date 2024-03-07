default device_input = "FFFFFF"
default world_line = "FFFFFF"
default device_target = "ending.bad_end_1"
default can_input = False
define translocator_visible = False
# define next_scene = "scene_2"

define config.layers = [ 'master', 'film_grain', 'lightning', 'transient', 'screens', 'overlay']

label start:
    show film_grain onlayer film_grain
    show screen translocator_shortcut
    jump scene_1
    return

label show_chapter():
    $ translocator_visible = False
    hide screen translocator_shortcut
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
    play music "audio/bgm/warp.mp3" fadein 0.5
    scene warp with dissolve 
    show screen chapter_modal with dissolve #? Try fade
    
    $ renpy.pause(6.5, hard=True)
    hide screen chapter_modal with dissolve #? Try fade
    $ quick_menu = True
    
    scene black with fade
    play sound "audio/sfx/chapter_start.mp3"
    stop music fadeout 5

    $ renpy.call(device_target)

screen chapter_modal():
    text "#[world_line]":
        size 100
        xalign .5
        yalign .5

##
# Images & Effects
##
image translocator_main_menu:
    Movie(
        play="images/main_menu/translocator_turn.webm",
        mask="images/main_menu/translocator_turn_mask.webm",
        loop=True,
        size=(768,768)
    )

image translocator_show:
    Movie(
        play="images/translocator/translocator_show.webm",
        mask="images/translocator/translocator_show_mask.webm",
        keep_last_frame=True,
        loop=False
    )

image translocator_hide:
    Movie(
        play="images/translocator/translocator_hide.webm",
        mask="images/translocator/translocator_hide_mask.webm",
        keep_last_frame=True,
        loop=False
    )

image warp:
    "warp_1" with dissolve
    pause 1.0
    "warp_2" with dissolve
    pause 1.5
    "warp_3" with dissolve
    pause 1.5
    "warp_4" with dissolve
    pause 1.5
    "warp_5" with dissolve
    pause 2.0

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
    pause 0.5
    "space_1" with dissolve #? Try this out
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

transform shaking:
    linear 0.1 xoffset -2 yoffset 2 
    linear 0.1 xoffset 3 yoffset -3 
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    repeat 2

##
# Functions
##
init python:
    # import time

    # Punctuation Pauses
    def punctuation_pause(input):
        punctuations = {
            ". " : ". {w=0.75}", 
            ", " : ", {w=0.45}",
            "? " : "? {w=0.75}",
            "! " : "! {w=0.75}",
            "...": "{cps=2}...{/cps} {w=0.1}"
        }
        for key in punctuations:
            input = input.replace(key, punctuations[key]) 
        return input
    config.say_menu_text_filter = punctuation_pause
    
    # Translocator
    def check_length():
        global device_input
        if len(device_input) > 6:
            device_input = ""

    def update_input(input):
        global device_input

        # Update device_input on Input
        if can_input:
            device_input = device_input + input
            check_length()
        
            # Numpad SFX    
            audio_index = renpy.random.randint(1, 4)
            renpy.play(f"audio/sfx/numpad/key_{audio_index}.mp3", "sound")

            if len(device_input) == 6:
                confirm_input()
        else:
            translocator_error(False)

    def translocator_error(generic = True):
        renpy.play("audio/sfx/beep_2.wav", "sound")
        
        if not generic:
            responses = [
                "Hm... The device seems unresponsive...",
                "It doesn't seem like it works...",
                "My input doesn't get registered...",
                "Weird, why doesn't it work?",
                "..."
            ]
            renpy.invoke_in_new_context(renpy.say, narrator, renpy.random.choice(responses))

    def confirm_input():
        global world_line
        global device_target
        world_line = device_input
        renpy.call("show_chapter") #? useful

    def toggle_translocator():
        global translocator_visible
        # global device_input

        # if can_input == True: # Keeping this just in case
        #     device_input = ""

        translocator_visible = not translocator_visible
        if translocator_visible: #! Add SFX
            renpy.notify("Translocator Visible")
        else:
            renpy.notify("Translocator Hidden")

    def translocator_alarm(force = False):
        global device_input
        global can_input
        global translocator_visible
        device_input = ""
        can_input = True
        renpy.play("audio/sfx/deviceBeep.mp3", "sound")

        if force:
            translocator_visible = True
    
    # Scene Jump
    def jump_to_scene(target):
        renpy.jump(target)


##
# Translocator Screen
##
style translocator_text:
    color "#000"
    insensitive_color "#08be4e"
    hover_color "#851400"
    selected_color "#930F00"
    size 54
    font "fonts/dot_matrix/DOTMATRI.TTF"

style translocator_shortcut_text:
    color "#000"
    hover_color "#5c5c5c"
    bold True

screen translocator_shortcut():
    zorder 2
    imagebutton:
        pos (1790,920)
        auto "images/translocator/shortcut/translocator_button_%s.png" 
        sensitive True  
        action Function(toggle_translocator)

screen translocator():
    zorder 2
    if translocator_visible:
        add "translocator_show" xalign 0.992
        timer 0.5 action [Show("translocator_numpad", transition=dissolve)]
    else:
        timer 0.1 action [Hide("translocator_numpad")]
        add "translocator_hide" xalign 0.992
        
screen translocator_numpad():
    zorder 2

    # Input Frame
    frame:
        modal True
        xysize (382, 94)
        xalign 0.935
        yalign 0.422
        padding (10, 10)
        background Null()

        text "#[device_input]":
            id "device_input"
            font "fonts/dot_matrix/DOTMATRI.TTF"
            antialias True
            color "#000"
            size 72

    # Numpad Frame
    frame:
        modal True
        xysize (333,333)
        xalign 0.974
        yalign 0.74
        background Null()
        padding (20,5)
        
        grid 4 4:
            xspacing 43
            yspacing 20
            textbutton "1": 
                text_style "translocator_text"  
                action [Function(update_input, "1")]
            textbutton "2":
                text_style "translocator_text"
                action [Function(update_input, "2")]
            textbutton "3":
                text_style "translocator_text"
                action [Function(update_input, "3")]
            textbutton "A":
                text_style "translocator_text"
                action [Function(update_input, "A")]
            textbutton "4":
                text_style "translocator_text"
                action [Function(update_input, "4")]
            textbutton "5":
                text_style "translocator_text"
                action [Function(update_input, "5")]
            textbutton "6":
                text_style "translocator_text"
                action [Function(update_input, "6")]
            textbutton "B":
                text_style "translocator_text"
                action [Function(update_input, "B")]
            textbutton "7":
                text_style "translocator_text"
                action [Function(update_input, "7")]
            textbutton "8":
                text_style "translocator_text"
                action [Function(update_input, "8")]
            textbutton "9":
                text_style "translocator_text"
                action [Function(update_input, "9")]
            textbutton "C":
                text_style "translocator_text"
                action [Function(update_input, "C")]
            textbutton "*":
                text_style "translocator_text"
                action [Function(translocator_error)]
            textbutton "O":
                text_style "translocator_text"
                action [Function(update_input, "O")]
            textbutton "#":
                text_style "translocator_text"
                action [Function(translocator_error)] 
            textbutton "D":
                text_style "translocator_text"
                action [Function(update_input, "D")]