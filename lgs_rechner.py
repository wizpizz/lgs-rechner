import requests
from bs4 import BeautifulSoup
import os

# Einsetzungsverfahren: "einsetz"
# Gleichsetzungsverfahren: "glsetz"
# Additionsverfahren: "add"

def lgs_rechner(gle1, gle2, verfahren):
  vf_short = {"Einsetzungsverfahren": "einsetz",
              "Gleichsetzungsverfahren": "glsetz",
              "Additionsverfahren": "add"}
  url = "https://www.mathepower.com/glsyst.php"
  payload = {"gle1": gle1,
             "gle2": gle2,
             "verfahren": vf_short[verfahren],
             "submit": "berechnen"
             }
  r = requests.post(url, data=payload)
  s = BeautifulSoup(r.text, "html.parser")
  xy = s.find_all(style="vertical-align:middle")
  x = xy[-1].get("alt")
  y = xy[-2].get("alt")
  return x, y

def menu():
  alle_verfahren = {"1": "Einsetzungsverfahren",
                    "2": "Gleichsetzungsverfahren",
                    "3": "Additionsverfahren"}
  os.system('cls')
  g1 = input("1. Gleichung: ?\n"
             "2. Gleichung: ?\n"
             "Verfahren: ?\n"
             "------------------------------------------------\n"
             "Tippe die 1. Gleichung ein: ")
  os.system('cls')
  g2 = input(f"1. Gleichung: {g1}\n"
             "2. Gleichung: ?\n"
             "Verfahren: ?\n"
             "------------------------------------------------\n"
             "Tippe die 2. Gleichung ein: ")
  os.system('cls')
  vf = alle_verfahren[input(f"1. Gleichung: {g1}\n"
             f"2. Gleichung: {g2}\n"
             "Verfahren: ?\n"
             "------------------------------------------------\n"
             "1: Einsetzungsverfahren\n"
             "2: Gleichsetzungsverfahren\n"
             "3: Additionsverfahren\n"
             "------------------------------------------------\n"
             "Tippe die Nummer des Verfahrens ein: ")]
  os.system('cls')
  again = input(f"1. Gleichung: {g1}\n"
                f"2. Gleichung: {g2}\n"
                f"Verfahren: {vf}\n"
                "------------------------------------------------\n"
                f"x = {lgs_rechner(g1, g2, vf)[0]}\n"
                f"x = {lgs_rechner(g1, g2, vf)[1]}\n"
                "------------------------------------------------\n"
                "Nochmal? (ja/nein): ")
  if again.lower() == "ja":
    menu()

menu()
