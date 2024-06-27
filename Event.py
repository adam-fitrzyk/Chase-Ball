from pygame import Rect, event as pgevent
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION

class Event:
    '''Event Class that polls for events '''

    def __init__(self) -> None:
        pass

    # Functional -----------------------------------------------------------------

    def poll(self, activation_areas:list[Rect]=None) -> int | tuple[Rect, str] | None:
        '''
        Checks every event and returns where and which if one has happened.
        Checks:
            close window -> -1,
            left click -> 'click',
            mouse movement -> 'hover'
        '''
        for event in pgevent.get([QUIT, MOUSEBUTTONDOWN, MOUSEMOTION]):
            if event.type == QUIT:
                return -1
            elif activation_areas:
                events = self.checkEvent(event, activation_areas)
                if events:
                    return events
                
    # Functions to check certain types of events ----------------------------------
                
    def checkEvent(self, event, activation_areas):
        retlist = []
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            button_pressed = self.checkClick(event, activation_areas)
            if button_pressed:
                retlist.append((button_pressed, "click"))
        if event.type == MOUSEMOTION:
            hoverbox_activated = self.checkHover(event, activation_areas)
            if hoverbox_activated:
                retlist.append((hoverbox_activated, "hover"))
        return retlist if len(retlist) > 0 else None
    
    def checkClick(self, event, buttons:list[Rect]=None) -> Rect:
        '''Returns Rect object if it was clicked '''
        for button in buttons:
            if button.collidepoint(event.pos):
                return button

    def checkHover(self, event, boxes:list[Rect]=None) -> Rect:
        '''Returns Rect object if the mouse is hovering over it '''
        for box in boxes:
            if box.collidepoint(event.pos):
                return box
                
def main() -> None:
    while True:
        from pygame.draw import rect
        from GraphicsEngine import GraphicsEngine
        from time import sleep
        ge = GraphicsEngine()
        ge.init()
        event = Event().poll([rect(ge.getScreen(), 'red', Rect(100, 100, 200, 200))])
        if event == -1:
            print('exited successfully')
            break
        sleep(0.01)

if __name__ == "__main__":
    main()