import PhysicsEngine as PE
import GraphicsEngine as GE
from Text import Text
from Event import Event
from pygame.draw import line

class Stage():
    '''Runs current stage in game. '''
    
    def __init__(self, stage_id, stage_data) -> None:
        '''Constructor Method for Stage Class. Takes SQL Row object for stage data. '''
        self.setStage(stage_data)
        self.__stage_id = stage_id
        self.__last_stage = False

    def setLastStage(self) -> None:
        self.__last_stage = True

    def setStage(self, stage_data) -> None:
        '''Takes SQL Row object and saves all stage data to class. '''
        if stage_data['playerStartPosX'] and stage_data['playerStartPosY']:
            self.__player_start_pos = (GE.GraphicsEngine.getScreenWidth() * stage_data['playerStartPosX'], GE.GraphicsEngine.getScreenHeight() * stage_data['playerStartPosY'])
        else:
            self.__player_start_pos = (GE.GraphicsEngine.getScreenWidth() // 2, GE.GraphicsEngine.getScreenHeight() // 2)
        if stage_data['enemyStartPosX'] and stage_data['enemyStartPosY']:
            self.__enemy_start_pos = (GE.GraphicsEngine.getScreenWidth() * stage_data['enemyStartPosX'], GE.GraphicsEngine.getScreenHeight() * stage_data['enemyStartPosY'])
        else:
            self.__enemy_start_pos = (GE.GraphicsEngine.getScreenWidth() * 3, GE.GraphicsEngine.getScreenHeight() * 3)
        if stage_data['playerRadius']:
            self.__player_radius = stage_data['playerRadius']
        else:
            self.__player_radius = 40
        if stage_data['enemyRadius']:
            self.__enemy_radius = stage_data['enemyRadius']
        else:
            self.__enemy_radius = 40
        if stage_data['friction']:
            self.__friction = stage_data['friction']
        else:
            self.__friction = 0.1
        if stage_data['playerAcceleration']:
            self.__player_acceleration = stage_data['playerAcceleration']
        else:
            self.__player_acceleration = 40
        if stage_data['enemyAcceleration']:
            self.__enemy_acceleration = stage_data['enemyAcceleration']
        else:
            self.__enemy_acceleration = 0
        if stage_data['bounce']:
            self.__bounce = stage_data['bounce']
        else:
            self.__bounce = 50
        if stage_data['goalText']:
            self.__goal_text = stage_data['goalText']
        else:
            self.__goal_text = 'no text provided'
        if stage_data['goalCenterX'] and stage_data['goalCenterY']:
            self.__goal_center = (GE.GraphicsEngine.getScreenWidth() * stage_data['goalCenterX'], GE.GraphicsEngine.getScreenHeight() * stage_data['goalCenterY'])
        else:
            self.__goal_center = (GE.GraphicsEngine.getScreenWidth() * 1.8, GE.GraphicsEngine.getScreenHeight() * 1.8)
        self.__goal_font = (stage_data['goalFontName'], stage_data['goalFontSize'])
        self.__criteria = (stage_data['criteriaType'], stage_data['criteriaValue'])
        if stage_data['captionText']:
            self.__caption_text = stage_data['captionText']
        else:
            self.__caption_text = 'no text provided'
        if stage_data['captionCenterX'] and stage_data['captionCenterY']:
            self.__caption_center = (GE.GraphicsEngine.getScreenWidth() * stage_data['captionCenterX'], GE.GraphicsEngine.getScreenHeight() * stage_data['captionCenterY'])
        else:
            self.__caption_center = (GE.GraphicsEngine.getScreenWidth() // 2, GE.GraphicsEngine.getScreenHeight() // 2)
        self.__caption_font = (stage_data['captionFontName'], stage_data['captionFontSize'])

    def getStageId(self) -> int:
        return self.__stage_id

    def run(self) -> bool:
        '''Runs the stage on the screen. Returns True if next stage is to be played, False if not. '''
        player_engine = PE.PhysEngine(self.__player_acceleration, self.__friction, self.__bounce, self.__player_start_pos, self.__player_radius)
        enemy_engine = PE.PhysEngine(self.__enemy_acceleration, self.__friction, self.__bounce, self.__enemy_start_pos, self.__enemy_radius)
        won = None
        collision = False
        bounce_time = 0
        done = False
        while not done:
            if Event().poll() == -1:
                return -1
            match self.__criteria[0]:
                case None:
                    criteria_matched = True
                case 'speed':
                    criteria_matched = player_engine.getSpeed() >= self.__criteria[1]
                case 'bounce':
                    bounce_time += player_engine.getDt()
                    if collision:
                        if bounce_time <= self.__criteria[1]:
                            criteria_matched = True
                        else:
                            collision = False
                            criteria_matched = False
                    else:
                        criteria_matched = False

            GE.GraphicsEngine.clearScreen()
            caption = Text(self.__caption_text, self.__caption_center, self.__caption_font)
            goal = Text(self.__goal_text, self.__goal_center, self.__goal_font)
            GE.GraphicsEngine.printText(caption)
            if criteria_matched:
                goal_ellipse = GE.GraphicsEngine.drawElip(goal.getRect(), "#9CB718")
                GE.GraphicsEngine.printText(goal)
            else:
                goal_ellipse = GE.GraphicsEngine.drawElip(goal.getRect(), "#739A56")
                GE.GraphicsEngine.printText(goal, 'black')
            player_circ = GE.GraphicsEngine.drawCirc((player_engine.getPos(), self.__player_radius), color='blue')
            GE.GraphicsEngine.drawCirc((enemy_engine.getPos(), self.__enemy_radius), color='red')

            player_engine.checkKeyPress()

            if enemy_engine.getPos().distance_to(player_engine.getPos()) <= self.__player_radius + self.__enemy_radius:
                won = False
                done = True
            elif goal_ellipse.findIntersection(player_circ) and criteria_matched:
                won = True
                done = True
            else:
                enemy_engine.moveTowards(player_engine.getPos())

            if player_engine.stepTime():
                collision = True
                bounce_time = 0
            enemy_engine.stepTime()                    

            GE.GraphicsEngine.printScreen()
            if won:
                done = True
        return won, self.__last_stage


def main() -> None:
    pass

if __name__ == "__main__":
    main()