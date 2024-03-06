# Amélioration grâce à l'IA d'une application existante

Ce projet est un équivalent de ce que vous pourriez faire pour votre projet E2. Il va permettre de revoir pas mal de choses notamment : 
- la gestion de projet Agile
- un peu de dev à travers du packaging d'application avec Flask et des appels à une API externe
- la reconnaissance d'image avec 2 approches (la seconde étant **facultative**) :
>- une solution Cloud
>- une solution *on-premise*, c'est-à-dire locale
- la restitution des résultats (rapport et présentation orale)

## Contexte

Triof est une start-up de tri et de recyclage des déchets spécialisée dans le traitement des déchets plastiques. Elle a développé une machine qu'elle loue aux entreprise : grâce à cette dernière les salariés peuvent déposer leurs déchets plastiques afin qu'ils soient recyclés en fil d'impression 3D.

Il est important de trier les déchêts plastiques avant de les recycler car la température de fusion de chaque plastique est différente. L'entreprise a donc conçu une interface où l'utilisateur sélectionne le type de dêchet qu'il dépose dans la machine. 

Malheureusement on a remarqué que les personnes n'indiquaient pas toujours bien quel déchet ils inséraient or cela a un impact négatif sur la qualité du filament.

Triof vous sollicite pour proposer une solution intégrant de l'IA afin de pallier ce problème. Ils vous suggèrent d'utiliser les services Cloud dans un premier temps.

## 1ère partie : questions préliminaires

### 1. Généralités sur l'intégration d'une IA dans une application existante

1. Expliquer en un paragraphe ce qu'est l'architecture client/serveur et quels sont ses avantages.

Architecture de conception réseau où le client est un dispositif ou un programme qui demande de ressources ou de services et le serveur répond à ces demandes. Architecture très utilisée dans les applications réseau et internet car permet une répartition claire des tâches entre les clients et les serveurs: Centralisation de la gestion des données, sécurité, scalabilité des serveurs.

2. Expliquer ce qu'est un *web service* et son utilité dans le développement d'applications.

Un web service est un service disponible sur Internet ou sur un réseau interne qui permet la communication et l'échange de données entre différents logiciels ou applications via des protocoles web standards tels que HTTP, SOAP (Simple Object Access Protocol) ou REST (Representational State Transfer). Il fonctionne selon le principe de l'architecture client/serveur où le client envoie une demande au service web (souvent sous forme de requête HTTP) et le service web répond avec les données demandées, souvent en format XML ou JSON. Facilite l'intégration de systèmes disparatres, l'interopérabilité entre applications hétérogènes. Les web services jouent un rôle clé dans la création d'applications basées sur le cloud et les architectures microservices, facilitant le déploiement, la maintenance et la mise à l'échelle des applications modernes.

3. Expliquer en quoi un modèle packagé dans un *web service* permet de l'utiliser en production.

Un modèle packagé dans un web service fait référence à l'encapsulation d'un modèle de machine learning ou d'un algorithme dans un service web, le rendant accessible via des requêtes HTTP. Ce processus est souvent désigné sous le terme de déploiement de modèle ou de mise en production de modèle. L'idée est de transformer le modèle, qui est initialement développé et testé dans un environnement de recherche ou de développement, en un service accessible et utilisable en temps réel dans des applications de production.

Le packaging d'un modèle dans un web service facilite son utilisation en production en le rendant plus accessible, évolutif (scalabilité), et facile à maintenir, tout en assurant la sécurité et la conformité des données traitées.

### 2. Généralités sur les solutions Cloud de Computer Vision

Dans la mesure on nous sommes ici à l'école IA **Microsoft**, et qu'on a réussi à vous avoir quelques crédits pour utiliser Azure, on utilisera dans ce projet Custom Vision de Azure Cognitive Services


1. Décrire en quelques ligne le fonctionnement, le mode de tarification et le coût de ce service.

Le service Custom Vision de Azure Cognitive Services permet aux utilisateurs de créer, former et déployer des modèles de vision par ordinateur personnalisés. Voici comment il fonctionne :

a. **Création et entraînement** : Les utilisateurs commencent par télécharger des images dans Custom Vision, puis ils tagguent ces images pour créer des labels. Le service utilise ces données pour entraîner un modèle de reconnaissance d'images personnalisé. Les utilisateurs peuvent tester et affiner le modèle directement dans le portail Custom Vision.

b. **Évaluation et itération** : Après l'entraînement, le modèle peut être évalué à l'aide de nouvelles images pour vérifier sa précision. Les utilisateurs peuvent itérer sur ce processus, en ajoutant plus d'images et en réentrainant le modèle pour améliorer ses performances.

c. **Déploiement et prédiction** : Une fois satisfait de la précision du modèle, l'utilisateur peut le déployer comme un service web accessible via une API HTTP. Les applications clientes peuvent alors envoyer des images à cette API et recevoir en retour des prédictions du modèle.

Concernant le mode de tarification et le coût :

Azure Custom Vision propose généralement deux types de tarification : une pour la phase d'entraînement (Training) et une pour la phase de prédiction (Prediction).

