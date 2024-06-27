from Stage import Stage

class Level():
    '''Level class that stores data for an entire level. '''

    def __init__(self, levelId:int, levelName:str, stages:list[Stage]) -> None:
        '''Constructor Method for Level Class. Takes level id, level name and a list of SQL columns of Stage objects. '''
        self.setStages(stages)
        self.setId(levelId)
        self.setName(levelName)

    def setId(self, levelId) -> None:
        self.__id = levelId

    def setName(self, levelName) -> None:
        if levelName:
            self.__name = levelName
        else:
            self.__name = self.__id

    def setStages(self, stages:list[Stage]) -> None:
        self.__stages = stages

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getNumStages(self) -> int:
        return len(self.__stages)

    def getStage(self, stageId) -> Stage:
        for stage in self.__stages:
            if stage.getStageId() == stageId:
                return stage
            

def main() -> None:
    pass

if __name__ == "__main__":
    main()