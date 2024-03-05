# Others
define config.speaking_attribute = "speaking"
define config.say_attribute_transition = dissolve

define narrator = Character(ctc="ctc_indicator", ctc_position="nestled")
# Main Characters
define cassian = Character("Cassian", color="#fff2f2", what_slow_cps=25)
define maike = Character("Maike", color="#fd9432", image="maike", what_slow_cps=20)
define franz = Character("Franz", color="#c96d6d", image="friend2", what_slow_cps=30)

# Side Characters
define fortune_teller = Character("Suspicious Guy", color="#6e2b2b", what_slow_cps=15)

image ctc_indicator:
    xysize(24,24)
    yalign 1.4
    xanchor -0.3
    "effects/ctc100.png"
    linear 0.5 alpha 0.0
    "effects/ctc100.png"
    linear 0.5 alpha 1.0
    repeat