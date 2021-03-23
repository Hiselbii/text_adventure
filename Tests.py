import json

alle_sachen = {
    "prolog": "\nProlog: \n\nChroniken von Naur, im Jahre 1121: \n\n\"Schon solange sich irgendjemand erinnern kann, "
              "manche sagen sogar seit der Mond auf die Erde \nstürzte und den ganzen Kontinent Aldir "
              "versenkten, "
              "sind die Königreiche Naur und Dagor im Krieg. \nBeide behaupten, die anderen seinen Einwanderer "
              "aus Aldir "
              "und hätten "
              "kein Anrecht auf des Land.\nSelbst, wenn es so wirkte, als wäre endlich Frieden "
              "eingekehrt. Selbst wenn die Könige Verträge \nunterzeichneten und alle hoch und heilig schworen, "
              "die Konflikte beizulegen, ging es nach mindestens \neiner Woche wieder von vorne los. Sei es, "
              "weil der Cousin des Dagor-Königs den Lieblingskuchen des \nPrinzen wegstibitzte oder weil seine "
              "Heiligkeit "
              "der obersten Priester sich beim Festmahl dem Wein etwas \nzu ausgiebig frönte und inbrünstig das "
              "Kinderlied „Der dumme Naurer“ anstimmte. Und weil es eben \nschon immer so gewesen war, "
              "wunderte das auch "
              "niemanden. \n \nSo trug es sich also auch bei den letzten Verhandlungen ähnlich zu. Die "
              "Triumpfkutsche "
              "des höchsten\ndagorischen Admirals wurde demoliert vorgefunden. Weswegen kurze Zeit "
              "später \ndie "
              "Streitereien wieder los gingen. Doch eine Magd vertraute Königin der Naur an, dass sie in "
              "der\nNähe der Ställe zuvor einen seltsamen Gnom gesehen hatte. So begann die Königin zu "
              "bezweifeln, "
              "\ndass die Kutsche von den Nauren oder den Dagorern zerstört wurde. \nIrgendjemand wollte "
              "scheinbar "
              "verhindern, dass die Königreiche Frieden schlossen. Aber wer? \n\nNach langen Nachforschungen "
              "der Spione "
              "der Königin wurde ein Verdächtiger entdeckt: \nDer legendäre, geniale, aber auch ein wenig "
              "verrückte Magier "
              "Torgow. Die Spionin und Ermittlerin Lin \nwurde in einem gewaltigen Wald , tief in den Bergen "
              "der Nebelhöhe "
              "entsandt, um ihn zu finden. \nAber als sie nach langem Suchen seine Hütte fand, was Torgow "
              "verschwunden. "
              "\nDoch vielleicht finden sich in seiner Behausung Hinweise darauf, was der alte Kauz ausheckte... "
              "\"\n\n\nVorsichtig öffnet Lin die Türe des Häuschens und betriff das Wohnzimmer des Magiers. "
              "\nWas "
              "möchtest du nun tun, Lin?\n\nHinweis: Mit Anschauen: Alles kannst du den ganzen Raum betrachten.",
    "interaktionen": "------------------------------------------------------------------------------------------------"
                     "-----\n(1) Anschauen             (2) Benutzen mit             (3) Interagieren             "
                     "(4) Gehe zu \n(0) Inventar              (9) Speichern und Beenden \n-----------------------------"
                     "-------------"
                     "-----------------------------------------------------------\n",
    "start_ort": "Wohnzimmer",
    "ende": "Ich glaube ich verstehe langsam.... Das alte Blut, davon habe ich schonmal etwas gehört. \nMeine "
            "Königin Navlia hat einmal erwähnt, dass ihre Familie und die Königsfamilie von Dagor \nangeblich "
            "vom "
            "alten Blut sein sollen. Sie tat es als Unsinn ab, aber was, wenn es wahr ist? \nDas alte Blut kommt "
            "aus Aldir und Torgow ist davon überzeugt, dass auch Naurs und Dagors \nKultur ursprünglich von dort "
            "sind. Das gewöhnliche Volk wird sich schnell mit den Einheimischen \nvermischt haben, "
            "aber die Königshäuser sind stolz auf ihre adelige Blutlinie. \nSie könnten das alte Blut noch in "
            "sich tragen. \n\nUnd wenn seine Berechnungen stimmen und der Fall des Mondes nicht für Aldirs "
            "Untergang \nverantwortlich ist, dann war vielleicht wirklich das alte Blut daran schuld. Ich habs. "
            "\nDavor hatte er Angst, die Friedensverträge. In ihnen war immer vereinbart, dass viele dutzend "
            "\nAdlige "
            "aus dem Dagorgeschlecht mit Nauren des Königshauses verheiratet werden sollten. \nAllein fließt "
            "eindeutig nicht genug altes Blut in den Familien, aber würden sie sich \nmischen, könnte ein Kind "
            "des alten Blutes geboren werden. Dieses Kind könnte entweder das \nwundervollste Geschöpf unserer "
            "Zeit werden oder aber unser größter Albtraum. Und so wie ich \ndie Nauren kenne, werden sie sicher "
            "versuchen ein Kind des alten Blutes zu schaffen, wenn sie \ndieses Wissen einmal haben. \n\nEs ist "
            "nun "
            "meine Entscheidung: \nEntweder ich bringe diese Neuigkeiten zu meiner Königin, um Frieden zu "
            "erlangen \noder ich vernichte all dieses Wissen und verhindere damit, dass vielleicht auch diesen "
            "Kontinent \nvon einen Verrückten des alten Blutes verstört wird. \n\n",
    "endscheidung_wahr": "\n\nIch kehrte also du meiner Königin zurück und berichtete ihr von der Wahrheit über \n"
                         "Torgows"
                         " Pläne. Sogleich erklärte Königin Navlia die Situation "
                         "den "
                         "anderen Adligen. \nSie konnte sie mit den neusten Ereignissen davon überzeugen, \n"
                         "dass die beiden Königreiche gemeinsam stärker sind. So kam es zu einem Frieden. \nNatürlich"
                         " versuchte Torgow weiter die Hochzeiten zu verhindern. Doch es \nwar zu spät. \nBei einem "
                         "gewaltigen Fest wurden hunderte von Nauren und Dagorern \nvermählt. All dies führte auch zu "
                         "einem "
                         "neuen Konflikt. \nDie einen waren Navlias Seite und glauben mit einem Kind des \nalten Blutes"
                         " würden die "
                         "Königreiche eine Waffe besitzen, mit der sie \nsich die ganze Welt zum Untertan machen "
                         "könnten. "
                         "\nDie "
                         "anderen wollen jedes solches Kind töten, für sie war die Gefahr zu gewaltig. \nDas war "
                         "nicht was ich "
                         "wollte, ich wollte nur Frieden, aber \nscheinbar ist alles nur eine Vorbereitung auf einen "
                         "noch "
                         "viel größeren Krieg. \nDoch nicht umsonst bin ich die beste Spionin im ganzen Land. \nEs "
                         "fällt mir schwer mich gegen mein Land und alles was ich jemals kannte zu "
                         "wenden, "
                         "\ndoch ich werde das Kind vor allen anderen finden. \nUnd ich werde es weit, weit wegbringen."
                         "Irgendwo hin, wo \nes keinen Schaden anrichten kann, irgendwo, wo es ein gutes Leben haben "
                         "kann.",
    "endscheidung_lüge": "\n\nIch ließ also das Feuer Torgows Labor und seine Hütte verschlingen und kehrte zu "
                         "\nmeiner "
                         "Königin zurück. Ich log und sagte ihr Torgow sei verrückt und liebte es seine \nkranken "
                         "Machtspielchen mit uns zu spielen. Es ging also so weiter, wie es \nimmer schon gewesen war. "
                         "\nDoch mein ganzes Leben war ich davon überzeugt gewesen, dass \nNaur im Recht war und Dagor "
                         "unser Erzfeind. Niemals hatte ich gedacht, dass wir \nvielleicht beide Seiten im Unrecht "
                         "waren. Und jetzt, wo ich die Wahrheit wusste, kam \nmir der ganze Krieg einfach sinnlos vor. "
                         "\nAußerdem erkannte ich schnell, wie riskant die Lage \ntrotz allem war. Ständig bestand "
                         "eine "
                         "Chance, dass sich ein Naurer und ein Dagorer \nvermählten. Wir leben einfach zu nah "
                         "beieinander. \nAlso begann ich Möglichkeiten zu erwägen, an die ich zuvor nie gedacht hatte."
                         "\nDenn obwohl es niemand zugeben wollte, waren fast alle erschöpft vom ewigen Kämpfen. "
                         "\nHier war "
                         "einfach nicht genug Platz für zwei Reiche, \nso war es schon seit ewigen Zeiten und so wird "
                         "es auch immer sein. Ob es einen \nWaffenstillstand gab oder nicht, es würde nie einen "
                         "wirklichen Frieden geben. \nUnd langsam wuchs eine Idee in mir, und je länger ich darüber "
                         "nachdachte, desto \nbesser schien sie. \nIch würde zum versunkenen Kontinent Aldir und die "
                         "Teile des gefallenen Mondes reisen. \nDort würden wir das Reich unserer Vorfahren "
                         "wiederaufbauen, \nund wenn die Bauern und die müden Soldaten kommen würden, müssten auch die "
                         "Adligen nachziehen. \nDenn lieber würden sie auswandern als eine Niederlage gegen Dagor zu "
                         "riskieren. \nSo wäre die Gefahr gebannt.",
    "labor_tisch_name": "Schreibtisch",
    "labor_tisch_look": "Der Schreibtisch ist komplett leer. Nur ein Zettel liegt da, auf diesem steht: "
                        "\n„Wer auch immer du bist, wenn du es bis hierher geschafft hast, dann musst du "
                        "ausgesprochen \nschlau sein. \nAlso schau dich um, hol dir deine Belohnung. "
                        "Aber tue mir einen Gefallen: \nLieß alles, lerne alles, verstehe alles und dann, "
                        "wenn du endlich weißt, warum. \nUnd wenn du wirklich so gewizt bist wie ich denke, "
                        "dann wirst du die richtige Entscheidung treffen. \nViel Spaß.“",
    "labor_tisch_inter": "Damit kann ich nichts machen.",
    "labor_tafel_name": "Tafel",
    "labor_tafel_look": "Wenn ich mich nicht irre, handelt es sich hier um Geräte der Astrologie. Hier ist auch "
                        "\nein Modell mit verschiedenen Himmelskörpern. Seltsam, bei dem Modell ist der "
                        "Mond Totu dabei. \nJeder weiß, dass er schon vor Jahrhunderten auf die Erde gefallen ist \nund"
                        " eine Menge Schaden angerichtet hat. Was hat der Mond nur mit unserem Krieg zu tun?",
    "labor_tafel_inter": "Die lasse ich lieber hier.",
    "labor_rechnungen_name": "Rechnungen",
    "labor_rechnungen_look": "Ich bin mir nicht sicher, ob ich sie richtig nachvollziehen kann. Er berechnet hier "
                             "etwas mit der \nMasse "
                             " des gefallenen Mond Tuto, einer Achse und Geschwindigkeit... Landmasse auf "
                             "der Erde spielt \nauch irgendwie "
                             "mit hinein. Er beschäftigt sich also hier wahrscheinlich mit dem Fakt, "
                             "dass der \nKontinent Aldir durch den "
                             "Fall des Mondes überschwemmt wurde. Aber mit seinen Rechnungen bekommt er "
                             "\nheraus, dass kein Kontinent wegen "
                             "einem abstürzenden Mond wie Tuto im Ozean untergehen "
                             "könnte. \nDa muss etwas nicht "
                             "stimmt. Jedes Kind weiß, dass es so war. \nIch sollte das mitnehmen.",
    "labor_rechnungen_unsichtbar": False,
    "labor_notizen_name": "Notizen",
    "labor_notizen_look": "Es sind lauter Legenden und Volksmärchen aus Aldir über den Untergang des "
                          "Kontinents. Torgow hat sie \nnach "
                          "ihrem geschätzten Alter geordnet. Alle Erzählungen der letzten zweihundert Jahre "
                          "erzählen von \neinem Mond "
                          "oder einem anderen Himmelskörper, der auf den Kontinent stürzte und ihn im Ozean "
                          "begrub. \nDoch hier sind "
                          "zwei noch ältere Geschichten, die ganz anders sind. \nHier steht etwas vom alten "
                          "Blut. \nEs soll alle handvoll Generationen "
                          "einem Menschen mit genug altem Blut unglaubliche magische Kräfte verleihen, "
                          "\naber diesen auch oft gierig "
                          "machen und in den Wahnsinn treiben. Der Sturz von Aldir soll also durch \neine "
                          "uralte, vergessene Magie "
                          "ausgelöst worden sein? \nKommt mir ein wenig weitergeholt vor. \nIch sollte das "
                          "einstecken.",
    "labor_notizen_unsichtbar": False,
    "labor_karten_name": "Karten",
    "labor_karten_look": "Die Karten befassen sich mit dem Ursprung der Länder Naur und Dagor, "
                         "besser gesagt mit der \nHerkunft "
                         "der Königshäuser. Mittlerweile sprechen wir alle die gemeine Zunge, aber alte "
                         "Schriften \nhaben scheinbar "
                         "Ähnlichkeiten zu den Sprachen von Einwanderern aus Aldir, dem gefallenen Kontinent. "
                         "\nHier werden auch "
                         "andere kulturelle Parallelen aufgeführt, wie alte Vasen und Grabrituale. \n\nSowohl Naur "
                         "und Dagor behaupten, dass der Feind \nursprünglich aus "
                         "Aldir kommt und somit kein "
                         "Anrecht auf die Länderein hat. Aber wenn Torgow Recht hat, \nkommen beide Königshäuser aus "
                         "Aldir. Dieses Wissen "
                         "könnten das Schicksal und Selbstverständnis \nmeines Lands für immer verändern. \nIch "
                         "nehme das lieber mit.",
    "labor_karten_unsichtbar": False,
    "labor_gegenstaende": ["Schreibtisch", "Tafel", "Rechnungen", "Notizen", "Karten"],
    "labor_name": "Labor",
    "labor_look": "Das geheime Labor sieht ganz anders aus, als ich es mir vorgestellt "
                  "hatte. Torgows Haus wirkte "
                  "\nschmuddelig, chaotisch und äußerst seltsam. Also genau so, wie ich "
                  "dachte, dass ein verrückter Magier "
                  "\nlebt. Das Labor ist das Gegenteil. Der Raum ist geräumig, hat keine "
                  "Fenster oder Türen und ist von "
                  "\nmassiven Steinwänden umgeben. Er ist sauber, aufgeräumt und erhellt "
                  "von einem seltsamen Licht, "
                  "\ndas von überall und nirgends zugleich zukommen scheint. \nStatt "
                  "verspielten Figürchen oder kunstvoll "
                  "geschnitzten Schränken, ist hier nur das nötigste. \nEin schlichter "
                  "Schreibtisch und ein Stuhl stehen in "
                  "der Mitte des Labors. \nVom Stuhl aus hat man die Wände im Blick. An der einen hängen präzise "
                  "Rechnungen. "
                  "\nAn einer anderen sind Karten, und an der letzten fein säuberlich "
                  "geordnete Notizen. \nAn der Rückseite "
                  "des Raums sind eine Reihe von filigranen Gerätschaften und \nModelle auf"
                  " einer langen Tafel aufgestellt. "
                  "\nWar die Hütte nur eine Fassade und das ist der echte Torgow? \n"
                  "Wenn er so einen Aufwand betreibt, "
                  "um etwas vorzutäuschen, was verbirgt er dann hier?",
    "labor_unsichtbar": True,
    "keller_wand_name": "Wand",
    "keller_wand_look": "Die Wand ist auffällig leer.",
    "keller_wand_inter": "So kann ich hier nichts ausrichten.",
    "keller_wand_inhalt": ["Labor"],
    "keller_brief_name": "Blatt",
    "keller_brief_look": "Ein alter Brief, es scheint Torgows Handschrift zu sein. Er wurde nie abgeschickt:"
                         "\n„Liebster Freund, \nIch weiß, was ich tue ist schrecklich und es schmerzt mich "
                         "fürchterlich. \nJeden Tag trauere ich um die unzähligen Menschen, "
                         "die wegen diesem unsinnigen Krieg sterben müssen. \nAber ihnen kann man nicht "
                         "trauen und was damals geschehen ist, darf auf keinen Fall noch einmal \npassieren."
                         "Zusammen ist das alte Blut zu stark in ihnen. Ich werde ein weitere Katastrophe "
                         "verhindern. \nEgal um welchen Preis.“",
    "keller_brief_unsichtbar": False,
    "keller_buch_name": "Buch",
    "keller_buch_look": "Es ist ein dickes, rotes Buch über Zauber, Flüche und andere Geheimnisse. \nEs "
                        "ist auf einer bestimmten Seite aufgeschlagen: \n\n„Portalzauber für Jedermann: "
                        "\nSpreche das passende dreisilbige Zauberwort vor einer Wand Ihrer Wahl. \n1. "
                        "Silbe:          zimtisch ( -tak )          saccheridisch ( -lok )          "
                        "ätzidisch ( -pif ) \n2. Silbe:          leknud ( -rop )            lleh ( -wil )   "
                        "                ßiew ( -mom ) \n3. Silbe:          modorn ( -knif )        "
                        "      jong ( -topi )                  olt ( -schnuk)” \n\nDarunter steht "
                        "per Hand hineingekritzelt: \n„Falls ich wieder vergesse, welcher richtig ist: "
                        "\nWie saurer Sud, \nWelch finsteres Tor, \nEin altes Blut, \nso geht’s ins "
                        "Labor.“",
    "keller_buch_inter": "Lieber nicht, wer weiß, was da für Schutzzauber drauf liegen.",
    "keller_gegenstaende": ["Wand", "Blatt", "Buch"],
    "keller_name": "Keller",
    "keller_look": "Der Keller ist kalt, dunkel und muffig. Hier ist eine Menge "
                   "Gerümpel verstaut. \nNur eine Wand ist ganz leer. Daneben liegt ein "
                   "Buch und ein beschriebenes Blatt auf einem \nkleinen Bücherständer.",
    "keller_unsichtbar": True,
    "wohnzimmer_regal_name": "Regal",
    "wohnzimmer_regal_look": "Ein Regal voller seltsamer, verstaubter Bücher. Über Kräuter, Kreaturen und "
                             "Kitzelzauber... \nNeben einem Buch über Witze für jede Gelegenheit steht eines über "
                             "Wichte, es hat weniger Staub als die anderen.",
    "wohnzimmer_regal_inter": "Schade, dahinter ist leider keine Geheimtür.",
    "wohnzimmer_buch_name": "Wichtebuch",
    "wohnzimmer_buch_look": "Wicht, der: \nEin Wesen, dass ursprünglich aus den Wäldern Aldurians kommt, "
                            "\naber mittlerweile oft sein Unwesen in den Häusern der Menschen treibt. \nHat "
                            "man erstmal einen Wichte im Haus, wird es sehr schwer ihn wieder los zu werden. "
                            "\nSo schwer sogar, dass viele verzweifelte Menschen versuchen mit ihnen zusammen "
                            "zu leben \nund ihnen Süßigkeiten als Opfer darbringen.",
    "wohnzimmer_buch_inter": "So wicht-ig sind mir Wichte nicht.",
    "wohnzimmer_tisch_name": "Tisch",
    "wohnzimmer_tisch_look": "Der Tisch sieht sehr unaufgeräumt aus. Hier stehen halb gegessenen "
                             "Mahlzeiten, \nkrakeligen Skizzen und gescheiterten Experimenten, sieht "
                             "alles sehr komlex aus. \nIch habe schon gehört, dass Torgow ein wahres Genie"
                             " ist. \nAlle hatten große Hoffnungen in ihn bis er von der Akademie geworfen"
                             " wurde. \nZwischen all den Sachen kann ich "
                             "einen Brief aus Pergament \nmit königlichem Siegel und eine Schere "
                             "erkennen.",
    "wohnzimmer_tisch_inter": "Aufräumen werd ich den sicher nicht...",
    "wohnzimmer_schere_name": "Schere",
    "wohnzimmer_schere_look": "Sehr schnittig.",
    "wohnzimmer_schere_unsichtbar": False,
    "wohnzimmer_brief_name": "Brief",
    "wohnzimmer_brief_look": "Der Brief ist aus kostbarem Material und hat ein königliches Siegel. \nIm Brief steht "
                             "in verschnörkelter Schrift geschrieben:\n\"Eure Majestät Tatelis, König von des "
                             "erbärmlichen Dagor, \nDen Sieg bei Hilis werde ich Euch heimzahlen, Ihr verdammicher "
                             "Kröterich. \nIhr werdet schon sehen, dass das reine Blut der Naur nicht von irgendwo "
                             "herkommt, \nwir werden Euch und eure ganze überriechende Sippe in die schleimigen "
                             "Sümpfe zurückbefördern, \nin die ihr hingehört... \"\nDas geht noch zwei Seiten so "
                             "weiter. Sehr seltsam, das ist gar nicht Königin Navlias Handschrift.",
    "wohnzimmer_brief_unsichtbar": False,
    "wohnzimmer_loch_name": "Loch",
    "wohnzimmer_loch_look": "Sieht nicht sehr einladend aus...",
    "wohnzimmer_loch_inter": "Da greif ich sicher nicht rein.",
    "wohnzimmer_tür_name": "Tür",
    "wohnzimmer_tür_look": "Die Tür sieht so aus, als würde sie in einen Keller führen.\nSeltsam, ich sehe "
                           "gar kein Schlüsselloch.",
    "wohnzimmer_tür_inter": "Die Tür ist verschlossen.",
    "wohnzimmer_tür_inhalt": ["Keller"],
    "wohnzimmer_gegenstaende": ["Regal", "Wichtebuch", "Tisch", "Brief", "Loch", "Schere", "Tür"],
    "wohnzimmer_name": "Wohnzimmer",
    "wohnzimmer_look": "Dieser Raum scheint das Wohnzimmer zu sein. Der Raum ist "
                       "halbmondförmig, alles ist aus Holz gemacht \nund wirkt ein "
                       "wenig baufällig. Trotzdem ist es gemütlich hier mit "
                       "Teppichen an den Wänden und einem Kamin, auch \nwenn es nicht "
                       "unbedingt aufgeräumt ist. Torgow bekommt scheinbar "
                       "nicht oft Besuch hier draußen. \nIn der Ecke ist sogar ein "
                       "Loch in der Wand. Sonst stehen hier ein Regal voll Bücher"
                       " und ein Tisch. \nEs gibt einen Durchgang in die "
                       "Küche und einen Vorratsraum. \nAußerdem sehe ich eine "
                       "Treppe in den Turm und eine Tür.",
    "wohnzimmer_unsichtbar": False,
    "küche_schrank_name": "Schrank",
    "küche_schrank_look": "Ein schöner, handgeschnitzter Schrank mit Eichhörnchen und keltischen Knoten als "
                          "Verzierung.",
    "küche_schrank_inter": "Äußerst seltsam, da ist gar nichts drin, nur in der Wand an der Rückseite ist ein Loch.",
    "küche_buch_name": "Tränkebuch",
    "küche_buch_look": "Auf der ein gemerkten Seite steht: \n\nSchlaftrank:\nVermenge Nesselblumen "
                       "und Zugluwurz und koche sie zusammen mit etwas Pfeffer. \n\nVergesstrank: \nRöste "
                       "Drachenschuppen und Lerchenschnäbel und dünste sie "
                       "anschließend mit Nesselblumen. \n\nTrank des frohen Vogels: \nSchmore etwas "
                       "Zugluwurz im Kessel, füge dann Nesselblumen hinzu \nund garniere mit einer Priese "
                       "Pfeffer.",
    "küche_buch_inter": "Das Buch liegt hier gut.",
    "küche_kessel_name": "Kessel",
    "küche_kessel_look": "Ein Kessel in dem Wasser brodelt. Hier war vor kurzem noch jemand.",
    "küche_kessel_inter": "Der ist zu schwer, um ihn mitzunehmen.",
    "küche_schuppen_name": "Drachenschuppen",
    "küche_schuppen_look": "Faszinierend, eine Schuppe eines Drachen ist so groß wie meine Hand.",
    "küche_schuppen_unsichtbar": False,
    "küche_schnäbel_name": "Lerchenschnäbel",
    "küche_schnäbel_look": "Ein Schnabel ist besser als eine Gabel.",
    "küche_schnäbel_unsichtbar": False,
    "küche_wurz_name": "Zugluwurz",
    "küche_wurz_look": "Sieht aus, als könnte man das rauchen.",
    "küche_wurz_unsichtbar": False,
    "küche_blumen_name": "Nesselblumen",
    "küche_blumen_look": "Sie pieksen, wenn man sie anfässt.",
    "küche_blumen_unsichtbar": False,
    "küche_pfeffer_name": "Pfeffer",
    "küche_pfeffer_look": "Den kann man überall hinpfeffern.",
    "küche_pfeffer_unsichtbar": False,
    "küche_gegenstaende": ["Kessel", "Schrank", "Drachenschuppen", "Lerchenschnäbel", "Pfeffer", "Zugluwurz",
                           "Nesselblumen", "Tränkebuch"],
    "küche_name": "Küche",
    "küche_look": "Die Küche ist viel kleiner als das Wohnzimmer. Von der Decke hängen "
                  "Kräuter, Räucherfleisch, aber auch \nFledermäuse und seltsam "
                  "leuchtende Pflanzen. Überall stehen selbstgemachte Figuren aus "
                  "\nKastanien und Tannenzapfen. Ist das für seine Magie oder ist Torgow "
                  "einsam hier draußen? \nIn einer Ecke steht ein kleiner Schrank und an "
                  "der Wand ist eine Ablage angebracht, \nauf der ein riesiger, "
                  "gusseiserner Kessel steht. Neben dem Kessel liegt ein Tränkebuch \nund "
                  "fünf verschiedene Behälter mit den Aufschriften: \nDrachenschuppen, "
                  "Lerchenschnäbel, Zugluwurz, Nesselblumen und Pfeffer. \nDavon halte "
                  "ich mich lieber fern, alles was ich koche ist immer ungenießbar bis "
                  "lebensbedrohlich.",
    "küche_unsichtbar": False,
    "turm_vogel_name": "Vogel",
    "turm_vogel_look": "Er ist ohnmächtig geworden und atmet unregelmäßig. Das arme Ding...Warum musstest du"
                       " den Schlüssel \nfressen? Hoffentlich überlebt er. Trotzdem hätte ich gerne diesen "
                       "Schlüssel.",
    "turm_vogel_unsichtbar": True,
    "turm_käfig_name": "Käfig",
    "turm_käfig_look": "Darin ist ein süßer kleiner Vogel und ein Schlüssel, der nützlich aussieht. Wer hätte "
                       "gedacht das \nTorgow knuffige Tiere mag? Vielleicht ist er nicht so schlimm, "
                       "wie ich dachte.",
    "turm_käfig_inter": "Die Tür des Käfigs klemmt.",
    "turm_käfig_inhalt": ["Vogel"],
    "turm_notiz_name": "Notiz",
    "turm_notiz_look": "Auf einen zerknitterten Zettel steht in krakeliger Handschrift geschrieben: \n„Solange "
                       "Naur und Dagor im Krieg sind, sind sie schwach und konsumiert von ihrem Hass "
                       "aufeinander. \nNur wenn sie abgelenkt sind durch ihr ewiges töten und foltern, "
                       "kann mein Plan funktionieren, \nnur dann werden sie nicht erkennen können wer wirklich "
                       "die Fäden zieht und was auf sie zukommt.“ \nWie kühl und sachlich er über den Tod "
                       "meiner Landsleute und meiner Freunde schreibt. \nWar er schon immer so grausam? Oder "
                       "verliert er den Verstand?",
    "turm_notiz_unsichtbar": True,
    "turm_kissen_name": "Kissen",
    "turm_kissen_look": "Das Kissen ist riesig und sieht sehr gemütlich aus. \nAber warte, liegt da etwas "
                        "drunter?",
    "turm_kissen_inter": "Es ist am Sofa festgenäht.",
    "turm_kissen_inhalt": ["Notiz"],
    "turm_name": "Turm",
    "turm_gegenstaende": ["Käfig", "Vogel", "Notiz", "Kissen"],
    "turm_look": "Der anstrengende Aufstieg hat sich wirklich gelohnt, vom Turmzimmer \nhat "
                 "man eine atemberaubende Aussicht auf dem ganzen Wald. Das Zimmerchen ist "
                 "klein, aber gemütlich. \nIn die Rundung schmiegt sich ein kreisförmiges "
                 "Sofa mit einem gewaltigen Kissen \nund auf der Balustrade steht ein "
                 "Käfig, indem sich ein Vogel und ein Schlüssel befinden. \nIch bin mir "
                 "sicher, hier saß Torgow und heckte seine Pläne aus.",
    "turm_unsichtbar": False,
    "vorratsraum_zettel_name": "Zettel",
    "vorratsraum_zettel_look": "Da steht: \n\"Ich kann kaum glauben, dass ich es echte wilde Wichte in diesen Wäldern"
                               " gibt. \nDie meisten müssen sich in den Städten der Menschen durchschlagen, "
                               "weil ihre Wälder langsam verschwinden. \nBis ich eine Tonik gegen die Sonne gebraut "
                               "habe, sollte ich ihn tagsüber in der Truhe lassen. \nEr scheint sie zu mögen. "
                               "Eigentlich wollte ich ihn zu seinem Stamm bringen, \naber er will hier bleiben. Ich "
                               "beschwere mich nicht über einen Gehilfen.\" \nSo freundlich zu Ungeziefer wie "
                               "Wichten, aber lässt hunderte Menschen \nin einem ewigen Krieg sterben. Wegen solchen "
                               "unerhöhrten Überlegungen ist er \naus der Akademie geflogen.",
    "vorratsraum_zettel_unsichtbar": True,
    "vorratsraum_truhe_name": "Truhe",
    "vorratsraum_truhe_look": "Sie sieht sehr stabil aus. Sie ruckelt ein wenig und macht leise Geräusche, sicher ist "
                              "die verzaubert.",
    "vorratsraum_truhe_inter": "Sie ist verschlossen.",
    "vorratsraum_truhe_inhalt": ["Zettel"],
    "vorratsraum_muffin_name": "Muffin",
    "vorratsraum_muffin_look": "Sieht lecker aus. Er ist pink mit Sträuseln drauf.",
    "vorratsraum_muffin_unsichtbar": False,
    "vorratsraum_brecheisen_name": "Brecheisen",
    "vorratsraum_brecheisen_look": "Damit bekommt man sicher vieles auf.",
    "vorratsraum_brecheisen_unsichtbar": False,
    "vorratsraum_loch_name": "Spinnenweben",
    "vorratsraum_loch_look": "Hinter den Spinnenweben ist wieder so ein Loch. Wo kommen die nur alle her?",
    "vorratsraum_loch_inter": "Greif du doch rein!",
    "vorratsraum_korb_name": "Korb",
    "vorratsraum_korb_look": "Ein großer Korb aus Reißich.",
    "vorratsraum_korb_unsichtbar": False,
    "vorratsraum_name": "Vorratsraum",
    "vorratsraum_look": "Der Vorratsraum ist klein und dunkel. Alles ist voll "
                        "mit Spinnenweben. \nAuf dem Boden ist "
                        "eine große Eichenholztruhe, ein Reißichkorb und ein "
                        "Brecheisen. \nWas ist das da im Regal? Ein Muffin?",
    "vorratsraum_gegenstaende": ["Truhe", "Zettel", "Muffin", "Brecheisen", "Spinnenweben", "Korb"],
    "vorratsraum_unsichtbar": False,
    "falle_name": "Falle",
    "falle_look": "Mal schauen was ich damit fangen kann.",
    "falle_unsichtbar": True,
    "schluessel_name": "Schlüssel",
    "schluessel_look": "Ein großer ein wenig angerosteter Schlüssel. Wie auch immer der in den Vogel gepasst hat.",
    "schluessel_unsichtbar": True,
    "trank_name": "Trank des ewigen Todes",
    "trank_look": "Der Trank sieht irgendwie nicht aus, als würde er so gehören.",
    "trank_unsichtbar": True,
    "inventar": [],
    "truhe_offen": False,
    "wicht_gefangen": False
}

with open('NeuesSpiel.json', 'w') as fp:
    json.dump(alle_sachen, fp)

# with open('Spielstand.json', 'w') as fp:
#    json.dump(alle_sachen, fp)

