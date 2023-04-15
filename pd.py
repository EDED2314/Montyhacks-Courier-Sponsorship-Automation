import pandas as pd
import gender_guesser.detector as gender

d = gender.Detector()
# >>> 
# >>> print(d.get_gender(u"Bob"))
# male
# >>> print(d.get_gender(u"Sally"))
# female
# >>> print(d.get_gender(u"Pauley")) # should be androgynous
# andy


data = pd.read_csv("data/data.csv")
data.pop("Contact Telephone #")
data.pop("Postal Address")
data.pop("Name of Representative")
data.pop("Current Status")
data.pop("1")
data.pop("Row #")
data.to_csv("data/clean.csv")
data = pd.read_csv("data/clean.csv")
for i in range(0, 13):
    try:
        data.pop(f"Unnamed: {i}")
    except KeyError:
        continue

new = data.loc[0:253, :]
new.to_csv("data/clean.csv")

data = pd.read_csv("data/clean.csv")

names = data.get("Contact Name")

newNames = []
for name in names:
    name = str(name)

    idx1 = name.find("(")
    idx2 = name.find(")", idx1, len(name) - 1)
    if(idx1 != -1):
        name = name[0:idx1]
    
    name.replace("Owner", "")
    name.replace("owner", "")
    name.replace("DMD", "")
    name.replace("Dr. ", "")
    name.replace("Dr.", "")
    
    name = name.split("-")[0]
    if name[len(name)-1] == " ":
        name=name[0:len(name)-1]
        
    
    
    print(name)

    

    # if name != "nan" or name != "na":
    #     gender = d.get_gender(name)
    #     if "male" in gender:
    #         name = "Mr. " + name
    #     elif "female" in gender:
    #         name = "Ms. " + name
    #     elif "andy" in gender:
    #         name = "Mr. " + name
            
    #     newNames.append(name) 
    # else:
    #     newNames.append(name)