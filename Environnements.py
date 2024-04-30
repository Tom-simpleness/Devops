#virtualisation
python3 -m venv venv

source venv/bin/activate
pip install pandas==1.5.3 requests==2.7.0

pip freeze > requirements.txt

#Docker images
Pour vérifier les images présentes sur votre VM, utilisez cette commande :

docker images

Pour supprimer une image en particulier, appliquez cette commande :

docker rmi <IMAGE ID>

Et pour supprimer toutes les images :

docker rmi $(docker images -q)

#Docker conteneurs
Pour afficher les conteneurs qui tournent :

docker ps

Stoppez-le en récupérant son id :

docker stop <CONTAINER ID>

Et stoppez tous les conteneurs en cours comme ceci :

docker stop $(docker ps -q)

Mais ce n'est pas tout, votre conteneur qui ne tourne pas prend de la place sur votre machine. Supprimez le seulement si vous ne voulez pas gardez de trâce des modifications que vous lui avez fait.

Affichez tous vos conteneurs avec leur taille avec cette commande :

docker ps -a -s

Supprimez tous vos conteneurs :

docker rm $(docker ps -a -q)

#Docker volumes
Listez vos volumes de la sorte :

docker volume ls

Supprimez tous vos volumes :

docker volume rm $(docker volume ls -q)

#Evaluation
help.datascientest.com. 

Sur votre machine virtuelle, rendez vous dans le dossier parent au dossier exam_NOM, puis créez une archive sans oubliez l'extension .tar :

tar -cvf exam_NOM.tar exam_NOM
Sur votre machine PERSONNELLE, téléchargez le fichier exam_NOM.tar qui se trouve sur votre machine virtuelle avec la commande suivante:

scp -i "<chemin_du_dossier_parent_à_la_clé_SSH>/data_enginering_machine.pem" ubuntu@IP_VM:<chemin_du_dossier_parent_à_l'archive>/exam_NOM.tar .