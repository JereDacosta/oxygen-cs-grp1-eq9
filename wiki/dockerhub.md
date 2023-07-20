# Publication des Images Docker sur Docker Hub

Ce document explique comment nos images Docker sont automatiquement publiées sur Docker Hub lorsque le pipeline est exécuté avec succès sur la branche principale (main). Les images sont publiées avec deux tags : "latest" et l'ID de l'exécution GitHub (github run-id).

## Tag "latest"

L'image est taguée avec le tag "latest". Ce tag représente la version la plus récente de l'image et est utilisé pour déployer la dernière version stable de notre application.

## Tag avec l'ID de l'exécution GitHub (github run-id)

En plus du tag "latest", nous utilisons l'ID de l'exécution GitHub (github run-id) comme deuxième tag. Cela nous permet d'associer l'image Docker à une exécution spécifique du pipeline CI/CD sur GitHub. En utilisant cet ID, nous pouvons facilement suivre l'historique des exécutions et associer une image Docker à une version spécifique de notre application.

# Repo DockerHub

Voici les deux repos DockerHub pour les projets metrics et oxygen-cs :

- https://hub.docker.com/r/jeredaco/oxygen-cs/tags
- https://hub.docker.com/repository/docker/jeredaco/metrics-cs/tags

