label erased_ending:
  scene space_3:
    distort("space_3")
  with fade
  play music "audio/bgm/warp_2.mp3" fadein 0.5 loop

  "Erased from Existence (1/4)"
  $ MainMenu(confirm=False)()

label fake_reality_ending:
  scene black with fade
  "I managed to go back..."
  "To a place that I don't fit in..."

  "Stranger in #725DD2 (2/4)"
  $ MainMenu(confirm=False)()

label alone_ending:
  "All alone in #313600 (3/4)"
  $ MainMenu(confirm=False)()

label nightmare_ending:
  scene space_3:
    distort("space_3")
  with fade
  play music "audio/bgm/warp_2.mp3" fadein 0.5 loop

  cassian "..." 

  cassian "..."

  "It's hard to breathe, and it feels as if no matter how hard I try nothing fills up my lungs."
  "Argh… the screeching again…"
  "I want it to end, I want to stop my body from hearing this…"
  "But alas, I can't."
  "I should've just… not touched that crap to begin with."
  "I will probably wake up in another world anyway…"

  "Lost in Time and Space (4/4)"
  $ MainMenu(confirm=False)()