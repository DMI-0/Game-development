import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 87, 51)
YELLOW = (255, 200, 50)
GRAY = (204, 204, 204)
GRASS = (0, 92, 8)
SKY = (33, 174, 255)
NIGHT = (35, 2, 82)
SUN = (255, 220, 56)
SET = (254, 76, 21)
MOON = (211, 211, 211)
PINK = (224, 43, 185)
BRI_YELLOW = (229, 255, 0)
BRI = (230, 205, 46)
DARK_RED = (102, 0, 0)
SPD = 3
IDK = [200, 970]
s_loc = [50, 160]
n1 = [10, 10]
x_speed = 0
score = 0
score_speed = 1
day_night = random.choice([SKY, NIGHT, SET])
COLOR = random.choice([WHITE, YELLOW])
FPS = 60
resets = 0

GRAVITY = 1



#[ 
    # '1111111111111111111111111',
    # '12                      1',
    # '1                    U  1',
    # '1                       1',
    # '1                       1',
    # '1        U              1',
    # '1               U       1',
    # '1    U                  1',
    # '1                       1',
    # '1           U           1',
    # '1                     1 1',
    # '1           3E          E',
    # '1      3               11',
    # '1    3    3     3  * *  1',
    # '1P *                    1',
    # '114                     1',
#]
start_screen = [
    '1111111111111111111111111',
    '14                      1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1P              2       1',
    '111111111111111 111111111',
    '1j             2        1',
    '1111111111111111111111111'
]

outline = [
    '1111111111111111111111111',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1P            2         1',
    '1111111111111111111111111'
]

# LAYOUT2 = [
#     '1111111111111111111111111',
#     '1  1                    1',
#     '1  1                    1',
#     '1P G                    1',
#     '1111                    1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1                       1',
#     '1P            2         1',
#     '1111111111111111111111111'
# ]

# G for gate
# 6 for sideways
LAYOUT = [
    '1111111111111111111111111',
    '14                     i1',
    '1                       1',
    '1                       1',
    '1  P                    1',
    '1  111                  1',
    '1                       1',
    '1        1 1            1',
    '1       >1 1            1',
    '1   111111 1            1',
    '1  <    > 5             1',
    '1  1111111111           1',
    '1j                      1',
    '11 1 1 1 1 1 1 1 1 1 11G1',
    '1 1 1 1 1 1 1 1 1 1 1  21',
    '1111111111111111111111111'
]
# print(len(LAYOUT[0]), len(LAYOUT))
BRICK_WIDTH = 50
big_width = 200
BRICK_HEIGHT = 50
PLAYER_WIDTH = 35
PLAYER_HEIGHT = 35
WIDTH = BRICK_WIDTH * len(LAYOUT[0])
HEIGHT = BRICK_HEIGHT * len(LAYOUT)
# print(WIDTH)
# 1250
wid = 25
hid = 25
frewid = 15
frehid = 15
ENEMY_WIDTH = 40 
ENEMY_HEIGHT = 40
slime_width = 50
slime_height = 50

test = 250

width = BRICK_WIDTH * len(LAYOUT[0])
height = BRICK_HEIGHT * len(LAYOUT)

# print(WIDTH)
# print(HEIGHT)

# print(LAYOUT[10])



LEVEL_1 = [
    '1111111111111111111111111',
    '12                      1',
    '1111                    1',
    '11        1111          1',
    '1    1           1      1',
    '111                  11 1',
    '111111                  1',
    '1                      11',
    '1                       1',
    '1                     111',
    '1          1111  11     1',
    '1    11111              1',
    '1                       1',
    '1        111111         1',
    '1P                     E1',
    '1111111111111111111111111',
]

LEVEL_2 = [
    '1111111111111111111111111',
    '12                      1',
    '1                       1',
    '1                       1',
    '1  1       1            1',
    '1  1   1       1        1',
    '1                       1',
    '1           1           1',
    '1                       1',
    '1              1        1',
    '1                 E     1',
    '1              111      1',
    '1            1          1',
    '1              1        1',
    '1P                     E1',
    '1111111111111111111111111',
    ]

LEVEL_3 =[
    '1111111111111111111111111',
    '1                       1',
    '1        11111  3 3 11  1',
    '1       1             1 1',
    '1     3                 1',
    '1        3 3 3 3      121',
    '1                       1',
    '1        E      3       1',
    '1         3 3 3         1',
    '1     1                 1',
    '1  1                    1',
    '1           1   E       1',
    '1P    1  1     1        1',
    '1                 1     1',
    '1                      E1',
    '1111111111111111111111111',
]

