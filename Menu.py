from GraphicsEngine import GraphicsEngine as GE
from Text import Text
from Event import Event
from time import sleep
from pygame import key, K_e, K_q

class Menu():
    '''Facade Class that runs menu screens. '''

    def __init__(self):
        self.__sel_level_text = Text('Welcome to ChaseBall!\nPlease choose a level', (GE.getScreenWidth() // 2, GE.getScreenHeight() // 4))
        self.__sel_stage_text = Text('Please choose a stage', (GE.getScreenWidth() // 2, GE.getScreenHeight() // 4))
        self.__back_text = Text('BACK', (80, GE.getScreenHeight() - 50))
        self.__quit_text = Text('QUIT', (GE.getScreenWidth() - 80, GE.getScreenHeight() - 50))
        self.__start_text = Text('Use w/a/s/d to move', (GE.getScreenWidth() // 2, GE.getScreenHeight() // 2))
        self.__win_text = Text('You won!\nPress E to play the next level, Q to return to home', (GE.getScreenWidth() // 2, GE.getScreenHeight() // 2))
        self.__lose_text = Text('You lost! Would you like to play again?\nPress E to play again, Q to return to home', (GE.getScreenWidth() // 2, GE.getScreenHeight() // 2))
        self.__beat_level_text = Text('Congratulations, you have beat this level!', (GE.getScreenWidth() // 2, GE.getScreenHeight() // 2))

    def getBeatText(self) -> Text:
        return self.__beat_level_text
    
    def getWinText(self) -> Text:
        return self.__win_text
    
    def getLoseText(self) -> Text:
        return self.__lose_text

    def selectLevel(self, num_levels) -> int:
        '''Displays level selection screen and waits for user to click on an option. Then returns number of the level chosen. '''
        GE.clearScreen()
        GE.printText(self.__sel_level_text)
        level_poses = []
        num_levels = num_levels
        for level in range(1, num_levels + 1):
            text_center = (GE.getScreenWidth() * (level) // (num_levels + 1), GE.getScreenHeight() // 2)
            level_text = Text(f"Level {level}", text_center)
            level_elip = GE.drawElip(level_text.getRect(), "#18B4B7")
            level_poses.append(level_elip.getRect())
            GE.printText(level_text)
        
        quit_ellipse = GE.drawElip(self.__quit_text.getRect(), 'red')
        GE.printText(self.__quit_text)
        GE.printScreen()
        waiting = True
        while waiting:
            events = Event().poll(level_poses + [quit_ellipse.getRect()])
            if events:
                if events == -1:
                    return -1
                for event_pos, type in events:
                    if type == "click":
                        chosen_rect = event_pos
                        waiting = False
            sleep(0.05)
        if chosen_rect == quit_ellipse.getRect():
                return -1
        for index, level_pos in enumerate(level_poses):
            if chosen_rect == level_pos:
                return index + 1

    def selectStage(self, level) -> int:
        '''Displays stage selection screen and waits for user to click on an option. Then returns number of the stage chosen. '''
        GE.clearScreen()
        GE.printText(self.__sel_stage_text)
        stage_poses = []
        num_stages = level.getNumStages()
        for stage in range(1, num_stages + 1):
            text_center = (GE.getScreenWidth() * (stage) // (num_stages + 1), GE.getScreenHeight() // 2)
            stage_text = Text(f"Stage {stage}", text_center)
            stage_elip = GE.drawElip(stage_text.getRect(), "#18B4B7")
            stage_poses.append(stage_elip.getRect())
            GE.printText(stage_text)
        
        back_ellipse = GE.drawElip(self.__back_text.getRect(), 'orange')
        GE.printText(self.__back_text)
        GE.printScreen()
        waiting = True
        while waiting:
            events = Event().poll(stage_poses + [back_ellipse.getRect()])
            if events:
                if events == -1:
                    return -1
                for event, type in events:
                    if type == "click":
                        chosen_rect = event
                        waiting = False
            sleep(0.05)
        if chosen_rect == back_ellipse.getRect():
                return 0
        for index, stage_pos in enumerate(stage_poses):
            if chosen_rect == stage_pos:
                return index + 1

    def startStage(self):
        GE.clearScreen()
        GE.printText(self.__start_text)
        GE.printScreen()
        sleep(2)

    def endStage(self, won, last_level) -> bool | int:
        '''Displays next screen depending if user won or lost, and returns True if wish to play again, False if not. '''
        GE.clearScreen()
        if won and last_level:
            GE.printText(self.getBeatText())
            GE.printScreen()
            sleep(2)
            return False
        elif won and not last_level:
            GE.printText(self.getWinText())
        else:
            GE.printText(self.getLoseText())
        GE.printScreen()
        while True:
            quit = Event().poll()
            if quit:
                return -1
            keys = key.get_pressed()
            if keys[K_e]:
                return True
            elif keys[K_q]:
                return False
            sleep(0.01)

    def quit(self):
        '''Ends the game '''
        GE.quitPG()


def main() -> None:
    menu = Menu()
    print(menu.selectLevel(4))

if __name__ == "__main__":
    main()