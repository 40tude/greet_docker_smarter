<!-- 
# remove all containers
docker rm -f $(docker ps -aq)
# remove image according the pattern 
docker rmi $(docker images -q "greet_img*")
-->

<!-- 
docker ps -a -q --filter "name=greet*" | ForEach-Object { docker rm $_ }
docker image ls --format "{{.Repository}}:{{.ID}}" | Select-String "^greet" | ForEach-Object { $id = ($_ -replace '.*:', ''); docker rmi -f $id }
 -->



<!-- ###################################################################### -->
<!-- ###################################################################### -->
# Intro

- C'est juste pour faire des tests avec Jenkins
- A la fin je veux lancer les tests à chaque fois que je fais un push sur GitHub
- Jenkins tourne en local dans une image Docker
- Les premiers tests montrent que c'est la misère (webhook, github doit appeler jenkins sur mon pc...)
- On va commencer par faire un lancement des tests si y a des changements sur Github en demandant d'aller vérifier toutes les 5 minutes 












<!-- ###################################################################### -->
<!-- ###################################################################### -->
# Setup

Je fais une copie d'un autre répertoire où j'avais fait des tests de testing dans des images Docker.
J'avais passé pas mal de temps à minimiser les fichiers requirements, Dockerfile... à maintenir. 
Si besoin lire ce [README.md](https://github.com/40tude/fraud_detection_2/blob/main/99_tooling/20_testing/README.md)

Je fais donc une copie de `C:\Users\phili\OneDrive\Documents\Programmation\fraud_detection_2\99_tooling\20_testing\05_greet_docker_smarter`
Dans ``C:\Users\phili\OneDrive\Documents\Tmp\greet_docker_smarter``

J'ouvre un terminal dans ce dossier
Je suis en environnement conda ``base``

code .

J'ajoute un .gitignore

Je fais le menage dans ``./assets`` et je supprime ``./img`` (sera recrée si besoin)

<p align="center">
<img src="./assets/img00.png" alt="drawing" width="400"/>
<p>

Je vérifie qu'il n'y a aucune image `greet_img` ou `greet_img_test` dans docker

J'ouvre un terminal à la racine du projet

```powershell
./run_app.ps1
./test_app.ps1
```
Tout fonctionne

<p align="center">
<img src="./assets/img01.png" alt="drawing" width="800"/>
<p>

Je quitte VSCode

Je switch en environnement `testing_no_docker` (où pytest est dispo)

```powershell
conda activate testing_no_docker
code .
```

J'ouvre un terminal à la racine du projet

```powershell
pytest
```

Tout fonctionne

<p align="center">
<img src="./assets/img02.png" alt="drawing" width="800"/>
<p>


Je switch de nouveau en environnement `base` et je relance VSCode


```powershell
conda deactivate
code .
```

Je fais un commit du projet sur github








<!-- ###################################################################### -->
<!-- ###################################################################### -->
# Préparation avant Jenkins
* Je ne vais pas pas pouvoir garder les ``secrets.ps1`` car quand Jenkins va vouloir faire quoi que ce soit, il le fera dans un contexte Linux
* Impossible pour lui de lancer `run_app.ps1` ni ``./secrets.ps1`` 

```powershell
# run_app.ps1

. "./app/secrets.ps1"
docker-compose up greet -d 
```

* Je vais 
    * utiliser les ``.env`` qui sont reconnus par docker-compose 
    * revérifier que tout fonctionne bien une seconde fois

## Installer les ``.env``

* Renommer ``./app/secrets.ps1`` en ``./app/secrets.ps1.bak``
* Ajouter ``.env`` à ``.gitignore``
* Ecrire le ``./app/.env`` correspndant à ``./app/secrets.ps1``


```powershell
# .env
PASSWORD=Zoubida_For_Ever
```

* Modifier `run_app.ps1` et `test_app.ps1`
    * Oui, oui je sais on pourra plus l'utilisé sous Jenkins mais pour l'instant il permet de tester la ligne de command qu'il faudra utiliser 
    * Exemple avec `run_app.ps1`


```powershell
# run_app.ps1

# . "./app/secrets.ps1"
# docker-compose up greet -d 

docker-compose --env-file ./app/.env up greet -d 
```

Avant d'essayer de lancer les containers, supprimer les containers et images utilisés avec "greet" préalablement 


```powershell
./clean_greet.ps1
```

Ensuite 


```powershell
./run_app.ps1
./test_app.ps1
```


Tout fonctionne

<p align="center">
<img src="./assets/img05.png" alt="drawing" width="800"/>
<p>


* Une image est générée dans ./img
* Un rapport est généré en 2 versions dans ``./test_reports``
    * Pour le rapport j'ouvre ``./test-reports/pytest-report.htm`` avec un browser


<p align="center">
<img src="./assets/img04.png" alt="drawing" width="800"/>
<p>



<!-- ###################################################################### -->
<!-- ###################################################################### -->
# Vérification avant Jenkins 


Lancer Jenkins. Dans mon cas je fais : 

```powershell
cd C:\Users\phili\OneDrive\Documents\Programmation\Formations_JEDHA\04_Data_Science_Lead2_oct_2024\07_MLOps\02_CICD\sample-jenkins-server
docker-compose up
```
Attendre 3H puis aller sur http://localhost:8080/


<p align="center">
<img src="./assets/img06.png" alt="drawing" width="800"/>
<p>









<!-- ###################################################################### -->
## Lancer l'application est les test dans des images












<!-- ###################################################################### -->
<!-- ###################################################################### -->
# Jenkins
New job
pipeline
Un vrai clickodrome...