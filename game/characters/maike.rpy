layeredimage maike:
  group base:
    attribute normal default:
      "chara/maike/base/default.png"
    attribute scared:
      "chara/maike/base/scared.png"
    attribute smirk:
      "chara/maike/base/smirk.png"
    attribute tired:
      "chara/maike/base/tired.png"
  group pose:
    attribute hip default:
      "chara/maike/pose_1.png"
    attribute crossed:
      "chara/maike/pose_2.png"
  group eyes:
    attribute normal default:
      "maike_default"
    attribute scared:
      "maike_scared"
    attribute smirk:
      "maike_smirk"
    attribute tired:
      "maike_tired"

image maike_default:
  "chara/maike/e_default.png"
  choice:
    2.0
  choice:
    3.1 
  choice:
    4.2
  choice:
    3.3
  "chara/maike/e_closed.png"
  .13
  repeat

image maike_scared:
  "chara/maike/e_scared.png"
  choice:
    2.0
  choice:
    3.1 
  choice:
    4.2
  choice:
    3.3
  "chara/maike/e_closed.png"
  .13
  repeat

image maike_smirk:
  "chara/maike/e_tired.png"
  choice:
    2.0
  choice:
    3.1 
  choice:
    4.2
  choice:
    3.3
  "chara/maike/e_closed.png"
  .13
  repeat

image maike_tired:
  "chara/maike/e_tired.png"
  choice:
    2.0
  choice:
    3.1 
  choice:
    4.2
  choice:
    3.3
  "chara/maike/e_closed.png"
  .13
  repeat