# Déploiement continue

## Infrastructure et Environnement

### Cluster Kubernetes

Nous avons utilisé un cluster Kubernetes pour le déploiement de notre application en production. La configuration pour accéder au namespace qui nous a été assigné nous a été fournie par la compagnie.

### Base de données

Nous avons déployé la base de données utilisée tout au long des Lab 1 et 2 sur notre cluster Kubernetes. La base de données stocke les nouvelles données générées à partir du déploiement de l'application.

### Images Docker

Nous avons créé les images Docker nécessaires pour notre application HVAC :
- Image Docker Metrics : [nom_image_metrics]
- Image Docker Oxygen-CS : [nom_image_oxygen-cs]

Ces images sont utilisées dans les déploiements sur le cluster Kubernetes.

## Déploiement sur Kubernetes

Nous avons créé plusieurs ressources Kubernetes pour faciliter le déploiement et la gestion de nos conteneurs :

### ConfigMaps

Nous avons utilisé des ConfigMaps pour gérer les variables d'environnement qui n'ont pas besoin d'être secrètes, telles que l'adresse de l'hôte HVAC.

### Secrets

Nous avons également utilisé des Secrets pour gérer les variables d'environnement sensibles, tels que le HVAC_TOKEN.

### Deployments

Nous avons créé des Deployments pour chaque application (Metrics, Oxygen-CS) afin de simplifier la maintenance des conteneurs dans le cluster.

### Cron Job

Nous avons déployé un Cron Job qui crée des sauvegardes périodiques de nos métriques dans la base de données.

## Mise à jour des Images

Nous avons choisi d'utiliser [Option 1 / Option 2] pour la mise à jour de nos images déployées.

## Monitoring avec Grafana

### Connexion avec la Base de Données

Nous avons établi une connexion entre l'instance Grafana et notre base de données déployée dans le premier sous-requis. Cela nous permet de récupérer les informations de la base de données et de les afficher sur Grafana.

### Dashboard pour Oxygen-CS

Nous avons créé un dashboard sur Grafana qui permet de visualiser les données de l'application HVAC (Oxygen-CS). Le dashboard inclut des graphiques pour les températures et un tableau pour les événements liés à l'application.

### Dashboard pour Metrics

Nous avons également créé un dashboard sur Grafana pour visualiser les métriques de processus créées lors des laboratoires précédents (Kanban, pull-request et CI/CD). Les données/métriques sont présentées sous la forme de [votre choix de présentation].

