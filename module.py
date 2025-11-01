from __builtins__ import *
# 各種共通関数を定義します。

# ------------------------------------------------------------ #
# 座標を指定した移動関数です。最短ルートで移動します。
# ------------------------------------------------------------ #
def move_to (
    nx # 移動先X座標
  , ny # 移動先Y座標
  , px = get_pos_x() # 移動元X座標
  , py = get_pos_y() # 移動元Y座標
  , ws = get_world_size() # ワールドサイズ
  , hs = get_world_size() // 2 # ワールドサイズの半分
):

  # 東西
  if nx != px:
    k = (nx - px) % ws
    if k <= hs:
      for _ in range(k):
        move(East)
    else:
      for _ in range(ws - k):
        move(West)

  # 南北
  if ny != py:
    k = (ny - py) % ws
    if k <= hs:
      for _ in range(k):
        move(North)
    else:
      for _ in range(ws - k):
        move(South)
