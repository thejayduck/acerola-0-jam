image friend1_talk:
  "chara/friend1/mouth_closed.png"
  .2
  "chara/friend1/mouth_mid.png"
  .2
  "chara/friend1/mouth_open.png"
  .2
  "chara/friend1/mouth_closed.png"
  .2
  repeat 3

layeredimage friend1:
  group base:
    attribute base default:
      "chara/friend1/base.png"
  group pose:
    attribute hip default:
      "chara/friend1/pose_1.png"
    attribute crossed:
      "chara/friend1/pose_2.png"
  group mouth:
    attribute normal default:
      "chara/friend1/mouth_closed.png"
    attribute speaking:
      "friend1_talk"

    
      
