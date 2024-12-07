(English version below)

# Père et mère nöel secret.e
"Père et mère nöel secret.e" est un échange de cadeau entre un groupe de personne ; chaque personne offre un cadeau à une autre personne choisie aléatoirement dans le groupe. Un organisateur ou une organistrice est souvent choisi.e pour gérer la distribution des noms, mais celui-ci ou celle-ci ne peut pas bénéficier également de la surprise. De nombreux sites internet proposent de jouer le rôle d'organisation mais en profitent pour récupérer au passage les données sur les participant.e.s et les revendrent afin de se faire du fric sur leur dos. 
Voici un code python permettant de réaliser simplement cette attribution en utilisant des adresses mél.

## Installation

Pour télécharger ce code, vous pouvez télécharger sous format .zip depuis github ou entrer les commandes suivantes dans un terminal linux (pour installer `git` : https://git-scm.com/downloads/linux) ou un terminal `git for windows` (https://git-scm.com/downloads/win):
```bash
git clone https://github.com/CyannPlard/secret_santa.git
cd secret_santa
```

Pour utiliser ce code, vous aurez besoin d'un environnement `python3`, avec la bibliothèque `pyyaml`. Un fichier YAML `env.yml` est disponible afin de créer un environnement `conda` correspondant aux besoins (pour installer `conda` : https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) :
```bash
conda env create -f env.yml
conda activate secret_santa
```

## Configuration

* Les informations des personnes participantes doivent être intégrées dans le fichier `info_participant(e)s.yml` sous la forme suivante : `Name1 : name1.email@email.email`.
* La configation mél de l'organisateur.rice doit être intégrée dans le fichier `config.yml` suivant le format du fichier. /ATTENTION\ : ce fichier de configuration n'est pas sécurisé ; le mot de passe étant nécessairement écrit de manière explicite, ne pas téléverser ce fichier en ligne ! Il est préférable de l'effacer du fichier après avoir envoyé les mails.

Pour lancer l'attribution des père et mère noël secret.e.s et envoyer les mails, simplement lancer la commande suivante :
```bash
python secret_santa.py
```

# Secret santa (english version)

"Secret Santa" is a gift exchange within a group where each person gives a present to another randomly chosen participant. An organizer is often selected to manage the name distribution, but they don't get to enjoy the surprise themselves. Many websites offer to handle the organization but exploit the opportunity to collect participants' data and sell it for profit. Here's a Python code to easily manage the assignment process yourself.

## Installation

To download this code, you can either download it as a .zip file from GitHub or enter the following commands in a Linux terminal (to install `git`, visit: https://git-scm.com/downloads/linux) or in a `git for windows` terminal (https://git-scm.com/downloads/win):  
```bash
git clone https://github.com/CyannPlard/secret_santa.git
cd secret_santa
```

To use this code, you will need a `python3` environment with the library `pyyaml`. A YAML file `env.yml` is provided to create a matching `conda` environment (to install `conda`, visit: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html):  
```bash
conda env create -f env.yml
conda activate secret_santa
```

## Configuration

* The information of participating individuals should be added to the file `info_participant(e)s.yml` in the following format: `Name1: name1.email@email.email`.
* The organizer's email configuration should be added to the file `config.yml` following the file's format.  
  /WARNING\: this configuration file is not secure; the password must be written explicitly, so do not upload this file online! It is recommended to delete the password from the file after sending the emails.

To start assigning secret Santa matches and send the emails, simply run the following command:  
```bash
python secret_santa.py
```
