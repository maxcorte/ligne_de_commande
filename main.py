import os
import argparse
import shutil


def trier_par_extension(repertoire_source, repertoire_destination):
    # les répertoires de destination existent ?
    if not os.path.exists(repertoire_destination):
        os.makedirs(repertoire_destination)

    # Parcoure tous les fichiers du répertoire
    for fichier in os.listdir(repertoire_source):
        chemin_fichier_source = os.path.join(repertoire_source, fichier)

        #  vérifie si il y a des fichiers
        if os.path.isfile(chemin_fichier_source):
            # Obtenez l'extension du fichier
            _, extension = os.path.splitext(fichier)
            extension = extension.lower()

            # Créez un répertoire pour l'extension si nécessaire
            repertoire_extension = os.path.join(repertoire_destination, extension[1:])
            if not os.path.exists(repertoire_extension):
                os.makedirs(repertoire_extension)

            # Déplace le fichier dans le répertoire correspondant à l'extension
            shutil.move(chemin_fichier_source, os.path.join(repertoire_extension, fichier))

    print("Tri des fichiers par extension terminé.")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Tri des fichiers par type d'extension.")
    parser.add_argument("source", help="Répertoire source des fichiers à trier.")
    parser.add_argument("destination", help="Répertoire destination pour le tri par extension.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    trier_par_extension(args.source, args.destination)


if __name__ == "__main__":
    main()