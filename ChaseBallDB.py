from Database import Database
from Stage import Stage
from Level import Level

class ChaseBallDB(Database):
    '''ChaseBall Game Database class for interacting with SQL stored data '''

    def __init__(self) -> None:
        super().__init__(r".\ChaseBall.db")

    def getNumLevels(self) -> int:
        sql = f'''SELECT count(*) AS count FROM levels'''
        countData = self.dbGetData(sql)
        if countData:
            for countRecord in countData:
                count = int(countRecord['count'])
            return count
        else:
            return 0

    def getVideoSettings(self) -> dict[str, any]:
        sql = '''
        SELECT settingType, settingValue
        FROM settings, settingCategories
        WHERE settings.settingId = settingCategories.settingId
        AND settingCategory = 'video'
        '''
        setting_data = self.dbGetData(sql)
        if setting_data:
            settings = {}
            for setting in setting_data:
                settings[setting['settingType']] = setting['settingValue']
            return settings
        else:
            print('Game Database Error: no existing settings ')

    def getAudioSettings(self) -> dict[str, any]:
        pass

    def getLevel(self, levelId) -> Level:
        sql = f'''SELECT
            levelName,
            stageName,
            playerStartPosX,
            playerStartPosY,
            enemyStartPosX,
            enemyStartPosY,
            playerRadius,
            enemyRadius,
            friction,
            playerAcceleration,
            enemyAcceleration,
            bounce,
            goalText,
            goalCenterX,
            goalCenterY,
            goalFontName,
            goalFontSize,
            criteriaType,
            criteriaValue,
            captionText,
            captionCenterX,
            captionCenterY,
            captionFontName,
            captionFontSize
        FROM stages, levels
        WHERE stages.levelId = levels.levelId = {levelId}
        ORDER BY stages.levelId, stageId
        '''
        level_data = self.dbGetData(sql)
        if level_data:
            stages: list[Stage] = []
            for index, stage_data in enumerate(level_data):
                stage = Stage(index + 1, stage_data)
                stages.append(stage)
            stages[-1].setLastStage()
            return Level(levelId, stage_data['levelName'], stages)
        else:
            print("Game Database Error: no existing level data ")


def main() -> None:
    db = ChaseBallDB()
    level1 = db.getLevel(1)
    print(level1.getName())
    db.getVideoSettings()

if __name__ == "__main__":
    main()