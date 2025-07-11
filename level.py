from platforms import Platform
from traps import Trap
from constant import *

def load_level(level_num):
    """Загружает уровень по номеру (1-6)"""
    levels = {
        1: Level1(),
        2: Level2(),
        3: Level3(),
        4: Level4(),
        5: Level5(),
        6: Level6(),
    }
    return levels.get(level_num, Level1())

class Level1:
    def __init__(self):
        self.platforms = [
            Platform(-100, GROUND, SCREEN_W + 100, 25),
            Platform(50 * 8, GROUND - 100, 100, 25),
            Platform(50 * 12, GROUND - 200, 100, 25),
            Platform(50*16, GROUND - 300, 100,25),
            Platform(50*20,GROUND- 250, 250,25),
            Platform(50*28,GROUND-350,100,25),
            Platform(50*24,GROUND-450,100,25),
            Platform(50*32,GROUND-450,100,25),
            Platform(50*19,GROUND-500,100,25),
            Platform(50*4,GROUND-500,500,25)
        ]
        self.traps = [
            Trap(50*22-25,GROUND-300,50,50,200,GROUND,True,"Осторожно",50*22,GROUND-350)
        ]
        self.player_start_pos = (50, GROUND-50) 
        self.exit_pos = (50*5, GROUND-550) 
        self.background_color = "white"
        self.level_name = "Обучение"

class Level2:
    def __init__(self):
        self.platforms = [
            Platform(50,100,150,25),
            Platform(50*6,150,400,25),  
            Platform(50*18,150,100,25),
            Platform(50*24,150,100,25),
            Platform(50*30,150,100,25),
            Platform(50*36,300,100,25),
            Platform(50*32,450,100,25),
            Platform(50*28,600,100,25),
            Platform(50*22,600,50,25),
            Platform(50*16,600,50,25),
            Platform(50*10,600,50,25),
            Platform(50*4,600,50,25),
        ]
        self.traps = [
            Trap(-100,GROUND+200,SCREEN_W+200,25,50,50),
            Trap(1,200,6*50,50,50,1),
            Trap(50*8,100,50,50,50,1),
            Trap(50*20,200,50*4,50,50,1),
            Trap(50*14,200,50*4,50,50,1),
            Trap(50*26,200,50*4,50,50,1),
        ]
        self.player_start_pos = (50, 1)
        self.exit_pos = (50,GROUND+150)
        self.background_color = "azure2"
        self.level_name = "Уровень 2"

class Level3:
    def __init__(self):
        self.platforms = [
            Platform(-100, GROUND+200, SCREEN_W + 100, 25),
            Platform(5*50,950,100,25),
            Platform(50,850,100,25),
            Platform(6*50,800,100,25),
            Platform(9*50,850,100,25),
            Platform(12*50,850,400,25),
            Platform(22*50,750,100,25),
            Platform(19*50,650,100,25),
            Platform(15*50,550,100,25),

            Platform(19*50,450,400,25),
            Platform(28*50,350,100,25),
            Platform(26*50,250,100,25),
            Platform(23*50,200,100,25),

            Platform(10*50,550,50,25),
            Platform(5*50,450,50,25),
            Platform(1*50,350,50,25),
            Platform(4*50,250,50,25),
            Platform(9*50,250,50,25),
            Platform(13*50,250,50,25),
            Platform(17*50,250,50,25),
            Platform(19*50,150,100,25),
        
        ]
        self.traps = [
            Trap(6*50,900,50,50,55,GROUND+60),
            Trap(50,800,50,50,55,GROUND+60),
            Trap(7*50,750,50,50,55,GROUND+60),
            Trap(10*50,800,50,50,55,GROUND+60),
            Trap(15*50,800,80,50,55,GROUND+60),
            Trap(22*50,400,50,50,55,GROUND+60),
            Trap(26*50,400,50,50,55,GROUND+60),
            Trap(26*50,200,50,50,55,GROUND+60)
        ]
        self.player_start_pos = (55, GROUND+60)
        self.exit_pos = (20*50,100)
        self.background_color = "gainsboro"
        self.level_name = "Уровень 3"

