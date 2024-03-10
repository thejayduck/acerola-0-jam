label show_chapter(scene_jump, scene_id):
  show active_background at distort(active_background) with dissolve

  $ translocator_visible = False
  hide screen translocator_shortcut
  $ quick_menu = False

  stop music fadeout 2.04
  
  pause 0.5
  play sound "audio/sfx/translocator.mp3" volume 0.5
  
  show lightning onlayer lightning
  pause 1
  
  $ renpy.pause(3, hard=True)
  scene black with dissolve

  $ renpy.pause(1.5, hard=True)
  hide lightning onlayer lightning with dissolve
  stop sound fadeout 1.0
  
  $ renpy.pause(1.5, hard=True)
  play music "audio/bgm/warp_2.mp3" fadein 0.5
  scene warp with dissolve 
  show screen chapter_modal(scene_id) with dissolve
  
  $ renpy.pause(6, hard=True)
  $ quick_menu = True
  
  hide screen chapter_modal with dissolve
  scene black with fade
  play sound "audio/sfx/chapter_start.mp3"
  stop music fadeout 5

  $ renpy.call(scene_jump)

transform modal_scroll():
    xcenter 0.5 yanchor 0.0 ypos 1.0
    ypos 150
    ease 4 ypos -1710
    ease .7 ypos -1697
    ease .3 ypos -1700
    # ease 6 zoom 1.5 ypos -2750

screen chapter_modal(scene_id):
  key "K_ESCAPE" action NullAction()
  key "K_MENU" action NullAction()
  key "mouseup_3" action NullAction()

  frame at modal_scroll():
    style_prefix "modal"
    background None
    xalign 0.5
    
    vbox:
      text "#1A2B3C"
      text "#4D5E6F"
      text "#7G8H9I"
      text "#J1K2L3"
      text "#4M5N6O"
      text "#7P8Q9R"
      text "#S1T2U3"
      text "#4V5W6X"
      text "#7Y8Z9A"
      text "#B1C2D3"
      text "#E4F5G6"
      text "#H7I8J9"
      text "#K1L2M3"
      text "#N4O5P6"
      text "#Q7R8S9"
      text "#T1U2V3"
      text "#W4X5Y6"
      text "#Z7A8B9"
      text "#C1D2E3"
      null height 24
      text"#[scene_id]":
        color "FFFFFF"
        size 120
      null height 24
      text "#F4G5H6"
      text "#I7J8K9"
      text "#L1M2N3"
      text "#O4P5Q6"
      text "#R7S8T9"
      text "#U1V2W3"
      text "#X4Y5Z6"
      text "#A7B8C9"
      text "#D1E2F3"
      text "#G4H5I6"
      text "#J7K8L9"

return

style modal_text:
  color "#ffffff20"
  size 95
  xalign .5
  yalign .5

#! End Testing Features

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