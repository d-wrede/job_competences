"""a first try to filter the job competences out of a text"""
# from collect_words import filter_string
import csv
import os
import re

os.chdir("c:/Users/danie/Documents/Software/projects/job_competences")


def filter_string(string):
    string = re.sub(r'[^a-zA-Z\säöüÄÖÜß-]', '', string)
    string = string.replace('--', '-')
    string = re.sub(r'[\n\t\xa0]+', ' ', string)
    string = string.lower()
    return string


with open("job_description.txt", "r", encoding='utf-8') as f:
    jdescription = filter_string(f.read(500))
    jdes = tuple(jdescription.split(sep=' '))
with open("usual_words_de.csv", "r") as g:
    usual_words = list(csv.reader(g, delimiter=','))[0]
    # usual_words = g.read()  # <-- list
with open("competences.csv", "r") as h:
    # str_comp = h.read()
    competences = list(csv.reader(h, delimiter=','))

print(f"list of competences: \n{competences}")
print(f"job description: {jdescription}")
print(usual_words[:20])

# job_data-structure: [['URL', 'job_title', ['comp1', 'comp2', 'comp3']],
#                       ['URL2', 'job_title2', ['comp1', 'comp2', 'comp3']],
#                       ['URL3', ..., [...]]] and so forth.
print("count('http'): ", jdes.count('http'))
job_data = [[None, None, []]
            for i in range(jdes.count('http'))]  # count number of URLs in 'jdes'
new_words = []

# job_data[0][0] = 'URL'
# job_data[0][1] = 'job_title'


# all this could run with a .. decorator(?) to ensure that the progress is
# saved, even if it is interrupted.

# Two processes:
# 1. sort known competences into a list to describe the job
# 2. if word not known, ask if it is a competence or not, add it to list
#    'usual_words' or 'competences' and, in latter case, add to list to
#    describe the job.

for word in jdes:
    if word in usual_words:
        print(f"'{word}' in usual_words!")
    if (word not in usual_words) and (word not in new_words):  # and len(word) > 1:
        if word in competences:
            # add to competence list
            print(f"'{word}' should be added to list.")

        else:
            # ask to either add to job competences
            # or to usual words.
            sorted = False
            while not sorted:
                answer = input(f"is '{word}' a competence? [y/n]: ")
                if answer == "y":
                    competences.append(word)
                    job_data[0][2].append(word)
                    print(f"'{word}' added to competences.")
                    print(f"'{word}' added to job_data.")
                    sorted = True
                elif answer == "n":
                    new_words.append(word)
                    print(f"'{word}' added to new_words.")
                    sorted = True
                else:
                    print("Please choose 'y' or 'n'.")
    print("new_words: ", new_words)