# Others
# define config.speaking_attribute = "speaking"
define config.say_attribute_transition = dissolve

# Characters
define narrator = Character(ctc="ctc_indicator", ctc_position="nestled-close")
define cassian = Character("Cassian", color="#fff2f2", what_slow_cps=25)
define maike = Character("Maike", color="#fd9432", image="maike", what_slow_cps=20)
define franz = Character("Franz", color="#68815E", image="franz", what_slow_cps=30)

define notification = Character("Notification", color="#53c5c5", what_prefix="> ")

image ctc_indicator:
    xysize(24,24)
    yalign 1.4
    xanchor -0.3
    "effects/ctc100.png"
    linear 0.5 alpha 0.0
    "effects/ctc100.png"
    linear 0.5 alpha 1.0
    repeat

transform night_color:
    matrixcolor TintMatrix('#7986c0') * BrightnessMatrix(0.1)

transform night_color_darker:
    matrixcolor TintMatrix('#475386') * BrightnessMatrix(0.1)

transform afternoon_color:
    matrixcolor TintMatrix('#ffe4a97a')

image franz night = LayeredImageProxy("franz", night_color)
image franz afternoon = LayeredImageProxy("franz", afternoon_color)

image maike night = LayeredImageProxy("maike", night_color)
image maike afternoon = LayeredImageProxy("maike", afternoon_color)

image living_room night:
    "living_room"
    night_color

image living_room afternoon:
    "living_room"
    afternoon_color

image bedroom night:
    "bedroom"
    night_color_darker

image bedroom afternoon:
    "bedroom"
    afternoon_color

image restaurant afternoon:
    "restaurant"
    afternoon_color
#! add colors for afternoon! especially for scene_2 living_room