class Level4:
    def __init__(self):
        self.platforms = [
            Platform(-100, GROUND+200, SCREEN_W + 1000, 25),
            Platform(50*4, 950, 100, 25),
            Platform(50*8, 850, 400, 25),
            Platform(50*18,750,100,25),
            Platform(50*8, 650, 400, 25),
            Platform(50*4, 550, 100, 25),
            Platform(50,450, 100, 25),
            Platform(1,350, 50, 25),
            Platform(50*3,250, 50, 25),
            Platform(50*7,250, 50, 25),
            Platform(50*11,250, 50, 25),
            Platform(50*15,250, 50, 25),
            Platform(50*18,300, 100, 25),
            Platform(50*20,200, 100, 25),
            Platform(50*24,400, 100, 25),
            Platform(50*25,600, 100, 25),
            Platform(50*30,550, 100, 25),
            

        ]
        self.traps = [
            Trap(50*10,800,50,50,50,GROUND),
            Trap(50*13,800,50,50,50,GROUND),
            Trap(50*10,600,50,50,50,GROUND),
            Trap(50*13,600,50,50,50,GROUND),
            Trap(50*4, 500, 40, 50,50,GROUND),
            Trap(50,400, 40, 50,50,GROUND),
            Trap(50*19,250, 50, 50,50,GROUND),
            Trap(50*24,350, 50, 50,50,GROUND),
            

        ]
        self.player_start_pos = (50, GROUND)
        self.exit_pos = (50*35, GROUND)
        self.background_color = "grey"
        self.level_name = "Уровень 4"
class Level5:
    def __init__(self):
        self.platforms = [
            Platform(30, GROUND+100, 200, 25),
            Platform(50*6, GROUND, 200, 25),
            Platform(50*12, GROUND-100, 100, 25),
            Platform(50*9, GROUND-200, 100, 25),
            Platform(50*6, GROUND-300, 100, 25),
            Platform(50*3, GROUND-400, 100, 25),
            Platform(50*6, GROUND-500, 100, 25),
            Platform(50*8, GROUND-600, 700, 25),
            Platform(50*24, GROUND-700, 100, 25),
            Platform(50*28, GROUND-600, 200, 25),
            Platform(50*16, GROUND+100,1000, 25),
            Platform(50*16, GROUND-500,25, 600),
            Platform(50*36, GROUND-800, 25, 925),
            Platform(50*16, GROUND-525,700, 25),
            Platform(50*30, GROUND-525, 25, 475),
            Platform(50*19, GROUND-50, 575, 25),
            Platform(50*16, GROUND,50, 25),

        ]
        self.traps = [
            Trap(-100, GROUND+200, SCREEN_W + 1000, 25,50,GROUND-52),
            Trap(50*8, GROUND-50, 50, 50,50,GROUND-52),
            Trap(50*13, GROUND-150, 50, 50),
            Trap(50*9, GROUND-250, 50, 50),
            Trap(50*3, GROUND-450, 50, 50),
            Trap(50*10, GROUND-625, 75, 25),
            Trap(50*14, GROUND-625, 75, 25),
            Trap(50*18, GROUND-625, 75, 25),
            Trap(50*25, GROUND-725, 50, 25),
            Trap(50*20, GROUND+75,50, 25),
            Trap(50*26, GROUND+75,50, 25),
            Trap(50*22, GROUND-550, 300, 25),

        ]
        self.player_start_pos = (50, GROUND-52)
        self.exit_pos = (50 * 26, GROUND - 150)
        self.background_color = (255, 220, 220)
        self.level_name = "Уровень 5"

class Level6:
    def __init__(self):
        self.platforms = [
            Platform(50,200,100,25),
            Platform(50*8,200,50,25),
            Platform(50*14,200,50,25),
            Platform(50*20,200,50,25),
            Platform(50*26,400,50,25),
            Platform(50*26,400,50,25),
            Platform(50*20,500,50,25),
            Platform(50,500,50,25),
            Platform(50*8,500,50,25),
            Platform(50*14,500,50,25),
            Platform(50,700,50,25),
            Platform(50*6,850,50,25),
            Platform(50*12,850,50,25),
            Platform(50*18,850,50,25),
            Platform(50*24,850,50,25),
        ]
        self.traps = [
            Trap(-100,GROUND+200,1000000,25,50,100),
            Trap(1,250,50*21,25,50,100),
            Trap(50*8,550,1300,25,50,100)

        ]
        self.player_start_pos = (50, 100)
        self.exit_pos = (50 *29, 850)
        self.background_color = "slategrey"
        self.level_name = "Финальный уровень"