import os
import shutil
import tkinter as tk
from tkinter import filedialog


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


def creer_fichier(chemin_fichier):
    with open(chemin_fichier, 'w'):
        print(f"Fichier '{chemin_fichier}' créé avec succès.")


def supprimer_fichier(chemin_fichier):
    try:
        os.remove(chemin_fichier)
        print(f"Fichier '{chemin_fichier}' supprimé avec succès.")
    except FileNotFoundError:
        print(f"Le fichier '{chemin_fichier}' n'existe pas.")


def renommer_fichier(ancien_nom, nouveau_nom):
    try:
        os.rename(ancien_nom, nouveau_nom)
        print(f"Fichier renommé de '{ancien_nom}' à '{nouveau_nom}'.")
    except FileNotFoundError:
        print(f"Le fichier '{ancien_nom}' n'existe pas.")


def choisir_dossier():
    root = tk.Tk()
    root.withdraw()  # Ne pas afficher la fenêtre principale

    dossier_selectionne = filedialog.askdirectory(title="Sélectionnez un répertoire")
    return dossier_selectionne


def interface_utilisateur():
    source = choisir_dossier()
    destination = choisir_dossier()
    while True:
        print("\nMenu:")
        print("1. Trier des fichiers par extension")
        print("2. Créer un fichier")
        print("3. Supprimer un fichier")
        print("4. Renommer un fichier")
        print("5. Quitter")

        choix = input("Choisissez une option (1/2/3/4): ")

        if choix == "1":
            trier_par_extension(source, destination)
        elif choix == "2":
            chemin_fichier = input("Entrez le chemin vers le fichier à créer : ")
            creer_fichier(chemin_fichier)
        elif choix == "3":
            chemin_fichier = input("Entrez le chemin vers le fichier à supprimer : ")
            supprimer_fichier(chemin_fichier)
        elif choix == "4":
            ancien_nom = input("Entrez le chemin vers le fichier à renommer : ")
            nouveau_nom = input("Entrez le nouveau nom du fichier : ")
            renommer_fichier(ancien_nom, nouveau_nom)
        elif choix == "5":
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


def main():
    interface_utilisateur()


if __name__ == "__main__":
    main()
