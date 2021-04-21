class SportScreen:
    def __init__(self, screen):
        self.screen = screen

    def display(self, msg):
        self.screen.clear()
        self.screen.print_at(msg, 0, 0)
        self.screen.refresh()
