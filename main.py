from lecteur_fichier import lire_services, lire_demandes
from evenement import generer_evenements
from simulation import Simulation

# On lit les services et les demandes à partir des fichiers texte
services = lire_services("./Data/services.txt")
demandes = lire_demandes("./Data/demandes.txt")

# Affichage des services pour information
print("Services chargés:")
for service in services:
    print(f"Service {service.id}: capacité {service.capacity}")

# Affichage des demandes pour information
print("\nDemandes chargées:")
for demande in demandes:
    print(f"Demande {demande.id}: {demande.capacity} conteneurs de {demande.origin} à {demande.destination}, départ jour {demande.departure_day}")

# Création et exécution de la simulation
print("\nDémarrage de la simulation complète:")
simulation = Simulation(services, demandes)
simulation.executer()