import pygame


def render_cheat_mode(window: pygame.Surface, lvl_max: int) -> None:
    pygame.display.set_caption("Cheat mode")
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont("arial", 48)
    clock = pygame.time.Clock()
    center_x = window.get_width() // 2
    done = False

    text_main_menu = font.render("Main menu", True, (255, 255, 255))
    text_rect_main_menu = text_main_menu.get_rect(
        center=(window.get_height() // 8, window.get_height() // 10)
    )
    text_cheat = font.render("Cheats node", True, (255, 255, 255))
    text_rect_cheat = text_cheat.get_rect(
        center=(center_x, window.get_height() // 10)
    )
    is_invincible = False
    text_invicibility = font.render("Invicibility", True, (137,137,137))
    text_rect_invicibility = text_invicibility.get_rect(
            center=(center_x, text_rect_cheat.bottom + 100)
    )
    
    is_ghost_freeze = False
    text_ghost_freeze = font.render("Ghost Freeze ", True, (137,137,137))
    text_rect_ghost_freeze = text_ghost_freeze.get_rect(
            center=(center_x, text_rect_invicibility.bottom + 50)
    )
    # A changer plus tard
    level = 0
    text_level = font.render(f"level {level}", True, (255,255,255))
    text_rect_level = text_level.get_rect(
            center=(center_x, text_rect_ghost_freeze.bottom + 50)
    )
    text_plus = font.render("+", True, (255,255,255))
    text_minus = font.render("-", True, (255,255,255))

    text_rect_plus_level = text_plus.get_rect(
            center=(text_rect_level.right + 50, text_rect_ghost_freeze.bottom + 50)
    )
    text_rect_minus_level = text_minus.get_rect(
            center=(text_rect_level.left - 50, text_rect_ghost_freeze.bottom + 50)
    ) 

    # A changer plus tard
    player_speed = 0.5
    text_player_speed = font.render(f"Player speed {player_speed}", True, (255,255,255))
    text_rect_player_speed = text_player_speed.get_rect(
            center=(center_x, text_rect_level.bottom + 50)
    )
    text_rect_plus_player = text_plus.get_rect(
            center=(text_rect_player_speed.right + 50, text_rect_level.bottom + 50)
    )
    text_rect_minus_player = text_minus.get_rect(
            center=(text_rect_player_speed.left - 50, text_rect_level.bottom + 50)
    )

    # A changer plus tard
    extra_lives = 3
    text_lives = font.render(f"Extra lives {extra_lives}", True, (255,255,255))
    text_rect_lives = text_lives.get_rect(
            center=(center_x, text_rect_player_speed.bottom + 50)
    )
    text_rect_plus_lives = text_plus.get_rect(
            center=(text_rect_lives.right + 50, text_rect_player_speed.bottom + 50)
    )
    text_rect_minus_lives = text_minus.get_rect(
            center=(text_rect_lives.left - 50, text_rect_player_speed.bottom + 50)
    )

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1):
                if text_rect_main_menu.collidepoint(event.pos):
                    done = True
                elif text_rect_invicibility.collidepoint(event.pos):
                    is_invincible = not is_invincible
                    if is_invincible:
                        text_invicibility = font.render("Invicibility", True, (255,255,255))
                    else:
                        text_invicibility = font.render("Invicibility", True, (137,137,137))
                elif text_rect_ghost_freeze.collidepoint(event.pos):
                    is_ghost_freeze = not is_ghost_freeze
                    if is_ghost_freeze:
                        text_ghost_freeze = font.render("Ghost Freeze", True, (255,255,255))
                    else:
                        text_ghost_freeze = font.render("Ghost Freeze", True, (137,137,137))
                elif text_rect_plus_level.collidepoint(event.pos) and level <= lvl_max:
                        level += 1
                        text_level = font.render(f"level {level}", True, (255,255,255))
                elif text_rect_minus_level.collidepoint(event.pos) and level > 0:
                        level -= 1
                        text_level = font.render(f"level {level}", True, (255,255,255))
                elif text_rect_plus_player.collidepoint(event.pos):
                        player_speed = round(max(0.0, player_speed + 0.1), 2)
                        text_player_speed = font.render(f"Player speed {round(player_speed,2)}", True, (255,255,255))
                elif text_rect_minus_player.collidepoint(event.pos) and player_speed > 0:
                        player_speed = round(max(0.0, player_speed - 0.1), 2)
                        text_player_speed = font.render(f"Player speed {round(player_speed,2)}", True, (255,255,255))
                elif text_rect_plus_lives.collidepoint(event.pos):
                        extra_lives += 1
                        text_lives = font.render(f"Extra lives {extra_lives}", True, (255,255,255))
                elif text_rect_minus_lives.collidepoint(event.pos) and extra_lives > 1:
                        extra_lives -= 1
                        text_lives = font.render(f"Extra lives {extra_lives}", True, (255,255,255))
        window.fill(BLACK)

        window.blit(text_lives, text_rect_lives)
        window.blit(text_plus, text_rect_plus_lives)
        window.blit(text_minus, text_rect_minus_lives)


        window.blit(text_player_speed, text_rect_player_speed)
        window.blit(text_plus, text_rect_plus_player)
        window.blit(text_minus, text_rect_minus_player)

        window.blit(text_level, text_rect_level)
        window.blit(text_minus, text_rect_minus_level)
        window.blit(text_plus, text_rect_plus_level)

        window.blit(text_cheat, text_rect_cheat)
        window.blit(text_invicibility, text_rect_invicibility)
        window.blit(text_ghost_freeze, text_rect_ghost_freeze)
        window.blit(text_ghost_freeze, text_rect_ghost_freeze)
        window.blit(text_main_menu, text_rect_main_menu)
        pygame.display.flip()
        clock.tick(30)