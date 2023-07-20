# Pipeline d'intégration continue

Ce document explique les différentes étapes de notre pipeline CI  mis en place sur GitHub. Notre pipeline vise à assurer la qualité du code, à exécuter des tests automatiques, à formater le code et à construire et publier une image Docker sur Docker Hub.

## Étapes du Pipeline

Voici les principales étapes executé dans notre pipeline.

### 1. Installation des dépendances Python

L'étape d'installation des dépendances Python garantit que toutes les dépendances requises pour exécuter notre application sont correctement installées. Cela permet de s'assurer que l'environnement de développement est cohérent pour tous les contributeurs du projet.

### 2. Tests avec pytest

Les tests automatisés jouent un rôle crucial dans la validation de la qualité et du bon fonctionnement de notre application Oxygen-cs. Nous utilisons le framework de test Pytest pour exécuter nos tests automatisés. Cette étape permet de vérifier si notre code fonctionne correctement et répond aux spécifications définies. Si les tests échouent, cela indique la présence d'un dysfonctionnement dans le code et arrête le pipeline CI.

### 3. Formattage du code avec Black

Le formattage du code est essentiel pour maintenir la cohérence et la lisibilité du code au sein de notre projet. Nous utilisons l'outil Black pour formater automatiquement notre code source Python. Cette étape s'assure que le code est uniformément formaté, facilitant ainsi la lecture, la compréhension et la collaboration entre les membres de l'équipe.

### 4. Linting avec Pylint

 Nous utilisons Pylint, un outil de linting populaire pour Python, pour effectuer l'analyse de notre code. Cette analyse a pour but de détecter les erreurs de programmation, les problèmes de style et les mauvaises pratiques. Le linting avec Pylint nous aide à identifier les problèmes potentiels dans notre code et à les corriger avant qu'ils ne deviennent des problèmes majeurs. Pylint nous permet d'évaluer notre code avec un score de 0 à 10. Nous visons le 10/10.

### 5. Construction de l'image Docker et publication sur Docker Hub

Nous utilisons Docker pour faciliter la gestion de nos applications dans des conteneurs. Cette étape consiste à construire une image Docker de notre application en utilisant un fichier de configuration Dockerfile et à la publier sur Docker Hub. La construction de l'image garantit que notre application est encapsulée dans un environnement reproductible, tandis que la publication sur Docker Hub permet de distribuer et de partager facilement notre image avec d'autres utilisateurs. L'image Docker est optimisée pour essayer d'être sous les 40 MO.