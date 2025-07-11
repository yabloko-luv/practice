import pygame as pg
import os
from constant import *
from player import Player
from level import load_level
from button import Button
from menu import Menu

music_enabled = True

def init_music():
    pg.mixer.init()
    pg.mixer.music.set_volume(0.5)

def play_music(filename):
    global current_music
    if music_enabled:
        if os.path.exists(filename):
            pg.mixer.music.load(filename)
            pg.mixer.music.play(-1) 
            current_music = filename

def toggle_music():
    global music_enabled
    music_enabled = not music_enabled
    if music_enabled and current_music:
        pg.mixer.music.unpause()
    else:
        pg.mixer.music.pause()

def draw_tutorial(surface):
    tutorial_width = SCREEN_W - 200
    tutorial_height = SCREEN_H - 200
    tutorial_surface = pg.Surface((tutorial_width, tutorial_height), pg.SRCALPHA)
    tutorial_surface.fill((0, 0, 0, 200))
    pg.draw.rect(tutorial_surface, (255, 255, 255), tutorial_surface.get_rect(), 2)
    
    font_title = pg.font.Font(None, 48)
    font_text = pg.font.Font(None, 36)
    
    title = font_title.render("Обучение", True, (255, 255, 255))
    tutorial_surface.blit(title, (tutorial_width//2 - title.get_width()//2, 20))
    
    instructions = [
        "Твоя задача добраться до конца уровня, избегая красных квадратов!",
        "Управление персонажем:",
        "A - Движение влево",
        "D - Движение вправо",
        "SPACE - Прыжок",
        "",
        "Tab - Показать/скрыть это окно",
        "ESC - Вернуться в меню",
        "M - Вкл/Выкл музыку"
    ]
    
    y_offset = 80
    for line in instructions:
        text = font_text.render(line, True, (255, 255, 255))
        tutorial_surface.blit(text, (tutorial_width//2 - text.get_width()//2, y_offset))
        y_offset += 40
    
    surface.blit(tutorial_surface, (100, 100))

def setka(surface):
    for x in range(0, SCREEN_W, 50):
        pg.draw.line(surface, (200, 200, 200), (x, 0), (x, SCREEN_H+100))
    for y in range(0, SCREEN_H, 50):
        pg.draw.line(surface, (200, 200, 200), (0, y), (SCREEN_W+100, y))

def init_game(level_num):
    level = load_level(level_num)
    player = Player(*level.player_start_pos, PLAYER_SPEED, PLAYER_JUMPFORCE)
    return player, level

def draw_game(surface, player, level, show_tutorial):
    surface.fill(level.background_color)
    setka(surface)
    
    for platform in level.platforms:
        platform.draw(surface)

    for trap in level.traps:
        trap.draw(surface)
        trap.update_text()
        trap.check_collision(player)

    exit_rect = pg.Rect(level.exit_pos[0] - 15, level.exit_pos[1] - 15, 30, 30)
    pg.draw.rect(surface, (0, 255, 0), exit_rect)
    pg.draw.rect(surface, (0, 180, 0), exit_rect, 2)

    player.draw(surface)
    
    if show_tutorial:
        draw_tutorial(surface)

def draw_results_screen(surface, level_name, time_elapsed, deaths):
    overlay = pg.Surface((SCREEN_W+100, SCREEN_H+100), pg.SRCALPHA)
    overlay.fill((50, 50, 50, 220))
    surface.blit(overlay, (0, 0))
    
    font_large = pg.font.Font(None, 72)
    font_medium = pg.font.Font(None, 48)
    
    title = font_large.render("Уровень пройден!", True, (255, 255, 255))
    surface.blit(title, (SCREEN_W//2 - title.get_width()//2, 150))
    
    stats = [
        f"Уровень: {level_name}",
        f"Время: {time_elapsed:.1f} сек",
        f"Смертей: {deaths}"
    ]
    y_pos = 250
    for stat in stats:
        text = font_medium.render(stat, True, (255, 255, 255))
        surface.blit(text, (SCREEN_W//2 - text.get_width()//2, y_pos))
        y_pos += 70

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_W, SCREEN_H), pg.FULLSCREEN)
    pg.display.set_caption(SCREEN_TITLE)
    clock = pg.time.Clock()

    init_music()
    play_music(os.path.join("assets", "music.mp3"))
    menu = Menu()
    player = None
    current_level = None
    show_tutorial = False 
    in_game = False
    level_completed = False
    results_buttons = []
    level_start_time = 0
    level_end_time = 0
    deaths_count = 0
    current_level_num = 1
    total_levels = 6
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if level_completed:
                if event.type == pg.MOUSEMOTION:
                    for button in results_buttons:
                        button.check_hover(event.pos)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for button in results_buttons:
                        action = button.handle_event(event)
                        if action == "menu":
                            level_completed = False
                            in_game = False
                            results_buttons = []
                        elif action == "restart":
                            player, current_level = init_game(current_level_num)
                            level_completed = False
                            deaths_count = 0
                            level_start_time = pg.time.get_ticks() / 1000.0
                            results_buttons = []
                            show_tutorial = (current_level_num == 1)
                        elif action == "next_level":
                            current_level_num += 1
                            player, current_level = init_game(current_level_num)
                            level_completed = False
                            deaths_count = 0
                            level_start_time = pg.time.get_ticks() / 1000.0
                            results_buttons = []
                            show_tutorial = (current_level_num == 1)
            
            elif in_game:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        in_game = False
                    elif event.key == pg.K_TAB:
                        show_tutorial = not show_tutorial
                    elif event.key == pg.K_m:
                        toggle_music()
                elif event.type == pg.USEREVENT + 1:
                    deaths_count += 1
            
            else:
                action = menu.handle_event(event)
                if action:
                    if action["action"] == "start_game":
                        player, current_level = init_game(action["level"])
                        in_game = True
                        level_completed = False
                        current_level_num = action["level"]
                        deaths_count = 0
                        level_start_time = pg.time.get_ticks() / 1000.0
                        show_tutorial = (current_level_num == 1)
                    elif action["action"] == "quit":
                        running = False
        if in_game and not level_completed and not show_tutorial:
            keys = pg.key.get_pressed()
            player.move(keys, current_level.platforms)
            
            exit_rect = pg.Rect(
                current_level.exit_pos[0] - 15,
                current_level.exit_pos[1] - 15,
                30, 30
            )
            if player.rect.colliderect(exit_rect):
                level_completed = True
                level_end_time = pg.time.get_ticks() / 1000.0
                
                button_width = 300
                button_height = 60
                center_x = SCREEN_W // 2 - button_width // 2
                y_pos = 500
                
                results_buttons = [
                    Button(center_x, y_pos, button_width, button_height, "Повторить", "restart"),
                    Button(center_x, y_pos + 80, button_width, button_height, "В меню", "menu")
                ]
                
                if current_level_num < total_levels:
                    results_buttons.append(
                        Button(center_x, y_pos + 160, button_width, button_height, 
                             "След. уровень", "next_level")
                    )
        screen.fill((0, 0, 0))
        if in_game:
            draw_game(screen, player, current_level, show_tutorial)
            
            if level_completed:
                time_elapsed = level_end_time - level_start_time
                draw_results_screen(
                    screen,
                    current_level.level_name,
                    time_elapsed,
                    deaths_count
                )
                for button in results_buttons:
                    button.draw(screen)
        else:
            menu.draw(screen)
        
        pg.display.flip()
    
    pg.quit()

if __name__ == "__main__":
    main()