import streamlit as st
import datetime

# Get current date
current_date = datetime.date.today()
START_DATE = datetime.date(2025, 2, 1)

# Define START_DATE and calendar_content here
# Create a dictionary to store content for each day
calendar_content = {
    1: {"text": """
        Wir beginnen mit einem schwedischen Klassiker, Opeth.
        Du siehst eine fast 20 Jahre alte live Aufnahme ihres wunderbaren Auftritts aus der Albert Hall in London  """,
        "video": "https://www.youtube.com/watch?v=5oiOnPbMQwE"},
    2: {"text": """Heute widmen wir uns mal Death Metal, genauer gesagt brasilianischem Death Metal. Die Frontfrau, Fernanda Lira, hat übrigens früher bei
        bei Nervosa gespielt, auch recht hörenswert, wenn man ein Herz für Thrash Metal hat...""",
        "video": "https://www.youtube.com/watch?v=t5pobBaJlv8"},
    3: {"text": """Auf zu einem weiteren Klassiker, Behemoth, die Heroen des blackened Death Metal, großartige live Shows und
        die Streams während der Pandemie haben Maßtäbe vom anderen Stern gesetzt """, 
        "video": "https://www.youtube.com/watch?v=-6nMcLKu5ik&list=PLLlXavPCWq1VeWbsNqkDAV6rmw3l0uv2s&index=9"},
    4: {"text": """ Nachdem wir uns die letzten zwei Tage aufgewärmt haben, wirds Zeit für ungewöhnlichere Klänge.
        Ja, man kann auch Metal mit Schlagzeug und Trombone machen!""",
        "video": "https://www.youtube.com/watch?v=8XNo4C_GGQ4"},
    5: {"text": """Trotz familiärer Vorbelastungen, Between the buried and me sind definitiv einen Hinhörer wert. Mein Lieblingssong von
        ihrer wunderbaren EP Automata II  """,
        "video": "https://www.youtube.com/watch?v=FtuIMfdnZnU"},
    6: {"text": """Norweger können soviel mehr als Kirchen anzünden und trve sein. Shining (nicht zu verwechseln mit der gleichnamigen,
        schwedischen Black Metal Band!) haben mit Blackjazz ein musikalisches Feuerwerk entzündet, bevor sie bedauerlicherweise vor ein paar Jahren
    in poppige Gefilde abgedriftet sind :face_with_spiral_eyes: """,
        "video": "https://www.youtube.com/watch?v=KGts0kR-rfw"},
    7: {"text": """Hypnotisch, sperrig, ultra fett, Humanity's last breath!!!
        Die neueren Aufnahmen sind etwas leichter zugänglich, falls hier übers Ziel hinaus geschossen worden sein sollte... """,
        "video": "https://www.youtube.com/watch?v=alR0NcANEBw"},
    8: {"text": """Nach dem Gewitter von gestern ist's Zeit für ne Runde poppigen Zirkus Metal, auf zu Avatar! Die gewünschte Aufnahme von Puppet Show wurde zwar nicht gefunden,
        aber für einen Einblick in die hochgradig unterhaltsamen Live Shows reichts """, 
        "video": "https://www.youtube.com/watch?v=V2Khlu7jBls"},
    9: {"text": """Zeit für einen wilden Genremix, oder wie ein YT Kommentator so treffend bemerkte: *Blood Incantation be like:
        We play death folk cosmic psychodelic heavy electronic metal now*""", 
        "video": "https://www.youtube.com/watch?v=6N4rLtjPzH0"},
    10: {"text": """Holländische Frauen machen Gerumpel und spielen auf vielen Seiten.  """,
         "video": "https://www.youtube.com/watch?v=u0rTdyYtBUM"},
    11: {"text": """Apropos weibliche Sänger. Vexed sind live ein wahrer Orkan, also auf zu einer Runde neumodischem Deathcore""",
         "video": "https://www.youtube.com/watch?v=BrVx05brvIk"},
    12: {"text": """Zu einem weiteren Klassiker - Fear Factory! Man munkelt ja, dass dieser bisher in Markt Schwaben keinerlei Aufmerksamkeit genossen hat :scream:
         Der Lead Gitarrist ist übrigens auch ein Band Diktator und einen Sängerwechsel gabs auch... """,
         "video": "https://www.youtube.com/watch?v=5GxWWk1wzlw"},
    13: {"text": """ Und noch ein Klassiker, Lamb of God! Es scheint, als ob die Kalendermacherin weniger abseitig ist, als behauptet.... """,
         "video": "https://www.youtube.com/watch?v=hBj0-dIU8HI"},
    14: {"text": """Valentinstag! Romantik! Genau der richtige Tag, um eine Chorsängerin beim Anschmachten eines norwegischen Black Metallers zu beobachten""", 
         "video": "https://www.youtube.com/watch?v=pwU22xcDiJ4"},
    15: {"text": "Zeit für ein bisschen Experimentelles, Imperial Triumphant!",
         "video": "https://www.youtube.com/watch?v=KnNHaH2kfkE"},
    16: {"text": """Uralt und auch kein Metal, aber einfach ein großartiger Song vom großartigen Trent Reznor""",
         "video": "https://www.youtube.com/watch?v=pJwt9qJb6Sw"},
    17: {"text": """Du wolltest schon immer mal all-female-black-Stoner-Doom hören? Hier bist du richtig!""",
         "video": "https://www.youtube.com/watch?v=NdR24AURUwU"},
    18: {"text": """Junge Läuche aus Neuseeland wandeln in eigenen Schuhen auf Sepulturas Pfaden und singen auf Maori """,
         "video": "https://www.youtube.com/watch?v=Lx_xGv70Yyo"},
    19: {"text": """An FireFree - Bei Revocation eine Songwahl treffen zu müssen, ist eine Frechheit! Die Band ist einfach lächerlich vielseitig,
         Thrash, Tech Death, Prog, alles dabei und immer auf höchstem Niveau. """,
         "video": "https://www.youtube.com/watch?v=mmg3jr7Bhfo"},
    20: {"text": """ Zeal and Ardor sind ja die neuen Lieblinge der Musikenthusiasten und sollten daher in keinem ordentlichen Metal Kalender
         fehlen. Ich fühl mich da eher an blutarmen Gospel-Rock-Schlager erinnert. Die Originalität kann ich nur in älteren Aufnahmen entdecken, drum: """,
         "video": "https://www.youtube.com/watch?v=BFGU0g1LA9I"},
    21: {"text": """Die anderen lallen immer was von Lorna Shore, blabla? Pfff, Du bist Profi und hörst Distant - DAS ist der deathcore der Stunde!""",
         "video": "https://www.youtube.com/watch?v=_8mRmkERONI"},
    22: {"text": """ Frei nach Loriot - Ein Monat ohne Meshuggah ist denkbar, aber sinnlos""",
         "video": "https://www.youtube.com/watch?v=I334n4zx6mM"},
    23: {"text": """Zeit für flächigen Black Metal aus Portugal zur Entspannung""",
         "video": "https://www.youtube.com/watch?v=P4u6XnKuxoQ"},
    24: {"text": """Kanonenfieber singen in wirklich beeindruckenden live Shows ausschließlich über das Grauen des ersten Weltkriegs.
           Die Kritik versteht das Publikum leider nicht immer...""",
         "video": "https://www.youtube.com/watch?v=TPUBnC4dKWw"},
    25: {"text": """Kein Bock auf Standardriffs, Standardarrangments? Alles Fade? Dann hör doch Igorr!""",
         "video": "https://www.youtube.com/watch?v=YCqG9B8j-cI"},
    26: {"text": "Author and Punisher - Musik oder Performance? Man weiß es nicht, ist auch egal. Auf jeden Fall werden die Instrumente selber gebaut. ", 
         "video": "https://www.youtube.com/watch?v=1UR3YjktJYI"},
    27: {"text": """Der metallische Kalender neigt sich langsam dem Ende zu, jetzt noch ein Ohrenschmeichler vor dem Endspurt """,
         "video": "https://www.youtube.com/watch?v=QRg_8NNPTD8"},
    28: {"text": """Meine neueste Entdeckung und dein Endgegner - Rivers ablaze. Zum Schluss nochmal eine Runde Sperrgut """,
         "video": "https://www.youtube.com/watch?v=bzZtLpPF5Xk"}
}

