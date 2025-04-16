from modeles import Service
from modeles import Demande

def lire_services(chemin_fichier):
    services = []
    with open(chemin_fichier, 'r') as fichier:
        next(fichier)  # sauter l'en-tête
        for ligne in fichier:
            if ligne.strip():
                parts = ligne.strip().split('\t')
                id_service = int(parts[0])
                capacite = int(parts[1])
                texte_route = parts[2]

                # Extraire la liste de tuples (départ, arrivée)
                raw_legs = texte_route.strip(';').split(';')
                route = []
                for leg in raw_legs:
                    if leg.strip():
                        debut, fin = leg.strip().split(', ')
                        route.append((debut, fin))

                service = Service(id_service, route, capacite)
                services.append(service)

    return services

def lire_demandes(chemin_fichier):
    demandes = []
    with open(chemin_fichier, 'r') as fichier:
        next(fichier)  # sauter l'en-tête
        for ligne in fichier:
            if ligne.strip():  # ignorer les lignes vides
                elements = ligne.strip().split('\t')
                id_demande = int(elements[0])
                capacite = int(elements[1])
                
                # Nettoyer les origines et destinations des points-virgules
                route_brute = elements[2].strip(';')
                origine, destination = route_brute.split(',')
                
                jour_depart = int(elements[3])
                temps_souhaite = int(elements[4])

                demande = Demande(
                    id_=id_demande,
                    capacity=capacite,
                    origin=origine.strip(),
                    destination=destination.strip(),  # Assure qu'il n'y a pas de ; ou d'espace
                    departure_day=jour_depart,
                    desired_time=temps_souhaite
                )

                demandes.append(demande)

    return demandes

#print(lire_services("./Data/services.txt"))
#print(lire_demandes("./Data/demandes.txt"))