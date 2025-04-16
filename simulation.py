from lecteur_fichier import lire_services, lire_demandes
from evenement import Evenement, generer_evenements

class Simulation:
    def __init__(self, services, demandes):
        # Initialisation avec les services et les demandes
        self.services = services
        self.demandes = demandes
        
        # Pour chaque demande, calculer la date limite d'arrivée
        for demande in self.demandes:
            # La date limite = jour de départ + temps souhaité
            demande.date_limite = demande.departure_day + demande.desired_time
        
        # Dictionnaire pour stocker les informations sur le trajet des terminaux
        # structure: {service_id: {terminal: [jours]}}
        self.carte_des_jours = {}
        
        # Créer une carte des jours où chaque service passe par chaque terminal
        for service in services:
            service_map = {}
            
            for debut, fin in service.route:
                terminal_debut = debut[0]  # La lettre du terminal (ex: "A" de "A1")
                jour_debut = int(debut[1:])  # Le jour exact (ex: 1 de "A1")
                
                terminal_fin = fin[0]
                jour_fin = int(fin[1:])
                
                # Ajouter le terminal de départ avec son jour exact
                if terminal_debut not in service_map:
                    service_map[terminal_debut] = []
                service_map[terminal_debut].append(jour_debut)
                
                # Ajouter le terminal d'arrivée avec son jour exact
                if terminal_fin not in service_map:
                    service_map[terminal_fin] = []
                service_map[terminal_fin].append(jour_fin)
            
            # Trier les jours pour chaque terminal
            for terminal in service_map:
                service_map[terminal].sort()
                
            self.carte_des_jours[service.id] = service_map
        
        # Résultats de l'affectation des demandes
        self.resultats = []
    
    def trouver_meilleur_service(self, demande):
        """Trouve le meilleur service pour une demande donnée"""
        meilleur_service = None
        meilleur_jour_depart = float('inf')
        meilleur_jour_arrivee = float('inf')
        
        for service in self.services:
            service_id = service.id
            service_map = self.carte_des_jours[service_id]
            
            # Vérifier si le service passe par l'origine et la destination
            if demande.origin in service_map and demande.destination in service_map:
                # Les jours où le service passe par l'origine (après le jour de départ souhaité)
                jours_origine = [j for j in service_map[demande.origin] if j >= demande.departure_day]
                
                # Les jours où le service passe par la destination
                jours_destination = service_map[demande.destination]
                
                # S'il n'y a pas de passage prévu à l'origine après le jour de départ souhaité
                if not jours_origine:
                    continue
                
                # Pour chaque jour de départ possible, trouver le meilleur jour d'arrivée
                for jour_depart in jours_origine:
                    # Trouver le premier jour d'arrivée après le départ
                    jours_arrivee_possibles = [j for j in jours_destination if j > jour_depart]
                    
                    if jours_arrivee_possibles:
                        jour_arrivee = min(jours_arrivee_possibles)
                        
                        # Vérifier si ce service offre un meilleur itinéraire
                        if jour_arrivee < meilleur_jour_arrivee or (jour_arrivee == meilleur_jour_arrivee and jour_depart < meilleur_jour_depart):
                            meilleur_service = service_id
                            meilleur_jour_depart = jour_depart
                            meilleur_jour_arrivee = jour_arrivee
        
        if meilleur_service is not None:
            # Une demande est "dans les temps" si elle arrive au plus tard à la date limite
            # (date limite = jour de départ + temps souhaité)
            return {
                'service_id': meilleur_service,
                'jour_depart': meilleur_jour_depart,
                'jour_arrivee': meilleur_jour_arrivee,
                'duree': meilleur_jour_arrivee - meilleur_jour_depart,
                'dans_les_temps': meilleur_jour_arrivee <= demande.date_limite
            }
        else:
            return None
    
    def executer(self):
        """Exécute la simulation en affectant chaque demande au meilleur service"""
        print("Affectation des demandes aux services...")
        
        for demande in self.demandes:
            print(f"\nAnalyse de la demande {demande.id}: {demande.origin} → {demande.destination}")
            print(f"  Jour de départ souhaité: {demande.departure_day}")
            print(f"  Temps souhaité: {demande.desired_time} jours")
            print(f"  Date limite d'arrivée: {demande.date_limite}")
            
            resultat = self.trouver_meilleur_service(demande)
            
            if resultat:
                self.resultats.append({
                    'demande': demande,
                    'affectation': resultat
                })
                
                statut = "DANS LES TEMPS" if resultat['dans_les_temps'] else "EN RETARD"
                print(f"  Affecté au service {resultat['service_id']}")
                print(f"  Départ: jour {resultat['jour_depart']}")
                print(f"  Arrivée: jour {resultat['jour_arrivee']}")
                print(f"  Durée: {resultat['duree']} jours")
                print(f"  Statut: {statut}")
            else:
                print(f"  Aucun service disponible pour cette demande")
                self.resultats.append({
                    'demande': demande,
                    'affectation': None
                })
    
    def afficher_tableau_resultats(self):
        """Affiche un tableau récapitulatif des résultats"""
        print("\n===== RÉSULTATS D'AFFECTATION DES DEMANDES =====")
        print(f"{'ID':^3} | {'Origine':^7} | {'Destination':^11} | {'Service':^7} | {'Départ':^6} | {'Arrivée':^7} | {'Durée':^6} | {'Limite':^6} | {'Statut':^12}")
        print("-" * 80)
        
        for resultat in self.resultats:
            demande = resultat['demande']
            affectation = resultat['affectation']
            
            if affectation:
                statut = "Dans les temps" if affectation['dans_les_temps'] else "En retard"
                print(f"{demande.id:^3} | {demande.origin:^7} | {demande.destination:^11} | {affectation['service_id']:^7} | "
                      f"{affectation['jour_depart']:^6} | {affectation['jour_arrivee']:^7} | {affectation['duree']:^6} | "
                      f"{demande.date_limite:^6} | {statut:^12}")
            else:
                print(f"{demande.id:^3} | {demande.origin:^7} | {demande.destination:^11} | {'N/A':^7} | {'N/A':^6} | "
                      f"{'N/A':^7} | {'N/A':^6} | {demande.date_limite:^6} | {'Non affectée':^12}")