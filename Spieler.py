from operator import xor
#from Game.Gegenstand import Moebel
#from Game.Gegenstand import Nehmbar
#from Game.Gegenstand import Schloss
#from Game.Gegenstand import Zutat
from Gegenstand import Moebel
from Gegenstand import Nehmbar
from Gegenstand import Schloss
from Gegenstand import Zutat
from random import randint


class Spieler:

    def __init__(self, raum, inventar, zutaten_count,truhe_offen, wicht_gefangen, rest_gegenstaende):
        self.raum = raum
        self.inventar = inventar
        self.zutaten_count = zutaten_count
        self.truhe_offen= truhe_offen
        self.wicht_gefangen = wicht_gefangen
        self.rest_gegenstaende = rest_gegenstaende

    def anschauen(self, eingabe):
        gegenstand = ""
        # Ist der Gegenstand im Inventar
        im_inventar = False
        for ding in self.inventar:
            if ding.get_name() == eingabe:
                im_inventar = True
                gegenstand = ding

        # Ist der Gegenstand im Raum
        im_raum = False
        for item in self.get_raum().get_gegenstaende():
            if item.get_name() == eingabe:
                im_raum = True
                gegenstand = item

        if im_raum or im_inventar:
            print(gegenstand.get_text_look())
        else:
            print("Das seh ich hier nicht, in diesem Raum gibt es nur: " + self.get_raum().print_gegenstaende())

    def benutzen_mit(self, benutze, mit):

        # Vogelrätsel Käfig öffnen
        if (benutze == "Brecheisen" and mit == "Käfig") or (
                benutze == "Käfig" and mit == "Brecheisen"):
            if self.enthalten_inventar("Brecheisen"):
                self.raum.schloss_oeffnen(self.raum.gegenstand_finden("Käfig"),
                                          "Ich konnte die Käfigtür mit dem Brecheisen aufbiegen. Doch gerade als ich "
                                          "in den Käfig greifen wollte, "
                                          "\nhat sich das kleine Vögelchen so erschrocken, dass es losgeflogen ist und"
                                          " den Schlüssel "
                                          "\nmit einem gewaltigen Satz heruntergeschluckt hat. Jetzt liegt er röchelnd"
                                          " auf dem Boden des Käfigs.")
                self.inventar.remove(self.finden_inventar("Brecheisen"))
            else:
                print("Das hab ich nicht in meiner Tasche.")

        # Notiz unterm Kissen
        elif (benutze == "Kissen" and mit == "Schere") or (
                benutze == "Schere" and mit == "Kissen"):
            if self.enthalten_inventar("Schere"):
                self.raum.schloss_oeffnen(self.raum.gegenstand_finden("Kissen"), "Ich habe das Kissen weggeschnitten. "
                                                                                 "Darunter liegt eine Notiz.")
                self.inventar.remove(self.finden_inventar("Schere"))
            else:
                print("Das hab ich nicht in meiner Tasche.")

        # Vogelrätsel Zaubertrank
        elif xor(benutze == "Kessel", mit == "Kessel") and xor(isinstance(self.finden_inventar(mit), Zutat), isinstance(self.finden_inventar(benutze), Zutat)):

            pot = ""
            zutat = ""
            if benutze == "Kessel":
                pot = self.raum.gegenstand_finden(benutze)
                zutat = self.finden_inventar(mit)
            else:
                pot = self.raum.gegenstand_finden(mit)
                zutat = self.finden_inventar(benutze)

            if self.enthalten_inventar(zutat.get_name()):
                if self.get_zutaten_count() < 2:
                    self.inventar.remove(zutat)
                    print("So, das kommt in den Kessel.")
                    self.zutaten_count += 1
                else:
                    self.inventar.remove(zutat)

                    trank = self.rest_gegenstaende["Trank"]
                    trank.set_unsichtbar(False)
                    print("Der Trank ist fertig, er sieht aber nicht sehr genießbar aus. Ich kann einfach nicht "
                          "kochen, \nalles was ich mache wird schrecklich. Deshalb bin ich so gut im Gifte brauen. "
                          "\nAber für einen weiteren Versuch habe ich nicht mehr genügend Zutaten.")

                    inventar_ohne_zutaten = []

                    for item in self.inventar:
                        if not isinstance(item, Zutat):
                            inventar_ohne_zutaten.append(item)

                    inventar_ohne_zutaten.append(trank)
                    self.inventar = inventar_ohne_zutaten

                    gegenstaede_ohne_zutaten = []
                    for ding in self.raum.get_gegenstaende():
                        if not isinstance(ding, Zutat):
                            gegenstaede_ohne_zutaten.append(ding)
                    self.raum.set_gegenstaende(gegenstaede_ohne_zutaten)

                    self.raum.get_gegenstaende().remove(pot)

            else:
                print("Das hab ich nicht in der Tasche.")

        # Vogelrätsel Trank dem Vogel geben
        elif (benutze == "Vogel" and mit == "Trank des ewigen Todes") or (
                benutze == "Trank des ewigen Todes" and mit == "Vogel"):
            if self.enthalten_inventar("Vogel") and self.enthalten_inventar("Trank des ewigen Todes"):
                print("Oh, das sieht gar nicht gut aus, ich glaub er ist gestorben... Oh Gott, aber irgendwie muss "
                      "\nich an den Schlussel kommen. Oh nein, iiiihgitt igitt. Ist das schleimig. Uhhh. \nIch will nie"
                      " wieder davon reden, was gerade passsiert ist.")
                self.inventar.remove(self.finden_inventar("Vogel"))
                self.inventar.remove(self.finden_inventar("Trank des ewigen Todes"))
                schluessel = self.rest_gegenstaende["Schlüssel"]
                schluessel.set_unsichtbar(False)
                self.inventar.append(schluessel)
            else:
                print("Das hab ich nicht in meiner Tasche.")

        # Vogelrätsel Truhe öffnen
        elif (benutze == "Schlüssel" and mit == "Truhe") or (
                benutze == "Truhe" and mit == "Schlüssel"):
            if self.enthalten_inventar("Schlüssel"):
                self.raum.schloss_oeffnen(self.raum.gegenstand_finden("Truhe"), "Die wackelnde Truhe geht auf. Zu "
                                                                                "meinem großen Schrecken springt mir "
                                                                                "plötzlich "
                                                                                "ein Wicht mit \neinem "
                                                                                "lauten Kriegerschrei ins Gesicht "
                                                                                "und "
                                                                                "verschwindet dann in einem Loch in "
                                                                                "der Wand. \nNachdem ich mich von "
                                                                                "diesem Schock erholt habe, "
                                                                                "bin ich mir sicher, dieser Wicht "
                                                                                "\nweiß etwas zu "
                                                                                "Torgows Plänen."
                                                                                "\nSonst ist die Truhe leer, "
                                                                                "bis auf einen kleinen "
                                                                                "knittrigen Zettel.")
                self.inventar.remove(self.finden_inventar("Schlüssel"))
                self.truhe_offen = True

            else:
                print("Das hab ich nicht in meiner Tasche.")

        # Wichträtsel Falle bauen
        elif (benutze == "Korb" and mit == "Muffin") or (
                benutze == "Muffin" and mit == "Korb"):
            if self.enthalten_inventar("Korb") and self.enthalten_inventar("Muffin"):
                print("Daraus lässt sich sicher etwas tolles bauen.")
                self.inventar.remove(self.finden_inventar("Korb"))
                self.inventar.remove(self.finden_inventar("Muffin"))
                falle = self.rest_gegenstaende["Falle"]
                falle.set_unsichtbar(False)
                self.inventar.append(falle)
            else:
                print("Das hab ich nicht in meiner Tasche.")

        # Wichträtsel Wicht fangen
        elif (benutze == "Loch" and mit == "Falle") or (
                benutze == "Falle" and mit == "Loch"):
            if self.enthalten_inventar("Falle") and self.truhe_offen:
                print("Nach einigem Warten höre ich leises Grunzen aus der Falle. Noch gerade im Richtigen Moment "
                      "\nerwischte ich den Wicht am Schlawitchen. Er schreit und nörgelt. Ich muss ihn lange "
                      "schütteln, "
                      "\nbis er endlich mit etwas nützlichem herausrückt. Das Passwort für die Kellertür ist \""
                      "Schnutzipu\"")
                self.inventar.remove(self.finden_inventar("Falle"))
                self.wicht_gefangen = True
            else:
                print("Im Loch ist nichts, dass ich fangen könnte.")

        # Wichträtsel Keller öffnen
        elif (benutze == "Tür" and mit == "Schnutzipu") or (
                benutze == "Schnutzipu" and mit == "Tür"):
            if self.wicht_gefangen:
                self.raum.schloss_oeffnen(self.raum.gegenstand_finden("Tür"), "Die Kellertür ist jetzt offen.")
            else:
                print("Was soll ich sagen?")

        # Kellerrätsel Labor öffnen
        elif (benutze == "Wand" and mit == "pifropschnuk") or (
                benutze == "pifropschnuk" and mit == "Wand"):
            self.raum.schloss_oeffnen(self.raum.gegenstand_finden("Wand"), "Vor mir bricht die Luft in weiße Flammen "
                                                                           "aus, dann spalten sich das Feuer "
                                                                           "plötzlich und "
                                                                           "bilden \neinen Kreis. Das innere des "
                                                                           "Kreises sieht aus wie tiefes, "
                                                                           "schwarzes Wasser. \nEs ist so dunkel, "
                                                                           "dass es das Licht aus dem Raum zu saugen "
                                                                           "scheint. \nDas muss das Portal zu Torgows "
                                                                           "geheimem Labor sein.")
        else:
            nicht_kombinierbar = [
                "Die beiden Sachen kann man nicht kombinieren.", "Das geht leider nicht.",
                "Ich weiß nicht, wie ich das zusammenkleben soll.", "So wird das nichts.", "Lieber nicht.",
                "Das wäre zwar witzig, bringt mir aber nichts"
            ]
            index = randint(0, len(nicht_kombinierbar) -1)
            print(nicht_kombinierbar[index])

    def interagieren(self, eingabe):

        # Ist der Gegenstand im Raum?
        gegenstand = ""
        for item in self.raum.get_gegenstaende():
            if eingabe == item.get_name():
                gegenstand = item

        if gegenstand != "":
            if not gegenstand.get_unsichtbar():
                if isinstance(gegenstand, Nehmbar):
                    if gegenstand.get_name() == "Rechnungen" or gegenstand.get_name() == "Notizen" or gegenstand.get_name() == "Karten":
                        print(gegenstand.get_text_look())
                    else:
                        print("Das kommt in meine Tasche.")
                    self.inventar.append(gegenstand)
                    self.raum.get_gegenstaende().remove(gegenstand)
                elif isinstance(gegenstand, Moebel) or isinstance(gegenstand, Schloss):
                    print(gegenstand.get_text_interact())
        else:
            # Ist der Gegenstand im Inventar?
            for ding in self.get_inventar():
                if eingabe == ding.get_name():
                    gegenstand = ding

            if gegenstand != "":
                print("Das ist schon in meiner Tasche.")
            else:
                print("Diesen Gegenstand seh ich nicht, hier gibt es nur: " + self.raum.print_gegenstaende())

    def set_raum(self, neuer_raum):
        self.raum = neuer_raum

    def get_raum(self):
        return self.raum

    def get_inventar(self):
        return self.inventar

    def set_inventar(self, neu):
        self.inventar = neu

    def print_inventar(self):
        ergebnis = "[  "
        for item in self.inventar:
            ergebnis += item.get_name() + "  "

        ergebnis += "]"
        return ergebnis

    def enthalten_inventar(self, eingabe):
        for item in self.inventar:
            if item.get_name() == eingabe:
                return True
        return False

    def finden_inventar(self, eingabe):
        for item in self.inventar:
            if item.get_name() == eingabe:
                return item
        return None

    def get_zutaten_count(self):
        return self.zutaten_count

    def meine_tasche(self):
        print("In meiner Tasche ist: " + self.print_inventar())

    def get_truhe_offen(self):
        return self.truhe_offen

    def get_wicht_gefangen(self):
        return self.wicht_gefangen

