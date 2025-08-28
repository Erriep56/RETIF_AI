import os
import json
import requests

# === Définition des variables ===

base_donnee = 4 # numéro de la base de données dans AGORHA (4 pour RETIF)
type_notice = "ARWORK" # types de notices à récupérer (ARTWORK pour les oeuvres)

# === Création du json === 

dir_export_json = "export_json"
if not os.path.exists(dir_export_json):
    os.makedirs(dir_export_json)

json_API = os.path.join(dir_export_json, f"export_{base_donnee}.json")



# NE FONCTIONNE PLUS SUITE À DES MODIFICATIONS DU FONCTIONNEMENT DE L'API

def export_db_json(num, jeton = None, all_notices=None) :
    if all_notices is None:
        all_notices = []

    params = {"noticeType": type_notice, # à modifier en fonction du type de données ("ARTWORK")
              "database": str(base_donnee), # à modifier en fonction de la base de données
              "token": jeton}

    requete = requests.get('https://agorha.inha.fr/api/notice/exportjson', params=params)
    # print(requete.url)

    reponse = requete.json()
    jeton = reponse.get("token", "")
    # print(jeton)
    notices = reponse.get("notices", [])
    # print(notices)
    all_notices.extend(notices)

    notice_ouput = os.path.join(dir_export_json, f"notices_{num}.json")

    with open(f"notices_{num}.json", "w", encoding="utf-8") as f:
        json.dump(notices, f, ensure_ascii=False)

    if len(jeton):
            export_db_json(str((int(num) + 1)), jeton=jeton, all_notices = all_notices)
    else :
        with open(json_API, "w", encoding="utf-8") as f_all:
            json.dump({"notices":all_notices}, f_all, ensure_ascii=False)
        print("fin")

resultat = export_db_json("1")



# === Création d'un fichier json contenant le lien des images ===

dir_export_links = "export_liens_images"
os.makedirs(dir_export_links, exist_ok=True)

# Charger le fichier JSON
with open(json_API, "r", encoding="utf-8") as f:
    data = json.load(f)

# Dictionnaire {uuid: lien de l'image}
images_links = {}

# Parcourir chaque notice
for notice in data.get("notices", []):
    permalink = notice.get("permalink")
    uuid = notice.get("internal", {}).get("uuid")
    prefPicture = (
        notice.get("content", {})
        .get("mediaInformation", {})
        .get("prefPicture", {})
        .get("thumbnail", "")
    )

    # Ajouter au dictionnaire si les deux infos sont présentes
    if uuid and prefPicture:
        images_links[uuid] = prefPicture

print(f"Nombre total de liens d'images trouvés : {len(images_links)}")

# Enregistrer dans un fichier JSON
json_images_links = os.path.join(dir_export_links, f"liens_images_{base_donnee}.json")

with open(json_images_links, "w", encoding="utf-8") as out_file:
    json.dump(images_links, out_file, ensure_ascii=False, indent=2)

print(f"Les liens des images ont été enregistrés dans {json_images_links}")


# === exporter les images dans un dossier ===

start_line = 0 # choix de la ligne de départ, peut être modifiée si besoin

# Charger les liens d’images
with open(json_images_links, "r", encoding="utf-8") as f:
    images_links = json.load(f)

total_images = len(images_links)

# Créer le dossier d’export s’il n'existe pas
dir_export_image = f"images/{base_donnee}"
os.makedirs(dir_export_image, exist_ok=True)

erreursfile = os.path.join(dir_export_links, f"erreurs_{base_donnee}.jsonl")

# Ouvrir le fichier d'erreurs en mode ajout
with open(erreursfile, "a", encoding="utf-8") as error_log:
    # Boucle principale
    for index, (uuid, img_url) in enumerate(images_links.items()):
        if index < start_line:
            continue

        if not img_url:
            json.dump({"uuid": uuid, "error": "Empty URL"}, error_log, ensure_ascii=False)
            error_log.write("\n")
            continue

        img_url = img_url.replace("thumbnail", "original")
        filename = os.path.join(dir_export_image, f"{uuid}.jpg")

        if os.path.exists(filename):
            print(f"[{index+1}/{total_images}] ✅ Déjà existant : {filename}")
            continue

        try:
            response = requests.get(img_url, timeout=10)
            if response.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"[{index+1}/{total_images}] ✅ Téléchargé : {filename}")
            else:
                raise Exception(f"HTTP {response.status_code}")
        except Exception as e:
            print(f"[{index+1}/{total_images}] ❌ Erreur : {img_url} -> {e}")
            json.dump({"uuid": uuid, "url": img_url, "error": str(e)}, error_log, ensure_ascii=False)
            error_log.write("\n")
        # time.sleep(1) # pas obligatoire puisque l'API d'AGORHA autorise

