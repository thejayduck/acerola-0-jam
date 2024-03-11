label scene_2:
  scene space_3:
    distort("space_3")
  play music "audio/bgm/warp_2.mp3" fadein 0.5 loop

  "A piercing screech tears through my skull, echoing like a band of whispers, from every corner of this place."
  "But, what just happened anyways…"
  "I can't see, I can barely think."

  cassian "..."

  "I try to scream in pain, but nothing comes out…"
  "I would gladly crack open my skull and tear out my brain to get rid of this sensation."
  "Not only that, it also feels as if I am moving around, unwillingly."
  "I try to look around, but my body feels like it's anchored to the ground with my eyes stitched shut."

  cassian "..."

  "I attempt to scream once again, knowing well it's futile. But my instincts tell me to do so."
  "What about the other two, Franz and Maike, where are they?"

  with hpunch
  "Argh, AAAAHHH!" with vpunch
  "The screech keeps assaulting me directly in my brain. Just where the hell is it coming from."
  "......"
  "I try to endure it with deep breaths, but the heavy air around me doesn't feel like it's entering my lungs, suffocating me."

  pause 3.0
  stop music fadeout 4.0 

  scene black with fade

  "The sound slowly dissipates, and I slowly gain the ability to control my body, once again."

  scene bedroom afternoon at nausea("bedroom afternoon", 3):
    blur 5
    xalign 0.5
    yalign 0.5
    ease 1.0 zoom 1.2
    ease 1.0 zoom 1.1
    repeat
  with dissolve 

  play music "audio/bgm/nightmare.mp3" fadein 1.0

  cassian "Arghhhhhh… Huff… Huff"

  "As soon as I wake up, I check all my body parts, and make sure each one of them functions as they should."

  cassian "Oh… I guess it was all a dream."

  cassian "A bad one."

  cassian "Where- Where am I?"

  "This time I can undoubtedly see, and feel my body for that matter."
  "I slowly observe my surroundings."
  
  scene bedroom afternoon with dissolve

  "This is my room, apartment number 27. A place where I live with Franz and hang out with Maike."
  "But why my room?"
  "I am pretty sure I've been at the fortune teller with Maike and Franz until a few minutes ago."

  cassian "H- ..."

  "I attempt to call out to Franz, but fail in the process."
  "My throat is so dry that my moving tongue hurts the insides of my mouth."
  "I force myself out of the bed and limp towards my door."

  scene living_room afternoon
  show maike afternoon:
    xpos .5
  show franz afternoon:
    xpos .1
  with fade

  # Door SFX
  play audio "audio/sfx/generic/door_open_room.mp3"

  maike "Oh? He finally got up. Good morning polar bear."

  show franz surprised

  franz "Damn it! What time is it?! I might still have a chance!" with hpunch

  show maike smirk crossed with dissolve

  maike "A chance? To think you were even close is insulting."

  maike "Let's see… hah~ 13:48, you certainly were 'close'."

  show franz sad

  franz "Awww~"

  "During their banter about a bet, I sneaked to the kitchen and drank 2 large cups of water."

  show franz normal hip with dissolve

  franz "Anyways, what did you do yesterday Cassian? It's rare for you to sleep for that long."

  show maike normal

  maike "...yeah."

  cassian "Huh? What are you two talking about, we've been together all day yesterday."

  show black with fade

  "I explained to them what had happened yesterday. But I kept the nightmare to myself."

  scene living_room afternoon
  show maike afternoon confused:
    xpos .5
  show franz sad hip afternoon:
    xpos .1
  with fade

  franz "Mystic's Fate Deceiving Properties? What does that even mean? A new mobile game?"

  cassian "What? Did you even listen to what I just said, you were the one to suggest that all three of us go there yesterday, the 13th."

  maike "You mean today?"

  "Huh?"

  cassian "No, no today's 14th isn't it?"

  maike "No, it's 13th."

  "..."

  "I check the time on my phone, thinking her might be out of sync."  
  
  # Audio looping
  $ loop = 0
  while loop < 2:
    $ renpy.play("audio/sfx/generic/phone_tap.mp3", "audio")
    pause renpy.random.uniform(0.5, 1.5)
    $ loop += 1

  cassian "Y-You are right..."

  show franz proud

  franz "Did waking up late finally start to mess with your head, and you guys keep telling me that I need to have a proper sleeping schedule."

  show maike tired crossed with dissolve

  maike "Your's is already messed up."

  show franz sad point with dissolve

  maike "Anyways, we haven't done anything today, not that we have time to waste our time. The assignment deadlines are nearing up."

  "This is weird… I am pretty sure we've been there."
  "No matter how much I tell my brain that it was probably just a dream, it doesn't accept it."
  "The two are completely oblivious to the events that just transpired. Or it just never happened to begin with."

  show franz happy

  franz "Never mind your dream, when are you planning to talk about that cool phone you are holding? Where'd you get it!?" with hpunch

  cassian "What phone are you even talking about? Mine's in my room."

  "Now that Franz mentioned it, I am holding onto something…"

  $ toggle_translocator(True)

  pause 2.0

  $ toggle_translocator(False)

  scene translocator_cg_1 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  "When did I pick it up?"
  
  scene translocator_cg_2 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  
  "How did I fail to realize it so far?"
  
  scene translocator_cg_3 with Dissolve(2.0)
  $ renpy.pause(1.5, hard=True)
  
  "Have I been holding onto it while drinking water too?"

  "A sudden surge of questions flooded my brain... unanswered."

  scene living_room afternoon
  show maike afternoon:
    xpos .5
  show franz afternoon happy hip:
    xpos .1
  with fade

  cassian "Since when did you realize it?"

  franz "Since the time you came out of your room of course. You can't hide that thing from me, can I use it now?"

  cassian "No! It's not a new phone. Just a project I am working on…" with hpunch

  "In truth, I have no clue what this is."

  $ toggle_translocator(True)

  "I take a closer look at it. The device seems simple. A tiny illuminated LCD screen, accompanied by a numpad, all connected with red wires."
  "A T9 layout, but with an addition—letters A, B, C, and D. Quite unusual from what the norm is."

  $ toggle_translocator(False)

  scene translocator_cg_1 with dissolve
  $ renpy.pause(0.5, hard=True)
  scene translocator_cg_2 with dissolve
  $ renpy.pause(0.5, hard=True)
  scene translocator_cg_3 with dissolve
  $ renpy.pause(0.5, hard=True)
  scene translocator_cg_1 with dissolve

  "How does this thing even power itself? "

  "Solar, perhaps? No, I don't see any panels for that…"

  #! Maybe invert colors?
  scene living_room afternoon
  show maike afternoon:
    xpos .5
  show franz afternoon happy hip:
    xpos .1
  with fade

  $ toggle_translocator(True)

  "I look at every side of the device and the only clue it has is the fact that the screen shows the number #725DD2."

  "What's that even mean…"

  "I better not play around with it."

  $ translocator_alarm(True)

  "Woah?! What was that..." with hpunch

  # Jumps to erased ending if device is used
  $ set_route("living_room afternoon", None, "erased_ending", "erased_ending")

  $ responses = [
      "The numbers on the device are... erased?",
      "Does it want me to write on it?",
      "No- I shouldn't do it without making sure what this thing is.",
      "..."
  ]
  while responses:
    "[responses.pop(0)]"

  $ can_input = False
  $ toggle_translocator(False)
  play sound "audio/sfx/put_down.mp3"

  "I stuff the device in my back pocket before the wolf hungry with curiosity gets his hands on it."

  hide screen translocator

  show franz annoyed

  franz "Hey hey, don't hide it now. Just give it to me for a while, I'll take care of it!"

  franz "Maike, say something to him."

  show maike tired

  maike "... I am busy."

  show franz sad

  scene black with Dissolve(1.0)

  "After Maike kills the conversation, I take out my laptop from my backpack and start working on my assignment."

  "Shortly after Franz, not to be left out joins us as well."

  #? Maybe night filter?
  scene living_room
  show maike tired:
    xpos .5
  show franz tired hip:
    xpos .1
  with fade

  play music "audio/bgm/casual_2.mp3"

  maike "Harrghh~"

  maike "I am done. What about you two."

  show franz proud point with dissolve

  franz "I am close to finishing it as well."

  "Not only Maike but also Franz as well?!"

  show maike:
    ease 1.0 xalign 0.45

  maike "..."

  show maike tired

  cassian "...and?"

  show maike smirk:
    xpos .6
  with ease

  maike "Only 257 words…"

  cassian "Of course."

  show franz annoyed

  franz "As if you did any more than I did Cassian!" with hpunch
  franz "How many words did you end up writing!" with hpunch

  "I did sit in front of my laptop to complete my assignment, but the device behind me has been eating my curiosity so much that I don't have a clue on what to write about."

  # Stomach sound
  play audio "audio/sfx/generic/stomach_grumble.mp3"

  cassian "..."

  show franz hip happy with dissolve

  franz "Ah! You couldn't write anything because you are hungry?"

  cassian "Yeah."

  franz "I know that feeling, my mind gets all fuzzy when I try to think on an empty stomach. What about you Maike, you hungry?"

  show maike normal crossed with dissolve

  maike "I was planning on eating leftovers from yesterday."

  show franz sad

  franz "Maike…"

  franz "That won't do, there's a new place in the city, and you decide to ignore it?!"
  
  franz"The reviews I read were all astonished by their food, let's all go together."

  cassian "Sure, I'll come along."

  maike "Eating out for once does sound nice… and the food isn't expensive, right? {nw}"

  show franz happy point with dissolve

  franz "Then it's decided! Come let's get ready Cassian."

  hide franz with moveoutleft
  pause 1.0
  play audio "audio/sfx/generic/door_close.mp3"

  scene bedroom night with dissolve

  "Franz shuts my laptop lid and forcefully pushes me inside my room, unable to contain his curious spirit."

  play audio "audio/sfx/generic/light_switch.mp3"
  scene bedroom with dissolve
  $ renpy.pause(1.0, hard=True)

  scene bedroom:
    xalign 0.3
    yalign 0.7
    ease 1.0 zoom 1.5
  play audio "audio/sfx/generic/lay_down.mp3"

  "I lay down on my bed."

  "I did agree to go with them, but I just can't stop thinking about the device."

  # Show device, you can input #! Decided not to make it input
  $ device_input = "725DD2"
  $ toggle_translocator(True)

  "It's a simple device really, nothing should happen even if I write anything on it…"

  "No, never mind."

  $ toggle_translocator(False)

  cassian "Ugh…"

  scene black with dissolve

  "I deeply sigh, get off my bed, and leave the device on my desk as a reminder for myself to look for information about it once I get back home."

  "I get out of my room, and enter the bathroom."

  scene bathroom with dissolve

  "There I see myself, did I look like this to them, that's not a way to present myself to them."
  
  scene bathroom:
    xalign 0.4
    yalign 0.1
    ease 1.5 zoom 1.5

  "Should've brushed my hair before I got out of the room when I woke up."

  "I get ready, and put on my jacket, calling out to my friends that I'm ready to leave."

  scene black with fade
  pause 3.0
  scene restaurant
  show franz happy hip at left
  show maike at right
  with fade

  franz "And this is the place!! Mr.{w=0} Romero's Italian Cuisine."

  "Franz stood proudly while pointing at the location that he had discovered. But isn't this place…"

  maike "I know this place …"

  cassian "T-This building is where that fortune teller was!?" with hpunch

  show franz sad

  franz "What are you talking about again, this place has been here since last week."

  show franz normal

  # Maike used to say this
  franz "It's a small business but has a large following on social media."

  show maike confused

  maike "mm~ yeah, our major even planned to go there with all the students after our term is over."
  
  maike "Pretty sure we talked about it together."

  cassian "R-really? Maybe I got the wrong place, haha~"

  franz "Let's go in already, I am about to die from starvation here."

  hide franz with dissolve
  hide maike with dissolve

  "Franz and Maike enter the place without a second thought."

  show restaurant:
    glitch("fortune_teller")
    xalign 0.5
    yalign 0.1
    ease 2.0 zoom 1.5
    pause 0.2
    "restaurant"

  "This is definitely the place where that fortune teller was, no doubt about it. But there's no sign of it… "

  show restaurant:
    glitch("warp_1")
    pause 0.5
    "restaurant"

  # Screech for a split second
  play music "audio/bgm/warp_2.mp3"
  pause 0.5
  stop music fadeout 1.0

  cassian "But maybe it's just my imagination."

  "I try to reassure myself, but the doubt lingers throughout my body and mind, refusing to let me go inside."

  show restaurant:
    ease 2.0 zoom 1.0
  pause 2.0

  play music "audio/bgm/casual_2.mp3"
  show franz proud at center with dissolve

  franz "Don't worry, the food is cheap here, you won't have to worry about running short on money."

  cassian "Huh?"

  scene black with fade

  "Franz pulled me inside with a dumb remark, that has nothing to do with my worries."

  "But… thanks to him I managed to go inside the restaurant. And enjoy a nice meal."

  scene living_room night with fade

  cassian "Hrrghh~ ahh~"

  show franz night at center with dissolve
  pause 0.4
  show franz tired with dissolve

  franz "You slept all day and still tir- Hrrgghhh~"

  cassian "Haha~ I guess we both are tired."

  show franz proud

  franz "Well eating requires a lot of exercise, of course, I would get tired."

  "Franz and I stretch our stiff bodies at the same time"

  "One was tired from eating a lot of food and doing a minimal amount of assignment work, and I on the other hand tired from thinking about the mismatching memories."

  "We saw Maike off to her apartment before entering ours, she should be tired from writing and arguing with us all day."

  cassian "Anyways, good night, I don't think I can handle any more social or physical activity today."

  franz "Same! Good night."

  "We both part aways to our rooms."

  stop music fadeout 3.0
  scene black with fade
  pause 3.0

  # Translocator going off
  play sound "audio/sfx/lightning.wav" volume 0.5 loop
  show lightning onlayer lightning

  "......"

  cassian "What the hell?!"

  scene bedroom night
  show franz night surprised at center
  with fade

  "I see Franz in my room, playing around with the device that I tried to hide from him."

  franz "Aaah~ I am sorry, I just couldn't fall asleep thinking about it!"

  "I shouldn't have left it on my desk, damn it!"

  # Screech BGM
  # Blurry Background

  "The world around me starts to twirl and twist in unnatural ways, as I lose consciousness once again."

  $ active_background = "bedroom night"
  $ confirm_input("scene_3", "341FC2")

  return