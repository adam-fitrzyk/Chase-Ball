from Menu import Menu
from ChaseBallDB import ChaseBallDB

'''
Add in red ball that shoots other red balls that also chase or stay in spot they are shot at like spikes and obstacles
'''

class ChaseBall:
    '''Facade Class that runs the ChaseBall game. '''

    def __init__(self) -> None:
        self.__Menu = Menu()
        self.__db = ChaseBallDB()

    def play(self) -> None:
        running = True
        choosing_stage = False

        while running:
            level_id = self.__Menu.selectLevel(self.__db.getNumLevels())
            if level_id == -1:
                running = False
            else:
                choosing_stage = True
                level = self.__db.getLevel(level_id)
            
            while choosing_stage:
                stage_id = self.__Menu.selectStage(level)
                if stage_id == -1:
                    running = False
                    choosing_stage = False
                    playing = False
                elif stage_id == 0:
                    choosing_stage = False
                    playing = False
                else:
                    playing = True
                    self.__Menu.startStage()

                while playing:
                    stage = level.getStage(stage_id)
                    ret = stage.run()
                    if ret == -1:
                        playing = False
                        choosing_stage = False
                        running = False
                    else:
                        won, last_stage = ret
                        play = self.__Menu.endStage(won, last_stage)
                        if play == -1:
                            playing = False
                            choosing_stage = False
                            running = False
                        elif won and play:
                            stage_id += 1
                        elif won and not play:
                            playing = False
                        elif not play:
                            playing = False
                        
        self.__Menu.quit()

def main() -> None:
    cb = ChaseBall()
    cb.play()

if __name__ == "__main__":
    main()