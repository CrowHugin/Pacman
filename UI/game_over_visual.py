from score import set_highscore
import pygame


def game_over(window: pygame.Surface,
              BLACK: tuple[int, int, int],
              font: pygame.font.Font) -> None:
    pygame.display.set_caption("GAME OVER")

    center_x = window.get_width() // 2

    box_width = 280
    box_height = 50
    box_x = center_x - (box_width // 2)

    clock = pygame.time.Clock()
    default_color = pygame.Color('dodgerblue2')
    color_limit_reached = pygame.Color('red')
    color = default_color
    text = 'Joe'
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_RETURN:
                    # Recuperer le filename et le score
                    # Ne pas quitter mais revenir au menu principal
                    set_highscore("score.json", [text, 20])
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    color = default_color
                else:
                    if len(text) != 10:
                        if event.unicode.isalnum() or event.unicode.isspace():
                            text += event.unicode
                            color = default_color
                    else:
                        color = color_limit_reached
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if text_rect_main_menu.collidepoint(event.pos):
                        print('Button pressed.')
                    elif text_rect_new_game.collidepoint(event.pos):
                        print('new game.')

        window.fill(BLACK)

        text_surface = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text_surface.get_rect(
            center=(center_x, window.get_height() // 6))
        window.blit(text_surface, text_rect)

        score = 10
        # Draw score
        text_score = font.render(f"Your score {score}", True, (255, 255, 255))
        text_rect_highscore = text_score.get_rect(
            center=(center_x, window.get_height() // 3))
        window.blit(text_score, text_rect_highscore)

        text_nickname = font.render("Enter Nickname", True, (255, 255, 255))
        text_rect_nickname = text_nickname.get_rect(
            center=(center_x, window.get_height() // 2.5))
        window.blit(text_nickname, text_rect_nickname)

        # Draw input box
        box_y = text_rect_nickname.bottom + 15
        input_box = pygame.Rect(box_x, box_y, box_width, box_height)
        pygame.draw.rect(window, color, input_box, 2)

        # Draw the input letters
        txt_surface = font.render(text, True, (255, 255, 255))
        window.blit(txt_surface, (input_box.x + 10, input_box.y + 5))

        text_instruction = font.render(
            "Press enter to save", True, (255, 255, 255))
        text_rect_instruction = text_instruction.get_rect(
            center=(center_x, window.get_height() // 1.8))
        window.blit(text_instruction, text_rect_instruction)

        text_main_menu = font.render("Main menu", True, (255, 255, 255))
        text_rect_main_menu = text_main_menu.get_rect(
            center=(center_x - 200, window.get_height() // 1.5))
        window.blit(text_main_menu, text_rect_main_menu)

        text_new_game = font.render("New game", True, (255, 255, 255))
        text_rect_new_game = text_new_game.get_rect(
            center=(center_x + 200, window.get_height() // 1.5))
        window.blit(text_new_game, text_rect_new_game)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    exit()
