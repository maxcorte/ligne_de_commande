import os
import shutil
import tkinter as tk
import re
from tkinter import filedialog


def trier_par_extension(repertoire_source, repertoire_destination):
    if repertoire_source and repertoire_destination:
        # Assurez-vous que les répertoires de destination existent
        if not os.path.exists(repertoire_destination):
            os.makedirs(repertoire_destination)

        # Parcourez tous les fichiers du répertoire source
        for fichier in os.listdir(repertoire_source):
            chemin_fichier_source = os.path.join(repertoire_source, fichier)

            # Assurez-vous que l'élément est un fichier
            if os.path.isfile(chemin_fichier_source):
                # Obtenez l'extension du fichier
                _, extension = os.path.splitext(fichier)
                extension = extension.lower()

                # Créez un répertoire pour l'extension si nécessaire
                repertoire_extension = os.path.join(repertoire_destination, extension[1:])
                if not os.path.exists(repertoire_extension):
                    os.makedirs(repertoire_extension)

                # Déplacez le fichier dans le répertoire correspondant à l'extension
                shutil.move(chemin_fichier_source, os.path.join(repertoire_extension, fichier))

        print("Tri des fichiers par extension terminé.")


def choisir_fichier():
    root = tk.Tk()
    root.withdraw()  # Ne pas afficher la fenêtre principale

    fichier_selectionne = filedialog.askopenfilename(title="Sélectionnez un fichier")
    if fichier_selectionne:
        return fichier_selectionne
    else:
        raise FileNotFoundError("Aucun fichier sélectionné.")


def creer_fichier(dossier, fichier):
    if bool(re.match("^[a-zA-Z0-9_.]+$", fichier)):
        chemin_fichier = os.path.join(dossier, fichier)
        if chemin_fichier:
            with open(chemin_fichier, 'w') as file:
                if file:
                    print(f"Fichier '{chemin_fichier}' créé avec succès.")
                    return
    raise OSError("Le nom du fichier est invalide.")


def supprimer_fichier(supp):
    if supp:
        os.remove(supp)
        print(f"Fichier '{supp}' supprimé avec succès.")


def renommer_fichier(ancien_nom, nouveau_nom):
    if ancien_nom:
        nom = os.path.basename(ancien_nom)
        if bool(re.match("^[a-zA-Z0-9_.]+$", nouveau_nom)):
            if nouveau_nom and nouveau_nom != nom:
                os.rename(ancien_nom, os.path.join(os.path.dirname(ancien_nom), nouveau_nom))
                print(f"Fichier renommé de '{ancien_nom}' à '{nouveau_nom}'.")
                return
            raise OSError("Le nouveau nom du fichier est invalide.")
        raise OSError("Le nouveau nom du fichier est invalide.")


def choisir_dossier():
    root = tk.Tk()
    root.withdraw()  # Ne pas afficher la fenêtre principale

    dossier_selectionne = filedialog.askdirectory(title="Sélectionnez un répertoire")
    if dossier_selectionne:
        return dossier_selectionne
    else:
        raise FileNotFoundError("Aucun répertoire sélectionné.")


def interface_utilisateur():
    try:
        while True:
            print("\nMenu:")
            print("1. Trier des fichiers par extension")
            print("2. Créer un fichier")
            print("3. Supprimer un fichier")
            print("4. Renommer un fichier")
            print("5. Quitter")

            choix = input("Choisissez une option (1/2/3/4/5): ")

            if choix == "1":
                source = choisir_dossier()
                destination = choisir_dossier()
                trier_par_extension(source, destination)
            elif choix == "2":
                dossier = choisir_dossier()
                fichier = input("Entrez le nom du fichier à créer : ")
                creer_fichier(dossier, fichier)
            elif choix == "3":
                supp = choisir_fichier()
                supprimer_fichier(supp)
            elif choix == "4":
                reno = choisir_fichier()
                nom = input("Entrez le nouveau nom du fichier : ")
                renommer_fichier(reno, nom)
            elif choix == "5":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")
    except KeyboardInterrupt:
        print("\nFermeture du programme.")


def main():
    interface_utilisateur()


if __name__ == "__main__":
    try:
        interface_utilisateur()
    except FileNotFoundError as e:
        print(f"il manque un fichier {e}.")
    except PermissionError as e:
        print(f"Erreur de permission : {e}")
    except OSError as e:
        print(f"Erreur lors du renommage : {e}")
