import pygame


def render_instruction(window: pygame.Surface) -> None:
    pygame.display.set_caption("Instruction")
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont("arial", 48)
    clock = pygame.time.Clock()
    center_x = window.get_width() // 2
    done = False

    text_main_menu = font.render("Main Menu", True, (255, 255, 255))
    text_rect_main_menu = text_main_menu.get_rect(
        center=(window.get_height() // 8, window.get_height() // 10)
    )
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and text_rect_main_menu.collidepoint(event.pos)
            ):
                done = True

        window.fill(BLACK)
        text_instruction = font.render("Instruction", True, (255, 255, 255))
        text_rect_instruction = text_instruction.get_rect(
            center=(center_x, window.get_height() // 10)
        )
        window.blit(text_instruction, text_rect_instruction)

        text_movement = font.render(
            "Use the arrow key to move freely in the maze",
            True, (255, 255, 255)
        )
        text_rect_movement = text_movement.get_rect(
            center=(center_x, text_rect_instruction.bottom + 100)
        )
        window.blit(text_movement, text_rect_movement)

        text_ghost = font.render(
            "Avoid the ghosts to not lose a life", True, (255, 255, 255)
        )
        text_rect_ghost = text_ghost.get_rect(
            center=(center_x, text_rect_movement.bottom + 70)
        )
        window.blit(text_ghost, text_rect_ghost)

        text_score = font.render(
            "Walk on the pacgum to increase your score", True, (255, 255, 255)
        )
        text_rect_score = text_score.get_rect(
            center=(center_x, text_rect_ghost.bottom + 70)
        )
        window.blit(text_score, text_rect_score)

        text_eat = font.render(
            "Walk on superpacgum and for 3 secondes", True, (255, 255, 255)
        )
        text_rect_eat = text_eat.get_rect(
            center=(center_x, text_rect_score.bottom + 70)
        )
        window.blit(text_eat, text_rect_eat)

        text_eat2 = font.render(
            "you will be able to eat a ghost", True, (255, 255, 255)
        )
        text_rect_eat2 = text_eat2.get_rect(
            center=(center_x, text_rect_eat.bottom + 30)
        )
        window.blit(text_eat2, text_rect_eat2)

        text_win = font.render(
            "To win you have to collect all the pacgum", True, (255, 255, 255)
        )
        text_rect_win = text_win.get_rect(center=(center_x,
                                                  text_rect_eat2.bottom + 70))
        window.blit(text_win, text_rect_win)

        text_win2 = font.render("within the time limit", True, (255, 255, 255))
        text_rect_win2 = text_win2.get_rect(
            center=(center_x, text_rect_win.bottom + 30)
        )
        window.blit(text_win2, text_rect_win2)

        text_lose = font.render(
            "You lose if you don't collect all the pacgum",
            True, (255, 255, 255)
        )
        text_rect_lose = text_lose.get_rect(
            center=(center_x, text_rect_win2.bottom + 70)
        )
        window.blit(text_lose, text_rect_lose)

        text_lose2 = font.render(
            "within the time limit or if you loose your 3 lives",
            True, (255, 255, 255)
        )
        text_rect_lose2 = text_lose2.get_rect(
            center=(center_x, text_rect_lose.bottom + 30)
        )
        window.blit(text_lose2, text_rect_lose2)
        window.blit(text_main_menu, text_rect_main_menu)
        pygame.display.flip()
        clock.tick(30)
