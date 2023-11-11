from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W.........................................W',
    'W.........................................W',
    'W.........................................W',
    'W.........................................W',
    'W........B..........GGGGG.................W',
    'W........B..............G....OOOOG........W',
    'W........B..............G.....OOOOG.......W',
    'W........B..............G......OOOG.......W',
    'W...........................OOOOOO........W',
    'W.............................OOOOOO......W',
    'W..............................GOOO.......W',
    'W...............................GGG.......W',
    'W......BBBBBBB...BBB...WWWW...............W',
    'W.........................................W',
    'W.........................................W',
    'W.OOOO....................................W',
    'WOOOOOO.O............................W....W',
    'WOOOOOOOOOO..........................W....W',
    'WOOOOOOO.............................W....W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

# text_map = [
    # ''.join('W' for i in range(WIDTH//TILE)),
    # ''.
    # ''.join('W' for i in range(WIDTH//TILE)),
# ]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char in TEXTURES.keys():
            world_map.add((i * TILE, j * TILE, char))