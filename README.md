# Discord Bot: Delete Messages

## Description

Ce script Python crée un bot Discord en utilisant la bibliothèque `discord.py`. Le bot permet à un utilisateur de supprimer tous ses messages dans un canal Discord en envoyant la commande `!delete_messages`. Avant de procéder à la suppression, le bot demande une confirmation via une réaction emoji "✅". Si l'utilisateur confirme, le bot supprimera tous ses messages envoyés dans les 1000 derniers messages du canal.

## Fonctionnalités

- **Commande `!delete_messages`** : Supprime tous les messages d'un utilisateur dans un canal.
- **Confirmation par réaction** : L'utilisateur doit confirmer avec un emoji "✅" avant que la suppression ne commence.
- **Suppression jusqu'à 1000 messages** : Le bot parcourt les 1000 derniers messages pour supprimer ceux envoyés par l'utilisateur.

## Prérequis

Avant de pouvoir exécuter ce bot, tu dois t'assurer d'avoir :

- **Python 3.5+** installé sur ton système.
- La bibliothèque `discord.py` installée. Tu peux l'installer en exécutant la commande suivante :
  ```bash
  pip install discord.py
Un token Discord pour ton bot. Si tu n'en as pas, tu peux en créer un en suivant ces étapes :
Va sur le portail des développeurs Discord.
Crée une nouvelle application.
Crée un bot pour cette application.
Copie ton token dans le fichier TK.txt (plus d'infos ci-dessous).
Installation
Clone ou télécharge ce dépôt.
Crée un fichier nommé TK.txt dans le même répertoire que ton script et place-y ton token Discord (sans espaces supplémentaires) : TonTokenDiscordIci

Installe les dépendances Python nécessaires :
pip install discord.py
Lance le bot avec la commande suivante :
python bot.py

Comment utiliser

Invite le bot sur ton serveur Discord (assure-toi d'ajouter les permissions nécessaires).
Dans un canal où le bot est présent, envoie la commande !delete_messages.
Le bot répondra avec un message de confirmation et attendra que tu réagisses avec l'emoji "✅" pour confirmer la suppression.
Une fois confirmé, le bot supprimera tous tes messages dans le canal.

Exemple : 

Commande envoyée :!delete_messages
Réponse du bot : @TonPseudo, je vais supprimer tous vos messages. Confirmez avec ✅.

L'utilisateur réagit avec "✅" et le bot commence à supprimer les messages envoyés par l'utilisateur dans le canal.

Message final du bot :
✅ @TonPseudo, j'ai supprimé 42 de vos messages.

Aide et support
Si tu rencontres des problèmes, n'hésite pas à ouvrir un ticket ou à poser une question dans les issues de ce dépôt.

Consulte aussi la documentation officielle de discord.py pour plus d'informations sur l'utilisation de la bibliothèque.

Licence
Ce projet est sous la licence MIT. Consulte le fichier LICENSE pour plus d'informations.

