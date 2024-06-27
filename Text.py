from pygame import Rect
from pygame.font import Font
import GraphicsEngine as GE

class Text():
    '''Text Object for displaying text on pygame screen '''

    def __init__(self, text:str=None, center:tuple[int,int]=None, font:tuple[str,int]=None) -> None:
        '''Constructor method for Text Object'''
        self.setText(text)
        self.setFont(font)
        self.setCenter(center)
        self.setSize()

    # Getters / Setters --------------------

    def setText(self, text=None) -> None:
        if text:
            self.__text = text
        else:
            self.__text = "Unknown text"

    def setFont(self, font) -> None:
        if font:
            if not font[0]:
                font_name = GE.GraphicsEngine.getDefaultTextFont()
            else:
                font_name = font[0]
            if not font[1]:
                font_size = GE.GraphicsEngine.getDefaultTextSize()
            else:
                font_size = font[1]
        else:
            font_name, font_size = GE.GraphicsEngine.getDefaultTextFont(), GE.GraphicsEngine.getDefaultTextSize()
        self.__font = Font(font_name, font_size)

    def setColor(self, color=None) -> None:
        if color:
            self.__color = color
        else:
            self.__color = GE.GraphicsEngine.getDefaultTextColor()

    def setCenter(self, center) -> None:
        if center:
            self.__center = center
        else:
            self.__center = (GE.GraphicsEngine.getScreenWidth()//2, GE.GraphicsEngine.getScreenHeight()//2)

    def setSize(self) -> None:
        '''Calculate number of lines, the length of each line, the height of a line of text, and the width of the longest line '''
        lines = self.getText().splitlines()
        num_lines = len(lines)
        line_widths = {}
        text_height = self.getFont().size(' ')[1]
        line_width = 0
        for index, line in enumerate(lines):
            for letter in line:
                line_width += self.getFont().size(letter)[0]
            line_widths[index] = line_width
            line_width = 0
        longest_line_width = 0
        for index in line_widths:
            if longest_line_width < line_widths[index]:
                longest_line_width = line_widths[index]
        self.__text_height = text_height
        self.__num_lines = num_lines
        self.__line_widths = line_widths
        self.__longest_line_width = longest_line_width
    
    def getText(self) -> str:
        return self.__text

    def getFont(self) -> Font:
        return self.__font
    
    def getTextHeight(self) -> int:
        return self.__text_height
    
    def getNumLines(self) -> int:
        return self.__num_lines
    
    def getLineWidths(self) -> dict[int: int]:
        '''Returns a dictionary with each entry being in the form (line index) : (length of line in pixels) '''
        return self.__line_widths
    
    def getLongestLineWidth(self) -> int:
        return self.__longest_line_width
    
    def getCenter(self) -> tuple[int, int]:
        '''Returns tuple of (x, y) coordinates of center '''
        return self.__center
    
    def getRect(self) -> Rect:
        '''Returns a Rect object '''
        '''Create Rect object '''
        margin = 30 * (1 - 1.01**(-self.getLongestLineWidth()))
        return Rect(
            self.getCenter()[0] - (self.getLongestLineWidth() // 2) - margin,
            self.getCenter()[1] - (self.getTextHeight()*self.getNumLines() // 2) - margin,
            self.getLongestLineWidth() + margin * 2,
            self.getTextHeight() * self.getNumLines() + margin * 2
        )
    
    # Functional -----------------------------------------------

    def blitText(self, max_width, color) -> None:
        '''Print text onto screen, centered and complying with a maximum width'''
        if not max_width:
            max_width = GE.GraphicsEngine.getScreenWidth()
        lines = [line.split(' ') for line in self.getText().splitlines()]  # 2D array where each row is a list of words.
        space_width = self.getFont().size(' ')[0]  # The width of a space and font word_height.
        
        if self.getLongestLineWidth() > max_width:
            x_default = self.getCenter()[0] - (max_width//2)
        else:
            x_default = self.getCenter()[0] - (self.getLongestLineWidth()//2)
        x = x_default
        y = self.getCenter()[1] - (self.getTextHeight()*self.getNumLines()//2 + 5*(self.getNumLines() - 1))

        for line in lines:
            for word in line:
                word_surface = self.getFont().render(word, None, color)
                word_width = word_surface.get_width()
                if x_default - x + word_width >= max_width:
                    x = x_default  # Reset the x.
                    y += self.getTextHeight()  # Start on new row.
                GE.GraphicsEngine.getScreen().blit(word_surface, (x, y))
                x += word_width + space_width
            x = x_default  # Reset the x.
            y += self.getTextHeight() + 5  # Start on new row.

def main() -> None:
    import pygame
    from time import sleep
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill('purple')
    mytext = Text("Hello World!\nThis is my game!!!\nAnother line!", (screen.get_width() // 2, screen.get_height() // 2), ('freesansbold.ttf', 32))
    print(mytext.getCenter())
    print(mytext.getLineWidths())
    print(mytext.getLongestLineWidth())
    GE.GraphicsEngine.printText([mytext])
    pygame.display.flip()
    sleep(5)
    pygame.quit()

if __name__ == "__main__":
    main()