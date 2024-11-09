<!-- 
# remove all containers
# docker rm -f $(docker ps -aq)
# remove image according the pattern 
# docker rmi $(docker images -q "greet*_img")
-->


Je fais une copie de `C:\Users\phili\OneDrive\Documents\Programmation\fraud_detection_2\99_tooling\20_testing\05_greet_docker_smarter`

Dans ``C:\Users\phili\OneDrive\Documents\Tmp\greet_docker_smarter``

J'ouvre un terminal dans ce dossier

Je suis en environnement conda base

code .

J'ajoute un .gitignore

Je fais le mesage dans./assets et je supprime ./img (sera recrée si besoin)

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

Je switch en environnement `testing_no_docker`

code .

```powershell
pytest
```

Tout fonctionne

<p align="center">
<img src="./assets/img02.png" alt="drawing" width="800"/>
<p>


Je quitte VSCode

Je switch en environnement `base`

code .






Je fais un commit sur github