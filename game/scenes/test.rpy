label test:
  $can_input = False
  # These display lines of dialogue.
  # scene warp with dissolve 

  maike "lets see how backgrounds look and decide on a shot that fits it the best."

  "Let's try to enter a number... automatically"

  scene bedroom
  show maike
  show franz at right
  maike "This is bedroom"

  scene bathroom
  show maike scared
  show franz at right
  maike "This is bathroom"

  scene hallway
  show maike smirk
  show franz happy hip at right
  maike "This is hallway"

  scene hallway_2
  show maike tired crossed
  show franz sad at right
  maike "This is hallway 2"

  scene living_room
  show maike
  show franz surprised at right
  maike "This is living_room"

  scene city_empty
  show franz tired at right
  maike "This is city_empty"

  scene restaurant
  show franz annoyed at right
  maike "This is restaurant"

  scene fortune_teller
  maike "This is fortune_teller"

  cassian "Maybe I can write on it now..."

  maike "Let's see how CG's look"

  scene franz_punch with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  franz "I look dumb here."

  scene franz_punch with hpunch

  maike "You always look like that"

  scene maike_scared with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  scene maike_scared_2 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  franz "Wow!" with hpunch

  franz "You can show emotions!!!" 

  scene cassian_crazy with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  scene cassian_crazy_2 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  franz "What... the hell happened to you dude?"

  cassian "Haha, my acting seems good right?"

  cassian "what does the translocator look like?"

  scene translocator_cg_1 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  scene translocator_cg_2 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  scene translocator_cg_3 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  scene translocator_cg_4 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  scene bedroom with dissolve
  $ active_background = "bedroom"
  $ force_input("313600")

  $ translocator_alarm()
  # if not translocator_visible:
  #   cassian "huh what's that?"
  # else:
  #   cassian "oh its this."

  # if not translocator_visible:
  #   $ translocator_alarm()
  #   cassian "Where is it coming from?"
  # else:
  #   cassian "oh its this."

  $ patience = 3

  while patience > 0:
    $ translocator_alarm()
    cassian "Where is it coming from?"
    
    $ patience -= 1

  $ translocator_alarm(True)
  cassian "oh its the device."

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

  maike "You can now input"

  maike "Once you add a story, pictures, and music, you can release it to the world!"

  jump scene_2

  return

  label ignore: # A way to structure endings.
  scene living_room
  show maike
  show franz at right
  $ translocator_visible = False
  cassian "Argh never mind this crappy device..."
  cassian "I would rather waste money on more fortune tellers."