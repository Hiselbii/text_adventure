class Gegenstand:

    def __init__(self, name, text_look):
        self.name = name
        self.text_look = text_look

    def get_text_look(self):
        return self.text_look

    def get_name(self):
        return self.name

    def set_text_look(self, wert):
        self.text_look = wert

    def get_unsichtbar(self):
        return False


class Nehmbar(Gegenstand):

    def __init__(self, name, text_look, unsichtbar):
        super().__init__(name, text_look)
        self.unsichtbar = unsichtbar

    def get_unsichtbar(self):
        return self.unsichtbar

    def set_unsichtbar(self, wert):
        self.unsichtbar = wert


class Zutat(Nehmbar):

    def __init__(self, name, text_look, unsichtbar):
        super().__init__(name, text_look, unsichtbar)


class Moebel(Gegenstand):

    def __init__(self, name, text_look, text_interact):
        super().__init__(name, text_look)
        self.text_interact = text_interact

    def get_text_interact(self):
        return self.text_interact

    def set_text_interact(self, wert):
        self.text_interact = wert


class Schloss(Moebel):

    def __init__(self, name, text_look, text_interact, inhalt):
        super().__init__(name, text_look, text_interact)
        self.inhalt = inhalt

    def oeffnen(self):
        for item in self.inhalt:
            item.unsichtbar = False



