import shutil
import unittest
import os
import tempfile
from main import trier_par_extension, creer_fichier, supprimer_fichier, renommer_fichier


class TestLignesDeCommandes(unittest.TestCase):
    def setUp(self):
        # Crée un répertoire temporaire pour les tests
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Supprime le répertoire temporaire après les tests
        shutil.rmtree(self.temp_dir)

    def test_tri_par_extension(self):
        source_dir = os.path.join(self.temp_dir, 'source')
        destination_dir = os.path.join(self.temp_dir, 'destination')

        # Crée quelques fichiers dans le répertoire source
        os.makedirs(source_dir)
        open(os.path.join(source_dir, 'file1.txt'), 'w').close()
        open(os.path.join(source_dir, 'file2.jpg'), 'w').close()
        open(os.path.join(source_dir, 'file3.lol'), 'w').close()

        trier_par_extension(source_dir, destination_dir)

        # Vérifie que les fichiers ont été déplacés correctement
        self.assertTrue(os.path.exists(os.path.join(destination_dir, 'txt', 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(destination_dir, 'jpg', 'file2.jpg')))
        self.assertTrue(os.path.exists(os.path.join(destination_dir, 'lol', 'file3.lol')))
        self.assertFalse(os.path.exists(os.path.join(source_dir, 'bru')))

    def test_creer(self):
        dossier = os.path.join(self.temp_dir, 'test_folder')
        os.makedirs(dossier)

        fichier = 'test_file.txt'
        fichier2 = 'test_file2.txt'
        fichier3 = 'test_file3.txt'
        fichier4 = 'tes&hye.txt'

        creer_fichier(dossier, fichier)
        creer_fichier(dossier, fichier2)

        # Vérifie que le fichier a été créé dans le bon dossier
        self.assertTrue(os.path.exists(os.path.join(dossier, fichier)))
        self.assertTrue(os.path.exists(os.path.join(dossier, fichier2)))
        self.assertFalse(os.path.exists(os.path.join(dossier, fichier3)))

        with self.assertRaises(OSError):
            creer_fichier(dossier, fichier4)

    def test_supprimer(self):
        fichier_a_supprimer = os.path.join(self.temp_dir, 'file_to_delete.txt')
        fichier = os.path.join(self.temp_dir, 'file.txt')
        open(fichier_a_supprimer, 'w').close()
        open(fichier, 'w').close()

        supprimer_fichier(fichier_a_supprimer)

        # Vérifie que le fichier a été supprimé
        self.assertFalse(os.path.exists(fichier_a_supprimer))
        self.assertTrue(os.path.exists(fichier))

    def test_renommer(self):
        nouveau_nom = "nouveau_nom.txt"
        nouveau_nom2 = "-7&oezf.txt"
        identique = "file.txt"
        fichier = os.path.join(self.temp_dir, 'file.txt')
        open(fichier, 'w').close()

        renommer_fichier(fichier, nouveau_nom)

        self.assertTrue(os.path.exists(os.path.join(self.temp_dir, nouveau_nom)))
        with self.assertRaises(OSError):
            renommer_fichier(fichier, identique)
            renommer_fichier(fichier, nouveau_nom2)
