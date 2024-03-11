label scene_4:
  $ translocator_visible = False
  hide screen translocator
  hide screen translocator_numpad
  "The space and time around me started to warp, once again."

  scene bedroom at nausea("bedroom", 3):
    blur 20
  with dissolve

  cassian "Urk!"

  "This time knowing what's about to come, I endure my nausea, until the warped world around me settles down."

  scene bedroom with dissolve

  cassian "The device, it worked! You've saw it too right, Maike?"

  "...She isn't here."

  scene living_room with fade

  "But her belongings are still here, in the living room."

  "What about Franz?!"

  #! Running SFX
  show hallway with Fade(0.2, 0.2, 0.2)
  
  cassian "It, it's back! The door that was sealed shut with cold concrete is back here!"

  cassian "Did the device work properly?!"

  #! Door Open SFX

  cassian "..."

  scene black with fade

  "With the door open, I was met with his usual room, messy as ever."

  "I would take a look around it, but I wouldn't dare to step on a landmine ."

  cassian "Maybe the two are outside, waiting for me."

  "Yeah, that must be it. Similar things happened before as well."

  cassian "Maybe they are around the campus."

  show city_empty with fade

  cassian "..."

  "Silence. No coughs, no music, no traffic, just unnatural quiet followed by the natural sounds."

  "It's not that the street is quiet, that's impossible around here."
  "A place many dreams of visiting, a place where nightlife is just as loud as the day."
  "Children screaming with joy throughout, 9 to 5 workers rushing to their offices."
  "The buses, cars, the smell of exhaust emitted from all those vehicles…"

  "All gone."

  "Hundreds of thousands of people walking around the city… all vanished."

  $ translocator_visible = True
  show screen translocator

  cassian "Damn you… DAMN YOU!" # hpunch

  $ translocator_visible = False
  pause 1.0
  hide screen translocator
  hide screen translocator_numpad
  
  #! Throw SFX

  "I throw the device with full force on the hot asphalt in the middle of the road." with hpunch

  "Yet, there's no one to see me… react to my outburst… there's- no one- at all."

  show city_empty:
    animated_glitch("city_empty")
    matrixcolor InvertMatrix(1.0)
  with dissolve 

  "I messed up."

  cassian "I messed up…"

  show franz:
    xpos .1
    matrixcolor OpacityMatrix(0.4)
    animated_glitch("franz")
  with dissolve

  cassian "Franz..."

  show maike:
    xpos .5
    matrixcolor OpacityMatrix(0.4)
    animated_glitch("maike")
  with dissolve

  cassian "Maike..."

  cassian "Both... gone."
  
  scene cassian_crazy_2:
    xalign 0.5
    yalign 1.0
    animated_glitch("cassian_crazy_2")
    linear 10 zoom 1.3
  with Dissolve(2.0)

  cassian "I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up I messed up"

  # Fall sfx?

  scene black with fade

  "Losing the feeling in my legs I fall face down on the road."

  "It hurts, it hurts, but that doesn't matter, I don't want to care anymore."

  scene translocator_cg_4 with Dissolve(2.0)

  "This thing… is still in perfect condition, no scratches, and looks as if it's brand new even after all that."

  show city_empty with fade

  $ translocator_visible = True
  show screen translocator

  # Show Device
  # If something is entered, go to end other wise

  $ translocator_alarm(True)
  
  $ set_route("city_empty", None, None, "nightmare_ending")

  $ responses = [
      "This annoying, sound again...",
      "Is there even a point anymore?",
      "I might as well input something nonesensical and see what happens.",
      "..."
  ]
  while responses:
    "[responses.pop(0)]"

  $ translocator_visible = False
  pause 1.0
  hide screen translocator
  hide screen translocator_numpad

  cassian "......"

  scene black with fade
  pause 2.0
  jump alone_ending

  # If the device is ignored (Alone in World (3/4)

  return