LEVEL_4 = [
    '1111111111111111111111111',
    '1                       1',
    '1          3 31         1',
    '1        3    1         1',
    '1      3      1   11    1',
    '1   3         1E      111',
    '1 E    3   3  1  11     1',
    '1            31     11  1',
    '1            E1         1',
    '1      11111111  11     1',
    '1      1                1',
    '1    3 1                1',
    '1     E1                1',
    '1P 11111                1',
    '11112 EF      E   E   F 1',
    '1111111111111111111111111',
]

LEVEL_5 =[
    '1111111111111111111111111',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1               111    21',
    '1           11      111 1',
    '1        1              1',
    '1         F1F           1',
    '1              111      1',
    '1         1F1           1',
    '1       11              1',
    '1    111                1',
    '1P                      1',
    '1111111111111111111111111',
]

LEVEL_6 = [
    '1111111111111111111111111',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1                       1',
    '1              E        1',
    '1     3 1     3 3 3 3   1',
    '12        3             1',
    '1     F              11E1',
    '1    E       1   1E1    1',
    '1       3  3            1',
    '1     1                 1',
    '1   F   3               1',
    '1P    E             E   1',
    '1111111111111111111111111',
]

LEVEL_7 = [
    '1111111111111111111111111',
    '1                       1',
    '1                       1',
    '1                       1',
    '1          2            1',
    '1                       1',
    '1             11        1',
    '1            E    3     1',
    '1   E    1E  111    E   1',
    '1     3                 1',
    '1    E   3   1E         1',
    '1   F3 3        3F      1',
    '1  3     3E   3  E      1',
    '1E1         3E          1',
    '1P1                     1',
    '1111111111111111111111111',
]

LEVEL_8 = [
    '1111111111111111111111111',
    '1P       U              1',
    '13              U       1',
    '1       3   E           1',
    '1  3       3  3  3      1',
    '1      3                1',
    '1           U       U   1',
    '1        E       T      1',
    '1    3      F          E1',
    '1                       1',
    '1 U    3      E         1',
    '1        E              1',
    '1    3      F          T1',
    '1        3      3       1',
    '1            3         21',
    '1                  *  311',
]

LEVEL_9 = [
    '1111111111111111111111111',
    '1 U                  U  1',
    '1                       1',
    '1        U     U        1',
    '1                       1',
    '1                       1',
    '1            2  *   *   1',
    '1   U                  11',
    '1            E        * 1',
    '1                    *  1',
    '1  E                *   1',
    '1                E *    1',
    '1     E           *     1',
    '1                *      1',
    '1P1             *       1',
    '111 3  3 3 *  3 3 3     1',
]

LEVEL_10 = [
    '1111111111111111111111111',
    '1           T           1',
    '1       U             U 1',
    '1        3 * * 1  *     1',
    '1    U              *   1',
    '1          *       U  3 1',
    '1      *         3 *    1',
    '1      T                1',
    '1  U            *       1',
    '1                  *    1',
    '1        T E          3 1',
    '1                1  1   1',
    '1             3        E1',
    '1               *       1',
    '12               3 * 3 P1',
    '1                      *1',
]

LEVEL_11 = [
    '1111111111111111111111111',
    '121           U        i1',
    '1G1       4           411',
    '1 44               U    1',
    '1      4 U              1',
    '1  R                    1',
    '1             3   3  44 1',
    '1        4              1',
    '1           U           1',
    '1           E           1',
    '1             444   1   1',
    '1 44  5    3            1',
    '1                       1',
    '1                      E1',
    '1P                      1',
    '11                      1',
]

LEVEL_12 =[
    '1111111111111111111111111',
    '12G      U1    U       i1',
    '1114R     1        1 1111',
    '1         1 4      1   E1',
    '1         1       51    1',
    '1    U    1   111111    1',
    '1         1          14 1',
    '1R        1          1  1',
    '1         1111111    1  1',
    '1         1     111111  1',
    '1   5     1             1',
    '1    111111     111111111',
    '1                      E1',
    '11111111111111111111111 1',
    '1P             R        1',
    '1111111111111111111111111'
]

LEVEL_13 = [
    '1111111111111111111111111',
    '12G        U   1        1',
    '111            1        1',
    '1       bB     1        1',
    '1U  11111111   1        1',
    '1          1   1    1   1',
    '1  1 11111 11111    1  i1',
    '1  1 1              11111',
    '1 11 111rrr    115      1',
    '1         1       bB    1',
    '1 1151111 1             1',
    '1 1111111 1             1',
    '1         1             1',
    '111    1151             1',
    '1P           bB         1',
    '1111111111111111111111111'
]

