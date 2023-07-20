# Utilisez l'image de base Python appropriée
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Définissez les variables d'environnement à l'aide des arguments de construction
ENV HOST=$HOST
ENV TOKEN=$TOKEN
ENV TICKETS=$TICKETS
ENV T_MAX=$T_MAX
ENV T_MIN=$T_MIN
ENV DATABASE=$DATABASE

# Installez les dépendances de l'application
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Expose le port utilisé par l'application
EXPOSE 8080

# Exécutez la commande de démarrage de l'application
CMD [ "python", "src/main.py" ]