import face_recognition

# Load the jpg files into numpy arrays
AlexCaruso_image = face_recognition.load_image_file(
    "static/img/players/Alex Caruso.png")
AnthonyDavis_image = face_recognition.load_image_file(
    "static/img/players/Anthony Davis.png")
AveryBradley_image = face_recognition.load_image_file(
    "static/img/players/Avery Bradley.png")
KentaviousCaldwellPope_image = face_recognition.load_image_file(
    "static/img/players/Kentavious Caldwell-Pope.png")
KostasAntetokounmpo_image = face_recognition.load_image_file(
    "static/img/players/Kostas Antetokounmpo.png")
QuinnCook_image = face_recognition.load_image_file(
    "static/img/players/Quinn Cook.png")
DeMarcusCousins_image = face_recognition.load_image_file(
    "static/img/players/DeMarcus Cousins.png")
TroyDaniels_image = face_recognition.load_image_file(
    "static/img/players/Troy Daniels.png")
DannyGreen_image = face_recognition.load_image_file(
    "static/img/players/Danny Green.png")
JaredDudley_image = face_recognition.load_image_file(
    "static/img/players/Jared Dudley.png")
TalenHortonTucker_image = face_recognition.load_image_file(
    "static/img/players/Talen Horton-Tucker.png")
DwightHoward_image = face_recognition.load_image_file(
    "static/img/players/Dwight Howard.png")
LeBronJames_image = face_recognition.load_image_file(
    "static/img/players/LeBron James.png")
KyleKuzma_image = face_recognition.load_image_file(
    "static/img/players/Kyle Kuzma.png")
JaValeMcGee_image = face_recognition.load_image_file(
    "static/img/players/JaVale McGee.png")
ZachNorvellJr_image = face_recognition.load_image_file(
    "static/img/players/Zach NorvellJr..png")
RajonRondo_image = face_recognition.load_image_file(
    "static/img/players/Rajon Rondo.png")


# Get the face encodings for each face in each image file
try:
    AlexCaruso_face_encoding = face_recognition.face_encodings(AlexCaruso_image)[
        0]
    AnthonyDavis_face_encoding = face_recognition.face_encodings(AnthonyDavis_image)[
        0]
    AveryBradley_face_encoding = face_recognition.face_encodings(AveryBradley_image)[
        0]
    KentaviousCaldwellPope_face_encoding = face_recognition.face_encodings(
        KentaviousCaldwellPope_image)[0]
    KostasAntetokounmpo_face_encoding = face_recognition.face_encodings(
        KostasAntetokounmpo_image)[0]
    QuinnCook_face_encoding = face_recognition.face_encodings(QuinnCook_image)[
        0]
    DeMarcusCousins_face_encoding = face_recognition.face_encodings(
        DeMarcusCousins_image)[0]
    TroyDaniels_face_encoding = face_recognition.face_encodings(TroyDaniels_image)[
        0]
    DannyGreen_face_encoding = face_recognition.face_encodings(DannyGreen_image)[
        0]
    JaredDudley_face_encoding = face_recognition.face_encodings(JaredDudley_image)[
        0]
    TalenHortonTucker_face_encoding = face_recognition.face_encodings(
        TalenHortonTucker_image)[0]
    DwightHoward_face_encoding = face_recognition.face_encodings(DwightHoward_image)[
        0]
    LeBronJames_face_encoding = face_recognition.face_encodings(LeBronJames_image)[
        0]
    KyleKuzma_face_encoding = face_recognition.face_encodings(KyleKuzma_image)[
        0]
    JaValeMcGee_face_encoding = face_recognition.face_encodings(JaValeMcGee_image)[
        0]
    ZachNorvellJr_face_encoding = face_recognition.face_encodings(
        ZachNorvellJr_image)[0]
    RajonRondo_face_encoding = face_recognition.face_encodings(RajonRondo_image)[
        0]

except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    AlexCaruso_face_encoding,
    AnthonyDavis_face_encoding,
    AveryBradley_face_encoding,
    KentaviousCaldwellPope_face_encoding,
    KostasAntetokounmpo_face_encoding,
    QuinnCook_face_encoding,
    DeMarcusCousins_face_encoding,
    TroyDaniels_face_encoding,
    DannyGreen_face_encoding,
    JaredDudley_face_encoding,
    TalenHortonTucker_face_encoding,
    DwightHoward_face_encoding,
    LeBronJames_face_encoding,
    KyleKuzma_face_encoding,
    JaValeMcGee_face_encoding,
    ZachNorvellJr_face_encoding,
    RajonRondo_face_encoding,
]
