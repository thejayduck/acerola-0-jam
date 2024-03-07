label scene_1:
  $can_input = False
  # These display lines of dialogue.
  maike "lets see how backgrounds look and decide on a shot that fits it the best."
  
  show screen translocator

  scene bedroom
  show maike
  show franz at right
  maike "This is bedroom"

  scene bathroom
  show maike
  show franz at right
  maike "This is bathroom"
  
  scene hallway
  show maike
  show franz at right
  maike "This is hallway"

  scene hallway_2
  show maike
  show franz at right
  maike "This is hallway 2"
  
  scene living_room
  show maike
  show franz at right
  maike "This is living_room"

  cassian "Maybe I can write on it now..."

  maike "Let's see how CG's look"

  scene franz_punch with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  franz "I look dumb here."

  scene franz_punch with hpunch

  maike "You always look like that"

  scene maike_scared with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  franz "Wow!" with hpunch

  franz "You can show emotions!!!" 

  cassian "what does the translocator look like?"

  scene translocator_cg_1 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  scene translocator_cg_2 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  scene translocator_cg_3 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  $ translocator_alarm()
  cassian "huh what's that?"

  $ translocator_alarm()
  cassian "Where is it coming from?"

  $ translocator_alarm(True)
  # $ renpy.pause(hard=True) #! Pauses story advancement
  cassian "Ah it's the translocator."

  cassian "Hmmm, I wonder if it works now."

  cassian "If I dont take the chance now, I will never know what this thing is..."

  maike "You've created a new Ren'Py game."

  cassian "Sup!!!!"

  "I am the narrator hello!"

  maike "Testing pauses. Uhhhh, so what's up? Have you been doing okay... Yeah cool cool."

  maike "AAAAHHHH! OMG WHAT WAS THAT? Oh btw, I am joking, we are still testing the pauses."

  maike "You can't Input anything yet... Wow Funny."

  $can_input = True
  maike "Try now"

  # call show_chapter("2", world_line) 

  maike "You can now input"

  maike "Once you add a story, pictures, and music, you can release it to the world!"

  jump scene_2

  return

label ignore: # A way to structure endings.
  scene living_room
  show maike
  show franz at right
  $ translocator_visible = False
  hide screen translocator_shortcut
  cassian "Argh never mind this crappy device..."
  cassian "I would rather waste money on more fortune tellers."

label .bad_end:
  "Bad End"
  return