from module import *

# シミュレーション
# simulate("f0", { Unlocks.Expand: 5, Unlocks.Cactus: 6, Unlocks.Plant: 1, Unlocks.Speed: 5 }, { Items.Pumpkin : 1000000000, Items.Power : 1000000000 }, {}, -1, 1)

# リーダーボード
# leaderboard_run(Leaderboards.Cactus_Single, "f0", 10000)

# サボテンを並び替えられているかチェックします。
def is_swapped(measures, x, y, ws):

  # 初期化
  world_border = ws - 1

  # 北側を検証
  if y < world_border and measures[x][y] > measures[x][y + 1]:
    return False
  
  # 南側を検証
  if y > 0 and measures[x][y] < measures[x][y - 1]:
    return False
  
  # 東側を検証
  if x < world_border and measures[x][y] > measures[x + 1][y]:
    return False
  
  # 西側を検証
  if x > 0 and measures[x][y] < measures[x - 1][y]:
    return False

  # 検証結果を返す
  return True

# サボテンを並び替えます。
def swap_cactus(measures, x, y, ws):

  # 初期化
  world_border = ws - 1
  is_swap = True

  # 並び替え
  while is_swap:

    # 今回の検証を初期化
    is_swap = False

    # 北側を検証
    if y < world_border and measures[x][y] > measures[x][y + 1]:
      is_swap = swap(North)
      measures[x][y] = measure()
      measures[x][y + 1] = measure(North)
    
    # 南側を検証
    if y > 0 and measures[x][y] < measures[x][y - 1]:
      is_swap = swap(South)
      measures[x][y] = measure()
      measures[x][y - 1] = measure(South)
    
    # 東側を検証
    if x < world_border and measures[x][y] > measures[x + 1][y]:
      is_swap = swap(East)
      measures[x][y] = measure()
      measures[x + 1][y] = measure(East)
    
    # 西側を検証
    if x > 0 and measures[x][y] < measures[x - 1][y]:
      is_swap = swap(West)
      measures[x][y] = measure()
      measures[x - 1][y] = measure(West)

  return measures

# サボテンを１面分処理します。
def do_cactus(ws = get_world_size()):

  # 各種値を設定
  range_list = range(ws)

  # 植える
  measures = {}
  for x in range_list:
    tmp = {}
    for y in range_list:
      till()
      plant(Entities.Cactus)
      tmp[y] = measure()
      move(North)
    measures[x] = tmp
    move(East)
  
  # 並び替える
  while True:

    # 並び替える
    is_swap = False
    for x in range_list:
      for y in range_list:
        if not is_swapped(measures, x, y, ws):
          is_swap = True
          move_to(x, y)
          measures = swap_cactus(measures, x, y, ws)
    
    # 並び替えが行われなかったら終了
    if not is_swap:
      break
  
  # 収穫する
  harvest()

# 実行
do_cactus()
