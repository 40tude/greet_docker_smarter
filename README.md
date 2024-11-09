<!-- 
# remove all containers
docker rm -f $(docker ps -aq)
# remove image according the pattern 
docker rmi $(docker images -q "greet_img*")
-->

# Intro

- C'est juste pour faire des tests avec Jenkins
- Je veux lancer les test à chaque fois que je fais un push
- Jenkins tourne en local dans une image Docker

# Setup

Je fais une copie d'un autre répertoire où j'avais fais des tests de tests dansdes images Docker et où j'avais passé pas mal de temps à minimiser les fichiers requirements, Dockerfile... à maintenir. Si besoin lire ce [README.md](https://github.com/40tude/fraud_detection_2/blob/main/99_tooling/20_testing/README.md)

Je fais une copie de `C:\Users\phili\OneDrive\Documents\Programmation\fraud_detection_2\99_tooling\20_testing\05_greet_docker_smarter`

Dans ``C:\Users\phili\OneDrive\Documents\Tmp\greet_docker_smarter``

J'ouvre un terminal dans ce dossier

Je suis en environnement conda base

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


Je quitte VSCode

Je switch de nouveau en environnement `base`


```powershell
conda deactivate
code .
```

Je fais un commit du projet sur github



# Préparations pour Jenkins 

Supprimer container et images

```powershell
docker rm -f $(docker ps -aq)
docker rmi $(docker images -q "greet_img*")
```


## Modifier

La section greet-test du ``docker-compose.yml``
    * Dans ``environment:``, ajouter ``PYTHONPATH``
    * Dans `volumes:`, ajouter `./test-reports:/app/test-reports`
    * Dans ``command:`` ajouter l'option de génération de rapport xml et html

```dockerfile
greet_test:
      image: greet_img_test
      build: 
        context: .
        dockerfile: docker/Dockerfile
        args:
          REQUIREMENTS_4TESTS: requirements_4tests.txt
      container_name: greet_test
      environment:
        - PASSWORD=${PASSWORD}
        - PYTHONPATH=/app
      volumes:
        - ./app:/home/app
        - ./img:/home/img
        - ./test-reports:/app/test-reports
      working_dir: /home/app
      command: pytest --junitxml=/app/test-reports/pytest-report.xml --html=/app/test-reports/pytest-report.html
```

Modifier le fichier `docker/requirements_4test.txt` pour y ajouter `pytest-html`

```
# requirements_4test.txt

pytest
pytest-html
```

```powershell
./run_app.ps1
./test_app.ps1
```
Tout fonctionne. Un rapport est généré en 2 versions dans ``./test_reports``


Pour pouvoir visualiser le rapport, j'ouvre un terminal en dohors de VSCode

```powershell
conda activate testing_no_docker
conda install pytest-html -c conda-forge -y
cd C:\Users\phili\OneDrive\Documents\Tmp\greet_docker_smarter\test-reports\


```
