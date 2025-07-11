import pygame as pg
from constant import *
from button import Button

class Menu:
    def __init__(self):
        self.music_enabled = True
        self.current_music = None
        self.music_volume = 0.5
        self.active_submenu = None 
        self.init_music()
        self.setup_menus()

    def init_music(self):
        pg.mixer.init()
        pg.mixer.music.set_volume(self.music_volume)
    
    def play_music(self, filename):
        self.current_music = filename
        if self.music_enabled:
            try:
                pg.mixer.music.load(filename)
                pg.mixer.music.play(-1)  
            except Exception as e:
                print(f"Ошибка загрузки музыки: {e}")

    def toggle_music(self):
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            if self.current_music:
                pg.mixer.music.unpause()
            else:
                self.play_music("assets/music/game_music.mp3")  
        else:
            pg.mixer.music.pause()
        self.update_music_button()

    def setup_menus(self):
        button_width = 300
        button_height = 60
        center_x = SCREEN_W // 2 - button_width // 2
        
        self.main_menu_buttons = [
            Button(center_x, 300, button_width, button_height, "Играть", "play"),
            Button(center_x, 380, button_width, button_height, "Выбор уровня", "levels"),
            Button(center_x, 460, button_width, button_height, "Настройки", "settings"),
            Button(center_x, 540, button_width, button_height, "Выход", "quit")
        ]
        
        self.setup_level_menu()
        
        self.setup_settings_menu()

    def setup_level_menu(self):
        level_button_size = 150
        margin = 30
        start_x = SCREEN_W // 2 - (3 * level_button_size + 2 * margin) // 2
        start_y = 300
        
        self.level_buttons = []
        for i in range(6):
            row = i // 3
            col = i % 3
            x = start_x + col * (level_button_size + margin)
            y = start_y + row * (level_button_size + margin)
            
            if i == 0:
                level_text = "Обучение"
            elif i == 5:
                level_text = "Финал"
            else:
                level_text = f'Уровень {i+1}'
                
            self.level_buttons.append(
                Button(x, y, level_button_size, level_button_size, 
                      level_text, f"level_{i+1}")
            )
        
        self.level_buttons.append(
            Button(SCREEN_W // 2 - 150, 
                 start_y + 2 * (level_button_size + margin), 
                 300, 60, "Назад", "back")
        )

    def setup_settings_menu(self):
        button_width = 300
        button_height = 60
        center_x = SCREEN_W // 2 - button_width // 2
        
        self.settings_buttons = [
            Button(center_x, 300, button_width, button_height, 
                  self.get_music_button_text(), "toggle_music"),
            Button(center_x, 380, button_width, button_height, "Назад", "back")
        ]

    def get_music_button_text(self):
        return f"Музыка: {'Вкл' if self.music_enabled else 'Выкл'}"

    def update_music_button(self):
        for button in self.settings_buttons:
            if button.action == "toggle_music":
                button.text = self.get_music_button_text()
                break

    def draw(self, surface):
        surface.fill(MENU_BG_COLOR)
        
        font = pg.font.Font(None, 72)
        title = font.render(SCREEN_TITLE, True, TEXT_COLOR)
        surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 150))
        
        buttons, subtitle = self.get_active_menu()
        
        font = pg.font.Font(None, 36)
        subtitle_text = font.render(subtitle, True, (200, 200, 200))
        surface.blit(subtitle_text, (SCREEN_W // 2 - subtitle_text.get_width() // 2, 250))
        
        for button in buttons:
            button.draw(surface)

    def get_active_menu(self):
        if self.active_submenu == "levels":
            return self.level_buttons, "Выберите уровень"
        elif self.active_submenu == "settings":
            return self.settings_buttons, "Настройки"
        return self.main_menu_buttons, "Главное меню"

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            self.handle_mouse_move(event.pos)
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            return self.handle_mouse_click()
        return None

    def handle_mouse_move(self, pos):
        for button in self.get_active_buttons():
            button.check_hover(pos)

    def handle_mouse_click(self):
        for button in self.get_active_buttons():
            action = button.handle_event(pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': pg.mouse.get_pos()}))
            if action:
                return self.handle_action(action)
        return None

    def get_active_buttons(self):
        buttons, _ = self.get_active_menu()
        return buttons

    def handle_action(self, action):
        if action == "play":
            return {"action": "start_game", "level": 1}
        elif action.startswith("level_"):
            return {"action": "start_game", "level": int(action.split("_")[1])}
        elif action == "levels":
            self.active_submenu = "levels"
        elif action == "settings":
            self.active_submenu = "settings"
        elif action == "back":
            self.active_submenu = None
        elif action == "quit":
            return {"action": "quit"}
        elif action == "toggle_music":
            self.toggle_music()
        return None