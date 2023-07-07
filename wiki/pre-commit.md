# Utilisation des Pre-commit Hooks 

Les Pre-commit Hooks sont des scripts ou des commandes qui s'exécutent automatiquement avant qu'un commit ne soit effectué sur le projet. Ils permettent d'automatiser les tâches de formatage du code, la vérification de la qualité, l'exécution des tests, etc.

## Installation 

1. Assurez-vous d'avoir Git installé sur votre système.

2. Ouvrez un terminal et accédez au répertoire racine de votre projet Python.

3. Lancez la commande `pre-commit install`

# Utilisation des Pre-commit Hooks

Une fois les Pre-commit Hooks installés, chaque fois que vous effectuez un commit dans votre projet Git, les hooks configurés seront automatiquement exécutés.

Lorsqu'un hook détecte des problèmes, il peut afficher un message d'erreur et empêcher le commit. Vous devrez alors corriger les problèmes signalés avant de pouvoir effectuer le commit.

Si vous souhaitez ignorer temporairement les hooks lors d'un commit, vous pouvez utiliser l'option --no-verify : `git commit --no-verify -m "Mon message de commit"`

# Hooks utilisés

- Test : PyTest
- Formattage : Black
- Linting : Pylint