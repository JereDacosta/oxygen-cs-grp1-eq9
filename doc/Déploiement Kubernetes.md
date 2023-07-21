# Déploiement Kubernetes Oxygen-Cs

Pour déployer notre application Oxygen-Cs sur Kubernetes, nous avons ajusté notre fichier `OnPush.yml` pour inclure les étapes de déploiement et d'application du manifeste de Kubernetes. Nous avons également ajouté nos variables d'environnement dans le fichier de déploiement du manifeste, car sur Kubernetes, nos variables d'environnement sont stockées dans les secrets. En effectuant cette étape, nous nous assurons que nos applications reconnaissent les variables d'environnement depuis Kubernetes.

Pour répondre à la demande de ne pas dépasser 500 Mi de mémoire et de CPU, nous avons alloué les limites suivantes :

```yaml
resources:
  limits:
    cpu: "200m"
    memory: "200Mi"
  requests:
    cpu: "150m"
    memory: "150Mi"
