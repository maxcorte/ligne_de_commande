import os
import shutil
import tkinter as tk
from tkinter import filedialog


def trier_par_extension(repertoire_source, repertoire_destination):
    try:
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

    except Exception as e:
        print(f"Erreur lors du tri des fichiers par extension : {e}")


def choisir_fichier():
    try:
        root = tk.Tk()
        root.withdraw()  # Ne pas afficher la fenêtre principale

        fichier_selectionne = filedialog.askopenfilename(title="Sélectionnez un fichier")
        return fichier_selectionne

    except Exception as e:
        print(f"Erreur lors de la sélection du fichier : {e}")
        return None


def creer_fichier(dossier, fichier):
    chemin_fichier = os.path.join(dossier, fichier)
    try:
        if chemin_fichier:
            with open(chemin_fichier, 'w'):
                print(f"Fichier '{chemin_fichier}' créé avec succès.")

    except PermissionError as e:
        print(f"Erreur de permission : {e}")
    except Exception as e:
        print(f"Erreur lors de la création du fichier : {e}")


def supprimer_fichier(supp):
    try:
        if supp:
            os.remove(supp)
            print(f"Fichier '{supp}' supprimé avec succès.")

    except FileNotFoundError:
        print(f"Le fichier '{supp}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier : {e}")


def renommer_fichier(ancien_nom):
    if ancien_nom:
        nouveau_nom = input("Entrez le nouveau nom du fichier : ")
        if nouveau_nom:
            try:
                # Utilisez os.rename pour renommer le fichier dans le même dossier
                os.rename(ancien_nom, os.path.join(os.path.dirname(ancien_nom), nouveau_nom))
                print(f"Fichier renommé de '{ancien_nom}' à '{nouveau_nom}'.")
            except FileNotFoundError:
                print(f"Le fichier '{ancien_nom}' n'existe pas.")
            except OSError as e:
                print(f"Erreur lors du renommage : {e}")


def choisir_dossier():
    try:
        root = tk.Tk()
        root.withdraw()  # Ne pas afficher la fenêtre principale

        dossier_selectionne = filedialog.askdirectory(title="Sélectionnez un répertoire")
        return dossier_selectionne

    except Exception as e:
        print(f"Erreur lors de la sélection du dossier : {e}")
        return None


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
                renommer_fichier(reno)
            elif choix == "5":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def main():
    interface_utilisateur()


if __name__ == "__main__":
    main()
