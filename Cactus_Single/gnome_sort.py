from module import *

# シミュレーション
# simulate("f0", { Unlocks.Expand: 5, Unlocks.Cactus: 6, Unlocks.Plant: 1, Unlocks.Speed: 5 }, { Items.Pumpkin : 1000000000, Items.Power : 1000000000 }, {}, -1, 1)

# リーダーボード
# leaderboard_run(Leaderboards.Cactus_Single, "f0", 10000)

# 指定セルを処理します。
def do_cactus_cell(x, y, ws):

  # 移動
  move_to(x, y)

  # 植える
  till()
  plant(Entities.Cactus)

  # 並び替え
  while True:

    # 今回の並び替えを初期化
    is_swap = False
    max_measure = measure()
    swap_way = None
    x = get_pos_x()
    y = get_pos_y()

    # 南側を検証
    ck = measure(South)
    if y > 0 and ck > max_measure:
      max_measure = ck
      swap_way = South
    
    # 西側を検証
    ck = measure(West)
    if x > 0 and ck > max_measure:
      max_measure = ck
      swap_way = West
    
    # 並び替えが不要
    if swap_way == None:
      break
    
    # 並び替え
    swap(swap_way)

    # 次のセルへ移動
    move(swap_way)

# サボテンを１面分処理します。
def do_cactus(ws = get_world_size()):

  # 各種値を設定
  range_list = range(ws)

  # 植えながら並び替える
  for x in range_list:
    for y in range_list:
      do_cactus_cell(x, y, ws)

  # 収穫
  while not can_harvest():
    continue
  harvest()

# 実行
do_cactus()
