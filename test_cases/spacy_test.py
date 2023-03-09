import spacy
import csv
nlp = spacy.load('de_core_news_sm') #lg

with open("competences.csv", "r") as h:
    text = ' '.join(sum(list(csv.reader(h, delimiter=',')), []))

# with open("job_descriptions_arbeitsagentur_api_klein.txt", "r", encoding='utf-8') as f:
#     jdescriptions = f.read().split(sep='\n')

#text = "www.zsw-bw-jobs.de.de 13788-k19921.306-S 2022-03-24 Testingenieur (m/w/d) für Untersuchungen an Batterien, Ingenieur/in - Erneuerbare Energien Das Zentrum für Sonnenenergie- und Wasserstoff-Forschung Baden-Württemberg (ZSW) ist eine gemeinnützige Stiftung des Landes Baden-Württemberg sowie verschiedener Institutionen und Unternehmen. Unsere Arbeitsschwerpunkte sind die wirtschaftsnahe Forschung und Entwicklung zu erneuerbaren Energien, Energiespeicherung und Energieeffizienz sowie Analysen von Energiesystemen. Als industrieorientiertes Forschungsinstitut ebnen wir gemeinsam mit unseren Partnern neuen Technologien den Weg in den Markt – dabei arbeiten wir von der Materialforschung über Systeme, Tests und Marktanalysen entlang der gesamten Wertschöpfungskette. Diese Expertise aus einer Hand ist für unsere Partner aus der Wirtschaft ein wesentlicher Erfolgsfaktor. Für das Fachgebiet Akkumulatoren (ECA) am Standort Ulm suchen wir zum nächstmöglichen Zeitpunkt einen Testingenieur (m/w/d) für Untersuchungen an Batterien Ihr Aufgabengebiet:" # • Messtechnische Untersuchungen an Li-Ionen Batterien und anderen modernen elektrischen Speichern • Planung, Aufbau, Programmierung, Durchführung und Auswertung von Versuchen an Batterien • Installation, Programmierung, Betreiben, Optimieren und Wartung von verschiedenen Prüfanlagen
# • Projektverantwortung mit Kundenkontakt für diese Projekte

# Ihr Profil:

# • Dipl.-Ing. (FH/TH), Bachelor, Master Elektrotechnik, Mechatronik oder vergleichbare Qualifikation
# • Einschlägige Berufserfahrung in den o.g. Aufgabenbereichen
# • Gute IT-Kenntnisse (CAN-Tools; Programmierkenntnisse in VBA, Python und/oder C)
# • Gute Kenntnisse in MS-Office und Englisch
# • Fähigkeit zu schneller Einarbeitung in neue Themen,Kommunikationsstärke und Teamfähigkeit
# • Hohes Maß an Engagement und Belastbarkeit, gewissenhaftes und zuverlässiges Arbeiten
# • Strukturierte, zielorientierte und selbständige Arbeitsweise

# Unser Angebot an Sie:
# Das ZSW bietet Ihnen eine kreative Atmosphäre, in der neues Wissen und nachhaltige Prozesse gefördert werden. Sie finden bei uns ein offenes Miteinander mit vielen Freiheiten, umfassendem Gestaltungsspielraum, flachen Hierarchien und der Möglichkeit zu selbstständigem Arbeiten. Möchten auch Sie die angewandte Energieforschung weiter voranbringen? Wir freuen uns auf Ihre Bewerbung!

# Das Arbeitsverhältnis ist zunächst auf 3 Jahre befristet, hat einen Beschäftigungsumfang von 100% und ist nach den im öffentlichen Dienst üblichen Regelungen (TV-L) eingestuft. Das ZSW bietet zusätzliche Sozialleistungen an. Wenn Sie Interesse an dieser Position haben, bewerben Sie sich bitte bis spätestens 27.04.2022 ausschließlich über das Bewerbungsformular. Fachliche Fragen beantwortet Ihnen Herr Dr. Olaf Böse gern unter der Telefonnummer +49 731 9530-551. Weitere Informationen erhalten Sie unter www.zsw-bw.de."

# erstelle eine Liste der bekannten Wörter
known_words = list(nlp.vocab.strings)

# filtere die unbekannten Wörter
caught_competences = []
for token in nlp(text):
    if token.text.lower() in known_words:
        caught_competences.append(token.text)

# gib die unbekannten Wörter aus
print('caught_competences:', caught_competences)
print('len(caught_competences):', len(caught_competences))