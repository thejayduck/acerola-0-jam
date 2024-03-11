default device_input = "FFFFFF"

default active_background = None
define can_input = False
define translocator_visible = False

default desired_input = None
default correct_exit = None
default wrong_exit = None

define config.layers = [ 'master', 'film_grain', 'lightning', 'transient', 'screens', 'overlay']

label start:
    show film_grain onlayer film_grain
    # show screen translocator_shortcut
    jump scene_1
    return

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

transform distort(target):
    animated_glitch(target, chroma=True, offset=10)
    parallel:
        function WaveShader(amp=0.2, speed=0.25, double="horizontal")

transform nausea(target, amp = 12):
    parallel:
        function WaveShader(amp=amp, period=3.495, direction="vertical")

##
# Functions
##
init python:
    # import time

    # target input, exit on right input, exit on wrong input
    def set_route(background, route, correct, wrong):
        global active_background
        global desired_input
        global correct_exit
        global wrong_exit
        
        active_background = background
        desired_input = route
        correct_exit = correct
        wrong_exit = wrong

    # Punctuation Pauses
    def punctuation_pause(input):
        punctuations = {
            ". " : ". {w=0.75}", 
            ", " : ", {w=0.45}",
            "? " : "? {w=0.75}",
            "! " : "! {w=0.75}",
            "...": "{cps=2}...{/cps} {w=0.1}",
            "…": "{cps=2}...{/cps} {w=0.1}"
        }
        for key in punctuations:
            input = input.replace(key, punctuations[key]) 
        return input
    config.say_menu_text_filter = punctuation_pause
    
    # Translocator
    def check_length(last_input):
        global device_input
        if len(device_input) > 6:
            device_input = ""

    def update_input(input, forced = False):
        global device_input
        global desired_input
        global correct_exit
        global wrong_exit

        if not can_input and not forced:
            translocator_error()
            return

        device_input += input
        check_length(input)

        audio_index = renpy.random.randint(1, 4)
        renpy.play(f"audio/sfx/numpad/key_{audio_index}.mp3", "sound")

        if len(device_input) == 6:   
            if forced:
                confirm_input(correct_exit, device_input)
                return

            if desired_input == None:
                confirm_input(wrong_exit, device_input)
            if device_input == desired_input:
                confirm_input(correct_exit, device_input)
            else:
                confirm_input(wrong_exit, device_input)

    def translocator_error():
        renpy.play("audio/sfx/beep_2.wav", "sound")

    def force_input(target):
        global device_input
        global translocator_visible

        translocator_visible = True
        renpy.show_screen("translocator")
        renpy.hide_screen("translocator_shortcut")
        device_input = ""
        
        renpy.pause(1.5, hard=True)
        
        index = 0
        while index < 6:
            character = target[index]
            update_input(character, True)

            pause_dur = renpy.random.uniform(0.5, 0.9)
            renpy.pause(pause_dur, hard=True)
            
            index += 1
            
        confirm_input()

    def confirm_input(label, id):
        global device_input
        device_input = id

        renpy.call("show_chapter", scene_jump=label, scene_id=id)

    def toggle_translocator():
        global translocator_visible
        # global device_input

        # if can_input == True: # Keeping this just in case
        #     device_input = ""

        translocator_visible = not translocator_visible
        if translocator_visible: #! Add SFX
            renpy.play("audio/sfx/pick_up.mp3", "sound")
            renpy.show_screen("translocator")
        else:
            renpy.play("audio/sfx/put_down.mp3", "sound")

    def translocator_alarm(force = False):
        global device_input
        global can_input
        global translocator_visible
        device_input = ""
        can_input = True
        renpy.play("audio/sfx/device_beep.mp3", "sound")

        if force:
            translocator_visible = True
            renpy.show_screen("translocator")
    
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
        timer 0.1 action [Hide("translocator_numpad", transition=dissolve)]
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
        background None

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
        background None
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