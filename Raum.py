class Raum:

    def __init__(self, name, gegenstaende, text, unsichtbar):
        self.name = name
        self.gegenstaende = gegenstaende
        self.text = text
        self.unsichtbar = unsichtbar

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def get_gegenstaende(self):
        return self.gegenstaende

    def set_gegenstaende(self, neu):
        self.gegenstaende = neu

    def get_unsichtbar(self):
        return self.unsichtbar

    def set_unsichtbar(self, wert):
        self.unsichtbar = wert

    def print_gegenstaende(self):
        liste = "[  "
        for item in self.gegenstaende:
            if not item.get_unsichtbar():
                liste += item.get_name() + "  "
        liste += "]"
        return liste

    def enthalten(self, eingabe):
        for item in self.gegenstaende:
            if item.get_name() == eingabe:
                return True
        return False

    def gegenstand_finden(self, eingabe):
        for item in self.gegenstaende:
            if item.get_name() == eingabe:
                return item
        return None

    def schloss_oeffnen(self, schloss, text):
        if schloss is not None:
            print(text)
            schloss.oeffnen()
            self.gegenstaende.remove(schloss)
        else:
            print("Diesen Gegenstand gibt es in diesem Raum nicht.")



