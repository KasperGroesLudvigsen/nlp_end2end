
import pandas as ps
document = """Ved sikkerhedskontrollen bliver de hjemmelavede skilte konfiskeret, og de adopteredes budskaber pakket væk til efter samrådet. Så herfra er det politikernes hjemmebane, og de adopterede må stille lytte til de folkevalgte diskutere, hvem og hvor meget der skal undersøges.

De adopterede vil have placeret et ansvar for de mange skandaler, der de seneste år og uger er tromlet ind over adoptionsområdet.

Men det var en skuffende affære. I hvert fald set fra de opstillede stolerækker under Proviantgårdens hvide hvælvinger.

Det siger David Kildendal Nielsen, der er adopteret fra Indien og er en af dem, der blev narret fra sin far og mor af den indiske børnehjemsleder Pastor George, som derefter bortadopterede ham til Danmark.

- Jeg havde troede, der ville komme mere, efter det, der er sket de seneste to dage, siger David Kildendal Nielsen.

Der er også sket en del. Tirsdag stod en tidligere centralt placeret medarbejder i Ankestyrelsen, Freja Bøggild, frem i interviews med DR og Danwatch. Her beskrev hun, hvordan myndighederne allerede i 1960'erne og i årtierne frem fik utallige alvorlige advarsler om mulige ulovlige og uetiske adoptionssager.

Det er Ankestyrelsen, der fører tilsyn med adoptionsområdet.

- Der fik vi alle sammen den følelse, jamen vi havde jo ret, siger David Kildendal Nielsen.

Det er er også kommet frem, at flere topministerier allerede i 1995 fik viden om en mulig ulovlig adoption. Her skrev en indisk mor et brev til den daværende statsminister om oplysninger om hendes datter, der var havnet i Danmark.

- Jeg havde forventet, at ministeren havde sagt: Okay, det er simpelthen for alvorligt det her til, at vi kan fortsætte som hidtil, siger David Kildendal Nielsen, som vil have den danske stat holdt ansvarlig."""

sentence_list = document.split(".")

for l in sentence_list:

    print(len(l))

chunks = []

max_len = 512

chunk = ""

for sentence in sentence_list:

    if len(chunk) + len(sentence) < max_len:

        chunk += sentence

    else:

        chunks.append(chunk)

        chunk = ""

for chunk in chunks:

    print(f"Chunk length: {len(chunk)}")

    print(chunk)

sum([1,2])

sum([len(chunk) for chunk in chunks])/len(chunks)

