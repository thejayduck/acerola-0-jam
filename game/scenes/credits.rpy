screen credits():
  style_prefix "credits"
  tag menu
  # add "images/main_menu/main_menu.png" matrixcolor BrightnessMatrix(-0.1)
  use game_menu(_("Credits"), scroll="viewport"):
    # textbutton _("Return") action Return() yalign 1.0
    vbox:
      label "Main"
      text "Programming: TheJayDuck"
      text "Writing: TheJayDuck"
      text "Sprite Art: TheJayDuck"
      text "CG Art: TheJayDuck"
      text "BG Art: TheJayDuck"
      text "Effect Art: TheJayDuck"
      text "Key Press 1-4: TheJayDuck"
      text "Device Beep: TheJayDuck"

      null height 48

      label "Extra"
      text "Translocator Model Parts"
      text " - {a=https://grabcad.com/library/lcd-display-16x2-3}LCD{/a}"
      text " - {a=https://grabcad.com/library/delphine-custom-numpad-pcb-1}Numpad{/a}"
      text " - {a=https://grabcad.com/library/cherry-mx-keycap-1}Keycaps{/a}"
      text "Music"
      text " - {a=https://freesound.org/people/younoise/sounds/614947/}Main Menu{/a}"
      text "SFX"
      text " - {a=https://freesound.org/people/0ktober/sounds/188831/}Space Ambiance{/a}"
      text " - {a=https://freesound.org/people/IndigoRay/sounds/339130/}Translocator Alarm{/a}"
      text " - Translocator (Mashup): " +\
      "{a=https://freesound.org/people/gusgus26/sounds/415097/}1{/a}, " +\
      "{a=https://freesound.org/people/Resaural/sounds/531421/}2{/a}, " +\
      "{a=https://freesound.org/people/Zat_Dude/sounds/402511/}3{/a}"
      
style credits_text:
  justify True
    
style credits_label_text:
  xalign 0.5
  size 48
  justify True
  text_align 0.5