- **Tarification d'entraînement** : Cette partie couvre les coûts associés à la création et à l'entraînement du modèle. Azure peut offrir un certain nombre d'heures d'entraînement gratuites chaque mois, après quoi des frais sont appliqués en fonction du temps d'entraînement et des ressources utilisées.

- **Tarification de prédiction** : Cette partie concerne les coûts associés à l'utilisation du modèle pour effectuer des prédictions. Cela peut être basé sur le nombre de prédictions faites, avec un certain nombre de prédictions gratuites allouées chaque mois et des frais supplémentaires appliqués au-delà de cette allocation.


2. Quels autres services Cloud fournis par différents providers (azure, google, amazon, ovh, etc) permettraient de répondre à la problématique exposée ? (vision par ordinateur et du traitement d'images personnalisé)

- **Google Cloud Vision AI** : Google Cloud propose Vision AI, un service qui permet aux utilisateurs de détecter des objets et des scènes dans des images, d'analyser des expressions faciales et de lire du texte imprimé. Google offre également **AutoML Vision**, qui permet aux utilisateurs de former des modèles de vision par ordinateur personnalisés sans avoir besoin d'une expertise approfondie en machine learning.

- **Amazon Rekognition** : Amazon Web Services offre Rekognition, un service qui permet d'identifier des objets, des personnes, du texte, des scènes et des activités dans des images et des vidéos, ainsi que de détecter tout contenu inapproprié. AWS propose également **SageMaker**, qui permet aux développeurs de construire, former et déployer des modèles de machine learning, y compris pour la vision par ordinateur.

- **IBM Watson Visual Recognition** : IBM propose un service de reconnaissance visuelle dans le cadre de ses services Watson qui permet aux utilisateurs de classifier et de former des modèles personnalisés pour reconnaître des éléments spécifiques dans des images.

- **OVHcloud AI Training** : Bien qu'OVHcloud ne propose pas directement un service de vision par ordinateur comme les autres, ils offrent AI Training, une solution qui permet aux utilisateurs de lancer des jobs de formation de machine learning, y compris pour les modèles de vision par ordinateur, en utilisant des ressources cloud.

3. Comparer ces différents services notamment en termes de coût, de mode de tarification, de rapidité. Vous pouvez synthétiser tout ça dans un tableau.

voir fichier joint: comparatifs-webservices.py

### 3. L'application Triof : analyse et compréhension du problème

Il s'agit dans un premier temps d'analyser le fonctionnement de l'application et d'expliquer votre compréhension du problème.

Pour cela, détailler les différents éléments de l'application : 
- la structure globale,
- les différents fichiers .py, .html, .css,
- que font les fonctions python
- etc...

### 4. Proposition d'une solution

Une fois cette partie terminée, vous devez avoir une vision nette du fonctionnement de l'application, une compréhension claire du problème et une idée des solutions Cloud existantes. Vous êtes donc en mesure de proposer une solution basée sur les services IA Cloud pour répondre au problème.

## 2ème partie : une solution IA Cloud

Élaboration, construction et intégration d'une solution utilisant Custom Vision de Azure Cognitive Services afin d'améliorer la classification des déchets de la machine Triof. Tout est dit ;)

### Gestion de projet Agile

Mettez en place **un planning Agile pour la construction d'une solution Cloud**.
Les 2 points fondamentaux de cette étape sont :
1. l'anticipation et la plannification des tâches (sachant que les questions préliminaires vous ont déjà fait gagner un peu de temps...)
2. l'estimation du temps passé sur chaque tâche

### Indications pour la mise en place de la solution Cloud

1. Entraîner sur Custom Vision un modèle de reconnaissance d'image permettant d'identifier les 3 types de déchets plastiques distingués par l'application (il y aura quelques étapes préalables notamment la création d'un groupe de ressources,  d'une ressource Cognitive Service et d'un projet Custom Vision)
2. Après avoir publié le modèle pour qu'il soit mobilisable par API, intégrer un appel API dans l'application en mettant en place la solution qui vous parait la plus adaptée : précocher le type de déchet plastique, suggérer le type de déchet, etc...

## 3ème partie facultative : une amélioration via une solution locale

### Re-contexte

Quelques mois se sont écoulés et Triof, très satisfait de votre travail, fait de nouveau appel à vous car ils font face à un autre problème : l'insertion par les salariés de déchets plastiques **sales** ce qui entraîne là encore, un fil d'impression de moindre qualité.

En revanche, une contrainte supplémentaire est qu'il ne veulent pas utiliser à nouveau Custom Vision afin de pouvoir monter en compétence sur l'IA en développant un modèle en local.

Proposer cette fois une solution sans recourir aux services IA Cloud pour résoudre ce problème.


### Indications pour la mise en place de la solution *on-premise*

- Vous êtes relativement libres sur cette partie mais l'idée est de construire un modèle permettant de classifier, en plus du type de déchet, la propreté du déchet.
- Vous pourrez soit construire votre propre modèle soit utiliser du *transfer learning* à partir de modèles de computer vision pré-implémentés.
- Une étape cruciale va être la constitution de votre jeu de données d'entraînement. Plusieurs solutions sont possibles notamment le scraping. Quoi qu'il en soit, n'oubliez pas l'existence de la *data augmentation*...
