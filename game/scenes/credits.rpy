screen credits():
  style_prefix "credits"
  tag menu
  use game_menu(_("Credits"), scroll="viewport"):
    vbox:
      text "Made for {a=https://itch.io/jam/acerola-jam-0/}Acerola Jam 0{/a} in 14 Days"
      text "{a=https://github.com/thejayduck/acerola-0-jam/}Source Code{/a}"
     
      null height 24

      label "Main"
      hbox:
        text "{a=https://thejayduck.itch.io/}Itch.io{/a} • "
        text "{a=https://ardarmutcu.com/}Website{/a} • "
        text "{a=https://github.com/thejayduck/}Github{/a}"
      text "Programming: TheJayDuck"
      text "Writing: TheJayDuck"
      text "Sprite Art: TheJayDuck"
      text "CG Art: TheJayDuck"
      text "BG Art: TheJayDuck"
      text "Effect Art: TheJayDuck"

      null height 48

      label "Extra"
      text "# Effects"
      text "  - {a=https://github.com/SoDaRa/RenpyWaveShader/}RenpyWaveShader{/a}"
      text "  - {a=https://github.com/Gouvernathor/renpy-ChromaGlitch}renpy-ChromaGlitch{/a}"
      text "# BGM (CC0)"
      text "  - {a=https://freesound.org/s/614947/}Main Menu{/a}"
      text "  - {a=https://freesound.org/s/720627/}Casual{/a}"
      text "  - {a=https://freesound.org/s/680333/}Casual 2{/a}"
      text "  - {a=https://freesound.org/s/541578/}Realization{/a}"
      text "  - {a=https://freesound.org/s/485971/}Something is Wrong{/a}"
      text "  - {a=https://freesound.org/s/466301/}Nightmare{/a}"
      text "  - {a=https://freesound.org/s/466298/}Casual Goodbye{/a}"
      text "  - {a=https://freesound.org/s/109506/}All Gone{/a}"
      text "# SFX (CC0)"
      text "  - Translocator (Mashup): " +\
      "{a=https://freesound.org/s/415097/}1{/a}, " +\
      "{a=https://freesound.org/s/531421/}2{/a}, " +\
      "{a=https://freesound.org/s/402511/}3{/a}"
      text "  - Device Throw (Mashup): " +\
      "{a=https://freesound.org/s/700857/}1{/a}, " +\
      "{a=https://freesound.org/s/447987/}2{/a}"
      text "  - {a=https://freesound.org/s/188831/}Space Ambiance{/a}"
      text "  - {a=https://freesound.org/s/339130/}Translocator Alarm{/a}"
      text "  - {a=https://freesound.org/s/681420/}Pickup and Putdown{/a}"
      text "  - {a=https://freesound.org/s/536748/}Phone Notification{/a}"
      text "  - {a=https://freesound.org/s/256512/}Door Knock{/a}"
      text "  - {a=https://freesound.org/s/442280/}Doorbell{/a}"
      text "  - {a=https://freesound.org/s/406639/}Door Open{/a}"
      text "  - {a=https://freesound.org/s/637482/}Room Door Open{/a}"
      text "  - {a=https://freesound.org/s/383774/}Laying Down{/a}"
      text "  - {a=https://freesound.org/s/205819/}Walking Towards{/a}"
      text "  - {a=https://freesound.org/s/369835/}Running{/a}"
      text "  - {a=https://freesound.org/s/459965/}Running Away{/a}"
      text "  - {a=https://freesound.org/s/326048/}Wall Hit{/a}"
      text "  - {a=https://freesound.org/s/348225/}Light Switch{/a}"
      text "  - {a=https://freesound.org/s/348241/}Punch{/a}"
      text "  - {a=https://freesound.org/s/338116/}Vomiting{/a}"
      text "  - {a=https://freesound.org/s/458545/}Stomach Grumble{/a}"
      text "  - Key Press 1-4: TheJayDuck"
      text "  - Device Error Beep: TheJayDuck"
      text "  - Phone Tap: TheJayDuck"
      text "# Translocator Model Parts"
      text "  - {a=https://grabcad.com/library/lcd-display-16x2-3}LCD Display{/a}"
      text "  - {a=https://grabcad.com/library/delphine-custom-numpad-pcb-1}Numpad{/a}"
      text "  - {a=https://grabcad.com/library/cherry-mx-keycap-1}Keycaps{/a}"

      null height 24

      text "I may have missed some sound effects due to the sheer amount of them. All additional assets besides what I created were either CC0 or Public Domain."

style credits_text:
  justify True
    
style credits_label_text:
  xalign 0.5
  size 48
  justify True
  text_align 0.5