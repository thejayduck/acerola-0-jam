label erased_ending:
  scene space_3:
    distort("space_3")
  with fade
  play music "audio/bgm/warp_2.mp3" fadein 0.5 loop

  "Erased from Existence (1/5)"
  $ MainMenu(confirm=False)()

label wrong_number:
  scene space_3:
    distort("space_3")
  with fade
  play music "audio/bgm/warp_2.mp3" fadein 0.5 loop

  "So that wasn't the previous number... huh?"
  "Wrong Number (2/5)"
  $ MainMenu(confirm=False)()

label fake_reality_ending:
  scene living_room:
    matrixcolor TintMatrix('#323246') * BrightnessMatrix(0.2)
  show maike:
    xpos 0.5
    matrixcolor TintMatrix('#1d1d1f') * BrightnessMatrix(0.1)
  show franz:
    xpos 0.1
    matrixcolor TintMatrix('#1d1d1f') * BrightnessMatrix(0.1)
  with fade

  "I managed to go back..."
  "To a place that I don't fit in..."
  "Stranger in #725DD2 (3/5)"
  scene black with fade
  pause 0.2
  $ MainMenu(confirm=False)()

label nightmare_ending:
  scene space_3:
    distort("space_3")
  with fade
  play music "audio/bgm/warp_2.mp3" fadein 0.5 loop

  cassian "..." 

  cassian "..."

  "It's hard to breathe, and it feels as if no matter how hard I try nothing fills up my lungs."
  "Argh… the screeching again…" with hpunch
  "I want it to end, I want to stop my body from hearing this…"
  "But alas, I can't."
  "I should've just… not touched that crap to begin with."
  "I will probably wake up in another world anyway…"

  "Lost in Time and Space (4/5)"
  $ MainMenu(confirm=False)()

label alone_ending:
  scene city_empty:
    matrixcolor TintMatrix('#323246') * BrightnessMatrix(0.2)
  with fade

  "All Alone in #313600 (5/5)"
  $ MainMenu(confirm=False)()