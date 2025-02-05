# Email Existence Checker

Ce script permet de vérifier si une adresse email existe en interrogeant les serveurs MX du domaine. Il utilise la bibliothèque `dnspython` pour récupérer les enregistrements MX du domaine et `smtplib` pour vérifier si l'email est valide via une connexion SMTP.

## Fonctionnalités

- Vérifie si une adresse email existe en résolvant les enregistrements MX du domaine.
- Si l'email existe, il renverra un message "[VVV] email [EXISTS]".
- Si l'email n'existe pas ou si un problème survient, il renverra un message "[XXX] email [NOT EXISTS]" ou "[!!!] ERROR".

## Prérequis

- Python 3.6+.
- Bibliothèque `dnspython` version 2.7.0.

## Installation

### Installation avec un environnement virtuel (`venv`)
1. Créer un environnement virtuel : `python3 -m venv venv`
2. Activer l'environnement virtuel :
   - Sous Linux/macOS : `source venv/bin/activate`
   - Sous Windows : `.\venv\Scripts\activate`
3. Installer les dépendances : `pip install dnspython==2.7.0`

**Note** : Si tu as un fichier `requirements.txt`, tu peux installer toutes les dépendances avec `pip install -r requirements.txt`

### Installation normale (sans environnement virtuel)
Si tu ne souhaites pas utiliser un environnement virtuel, tu peux installer `dnspython` globalement avec :  
`pip install dnspython==2.7.0`

## Utilisation
1. Exécuter le script pour vérifier si un email existe :  
`python emailActiv.py <email>`  
Remplace `<email>` par l'email que tu souhaites vérifier.  
Exemple : `python emailActiv.py test@example.com`

Le script retournera un message indiquant si l'email existe ou non.

## Résolution des problèmes
Si tu rencontres une erreur liée à la version de `dnspython`, le script vérifiera si la version correcte (2.7.0) est installée. Si ce n'est pas le cas, il affichera un message d'erreur avec une suggestion pour installer la bonne version. Exemple :  
`[... ] VERSION  <current_version> [KO]`  
`[ \o/ ] pip install dnspython==2.7.0`

### Exemple de sortie
Si l'email est valide :  
`[VVV] test@example.com [EXISTS]`  
Si l'email n'existe pas :  
`[XXX] test@example.com [NOT EXISTS]`  
Si une erreur survient pendant la tentative de vérification :  
`[!!!] ERROR test@example.com: <error_message>`

## Auteurs
Développé par [Ton Nom].
