# Variable d'environnement

Pour les variables d'environnement, nous avons décidé d'en avoir 6 avec des valeurs par défaut.

- HOST: "http://34.95.34.5"
- TOKEN: "Default"
- TICKETS: 10
- T_MAX: 90
- T_MIN: 10
- DATABASE: "Default"

Pour lancer le script avec ces variables, utilisez la commande suivante :

```bash
HOST=$XXX TOKEN=$XXX TICKETS=$XXX T_MAX=$XXX  T_MIN=$XXX DATABASE=$XXX  pipenv run starts
