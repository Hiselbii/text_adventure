import sys
from Spieler import Spieler
#from Game.Raum import Raum
#from Game.Gegenstand import Nehmbar
#from Game.Gegenstand import Moebel
#from Game.Gegenstand import Schloss
#from Game.Gegenstand import Zutat
from Raum import Raum
from Gegenstand import Nehmbar
from Gegenstand import Moebel
from Gegenstand import Schloss
from Gegenstand import Zutat
import json


def spielen():
    print("\n ~VOM ALTEN BLUT~ \n\n (1) Neues Spiel \n\n (2) Letzten Spielstand laden \n\n (3) Beenden\n")
    ein = ""
    while not (ein == "1" or ein == "2" or ein == "3"):
        ein = input("Wähle eine Option: ")
        if ein == "1":
            with open('NeuesSpiel.json', 'r') as fp:
                file = json.load(fp)
            print(file['prolog'])
        elif ein == "2":
            with open('Spielstand.json', 'r') as fp:
                file = json.load(fp)
        elif ein == "3":
            sys.exit(0)
        else:
            print("Gib 1, 2 oder 3 ein, je nachdem was du tun willst.")

    # Labor
    tisch = Moebel(file['labor_tisch_name'], file['labor_tisch_look'], file['labor_tisch_inter'])
    tafel = Moebel(file['labor_tafel_name'], file['labor_tafel_look'],file['labor_tafel_inter'])
    rechnungen = Nehmbar(file['labor_rechnungen_name'], file['labor_rechnungen_look'],
                         file['labor_rechnungen_unsichtbar'])
    notizen = Nehmbar(file['labor_notizen_name'], file['labor_notizen_look'], file['labor_notizen_unsichtbar'])
    karten = Nehmbar(file['labor_karten_name'], file['labor_karten_look'], file['labor_karten_unsichtbar'])
    alle_gegenstaende_labor = [
        tisch,
        tafel,
        rechnungen,
        notizen,
        karten
    ]
    gegenstaende_labor = []

    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['labor_gegenstaende']:
        for item in alle_gegenstaende_labor:
            if item.get_name() == name:
                gegenstaende_labor.append(item)

    labor = Raum(file['labor_name'], gegenstaende_labor, file['labor_look'], file['labor_unsichtbar'])

    # Keller
    inhalt_wand = [labor]
    wand = Schloss(file['keller_wand_name'], file['keller_wand_look'], file['keller_wand_inter'], inhalt_wand)
    brief_keller = Nehmbar(file['keller_brief_name'], file['keller_brief_look'], file['keller_brief_unsichtbar'])
    portal_buch = Moebel(file['keller_buch_name'], file['keller_buch_look'], file['keller_buch_inter'])

    alle_gegenstaende_keller = [
        wand,
        brief_keller,
        portal_buch,
    ]
    gegenstaende_keller = []
    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['keller_gegenstaende']:
        for item in alle_gegenstaende_keller:
            if item.get_name() == name:
                gegenstaende_keller.append(item)

    keller = Raum(file['keller_name'], gegenstaende_keller, file['keller_look'], file['keller_unsichtbar'])

    # Wohnzimmer
    regal = Moebel(file['wohnzimmer_regal_name'], file['wohnzimmer_regal_look'], file['wohnzimmer_regal_inter'])
    wichtbuch = Moebel(file['wohnzimmer_buch_name'], file['wohnzimmer_buch_look'], file['wohnzimmer_buch_inter'])
    schreibtisch = Moebel(file['wohnzimmer_tisch_name'], file['wohnzimmer_tisch_look'], file['wohnzimmer_tisch_inter'])
    schere = Nehmbar(file['wohnzimmer_schere_name'], file['wohnzimmer_schere_look'],
                     file['wohnzimmer_schere_unsichtbar'])
    brief = Nehmbar(file['wohnzimmer_brief_name'], file['wohnzimmer_brief_look'], file['wohnzimmer_brief_unsichtbar'])
    loch = Moebel(file['wohnzimmer_loch_name'], file['wohnzimmer_loch_look'], file['wohnzimmer_loch_inter'])
    inhalt_kellertuer = [keller]
    kellertuer = Schloss(file['wohnzimmer_tür_name'], file['wohnzimmer_tür_look'], file['wohnzimmer_tür_inter'],
                         inhalt_kellertuer)

    alle_gegenstaende_wohnzimmer = [
        regal,
        wichtbuch,
        schreibtisch,
        brief,
        loch,
        schere,
        kellertuer
    ]
    gegenstaende_wohnzimmer = []

    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['wohnzimmer_gegenstaende']:
        for item in alle_gegenstaende_wohnzimmer:
            if item.get_name() == name:
                gegenstaende_wohnzimmer.append(item)

    wohnzimmer = Raum(file['wohnzimmer_name'], gegenstaende_wohnzimmer, file['wohnzimmer_look'],
                      file['wohnzimmer_unsichtbar'])

    # Küche:
    schrank = Moebel(file['küche_schrank_name'], file['küche_schrank_look'], file['küche_schrank_inter'])
    traenkebuch = Moebel(file['küche_buch_name'], file['küche_buch_look'], file['küche_buch_inter'])
    kessel = Moebel(file['küche_kessel_name'], file['küche_kessel_look'], file['küche_kessel_inter'])
    drachenschuppen = Zutat(file['küche_schuppen_name'], file['küche_schuppen_look'], file['küche_schuppen_unsichtbar'])
    lerchenschnaebel =Zutat(file['küche_schnäbel_name'], file['küche_schnäbel_look'], file['küche_schnäbel_unsichtbar'])
    zugluwurz = Zutat(file['küche_wurz_name'], file['küche_wurz_look'], file['küche_wurz_unsichtbar'])
    nesselblumen = Zutat(file['küche_blumen_name'], file['küche_blumen_look'], file['küche_blumen_unsichtbar'])
    pfeffer = Zutat(file['küche_pfeffer_name'], file['küche_pfeffer_look'], file['küche_pfeffer_unsichtbar'])

    alle_gegenstaende_kueche = [
        drachenschuppen,
        lerchenschnaebel,
        zugluwurz,
        nesselblumen,
        pfeffer,
        traenkebuch,
        schrank,
        kessel
    ]
    gegenstaende_kueche = []
    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['küche_gegenstaende']:
        for item in alle_gegenstaende_kueche:
            if item.get_name() == name:
                gegenstaende_kueche.append(item)

    kueche = Raum(file['küche_name'], gegenstaende_kueche, file['küche_look'], file['küche_unsichtbar'])

    # Turm
    vogel = Nehmbar(file['turm_vogel_name'], file['turm_vogel_look'], file['turm_vogel_unsichtbar'])
    inhalt_kaefig = [vogel]
    kaefig = Schloss(file['turm_käfig_name'], file['turm_käfig_look'], file['turm_käfig_inter'], inhalt_kaefig)
    notiz = Nehmbar(file['turm_notiz_name'], file['turm_notiz_look'], file['turm_notiz_unsichtbar'])
    inhalt_kissen = [notiz]
    kissen = Schloss(file['turm_kissen_name'], file['turm_kissen_look'], file['turm_kissen_inter'], inhalt_kissen)

    alle_gegenstaende_turm = [
        kaefig,
        vogel,
        notiz,
        kissen
    ]

    gegenstaende_turm = []
    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['turm_gegenstaende']:
        for item in alle_gegenstaende_turm:
            if item.get_name() == name:
                gegenstaende_turm.append(item)

    turm = Raum(file['turm_name'], gegenstaende_turm, file['turm_look'], file['turm_unsichtbar'],)

    # Vorrautsraum
    zettel = Nehmbar(file['vorratsraum_zettel_name'], file['vorratsraum_zettel_look'],
                     file['vorratsraum_zettel_unsichtbar'])
    inhalt_truhe = [zettel]
    truhe = Schloss(file['vorratsraum_truhe_name'], file['vorratsraum_truhe_look'], file['vorratsraum_truhe_inter'],
                    inhalt_truhe)
    muffin = Nehmbar(file['vorratsraum_muffin_name'], file['vorratsraum_muffin_look'],
                     file['vorratsraum_muffin_unsichtbar'])
    brecheisen = Nehmbar(file['vorratsraum_brecheisen_name'], file['vorratsraum_brecheisen_look'],
                         file['vorratsraum_brecheisen_unsichtbar'])
    loch_vorrat = Moebel(file['vorratsraum_loch_name'], file['vorratsraum_loch_look'], file['vorratsraum_loch_inter'])
    korb = Nehmbar(file['vorratsraum_korb_name'], file['vorratsraum_korb_look'], file['vorratsraum_korb_unsichtbar'])

    alle_gegenstaende_vorratsraum = [
        truhe,
        zettel,
        muffin,
        brecheisen,
        loch_vorrat,
        korb
    ]

    gegenstaende_vorratsraum = []
    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['vorratsraum_gegenstaende']:
        for item in alle_gegenstaende_vorratsraum:
            if item.get_name() == name:
                gegenstaende_vorratsraum.append(item)

    vorratsraum = Raum(file['vorratsraum_name'], gegenstaende_vorratsraum, file['vorratsraum_look'],
                       file['vorratsraum_unsichtbar'])

    # Rest Gegenstände
    falle = Nehmbar(file['falle_name'], file['falle_look'], file['falle_unsichtbar'])
    schluessel = Nehmbar(file['schluessel_name'], file['schluessel_look'], file['schluessel_unsichtbar'])
    trank = Nehmbar(file['trank_name'], file['trank_look'], file['trank_unsichtbar'])

    rest_gegenstaende = {
        "Falle": falle,
        "Schlüssel": schluessel,
        "Trank": trank
    }

    raeume = [
        wohnzimmer,
        turm,
        kueche,
        vorratsraum,
        keller,
        labor
    ]

    # Init:
    alle_items = [
        rechnungen,
        notizen,
        karten,
        brief_keller,
        brief,
        schere,
        kellertuer,
        drachenschuppen,
        pfeffer,
        nesselblumen,
        lerchenschnaebel,
        zugluwurz,
        vogel,
        notiz,
        zettel,
        muffin,
        brecheisen,
        korb,
        falle,
        schluessel,
        trank
    ]

    inventar = []
    # Speicherstand von Liste an Gegenständen abrufen
    for name in file['inventar']:
        for item in alle_items:
            if item.get_name() == name:
                inventar.append(item)
    interaktionen = file['interaktionen']

    start_ort = ""
    for ort in raeume:
        if ort.get_name() == file['start_ort']:
            start_ort = ort
    done = False

    player = Spieler(start_ort, inventar, 0, file['truhe_offen'], file['wicht_gefangen'], rest_gegenstaende)

    entscheidung = ""

    while not done:

        aktion = input(interaktionen).strip()
        if aktion == "1":
            anschauen = input("Anschauen: ").strip()
            if anschauen == "Alles" or anschauen == "alles":
                print(player.get_raum().get_text())
            else:
                player.anschauen(anschauen)

        elif aktion == "2":
            benutze = input("Benutze: ").strip()
            mit = input("Mit: ").strip()

            player.benutzen_mit(benutze, mit)

        elif aktion == "3":
            interagieren = input("Interagiere mit: ").strip()
            player.interagieren(interagieren)

        elif aktion == "4":
            gehen = input("Gehe zu: ").strip()
            raum_begehbar = False
            for raum in raeume:
                if raum.get_name() == gehen and not raum.get_unsichtbar():
                    player.set_raum(raum)
                    raum_begehbar = True
                    if raum == kueche:
                        print("Ich bin jetzt in der Küche.")
                    else:
                        print("Ich bin jetzt im " + raum.get_name() + ".")

            if not raum_begehbar:
                print("Da kann ich nicht hingehen. Man kann nach " + print_raeume(raeume) + " gehen.")

        elif aktion == "0":
            player.meine_tasche()

        elif aktion == "9":
            done = True

            # Speichern von Gegenständen in den Räumen und dem Inventar

            file['labor_gegenstaende'] = []
            for item in labor.get_gegenstaende():
                file['labor_gegenstaende'].append(item.get_name())

            file['keller_gegenstaende'] = []
            for item in keller.get_gegenstaende():
                file['keller_gegenstaende'].append(item.get_name())

            file['wohnzimmer_gegenstaende'] = []
            for item in wohnzimmer.get_gegenstaende():
                file['wohnzimmer_gegenstaende'].append(item.get_name())

            file['küche_gegenstaende'] = []
            for item in kueche.get_gegenstaende():
                file['küche_gegenstaende'].append(item.get_name())

            file['turm_gegenstaende'] = []
            for item in turm.get_gegenstaende():
                file['turm_gegenstaende'].append(item.get_name())

            file['vorratsraum_gegenstaende'] = []
            for item in vorratsraum.get_gegenstaende():
                file['vorratsraum_gegenstaende'].append(item.get_name())

            file['inventar'] = []
            for item in player.get_inventar():
                file['inventar'].append(item.get_name())

            file['start_ort'] = player.raum.get_name()
            file['turm_vogel_unsichtbar'] = vogel.get_unsichtbar()
            file['turm_notiz_unsichtbar'] = notiz.get_unsichtbar()
            file['vorratsraum_zettel_unsichtbar'] = zettel.get_unsichtbar()
            file['falle_unsichtbar'] = falle.get_unsichtbar()
            file['trank_unsichtbar'] = trank.get_unsichtbar()
            file['schluessel_unsichtbar'] = schluessel.get_unsichtbar()
            file['labor_unsichtbar'] = labor.get_unsichtbar()
            file['keller_unsichtbar'] = keller.get_unsichtbar()
            file['truhe_offen'] = player.get_truhe_offen()
            file['wicht_gefangen'] = player.get_wicht_gefangen()

            with open('Spielstand.json', 'w') as fp:
                json.dump(file, fp)
            sys.exit(0)

        else:
            print("Hey, ich kann halt nur fünf Sachen machen.")

        rechnung_im_inventar = player.enthalten_inventar("Rechnungen")
        notizen_im_inventar = player.enthalten_inventar("Notizen")
        karten_im_inventar = player.enthalten_inventar("Karten")
        if rechnung_im_inventar and notizen_im_inventar and karten_im_inventar:
            done = True
            print("\n")
            print(file['ende'])
            entscheidung = input("(1) Der Köngin die Wahrheit sagen              (2) Torgows Wissen vernichten:\n")

    fertig = False
    while not fertig:
        if entscheidung == "1":
            print(file['endscheidung_wahr'])
            fertig = True
            sys.exit(0)
        elif entscheidung == "2":
            print(file['endscheidung_lüge'])
            fertig = True
            sys.exit(0)
        else:
            entscheidung = input("Gib 1 oder 2 ein:")


def print_raeume(raeume):
    text = "[  "
    for raum in raeume:
        if not raum.get_unsichtbar():
            text += raum.get_name() + "  "
    text += "]"
    return text


def print_inventar(inventar):
    text = "[  "
    for item in inventar:
        text += item.get_name() + "  "
    text += "]"
    return text


spielen()
