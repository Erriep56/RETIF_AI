# 📦 Livrables du stage M2 TNAH - INHA, PictorIA

Ce dépôt contient les livrables réalisés dans le cadre de mon stage de Master 2 *Technologies Numériques Appliquées à l’Histoire* (TNAH) à l'INHA, en collaboration avec le consortium Huma-Num PictorIA, entre avril et juillet 2025.

---

## 📁 Contenu du dépôt

### 1. 🧠 Conversion du thésaurus Garnier (XML-RDF → JSON & TXT)

Le dossier [1_conversion_garnier](https://github.com/Erriep56/RETIF_IA/tree/main/1_conversion_garnier) contient un script Python permettant de convertir le fichier XML-RDF du **thésaurus Garnier (INHA)** en deux formats plus facilement exploitables : JSON et TXT et un Jupyter Notebook permettant de faire du matching en fonction d'une liste de titres.

Le fichier XML-RDF du thesaurus Garnier (INHA) est déjà contenu dans le dépôt.

#### ⚙️ Prérequis

Avant d'exécuter le script, installez la librairie `rdflib` :

```bash 
pip install rdflib
```

ou

```bash
cd 1_conversion_garnier
pip install -r requirements.txt
```

Le fichier Jupyter Notebook utilise le thésaurus ainsi généré pour chercher les termes du thésaurus parmi les titres. Le script n'est pas terminé complétement mais il est fonctionnel.



#### 📄 Fichiers générés

Deux fichiers sont ainsi générés :

- **JSON** : une représentation hiérarchique complète du thésaurus. Pour chaque concept, sont inclus :
  - L'URI (`id`)
  - Le label principal (`prefLabel`)
  - Les labels alternatifs (`altLabels`)
  - Les enfants (`children`)

  Les concepts sont structurés sous forme de dictionnaires imbriqués, triés par ordre alphabétique.

- **TXT** : une version textuelle du thésaurus, avec uniquement les labels principaux (`prefLabel`). La hiérarchie est visualisée grâce à une indentation par niveau.

---

### 2. 🖼️ Téléchargement des images du RETIF & Application Streamlit avec CLIP

Le dossier [2_projet_clip](https://github.com/Erriep56/RETIF_IA/blob/main/2_projet_clip) contient :
- **Deux notebooks Jupyter** :
  - Le **notebook 1** [1_recup_images_AGORHA.ipynb](https://github.com/Erriep56/RETIF_IA/blob/main/2_projet_clip/1_recup_images_AGORHA.ipynb) permet le téléchargement des images du RETIF via l’API d’AGORHA
  - Le **notebook 2** [2_embeddings_CLIP.ipynb](https://github.com/Erriep56/RETIF_IA/blob/main/2_projet_clip/2_embeddings_CLIP.ipynb) sert à générer les embeddings des images à l’aide du de la technologie CLIP
  
- Un fichier python [app.py](https://github.com/Erriep56/RETIF_IA/blob/main/2_projet_clip/app.py) permettant de lancer l'**application Streamlit** pour la recherche visuelle d’images à partir de texte et d'images, en s’appuyant sur les embeddings CLIP générés par le Notebook 2.


#### 🏃‍♀️ Lancer l'application Streamlit

Pour lancer l'application Streamlit, il faut d'abord télécharger les images avec le **Notebook 1** puis générer les embeddings avec le **Notebook 2**.

Ensuite, installer les `requirements_streamlit.txt` depuis le dossier `2_recup_images_CLIP`(ils peuvent être également installés avant l'utilisation des Jupyter Notebooks) :

```bash
pip install requirements_streamlit.txt
```

Pour lancer l'application, écrivez la commande suivante dans le terminal, depuis le dossier `2_projet_clip` :

```bash
streamlit run app.py
```


---

### 3. 📗 Protocole : Indexation avec Panoptic

Un fichier Markdown décrivant **le protocole d’utilisation de Panoptic** pour indexer les images du RETIF à l'aide du thesaurus Garnier. Ce document sert de guide pour reproduire l’indexation ou adapter le processus à d'autres corpus.

---

## 🧪 Environnement conseillé

- **Python 3.9 à 3.12+**
- Librairies nécessaires : 
  - `rdflib`
  - `streamlit`
  - `git+https://github.com/openai/CLIP.git`
  - `numpy==1.26.1`

---

## 📑 Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