st.set_page_config(
    page_title="Mehr Metal",
    layout="wide",
    page_icon=":sign_of_the_horns:"
)
st.title(":sign_of_the_horns: Willkommen im metallischen Februar")
st.markdown("""
   Joe's Metal Kalender schlägt Dir jeden Tag ein Video vor, mit dem Du Klassiker oder Abseitiges genießen kannst""")

rows = 7
cols = 4

# Initialize session state for clicked button if not exists
if 'clicked_button' not in st.session_state:
    st.session_state.clicked_button = None

# Create buttons in the sidebar
st.sidebar.header("Metal Kalender")
# Add instructions
st.sidebar.write("Klicke auf den entsprechenden Tag und spitze deine Ohren ")
st.sidebar.info("Obacht: Vorspulen ist untersagt!", icon="🔥")

for i in range(rows):
    columns = st.sidebar.columns(cols)
    for j in range(cols):
        button_number = i * cols + j + 1
        with columns[j]:
            if st.button(f"{button_number}", key=f"btn_{button_number}"):
                st.session_state.clicked_button = button_number

# Display content in the main area
if st.session_state.clicked_button:
    button_number = st.session_state.clicked_button
    if current_date >= START_DATE + datetime.timedelta(days=button_number - 1):
        st.header(f"Tag {button_number}")
        st.markdown(calendar_content[button_number]["text"])
        st.video(calendar_content[button_number]["video"])
    else:
        st.error(":face_with_raised_eyebrow: Ich hab doch gesagt, Schummeln ist nicht erlaubt! Imupulskontrolle, junger Mann")
else:
    st.write("Auf dass ein paar neue Entdeckungen darunter sind!")