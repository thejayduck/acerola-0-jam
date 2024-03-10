label mess_up:
  scene bedroom:
    parallel:
      function WaveShader(amp=1, period=3.495, direction="vertical", double="horizontal")
  with dissolve
  
  "Don't mess up."
  $ MainMenu(confirm=False)()

label fake_reality:
  "Somewhere you dont belong."
  $ MainMenu(confirm=False)()

label alone:
  "alone in world"
  $ MainMenu(confirm=False)()

label lost:
  "lost in time and space."
  $ MainMenu(confirm=False)()