label scene_3:
  "..."

  cassian "Ah!"

  scene bedroom at nausea("bedroom", 3):
    blur 5
    xalign 0.5
    yalign 0.5
    ease 1.0 zoom 1.2
    ease 1.0 zoom 1.1
    repeat
  with dissolve 

  "I gain consciousness once again."

  cassian "Urk!"

  "A sour taste rose in my throat, and I tried to swallow it unwillingly so as not to make a mess in my room."

  "I got out of my bed, my limbs feel as if they are jelly and my head feels like it was used as a football."

  "Feeling another rush of acidic taste coming I stumble towards the bathroom." with hpunch

  # Run SFX
  play audio "audio/sfx/generic/running.mp3"

  scene bathroom at nausea("bathroom", .5):
    blur 5
  with dissolve 

  "I rush inside without a second thought and fall to my knees before the toilet."

  "Without warning, the contents of my stomach surged upwards, and I retched violently, emptying my insides into the bowl."

  cassian "Bleerrghh!" with hpunch

  #! Vomit SFX

  scene bathroom with dissolve

  "Right after getting the sour bile out of my system, the nauseousness fades away, as if it were never there to begin with, but the scene is still is caused was still apparent."

  cassian "Was it all because of the food we ate yesterday."

  cassian "Is Franz okay?"

  "Worried, I go ahead and check up on him."

  play audio "audio/sfx/generic/running.mp3"
  scene hallway_2 with fade

  cassian "......"

  cassian "The- the door… is gone?"
  
  play audio "audio/sfx/generic/hit_wall.mp3"
  $ renpy.pause(2.0, hard=True)
  "What?{w} How?{w} Why?{w} When?{w}"

  show hallway_2:
    xalign 0.15
    yalign 0.1
    ease 1.5 zoom 1.5

  "Once again, something is not right, just like yesterday…"

  "I touch the walls, try to scrape the paint. To hell with the landlord, my friend is locked behind a door that's shut with concrete."

  show hallway_2:
    ease 1.0 xalign 0.8
    ease 1.0 yalign 0.4
    ease 1.5 zoom 1.3
  "But, there's nothing. No passage, just pure concrete wall."

  show hallway_2:
    ease 1.0 zoom 1.0

  cassian "What about his belongings?"

  show living_room with Fade(0.2, 0.2, 0.2)

  play audio "audio/sfx/generic/running.mp3"

  "I run towards the living room…"

  show living_room:
    ease 1.1 zoom 1.5 ypos 1200

  "N-Nothing!"

  cassian "Aahahaha…"

  show living_room:
    ease 1.5 zoom 1 ypos 1080

  "As I keep looking around every nook and cranny, I get more nervous, it's as if his existence has been erased. Not a single part of him is left."

  "His- His contact, I should still have it."

  # Audio looping
  $ loop = 0
  while loop < 5:
    $ renpy.play("audio/sfx/generic/phone_tap.mp3", "audio")
    pause renpy.random.uniform(0.5, 1.5)
    $ loop += 1
  
  "I look at our chat groups, call history, messages we sent to each other over the years…"

  cassian "All gone…"

  "..."

  "It's hard to breathe, the sour taste left in my mouth doesn't help with anything either."

  play sound "audio/sfx/phone.ogg"

  cassian "Is it Franz?" with hpunch

  play sound "audio/sfx/generic/phone_tap.mp3"

  notification "Are you home? I am outside your door.\n - Maike 12:07 PM"

  cassian "Oh, she's safe. Maybe she knows something."

  scene living_room
  show maike at center
  with Fade(2.0, 2.0, 2.0)

  # "After reading the notification I wash my face real fast and greet Maike waiting in front of my door with all her documents. "

  cassian "What brings you here today, I thought you were done with your assignment already?"

  maike "What makes you think that I was already done? Didn't we both agree to meet and finish it together today?"

  cassian "When did we agree on that?"

  show maike tired

  maike "Urgh- Are you planning to leave this assignment until the last day, and get a barely passing grade again?"

  cassian "No- I… I am pretty sure we made some progress yesterday, I even started writing it."

  "I get my laptop under the piles of grocery store listings and open up my documents folder."

  maike "So where's your 'progress'."

  cassian "It was right here, I had written some parts of it!"

  cassian "But then Franz suggested that we go to a restaurant called Romero's, where we spent the entire day eating after working on our project!"

  "I look at Maike again to get a reaction out of her but she looks, puzzled."

  maike "Cassian, who exactly is Franz? A friend of yours?"

  # show living_room:
  #   matrixcolor InvertMatrix(1.0)
  # show maike:
  #   matrixcolor InvertMatrix(1.0)
  # with dissolve
  
  cassian "What…"

  cassian "I told you we all went to that restaurant yesterday, you two don't really get along well, but we always hang out here, together."

  maike "I had lectures all day yesterday, I didn't have time to go outside, not even once!"

  "What is she talking about, who is Franz? Obviously, the idiot that dyed his hair because his barber insisted that it would look good on him."

  show franz:
    matrixcolor OpacityMatrix(0.4)
    animated_glitch("franz")
  with dissolve

  "The person that all three of us hung out with for the past 3 years, almost every single day."

  hide franz with dissolve

  "I grab Maike by her shoulders, and draw her near to my face, maybe she is trying to get a laugh out of me."

  show maike tired crossed with dissolve

  maike "Hey, stop it!"

  "She tries to get away from my grip, but fails."

  scene maike_cg_1 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)

  cassian "What do you mean you have never heard about that name?!" with hpunch

  cassian "We've been gathering at my place almost every day, spending time, laughing, playing games, and doing dumb activities that he kept forcing us to." with vpunch

  "I unconsciously tighten my grip around her shoulder."

  maike "Oww~ What's gotten into you, calm down!"

  cassian "How can I-"

  cassian "How can I calm down, when even yesterday, you two forgot about what happened on the 13th, and today, Franz isn't here out to hide from me and you came here to make fun of me saying stupid stuff like 'Who's Franz?'!"

  cassian "If it's just a joke just say so!" with hpunch

  maike "There's no room for someone else at your place, this is a single-room apartment."

  "Now that she mentioned that, I couldn't find his door, nor belongings no matter where I looked. His contacts were also erased from my phone."

  scene maike_cg_2 with vpunch
  $ renpy.pause(1.5, hard=True)

  "I loosen my grip just enough for Maike to gain some distance away from me, and rush towards the door."

  scene living_room
  show maike scared at center:
    xzoom -1.0
  with fade

  cassian "No, wait! Let me explain again!"

  maike "I-I'm sorry… I have to go."

  hide maike with moveoutright

  # Running & Door Close SFX
  play audio "audio/sfx/generic/running_away.mp3"
  $ renpy.pause(3.0, hard=True)
  play audio "audio/sfx/generic/door_close_fast.mp3"

  scene black with Fade(0.2, 0.2, 0.2)

  pause 1.5

  "After a minute of looking at the ground, the adrenaline from interrogating Maike, wears off."

  scene living_room:
    nausea("living_room", 0.2)
  with dissolve

  "I just woke up but my body already feels heavy, wanting me to sleep."

  cassian "Maybe tomorrow..."

  cassian "I'll wake up from this."

  scene bedroom:
    nausea("bedroom", 0.2)
  with dissolve

  cassian "Oh right, didn't Franz play with the device yesterday, it's still where I left it."

  $ toggle_translocator(True)

  cassian "Weird, the number on the LCD changed to #341FC2"

  cassian "I still have no clue on what that means."

  $ translocator_alarm(True)
  
  $ set_route("bedroom", "725DD2", "fake_reality_ending", "erased_ending")

  "It's beeping like it did previously..." with hpunch

  $ responses = [
      "What was the previous number again?",
      "Stuff happened when Franz did something to the device.",
      "...Is that why he isn't here anymore?",
      "I remember the same sensation in that fortune teller as well…",
      "But back then I didn't have the device.",
      "Maybe I should enter a number…"
  ]
  while responses:
    "[responses.pop(0)]"

  # Ending 2/4 (Fake Reality) if the player enters the number from the previous world line.

  $ toggle_translocator(False)

  "No, that would be dumb, what if I lose Maike as well?"

  "I'll be left all alone."

  cassian "But… What if writing something can end this nightmare? It's just a few key presses."

  "But do you even know how this thing works? What do these numbers stand for anyway?"

  cassian "T-That doesn't matter, it's already mysterious enough for this contraption to work without a power source."

  cassian "Maybe it won't work at all."

  "Won't work after what happened for the past few days… I am not sure about that."

  "My body and mind wouldn't listen to me, it's as if I am not myself, but in someone else's body, just temporarily controlling it."

  scene black with fade

  cassian "..."

  "How long has it been?"

  cassian "......"

  "A few minutes, hours? I don't even know anymore."

  # Door Knocking SFX
  play audio "audio/sfx/generic/door_knock_distant_3.mp3"
  pause 1.0

  "I don't want to answer."

  # Door Bell
  play audio "audio/sfx/generic/doorbell_distant.mp3"
  pause 1.0

  "Just leave me alone."

  # Door Open & Steps Coming Closer
  play audio "audio/sfx/generic/door_open_distant.mp3"
  $ renpy.pause(1.0, hard=True)
  play audio "audio/sfx/generic/walk_towards.mp3"
  $ renpy.pause(6.0, hard=True)
  play audio "audio/sfx/generic/door_open_room.mp3"
  pause 1.0
  play audio "audio/sfx/generic/light_switch.mp3"

  cassian "Huh-"

  cassian "..."

  # Bed Sheets
  play audio "audio/sfx/generic/bedsheets.mp3"

  scene bedroom:
    matrixcolor BrightnessMatrix(.65)

  show maike at center:
    matrixcolor BrightnessMatrix(0.65)
  with fade

  cassian "Argh-"

  "The sudden change in lighting burns my eyes."

  "I try blinking several times, to get used to it."

  scene bedroom:
    ease 0.5 matrixcolor BrightnessMatrix(0.65)
    ease 1.0 matrixcolor BrightnessMatrix(0)
  
  show maike at center:
    ease 0.5 matrixcolor BrightnessMatrix(0.65)
    ease 0.5 matrixcolor BrightnessMatrix(0)

  cassian "... Weren't you going to call for help? Why are you back."

  #! Show Maike worried
  show maike worried

  maike "I lied about that part, I couldn't bring myself to call someone without seeing how you were doing again."

  maike "You look worse than you did this morning… Are you still confused?"

  cassian "I- I am not confused, it's just that…"

  scene black with fade

  "I explain everything that has transpired so far, about the Fortune Teller we visited."
  "How Franz and Maike's memories weren't matching mine."
  "The disappearance of Franz and the change in the apartment interior."
  "Everything… feeling off…"

  scene bedroom

  show maike confused at center
  with fade

  maike "This… You are not joking are you…"

  "I vigorously shake my head from side to side, a clear declaration of refusal. And look at her with a tired face."

  maike "It doesn't sound like a made-up story, everything you talked about sounds real, yet I can't recall any of it."

  "Ah right, I didn't show her the device yet, she might remember that."

  $ device_input = "341FC2"
  $ can_input = False
  $ toggle_translocator(True)

  cassian "Ever seen this device? I showed this to you and Franz yesterday."

  maike "No, sorry."

  "Right, as expected."

  $ toggle_translocator(False)

  maike "Have you tried messing with the device? Entering a number, or taking it apart?"

  cassian "How could I?! I have no clue what the numbers on the screen mean, and every time something goes wrong, the number on the device changes."

  cassian "I- I don't want to break what I have already."

  "But- I do want to-"

  show maike normal crossed with dissolve

  maike "But you probably want to go back to how things were."

  "She did it again, reading my mind like an esper… haha~"

  cassian "What if it gets worse? And you forget about me as well?"

  show maike crossed smirk

  maike "Then… I swear I'll find you on the other side as well, and deal with this thing together."

  "An empty promise, but it makes me feel safe and confident."

  cassian "Any ideas on what I should write?"

  show maike tired

  maike "Hmm~ Good question…"

  maike "How about the numbers that correlate with our initials, including that other guy."

  cassian "So that that would be…"

  maike "3136 and maybe double 0 at the end, #313600"

  cassian "I guess that's better than not having any ideas…"

  "Now I just need to write #313600 on the device."

  $ set_route("bedroom", "313600", "scene_4", None)

  $ toggle_translocator(True)
  pause 3.0
  $ toggle_translocator(False)

  maike "Aren't you going to write anything?"

  cassian "It's just that... thank you Maike."

  cassian "I would've probably stayed at a place I didn't want to if not for you."

  "I give my goodbye to the Maike here, knowing full well, this scene will not be remembered by her."

  "It's kinda sad really, being the only one to know what's about to happen."

  show maike smirk

  maike "You're welcome, Cassian."

  $ force_input("313600")

  return