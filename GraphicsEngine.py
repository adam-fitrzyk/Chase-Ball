from pygame import Vector2, Surface, Rect, Color, display, draw, quit, init, RESIZABLE
from Shapes import Circle, Ellipse
import ChaseBallDB as DB

class GraphEngine():
    '''Graphics Engine Class for running game graphics. '''

    def __new__(cls):
        try:
            GraphEngine.instance
        except:
            GraphEngine.instance = super(GraphEngine, cls).__new__(cls)
        return GraphEngine.instance

    def __init__(self) -> None:
        '''Constructor Method for Graphics Engine Class '''
        self.setSettings(DB.ChaseBallDB().getVideoSettings())
        init()
        self.__screen = display.set_mode(self.__getScreenSize(), self.getWindowFlag())
        display.set_caption(self.getWindowCaption())
        self.setScreenSize()

    # Getters / Setters ----------------------------------------

    def setSettings(self, settings:dict[str:any]=None) -> None:
        if settings:
            for setting in settings:
                match setting:
                    case 'backgroundColor':
                        self.__background_color = settings[setting]
                    case 'defaultTextSize':
                        self.__default_text_size = settings[setting]
                    case 'defaultTextFont':
                        self.__default_text_font = settings[setting]
                    case 'defaultTextColor':
                        self.__default_text_color = settings[setting]
                    case 'screenSizeX':
                        self.__screen_size_x = settings[setting]
                    case 'screenSizeY':
                        self.__screen_size_y = settings[setting]
                    case 'windowFlag':
                        if settings[setting]:
                            self.__window_flag = settings[setting]
                        else:
                            self.__window_flag = RESIZABLE
                    case 'FPS':
                        if settings[setting]:
                            self.__FPS = settings[setting]
                        else:
                            self.__FPS = 60
                    case 'windowCaption':
                        self.__window_caption = settings[setting]

    def setScreenSize(self) -> None:
        self.__screen_width = self.__screen.get_width()
        self.__screen_height = self.__screen.get_height()

    def getScreen(self) -> Surface:
        return self.__screen

    def getScreenWidth(self) -> int:
        return self.__screen_width
    
    def getScreenHeight(self) -> int:
        return self.__screen_height
    
    def getBackgroundColor(self) -> str:
        try:
            return self.__background_color
        except:
            return 'purple'
        
    def getDefaultTextSize(self) -> str:
        try:
            return self.__default_text_size
        except:
            return 32

    def getDefaultTextColor(self) -> str:
        try:
            return self.__default_text_color
        except:
            return 'cornsilk'
        
    def getDefaultTextFont(self) -> str:
        try:
            return self.__default_text_font
        except:
            return 'freesansbold.ttf'

    def __getScreenSize(self) -> tuple[int, int] | None:
        '''Returns tuple of (width, height) values of screen size '''
        try:
            return (self.__screen_size_x, self.__screen_size_y)
        except:
            return (0, 0)

    def getWindowFlag(self) -> int:
        try:
            return self.__window_flag
        except:
            return RESIZABLE
        
    def getWindowCaption(self) -> str | None:
        try:
            return self.__window_caption
        except:
            return ''
 
    def getFPS(self) -> int:
        return self.__FPS
    
    # Functionality ---------------------------------------------------------

    def clearScreen(self) -> None:
        self.__screen.fill(self.getBackgroundColor())

    def printScreen(self) -> None:
        display.flip()

    def printText(self, texts=None, color:str=None) -> None:
        '''Prints list of Text objects onto screen '''
        if not color:
            color = Color(self.getDefaultTextColor())
        if type(texts) == list:
            for text in texts:
                text.blitText(self.__screen_width, color)
        else:
            texts.blitText(self.__screen_width, color)

    def drawRect(self, rect:Rect, color:str='black') -> Rect:
        '''Draws a rectangle on screen. '''
        color = Color(color)
        return draw.rect(self.__screen, color, rect)

    def drawCirc(self, centre_radius:tuple[tuple|Vector2, int]=None, rect:Rect=None, color:str='black') -> Circle:
        '''Draws a circle on screen using either centre and radius data (returns Rect object of drawn shape) or Rect object data '''
        color = Color(color)
        if centre_radius:
            return Circle(draw.circle(self.__screen, color, centre_radius[0], centre_radius[1]))
        elif rect:
            return Circle(draw.circle(self.__screen, color, rect.center, rect.height // 2))
    
    def drawElip(self, rect:Rect, color:str='black') -> Ellipse:
        '''Draws an ellipse on screen '''
        color = Color(color)
        return Ellipse(draw.ellipse(self.__screen, color, rect))

    def quitPG(self) -> None:
        '''Terminates PyGame module '''
        quit()

GraphicsEngine = GraphEngine()


def main() -> None:
    ge = GraphicsEngine
    ge.clearScreen()
    ge.drawCirc(((200, 200), 20), color='red')
    ge.printScreen()
    from time import sleep
    sleep(1)
    ge.quitPG()

if __name__ == "__main__":
    main()