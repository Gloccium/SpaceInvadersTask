from enum import Enum


class GameStates(Enum):
    MAIN_MENU, GAME_SCREEN, RESTART_WINDOW, LEADERBOARD_SCREEN = range(4)
