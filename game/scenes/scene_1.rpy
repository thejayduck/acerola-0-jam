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
  
  scene living_room
  show maike
  show franz at right
  maike "This is living_room"

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