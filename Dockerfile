# Utilisez l'image de base Python appropriée
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Déclarez les arguments de construction comme variables d'environnement
ARG HOST
ARG TOKEN
ARG TICKETS
ARG T_MAX
ARG T_MIN
ARG DATABASE

# Définissez les variables d'environnement à l'aide des arguments de construction
ENV HOST=$HOST
ENV TOKEN=$TOKEN
ENV TICKETS=$TICKETS
ENV T_MAX=$T_MAX
ENV T_MIN=$T_MIN
ENV DATABASE=$DATABASE

# Installez les dépendances de l'application
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install

# Exécutez la commande de démarrage de l'application
CMD [ "python", "main.py" ]