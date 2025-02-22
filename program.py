from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import random

CL = 0
# Pas le même temps à chaque fois pour éviter d'être detecté
def temps_aleatoire():
    return random.randint(1, 30)

# Multiples comptes pour éviter banissement
def choix_compte(numero_compte):
    comptes = {
        1: ("compte_IG_1", "mdp_compte"),
        2: ("compte_IG_1", "mdp_compte"),
        3: ("compte_IG_1", "mdp_compte"),
        4: ("compte_IG_1", "mdp_compte"),
    }
    CL = len(comptes)
    return comptes.get(numero_compte, ("", ""))

def choix_commentaire():
    commentaires = [
        "Ceci est un commenataire",
        "Ceci est un autre commenataire",
        "J'aime cette publication!",
    ]

    return random.choice(commentaires)

def init_driver():
    # Suppress logging for selenium
    logging.getLogger('selenium').setLevel(logging.CRITICAL)

    # Path to the chromedriver executable
    chromedriver_path = "./chromedriver_win32/chromedriver.exe"
    service = Service(chromedriver_path)
    op = webdriver.ChromeOptions()
    op.add_argument("--log-level=3")  # Suppress logs
    op.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=op)
    return driver

def valider_cookies(driver):
    try:
        button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, '_a9_0'))
        )
        button.click()
        print("Cookies validés")
    except:
        print("Cookies non validés")

def rediriger(driver):
    try:
        redirection = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, '_aa5h')) # nom de la classe concernée
        )
        redirection.click()

        time.sleep(1)

        redirection = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'x7l2uk3'))
        )
        redirection.click()
        print("Redirection ok")
    except:
        remplir_formulaire()
        print("Redirection Erreur")


def passer_intro(driver):
    try:
        ignorer = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'x173jzuc'))
        )
        ignorer.click()
        print("Intro passé")
    except:
        print("Intro Erreur")

def remplir_formulaire(driver, compte):
    try:
        champs = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, '_aa48'))
        )

        for champ, texte in zip(champs, compte):
            champ.send_keys(texte)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, '_acap'))
        )
        submit_button.click()
        print("Formulaire Ok")
    except:
        print("Formulaire Erreur")

def commenter(driver, commentaire, aria_label):
    try:
        textarea = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//textarea[@aria-label='{aria_label}']"))
        )
        textarea.click()

        textarea = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//textarea[@aria-label='{aria_label}']"))
        )
        textarea.send_keys(commentaire)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'x1yc6y37'))
        )
        submit_button.click()

        time.sleep(temps_aleatoire())
        print("Commentaire ajouté.")
    except:
        print("Erreur lors de la publication du commentaire.")

def ouvrir_publication(driver, leCompte, compter, url_post):
    print("")
    print("---------------------------------------")
    print("Ouverture du compte ", compter,
          " | Utilisateur: ", leCompte[0], ". ")
    driver.get(url_post)
    print("---------------------------------------")
    time.sleep(2)
    valider_cookies(driver)
    time.sleep(2)
    rediriger(driver)
    time.sleep(2)
    remplir_formulaire(driver, leCompte)
    time.sleep(5)
    passer_intro(driver)
    print("---------------------------------------")
    time.sleep(2)
    nb_com = 0
    for _ in range(15):
        commentaire = choix_commentaire()
        commenter(driver, commentaire, "Ajouter un commentaire...")
        nb_com += 1
        print("commentaire: ", nb_com)
        print("---------------------------------------")
        if nb_com == 100:
            compter += 1
            print("accès au compte ", compter, " en cours..")
            nb_com = 0
            driver.quit()
            print("driver fermé")
            print("---------------------------------------")
            return compter  # Retourner le compteur pour le prochain compte

# URL de la publication
url_post = "https://www.instagram.com/......"

# Boucle principale pour gérer les comptes
compter = CL 
X = CL

while compter <= X:  # Limite de x comptes adapaté en fonction de la longueur du tableau comptes (CL)
    leCompte = choix_compte(compter)
    driver = init_driver()
    try:
        compter = ouvrir_publication(driver, leCompte, compter, url_post)
    except Exception as e:
        print(f"Erreur avec le compte {compter}: {e}")
        driver.quit()
        print("driver fermé suite à une erreur")
    time.sleep(5)  # Attendre avant de passer au compte suivant

time.sleep(12000)