layeredimage franz:
  group base:
    attribute normal default:
      "chara/franz/base/default.png"
    attribute happy:
      "chara/franz/base/happy.png"
    attribute sad:
      "chara/franz/base/sad.png"
    attribute surprised:
      "chara/franz/base/surprised.png"
    attribute tired:
      "chara/franz/base/tired.png"
    attribute annoyed:
      "chara/franz/base/annoyed.png"
    attribute proud:
      "chara/franz/base/default.png"
  group pose:
    attribute point default:
      "chara/franz/pose_1.png"
    attribute hip:
      "chara/franz/pose_2.png"
  group eyes:
    attribute normal default:
      "franz_default"
    attribute happy:
      "chara/franz/e_happy.png"
    attribute sad:
      "chara/franz/e_closed.png"
    attribute surprised:
      "franz_default"
    attribute tired:
      "chara/franz/e_closed.png"
    attribute annoyed:
      "franz_annoyed"
    attribute proud:
      "franz_annoyed"

image franz_default:
  "chara/franz/e_default.png"
  choice:
    2.0
  choice:
    3.1 
  choice:
    4.2
  choice:
    3.3
  "chara/franz/e_closed.png"
  .13
  repeat

image franz_annoyed:
  "chara/franz/e_gaze.png"
  choice:
    2.0
  choice:
    3.1 
  choice:
    4.2
  choice:
    3.3
  "chara/franz/e_closed.png"
  .13
  repeat
