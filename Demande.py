"""def lire_demande(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_demande}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation

# Solution 1 : Utiliser des doubles antislashs
nom_fichier = "C:\\Users\\quent\\Desktop\\Projet Simu opti décisionnel\\20221004_Donnees_Simulation_Reelles_IWNET\\fichier_demande_4_1_12_52.txt"
lire_demande(nom_fichier)
"""
"""def lire_demande_chemin(nom_demandes_chemin):
    try:
        with open(nom_demandes_chemin, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_demandes_chemin}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

nom_demandes_chemin="C:\\Users\\quent\\Desktop\\Projet Simu opti décisionnel\\20221004_Donnees_Simulation_Reelles_IWNET\\fichier_demandes_chemin_4_1_12_52.txt"
lire_demande_chemin(nom_demandes_chemin)
"""
def lire_services(nom_services):
    try:
        with open(nom_services, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_services}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

nom_services="C:\\Users\\quent\\Desktop\\Projet Simu opti décisionnel\\20221004_Donnees_Simulation_Reelles_IWNET\\fichier_services_4_1_12_52.txt"
lire_services(nom_services)


def lire_resultats(nom_resultats):
    try:
        with open(nom_resultats, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_resultats}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

nom_resultats="C:\\Users\\quent\\Desktop\\Projet Simu opti décisionnel\\20221004_Donnees_Simulation_Reelles_IWNET\\Resultat_4_1_12_52.txt"
lire_resultats(nom_resultats)