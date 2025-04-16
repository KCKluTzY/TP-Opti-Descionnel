# On importe la fonction lire_services depuis un autre fichier pour charger les services (trajets des barques)
from lecteur_fichier import lire_services

# Définition de la classe Evenement
class Evenement:
    # Constructeur de la classe, appelé quand on crée un nouvel événement
    def __init__(self, type_, time, barge=None, terminal=None, demande=None):
        self.type = type_      # Le type de l'événement : "attente", "départ" ou "arrivée"
        self.time = time       # Le moment où l'événement a lieu (jour)
        self.barge = barge     # L'identifiant de la barque concernée

    # Méthode pour afficher proprement un objet Evenement quand on fait un print
    def __repr__(self):
        return f"Evenement(type={self.type}, time={self.time}, barge={self.barge})"
    def __lt__(self,other):
        return self.time < other.time

# Fonction pour générer les événements à partir d'un service (trajet d'une barque)
def generer_evenements(service):
    evenements = []       # On prépare une liste vide pour stocker les événements
    temps = 0             # On commence à la demi-journée 0

    # On parcourt chaque étape du trajet (chaque tuple (début, fin))
    for leg in service.route:
        debut, fin = leg  # On récupère le point de départ et d'arrivée

        terminal_debut = debut[0]  # La lettre du terminal de départ (ex : "A" dans "A1")
        terminal_fin = fin[0]      # La lettre du terminal d'arrivée

        # Si la barque reste sur le même terminal, c’est un événement "attente"
        if terminal_debut == terminal_fin:
            evt = Evenement(type_="attente", time=temps, barge=service.id)
            evenements.append(evt)  # On ajoute l’événement à la liste

        # Sinon, la barque change de terminal → on crée un départ et une arrivée
        else:
            evt_depart = Evenement(type_="depart", time=temps, barge=service.id)
            evt_arrivee = Evenement(type_="arrivee", time=temps + 1, barge=service.id)
            evenements.extend([evt_depart, evt_arrivee])  # On ajoute les deux événements

        temps += 1  # On avance d’un jour pour l’étape suivante

    return evenements  # On renvoie la liste de tous les événements créés