LEVEL_14 = [
    '1111111111111111111111111',
    '1  P         1 i   U    1',
    '11 1111111111111111111  1',
    '1  1        21          1',
    '1  11G11111111       3  1',
    '1            bB         1',
    '1 5111111111111  4  11  1',
    '141               U   451',
    '1 1 4111  4  11         1',
    '1 1   11     11        E1',
    '1     11     11         1',
    '1 11 111     11         1',
    '1            11         1',
    '1 111111     11         1',
    '1            11         1',
    '1 11111      11      5111'
]

LEVEL_15 = [    
    '1111111111111111111111111',
    '1i     111111   111111  1',
    '1            bB 1 U  1  1',
    '1     11111111     1    1',
    '1R   1        1 1  111151',
    '1115 1      U 111 4     1',
    '121           1      1  1',
    '1G1111111     1111   1  1',
    '1       1      1   U    1',
    '1rrr    1      1     1  1',
    '1     111      1111  1  1',
    '1111 1  U         1111  1',
    '1  1 1            1    51',
    '1         bB      1 11111',
    '1P  5                 1 1',
    '1111111111111111111111111'
]

LEVEL_16 = [
    '1111111111111111111111111',
    '1 P  1      1           1',
    '1 1  1111 1 1 1     111 1',
    '  11bB    1 1 1     1i   ',
    '1 111111111 1 1  5  11111',
    '1 1   1      4111114    1',
    '1R1   1111  1          31',
    '1     1 11 11 1 111 11111',
    '            1   1    bB  ',
    '1111111111111 111       1',
    '1 1 111111111 1111111   1',
    '  1   GbB                ',
    '1 1 1 111111 111111 11111',
    '1 1  1      1      1    1',
    ' bB     1       1     1 2',
    '1111111111111111111111111'
]

LEVEL_17 = [
    '1111111111111111111111111',
    '1i 1                 1 U1',
    '1  1 111111          1  1',
    '14 1   R  1 3 11111141  1',
    '1  1  1   1   1U1       1',
    '1  1111   111 1 111     1',
    '1       111 1 1      1  1',
    '1 U   LL    111    1    1',
    '1                111E 111',
    '1      U11r      1      1',
    '1   1   1        1111   1',
    '1   11111       E       1',
    '1   1      1         5 11',
    '11111 111   11  111111121',
    '1PR             G      E1',
    '111111     LLLL  3 111111'
]

LEVEL_18 = [
    '1111111111111111111111111',
    '1P 1                  1 1',
    '11 1         1        1 1',
    '1  1        1 11 11111111',
    '1  111141  bB           1',
    '1 <     1      151      1',
    '1 11111 1   1 1 1 1 1   1',
    '1 1i    1   1    >      1',
    '1 1111111111111 1 1 1   1',
    '1R             1 1      1',
    '11111111     1          1',
    '1  11  1  <             1',
    '1  11  1  11111  1 5    1',
    '111                   E51',
    '12G   11                1',
    '1111                    1'
]

LEVEL_19 = [
    '1111111111111111111111111',
    '1i b               B    1',
    '1h        1 1 1h11h     1',
    '111        1 1 1  m     1',
    '1     mmm1              1',
    '1    b           11111  1',
    '1             B         1',
    '1         11 1 1 1     11',
    '1     mmm   1 1 1      h1',
    '1                     111',
    '1     11111           121',
    '1     1h               G1',
    '1    51       B11       1',
    '1   111111  m    1 1 1 m1',
    '1P    h   <      >1 1 1 1',
    '1111111111111111111111111'
]

LEVEL_20 = [
    '1111111111111111111111111',
    '12G                     1',
    '111                     1',
    '1 Um               LLL  1',
    '1 R h                  h1',
    '1   1      h   1mm     E1',
    '1    41mmm h m          1',
    '1          1            1',
    '1        h           U i1',
    '1         >    <        1',
    '1     11111  U 11111mmmm1',
    '1                       1',
    '1                       1',
    '1h     1             E  1',
    '1P            5         1',
    '11mmmmmmmm111111111111111'
]

LEVEL_21 = [
'1111',
'1  1',
'1  1',
'1P G',
'1111'
]

level_list = [outline, LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4,LEVEL_5, 
              LEVEL_6, LEVEL_7, LEVEL_8, LEVEL_9, LEVEL_10, outline,
              LEVEL_11, LEVEL_12, LEVEL_13, LEVEL_14, LEVEL_15, LEVEL_16, 
              LEVEL_17, LEVEL_18, LEVEL_19, LEVEL_20, outline]
