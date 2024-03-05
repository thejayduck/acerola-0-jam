label scene_1:




  # These display lines of dialogue.
  friend1 "lets see how backgrounds look and decide on a shot that fits it the best."
  
  scene room_1
  show friend1
  show friend2 at right
  friend1 "This is room 1"

  scene bathroom
  show friend1
  show friend2 at right
  friend1 "This is bathroom"
  
  scene hallway
  show friend1
  show friend2 at right
  friend1 "This is hallway"
  
  scene living_room
  show friend1
  show friend2 at right
  friend1 "This is living_room"




  friend1 "You've created a new Ren'Py game."

  protagonist "Sup!!!!"

  friend1 "Testing pauses. Uhhhh, so what's up? Have you been doing okay... Yeah cool cool."

  friend1 "AAAAHHHH! OMG WHAT WAS THAT? Oh btw, I am joking, we are still testing the pauses."

  friend1 "You can't Input anything yet... Wow Funny."

  $canInput = True
  friend1 "Try now"

  # call show_chapter("2", worldLine) 

  friend1 "You can now input"

  friend1 "Once you add a story, pictures, and music, you can release it to the world!"

  jump scene_2

  return