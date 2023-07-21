# Modification du Code Source

Au niveau du code source fourni, nous avons implémenté deux nouvelles fonctionnalités.

## 1- Envoi des données de température à la base de données MySQL

Pour cette fonctionnalité, nous avons ajouté une méthode dans le fichier `main.py` appelée `send_temperature_to_database()`. Cette méthode permet d'envoyer les nouvelles données de température reçues à notre base de données MySQL. Les informations sont conservées dans la base de données avec un ID et un Timestamp pour une meilleure traçabilité.

## 2- Envoi des données d'événements à la base de données MySQL

La deuxième fonctionnalité ajoutée est liée à l'envoi des données d'événements à la base de données MySQL. Cette fonctionnalité est également implémentée dans le fichier `main.py` à l'aide de la méthode `send_event_to_database()`. La méthode envoie les nouvelles actions, qui peuvent être soit "TurnOnAc" (allumer la climatisation) ou "TurnOnHeater" (allumer le chauffage), à la base de données. Ces informations sont également enregistrées dans la base de données avec un ID et un Timestamp.
