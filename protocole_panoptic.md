# Protocole pour l'utilisation de Panoptic sur le RETIF

# **1 \- Préambule**

Ce protocole a pour vocation de présenter les technologies offertes par [*Panoptic*](https://github.com/CERES-Sorbonne/Panoptic) pour envisager l’indexation les tableaux du [RETIF](https://agorha.inha.fr/database/4) à l'aide du thésaurus Garnier.

## A \- Le Thésaurus

Tout au long du processus, il est recommandé de disposer d’une version structurée du thésaurus Garnier interrogeable à tout moment, afin de pouvoir effectuer des recherches lors de l’emploi d’un nouveau descripteur. Nous conseillons d’utiliser une version en format texte (txt) dont la hiérarchie est restituée par des indentations, elle peut être récupérée à partir du fichier RDF à l’aide du script Python présent ici : [https://github.com/Erriep56/RETIF\_IA/tree/main/1\_conversion\_garnier](https://github.com/Erriep56/RETIF_IA/tree/main/1_conversion_garnier). 

## B \- Ordre des tâches

À l’exception des premières étapes, ce protocole **n'est pas chronologique**, les fonctionnalités indiquées sont à prendre en considération tout au long l'indexation. Nous conseillons donc de lire l'ensemble de ce guide avant de commencer le travail.

## C \- Points d’attention

Indexer plus de 12 000 images constitue, pour un seul indexeur, une tâche considérable. Il est important de rappeler que chaque image est accompagnée d’un titre : l’indexation doit donc s’appuyer sur ces données existantes et chercher à leur apporter des informations complémentaires. Par ailleurs, ce travail **n’a pas vocation à atteindre la perfection**. L’objectif est avant tout d’améliorer significativement l’état actuel de l’indexation et de faciliter les recherches, tout en économisant un temps considérable par rapport à un traitement manuel image par image.  
Même en utilisant l’outil Panoptic, l’indexation **ne doit pas devenir une épreuve de vitesse** : **chaque image doit être observée** avant qu’un descripteur ne lui soit associé.

# **1 \- Étapes préliminaires**

## A \- L’indexation

La première étape consiste à comprendre le rôle de l’indexation, en particulier sur la plateforme [AGORHA](https://agorha.inha.fr/). Idéalement, avant de commencer le travail, il faut penser à son utilité pour la recherche en histoire de l’art, mais aussi dans d’autres disciplines, en tenant compte des usages actuels et des besoins futurs. Cette phase suppose également de **solliciter l’expertise des documentalistes** et, si possible, **d’interroger les pratiques des utilisateurs** des bases de données.

## B \- comprendre et prendre en main le thésaurus Garnier

Avant de commencer l’indexation, il est recommandé d’**étudier d'abord l’usage du thésaurus et son organisation**, en particulier comment il est utilisé pour d’autres notices. Voici les concepts que nous conseillons de prendre en considération pendant cette tâche : 

- le **caractère général de la représentation**, notamment les sujets (*sujet biblique, sujet mythologique, portrait, scène de genre, nature morte,...*)  
- la **scène représentée** (*Annonciation, bataille, métamorphose...)*  
- les **personnages** et les **lieux représentés**  
- les **éléments particuliers** (animaux, objets, etc.)

Au cours de l’indexation, il faut être attentif aux difficultés possibles, notamment pour décrire des concepts abstraits ou émotionnels tels que la joie ou la tristesse, qui peuvent être des caractères intéressants à noter. Enfin, l’indexation reste une démarche interprétative : **il n’existe pas de solution parfaite**. L’objectif est de fournir une **description cohérente de la représentation** qui peut être exploitée pour la recherche.  
Nous recommandons de consulter les graphiques présentés ici, en particulier la section « Concepts utilisés », permettant de visualiser l’usage des termes du thésaurus selon les différentes bases de données. Dans cette section, il est possible de filtrer les concepts en sélectionnant une base de données dans le diagramme de gauche. [Liens datavisualisations](https://public.tableau.com/app/profile/pierre.husson/viz/AGORHA/UtilisationdeGarnierdansAgorha) 

## C \- Intégrer les images et les métadonnées dans Panoptic

### Les images

La première étape est d'intégrer les images dans Panoptic. Le modèle CLIP procédera ensuite à leur **encodage**. Attendez que le processus soit terminé avant de les manipuler. Il est recommandé d’encoder les images en couleurs (RGB) et **en noir et blancs (greyscale)** pour obtenir de meilleurs résultats lors des recherches par similarité.

### Les métadonnées

Ensuite, intégrer les **métadonnées** issues des notices d’AGORHA est primordial pour faciliter l’identification des scènes et permettre des sélections. Notez que le moteur CLIP n’est pas plus performant lorsque les images sont accompagnées de données textuelles.

Les informations les plus importantes à sélectionner sont le **titre**, pour faciliter la reconnaissance du sujet, et **l’artiste auteur** **du modèle**, permettant de rassembler les copies si l’auteur du modèle est identifié.  
Les dates et le lieu de conservation peuvent parfois faciliter le travail, mais ces données sont facultatives pour l'indexation iconographique.

L'intégration des données dans panoptic demande de se plier à un format de données précis : il doit prendre la forme d’un tableur csv organisé ainsi :

- Les séparateurs du csv doivent être des **points virgules “;”** (les **virgules** “,” servent de séparateurs entre des *tags*)  
- L’en-tête de la première colonne doit contenir le **chemin absolu** des images du projet et son en-tête doit s’intituler ***path***  
- Chaque colonne qui contient des informations à intégrer dans l’application doit avoir pour **en-tête** le **nom de propriété** suivi immédiatement du **type de la propriété entre crochets**, par exemple `auteur[tag]` ou encore `titre[text]`  
- Voici la liste des types de propriétés disponibles :  
  - text  
  - tag  
  - multitag  
  - color   
  - date  
  - checkbox (boîte à cocher)

- Pour les catégories ***\[tag\]*** et ***\[multitag\],*** les virgules servent de séparateur entre les étiquettes 

Voici un exemple de tableur prêt à être importé :

| path | Titre\[text\] | Artiste\[tag\] | Indexation préexistante\[multitag\] | Date\[date\] | Image traitée\[checkbox\] |
| :---- | :---- | :---- | :---- | :---- | :---- |
| /home/images/1.jpg | Les Noces de Cana  | Paul Véronèse | Sujet biblique, Christ | 1560 | False |
| /home/images/2.jpg | L’homme au gant | Titien | portrait, homme, en buste, gant | 1540 | True |

En langage csv, le fichier est présenté ainsi :  
path;Titre\[text\];Artiste\[tag\];Indexation préexistante\[multitag\];Date\[date\];Image traitée\[checkbox\]  
/home/images/1.jpg;Les Noces de Cana;Paul Véronèse;Sujet biblique, Christ;1560;False  
/home/images/2.jpg;L’homme au gant;Titien;portrait, homme, en buste, gant;1540;True

# **3 \- L’indexation avec panoptic**

Comme indiqué en préambule de ce guide, lors de l’indexation, il faut se référer constamment au thesaurus lors de l’utilisation d’un nouveau terme et toujours observer les images.  
Pour accompagner le lecteur, nous présentons ici les fonctionnalités de Panoptic utiles pour l'indexation iconographique de ce corpus. L’ordre de leur utilisation est à titre indicatif mais ne doit pas constituer une obligation.  
Notons que Panoptic ne permet pas de faire des zooms dans les images. Un curseur en haut de l’interface permet d’agrandir leur taille d’affichage. En maintenant la touche “contrôle” enfoncée et en passant la souris sur les images, elle peuvent être observées en plus grande taille. 

## A \- Créer des clusters

L’outil **créer des *clusters*** permet de séparer le corpus en plusieurs groupes d’images similaires entre elles afin d’identifier les schémas visuels récurrents au sein de la base de données. Deux types de *clusters* sont utiles : 

- Créer un **nombre défini** de *clusters* : permet de créer un nombre fixe de clusters dans lesquelles les images vont être réparties en fonction de leur similarité réciproque. Les clusters peuvent être enregistrés si besoin. Chaque cluster possédera un nombre à peu près équivalent d’images. Cela peut être problématique lorsque les ensembles homogènes d’images sont de tailles différentes (dans le cas du RETIF, il y a environ 300 natures mortes sur 12000 images, il faudrait donc créer autour de 40 *clusters* pour que l’un d’entre eux les rassemble. Au contraire, il y a plus d’un millier de Vierge à l'enfant). Cet outil est surtout utile pour l’exploration et la compréhension du corpus.  
- Créer des clusters en fonction d’un **seuil** de similarité entre les images : les clusters ne contiendront qu’un groupe d’images dont la similarité est égale ou supérieure au seuil défini. Cette fonction est utile pour identifier des doublons, des copies ou des groupes d'images, sans limitation du nombre de cluster. Cependant, elle demande parfois un temps de chargement assez long, et peut créer un trop grands nombres de regroupements.

Ces fonctionnalités peuvent également être appliquée sur une **fraction** du corpus qui a préalablement été filtré. Par exemple, dans un groupe de paysage, cet algorithme peut permettre de différencier des ensembles (montagneux, urbains,...).

## B \- Recherche avec CLIP

CLIP permet de chercher des images à l'aide de requêtes textuelles sans sonder les métadonnées, mais en s’appuyant sur les paires images-textes que le modèle a analysé au cours de son entraînement. Il faut noter que cette fonction n’est pas toujours efficace pour analyser des tableaux, puisque le modèle a surtout été entraîné sur des photographies. (Le modèle utilisé par le plugin PanopticML est le modèle Vit-B/32, ce n’est pas le plus puissant mais il est performant et léger). Il est recommandé de chercher en anglais. Cette fonction peut être utile pour chercher des éléments de la représentation, particulièrement quand le titre ne les mentionne pas. Voici quelques exemples qui peuvent être intéressants à chercher : les animaux, les objets (notamment ceux présents dans les natures mortes ou les intérieurs), des sujets iconographiques aux caractéristiques formelles récurrentes (paysages, plafonds, croix,...), des lieux identifiables (Venise, Rome) ou des personnages à l’apparence normalisée (Polichinelle, les papes), des périodes historiques (Antiquité), des éléments de paysage et des bâtiments (châteaux, pyramides, obélisques, arbres,...).

## C \- Lespropriétés

Nous conseillons de créer plusieurs propriétés multitags pour repartir les étiquettes liées à des termes du thesaurus, Une seule propriété rassemblant tous les descripteurs utilisé provoque des problèmes d’ergonomie.  
Lors de notre expérimentation, nous avons réparti les termes utilisés dans différentes catégories : "sujet" pour le thème de la représentation (*nature morte, sujet biblique…*), "scène" pour la scène représentée en particulier (*les Noces de Cana, métamorphose,..*.) , "personnage" pour les figures reconnaissables, comme les saints, "animaux", "objets", "éléments de paysage", "lieu identifié" pour les villes et lieux,...  
De plus, une propriété ***checkbox*** peut être créée afin d’indiquer quand l'indexation des images est considérée comme achevée, afin de ne pas avoir à l’analyser de nouveau et de l'écarter des prochaines analyses. Cette propriété doit surtout garder un caractère indicative et permettre d'écarter des images lors de certaines tâches. (Rappelons que si sa complétion pourrait représenter l’aboutissement du travail, une bonne indexation ne nécessite pas d’avoir décrit l’ensemble du contenu de chaque image, mais d'avoir identifié des éléments utiles pour les différentes recherches touchant à ce corpus.)

## D \- Rechercher dans les titres

Pour rechercher efficacement dans les titres sans prendre en compte les autres métadonnées, il est préférable d’utiliser l’outil ***Filtrer*** puis d’utiliser le volet “*contient*” afin de limiter la recherche à cette propriété.   
Cette recherche est efficace pour identifier les genres iconographiques (“paysage”, “‘nature morte”,...).  
Cependant, dans de nombreux cas, il faut faire preuve de precautions. C’est notamment cas pour les homonymes, les mots similaires sans rapport hiérarchique et les noms de personnes. Par exemple, pour les saints, il faut d'abord commencer par traiter le plus complexe avant d’aller vers le plus simple : les “saint Jean Chrysostome” et “saint Jean-Batiste” doivent être identifiés avant de chercher “saint Jean”.

## E \- l'outil grouper et proposer d’images similaires

L’une des fonctionnalités permet de grouper les images en fonction des différents tags d'une propriété : les images seront répartis selon l’étiquette qui les décrit au sein d’une propriété. Ensuite, Panoptic peut proposer des images similaires à un groupe ainsi formé. En les ajoutant au groupes, ces images recevront ce tag pour les décrire. Cette fonctionnalité est utile quand on a identifié quelques images correspondant à un terme du thesaurus et qu’on veut en trouver d'autres à indexer ainsi. Par exemples, après avoir identifié des images de crucifixion et indexé à l’aide du tag “Crucifixion” dans la propriété “Scène”, on effectue un groupement selon cette propriété. Les images vont alors être divisés selon les tags de la propriété, et un bouton permet de proposer des images similaires pour un groupe donné, qui pourront être ajoutées ou refusées. 

## F \- consulter les images similaires

En cliquant sur une image, une fenêtre s’ouvre : les métadonnées apparaissent à gauche tandis qu’à droite s’affiche une galerie d’images similaires, classées de la plus proche à la plus éloignée. Ces images peuvent être sélectionnées et indexées ensemble. En maintenant la touche *Ctrl* enfoncée et en passant la souris dessus, il est possible de les agrandir.

## Quelques remarques techniques

- Après de la sélection multiple de plusieurs images pour les tagguer ensemble, il ne faut pas oublier de les désélectionner en appuyant sur la croix en haut à droite. Ajouter une étiquette à une image ne retire la retire pas de la sélection.  
- Lors de l’écriture d’une nouveau tag dans une propriété, ne pas oublier d’appuyer sur la touche entrée pour valider sa création.

# **CLIP en quelques mots**

CLIP est une technologie de vision par ordinateur, dont le modèle original Vit-L a été conçu par OpenAI. Ce modèle est entraîné sur plusieurs millions de paires textes-images afin de les rapprocher dans un même espace vectoriel. Lors de son utilisation, le modèle encode des textes et des images, en créant une suite de nombre mathématiques, pour les placer dans cet espace vectoriel commun. Au sein de cet espace, plus une image et un texte est proche, plus il est probable que le texte décrive l’image, et inversement.  
Les modèles entraînés à l'aide de cette méthode peuvent être téléchargés sur un ordinateur pour encoder un corpus d’images ou de textes, calculer des similarités entre les images ou effectuer des recherches en langage naturel.