# Sainte-Marie-à-Py V16 : 2 à 4 joueurs sur le même ordinateur

## Démarrage
`python3 -m http.server 8020` dans ce dossier, puis ouvrir http://localhost:8020. Aucune connexion externe nécessaire.

## Jouer
- Choisir 2, 3 ou 4 joueurs et cliquer sur **Nouvelle partie**.
- Le joueur actif lance une fois le dé, sélectionne les sorties aux carrefours et ponts si nécessaire, résout les choix de la Py.
- **Terminer le tour** devient disponible quand le déplacement et les choix sont terminés. Le pion suivant joue alors.
- Les positions, scores écologiques et tours à sauter sont indépendants. Tous les pions sont visibles. Le tour actif est surligné.
- Un tour sauté par nettoyage se consomme à l'action « Lancer le dé », puis il faut passer au joueur suivant.
- La partie est sauvegardée automatiquement en localStorage après chaque phase terminée (une actualisation pendant un choix reprend au dernier état stable) sur l'origine HTTP. Ne pas changer le port si tu souhaites retrouver la même sauvegarde.

## Géographie et règles
- Les seules voies jouables restent les voies nommées du JSON V38 ainsi que la Py. Routes IGN, bâti et relief ne sont pas modifiés.
- Cases rues ~25 m, cases Py 13 par section. Pont : suivre la Py jusqu'au suivant. Les effets de cartes et économie ne sont pas implémentés.
- Ce mode est multijoueur local *à tour de rôle*, sans connexion réseau.
- La V15 demeure indépendante.


## Mise à jour V16.2
- Ponts affichés avec un pictogramme dédié (`assets/pont_picto.png`).
- Points d'arrivée affichés avec un drapeau (`assets/drapeau_arrivee.png`) quand plusieurs trajectoires sont possibles.
- Lors d'un choix de déplacement, les trajets possibles clignotent en rouge.
- Caméra recentrée en douceur sur le pion du joueur actif ; le nom du joueur est affiché au-dessus du pion.
- Cases blanches de la Py : investissement (minimum 10 pyons), nettoyage des berges (+4 éco et tour sauté) ou cession de 1 point éco.
- Une taxe Py de 10 pyons est appliquée si la case possède un investisseur majoritaire (>50 % du total) : 50 % vont au pot commune, 50 % au joueur majoritaire.
- Hypothèse de départ pour les tests : chaque joueur commence avec 100 pyons.
\n\n## V16.3 : choix direct sur la carte\n- Les destinations affichent un drapeau cliquable lorsqu'un choix est proposé.\n- Cliquer sur le drapeau correspondant valide le même choix que le bouton du panneau.\n- Les tracés rouges clignotants sont remplacés par des rubans beige sable bordés de pierre.\n- Le réseau IGN n'est pas modifié. Les boutons restent accessibles.\n

## V16.4 : lisibilité des déplacements
- Dé de test passé en D8.
- Affichage du tirage agrandi avec rappel du nombre de cases/sphères.
- Chaque itinéraire possible reçoit une couleur distincte.
- Une sphère affichée = une case parcourue.
- Les marqueurs permanents des cases de rue sont masqués pour éviter l'effet fouillis.
- Les tracés de prévisualisation sont rendus comme des chemins/voies du jeu, avec centre coloré et bordure.
- Les trajectoires et les sphères sur la Py sont abaissées et plaquées sur l'eau ; les sphères de la Py sont semi-immergées visuellement.
- Pendant le choix d'itinéraire, les autres repères texte sont masqués pour améliorer la lecture.


## V16.4.1 : lisibilité renforcée
- Affichage du dé corrigé : plus jamais de résultat 0. Avant lancer : D8 : — ; après lancer : dernier tirage réel.
- Chaque sphère de prévisualisation porte maintenant son numéro de pas.
- Les cases de la Py sont affichées en demi-sphères explicites.
- Les tracés de la Py sont abaissés au niveau de l'eau.
- Le compteur visuel de cases dans le panneau reste synchronisé avec les sphères affichées sur la carte.


## V16.4.2 : arrêt sur pont
- Traverser un pont en cours de lancer ne provoque aucun changement de réseau.
- Terminer exactement le dé sur la case de pont déclenche obligatoirement une entrée dans la Py.
- Le trajet fluvial commence au lancer suivant, sans consommer de pas supplémentaires.
- Si plusieurs sections sont possibles, seule la direction dans la Py est à choisir. Il n’est pas possible de rester sur la rue.
- Les panneaux et drapeaux d’itinéraire ne proposent plus d’entrée volontaire sur un pont traversé.
- Cartographie IGN inchangée ; aucun chemin supplémentaire n’est jouable.


## V16.4.3 : cadrage automatique des arrivées
- Au tirage du D8, la caméra s’éloigne et se recentre progressivement pour inclure tous les itinéraires et drapeaux d’arrivée.
- Le cadrage réserve de l’espace pour les panneaux latéraux et ajoute une marge pour les drapeaux en hauteur.
- À la sélection du drapeau, la caméra suit de nouveau le joueur actif.
- Aucun changement aux règles de déplacement, aux ponts et aux données IGN.


## Correctif V16.4.4
- Correction bloquante : `lastRoll` était utilisé sans déclaration, ce qui empêchait la création de partie et la liaison des boutons.
- Suppression des sphères de cases permanentes du parcours de la Py (65 cases toujours conservées pour le moteur).
- Maintien des cases numérotées **temporaires** pendant la sélection d’itinéraire.
- Les boutons de déplacement sont désormais reliés avant la reconstruction du graphe, avec diagnostic visible en cas d’erreur.

### Test
1. Nouvelle partie : les joueurs doivent apparaître.
2. Lancer le dé : le D8 affiche une valeur comprise entre 1 et 8.
3. Sur la carte, les sphères permanentes de la Py ne sont plus dessinées.
4. À une intersection, choisir un drapeau.


## V16.4.5 : numérotation du parcours
- La case de départ n'est pas comptée dans la numérotation affichée.
- Les pastilles “1” du premier pas sont supprimées pour éviter le fouillis visuel.
- Les anciens “2”, “3”, etc. deviennent “1”, “2”, etc. sur les sphères intermédiaires.
- Le picto d'arrivée affiche le total du tirage.


## V16.5 : cases de Py et investissements
- Pont Tahure -> Pont Est (C) : 12 cases, 3 spéciales (indices 3, 6, 9).
- Pont Central -> Pont Tahure (B) : 24 cases, 5 spéciales.
- Pont Ouest -> Pont Central (A) : 32 cases, 6 spéciales.
- Extrémité Ouest -> Pont Ouest (W) : 24 cases, 5 spéciales.
- Pont Est -> Extrémité Est (E) : 24 cases, 5 spéciales.
- Total : 116 cases, 24 cases spéciales. Les cases sont repositionnées par interpolation sur les tracés géographiques existants ; les routes IGN sont inchangées.
- Investissement : 1 Pyon + 2 éco sur case vierge. Prix en Pyons = 1 + nombre de joueurs investisseurs distincts déjà présents sur cette case ; coût écologique maintenu à 2 à chaque opération (hypothèse à confirmer).
- Les actions de case blanche ne s'activent qu'à l'arrêt sur la case.
- La sauvegarde V16.5 utilise une nouvelle clé pour éviter la reprise de positions désormais incompatibles avec les nouveaux nombres de cases.


## V16.5.1 : prévisualisation avant validation
- Après un lancer de dé, le trajet complet est prévisualisé avant tout déplacement effectif.
- Même sans croisement, le joueur voit toutes les cases du trajet et doit valider en cliquant sur le drapeau d'arrivée.
- La prévisualisation sur la Py montre maintenant tout le tracé bleu et toutes les cases du déplacement.
- Le déplacement n'est plus automatique au lancer du dé.


## V16.5.2 : surcouches plaquées au sol
- Tracés de prévisualisation routiers et fluviaux abaissés au ras du relief / de la chaussée.
- Cases numérotées routières aplaties sur la route ; cases fluviales abaissées au niveau de l'eau.
- Ponts statiques abaissés au ras de la carte.
- Seuls le pion du joueur et le picto d'arrivée restent volontairement en hauteur.


## V16.5.3 : investissements des cases ordinaires de la Py
- Les trois actions sont toujours proposées sur les cases ordinaires : investir, nettoyer, céder 1 éco.
- Première mise sur une case libre : 1 Pyon et 2 éco.
- Pour racheter une case détenue, la mise cumulée du nouveau propriétaire doit dépasser celle de l'ancien propriétaire d'au moins 1 Pyon.
- Une même personne peut compléter sa mise précédente : seul l'apport nécessaire pour dépasser le propriétaire est débité.
- Le propriétaire actuel peut renforcer sa mise par apport de 1 Pyon.
- Si le joueur manque de ressources, le bouton reste affiché et un message indique ce qui manque ; la transaction ne se fait pas.
- Les cases spéciales restent réservées à leurs événements.
- Les données IGN, OSM, relief, ponts et tracés jouables sont inchangées.


## V16.5.4 : pions visibles et étiquettes retirées
- Étiquettes « Mairie » et « Église Notre-Dame » retirées de la carte (les boutons de recentrage restent disponibles).
- Pions rendus visibles au-dessus des routes, des chemins et du relief, avec anneau blanc contrasté.
- Pions sur une même case légèrement décalés pour qu'aucun ne soit masqué.
- Nom du joueur actif conservé au-dessus de son pion, dans un format plus compact.
- Règles Py V16.5.3 inchangées.


## V16.5.6 : pont = case commune, D8 cohérent
- Les 4 ponts partagent une unique position de case entre routes jouables et Py, sans changer les tracés IGN et OSM sources.
- Le passage route→Py au pont ne consomme pas de case supplémentaire.
- L’embranchement entre deux tronçons ne consomme pas non plus de case.
- Un D8=1 montre seulement « 1 » sur le drapeau d’arrivée. D8=4 montre 1, 2, 3 sur les cases intermédiaires et 4 sur le drapeau.
- Les drapeaux sont abaissés à hauteur de chaussée ; le nombre se superpose au picto.
- Les positions de la Py sont tirées des 116 cases équidistantes dans le JSON, avec suivi des méandres pour le tracé.


## V16.5.7 : décision différée sur les ponts
- À l’arrivée sur un pont, le tour s’arrête sans proposer de direction.
- Au tour suivant du même joueur, lancer le D8 déclenche les propositions d’itinéraires depuis le pont.
- Un joueur venant de la route entre obligatoirement dans la Py.
- Un joueur venant de la Py peut choisir entre repartir sur la Py ou emprunter une route jouable.
- Le changement de réseau au niveau du pont ne consomme pas de case.
- La sauvegarde locale conserve l’état « en attente au pont ».


## V16.5.8 : filtrage des choix sur case blanche de la Py
- Après les taxes éventuelles, les actions proposées dépendent des ressources du joueur.
- Investir uniquement si Pyons et points éco suffisants pour le coût de prise de propriété.
- Céder 1 éco uniquement si le joueur possède au moins 1 point éco.
- Nettoyer les berges reste toujours proposé (+4 éco, prochain tour sauté).
- Les cases spéciales n’offrent pas ce menu.


## V16.5.9 : première participation attribuée lors d'une action écologique

Sur une case ordinaire de la Py sans aucun investisseur :
- Nettoyer les berges : +4 points éco, prochain tour sauté, et attribution d'une participation de 1 Pyon.
- Céder 1 point éco : -1 point éco, fin normale du tour, et attribution d'une participation de 1 Pyon.
- Cette attribution ne débite pas le portefeuille en Pyons : elle représente la valeur initiale de propriété de la case.

Si une participation existe déjà, nettoyer et céder conservent leurs effets habituels, sans changer le propriétaire ni la mise. L'investissement direct et les règles de surenchère sont conservés. Les choix restent filtrés selon les ressources.


## V16.6 : 2 à 8 joueurs et attribution initiale des ponts
- Quatre ponts distincts, non investissables et sans actions écologiques des cases ordinaires.
- Au lancement d’une nouvelle partie : les ponts sont attribués équitablement aux joueurs, avec copropriété lorsque le nombre de joueurs dépasse quatre.
- 2 joueurs : 2 ponts chacun ; 3 joueurs : 2, 1, 1 ; 4 joueurs : 1 chacun ; 5 à 8 : répartition avec deux titulaires maximum par pont.
- Les joueurs débutent sur l’un des ponts qui leur est attribué. Le pont ne compte pas comme une case dépensée au lancer suivant.
- Les déplacements, passages sur la Py et règles d’investissement des cases ordinaires restent inchangés.
- La version utilise une nouvelle clé de sauvegarde afin de ne pas reprendre une partie incompatible.


## V16.6.2 : pont Tahure et visibilité de toutes les cases de la Py
- Le pont de Tahure est maintenant exactement au croisement géométrique entre l’axe de la Rue de Tahure (E017) et l’axe du cours d’eau La Py (OSM), calculé en Lambert-93.
- Sections B et C réalignées sur l’axe OSM et leurs 24 et 12 cases rééchantillonnées à distance identique.
- Une pastille bleu foncé par case jouable de la Py. Case spéciale : nénuphar vert (image `assets/nenuphar_case_speciale.png`).
- Lorsqu’une case ordinaire a un propriétaire, point au centre de la couleur du joueur propriétaire. Les ponts sont attribués à plusieurs joueurs dès le début et ne sont pas investissables.
- Toutes les pastilles sont posées au ras de l’eau et leur affichage peut être désactivé via « Cases Py ».
- Une case de pont n’est affichée qu’une fois à la jonction entre sections. Aucun changement à la règle des ponts ni au nombre de joueurs maximal (8).
- La position précise est celle de l’intersection des deux axes cartographiques fournis, pas une certification topographique du pont physique.


## V16.6.5 : taxe de passage à la place de céder un point éco
- Sur les cases blanches ordinaires de la Py, « Céder 1 point écologique » est remplacé par « Payer la taxe de passage ».
- Coût : 1 Pyon + 1 éco si le rachat demandé au joueur coûte au plus 20 Pyons ; au-delà de 20 Pyons, 20 % de ce prix de rachat, arrondis au Pyon supérieur, + 1 éco.
- Choix affiché uniquement si le joueur dispose des deux ressources nécessaires.
- Suppression de la taxe automatique de 10 Pyons à l'arrivée : la taxe est payée uniquement si le joueur choisit cette action.
- Le produit est réparti entre commune et propriétaire tiers selon l'ancienne règle (50/50, arrondi à la commune), ou intégralement à la commune si aucun propriétaire tiers.
- Payer la taxe ne confère aucune participation dans la case ; nettoyer les berges sur une case vierge conserve la règle d'attribution automatique de 1 Pyon.
- Autres règles, ponts et géométrie de la V16.6.2 conservés.


## Nouveautés V16.6.5
- arbres repoussés hors du cours de la Py quand ils tombent sur la rivière ;
- 8 pictos de personnages comme pions ;
- réglages du type de dé (D4, D6, D8, D10, D12, D16, D20) et du nombre de dés par tirage (1 à 5).


## V16.6.6 : ancrage des personnages et arbres hors rivière
- Les textures des huit pions, leurs règles et les réglages de dés sont conservés.
- Le socle du pion est repositionné à 1,55 unité du relief ; le sprite du personnage descend avec lui et ne flotte plus au-dessus de la case.
- Les lignes de la Py sont préchargées avant la plantation de **tous** les arbres, y compris les bois issus des surfaces OSM.
- Chaque arbre doit être à au moins 23 m de l'axe OSM ; des vérifications itératives préviennent un déplacement dans un autre méandre.
- Si une plantation reste impossible sans empiéter sur la rivière ou sortir de la commune, l'arbre est omis.
- Les données géographiques, l'altitude des bâtiments et les parcours jouables sont inchangés.


## V16.6.7 : actions sur la Py sans validation du trajet
Lorsqu’un seul itinéraire arrive sur une case ordinaire de la Py, les actions financièrement accessibles (investir, nettoyer, taxe) s’affichent directement pendant que le tracé complet reste visible. Choisir une action valide à la fois le déplacement et cette action. Pour les embranchements, le joueur choisit toujours son itinéraire avant l’action. Ponts et cases spéciales conservent leur comportement.


## V16.6.10 : tour sauté
- Lorsqu’un joueur doit passer son tour (après nettoyage), son panneau n'affiche qu’un bouton d’action « PASSER MON TOUR ».
- Aucun tirage de dé ni déplacement ne sont possibles à ce tour.
- Le clic déclenche un petit saut sur place (animation de 850 ms), sans changer de case, puis passe automatiquement au joueur suivant.
- Le compteur des tours sautés diminue seulement lors du clic. Les 8 pions, réglages des dés, cartes et règles financières sont conservés.


- Correctif V16.6.10 : le nom de chaque destination est affiché directement sur la carte, à côté de chaque drapeau de choix.


## V16.6.11 : fin de tour immédiate sur trajet unique
- Si le lancer n’offre qu’un seul itinéraire et aucune action à choisir sur la Py, le trajet est validé sans clic sur le drapeau.
- Le bouton « Terminer mon tour » devient immédiatement actif.
- Si la case d’arrivée impose un investissement, un nettoyage ou une taxe, les choix d’action sont toujours proposés avant la fin du tour.
- Pour plusieurs arrivées, le choix manuel du trajet reste obligatoire.
- Les sauvegardes V16.6.10 sont conservées.


## V16.6.12 : ancrage des pions
- Suppression du socle circulaire intégré aux huit pictos personnages et conservation de leur silhouette.
- Chaque image est recadrée avec la partie la plus basse des chaussures sur la ligne du sol.
- Ancrage de chaque sprite à sa base (`center.y=0`), positionné au niveau du relief, sans disque ni couronne de support.
- Les règles et les données de jeu ne changent pas.


V16.6.13 : le nombre flottant a cote du drapeau d’arrivée a ete supprime. Apres une decision explicite (itineraire ou action Py), le joueur suivant commence automatiquement si aucune autre action n’est en attente. Les trajets uniques valides automatiquement ne forcent pas le passage au joueur suivant. Les tours sautes restent animes.


## V16.6.14 : chemin unique visible jusqu’à la fin du tour
- Avec un seul trajet et aucune action à sélectionner, le mouvement est appliqué automatiquement mais son tracé et ses points de passage restent visibles.
- Le bouton « Terminer mon tour » est actif après le lancer et le tour ne se termine pas automatiquement.
- Le tracé est effacé seulement au passage au joueur suivant.
- Plusieurs trajets et les cases de la Py demandant une action conservent leurs validations habituelles.


## V16.6.15 : drapeau d’arrivée toujours visible
- Le picto d’arrivée et son étiquette sont dessinés en tout dernier plan, y compris devant les pastilles permanentes de la Py et les modèles de joueurs.
- Il reste ancré sur la case d’arrivée et cliquable lorsqu’un choix existe.
- Le tracé unique reste affiché jusqu’au clic sur « Terminer mon tour ».
- Aucun changement sur les règles, les données et le calcul des trajets.


## V16.6.16 : végétation enrichie

- Plantation géoréférencée depuis les zones OSM forest/wood, scrub/heath, espaces verts et alignements `tree_row`.
- Densification des deux berges de la Py avec arbres low-poly et buissons, tout en laissant l'eau libre.
- Modèle local `data/vegetation_v16_6_16.json` contenant 1 885 arbres et 2 192 buissons, placés par algorithme à partir des données cartographiques.
- Évitement géométrique des cours d'eau (19 m pour les arbres, 8,5 m pour les buissons), des routes IGN/OSM et des bâtiments OSM. Les champs agricoles restent ouverts.
- Objets affichés par lots 3D (InstancedMesh) pour préserver les performances et recalés au relief triangulé.
- Ce peuplement est stylisé et estimé à partir des zones cartographiques ; le plan-image reste une référence visuelle et non une mesure cadastrale de chaque arbre.
- Jeu, cases, propriétés et règles de la V16.6.15 inchangés.


## V16.6.17 : relief, dés, végétation et bond de fin de tour
- Relief initial : ×1,5 ; curseur toujours réglable.
- Dés initiaux : 2D6 ; curseurs de nombre et de faces toujours réglables.
- Anciennes sauvegardes migrées vers 2D6 au premier chargement, puis choix des dés persistés.
- À chaque fin de tour normale ou automatique : petit bond sur place, puis passage au joueur suivant. Le tour sauté conserve son bond.
- Buissons : retrait déterministe de 20 % des implantations de la V16.6.16.
- Arbres : 10 % (arrondi au sujet entier) sont agrandis ×1,7 minimum ; positions inchangées.


## V16.6.18 : déplacement animé fluide et bondissant
- Après la validation d’un trajet, le personnage parcourt réellement les cases à une vitesse fixe (380 ms par case).
- Le déplacement suit les méandres géographiques de la Py grâce aux portions détaillées du parcours.
- Chaque case est parcourue avec accélération/décélération douce et petit bond vertical.
- Les interactions et mises à jour financières ne sont appliquées qu’à l’arrivée ; l’interface est verrouillée pendant le trajet.
- Le chemin unique reste visible et le bouton « Terminer mon tour » n’est activé qu’une fois l’arrivée atteinte.
- Après un choix explicite, le bond de fin de tour habituel s’exécute à l’arrivée, puis le joueur suivant prend la main.
- Les réglages 2D6, relief ×1,5 et végétation V16.6.17 sont conservés.
- La vitesse de déplacement n’est pas encore paramétrable.


## V16.6.19 : cases colorées sans trait de liaison
Après le lancer, seules les cases du parcours sont colorées dans la couleur du pion actif. Le drapeau est situé sur la dernière case. La sélection des trajets et les déplacements animés restent actifs.


## V16.6.20 : nénuphars colorés et drapeau posé
- Après le lancer, toutes les cases traversées sont colorées, y compris les cases nénuphars spéciales (diamètre adapté aux grandes pastilles).
- Image du drapeau recadrée pour retirer la marge transparente du bas.
- Drapeau ancré en bas de son sprite, sur la surface réelle de la dernière case et selon le relief.
- Aucun changement des dés, des règles, du déplacement animé ni des données de parcours.


## V16.6.21 : extrémités de la Py et gel des déplacements
- Extrémité ouest : demi-tour automatique, future liaison vers « Les bunkers ».
- Extrémité est : demi-tour automatique, future liaison vers l’Ossuaire de Navarin.
- Les cases terminales comptent comme une case : si des pas restent, le personnage rebrousse chemin dans le même tirage ; sinon, il partira vers l’intérieur de la Py au prochain tour.
- Aucun faux pont ni choix de direction bloquant à ces deux extrémités.
- Récupération des sauvegardes déjà bloquées à une extrémité.
- Les autres règles et les déplacements animés sont conservés et figés pour la prochaine phase de développement.


## V16.6.22 : enchères sur les cases de la Py déjà investies
- Arrivée sur une case d’un autre joueur : investir plus (enchère), payer la taxe, nettoyer les berges, suivant les moyens du joueur.
- Mise d’ouverture : investissement cumulé du propriétaire + 1 Pyon.
- Surenchère minimale : 1 Pyon ; propositions rapides +1, +5, +10.
- Alternance propriétaire / challenger : à son tour, chaque participant peut surenchérir ou abandonner.
- À l'abandon d'un participant, le dernier enchérisseur gagne et paie la totalité de son offre, ainsi que 2 points éco conformément au coût d'investissement existant. Le perdant ne paie rien.
- Le gagnant reçoit la propriété de la case, sa mise payée s'ajoute aux investissements de la case.
- Le moteur de déplacement de la V16.6.21 est conservé.
- Les enchères sont locales à une seule session : si l'onglet est fermé pendant une enchère, reprendre à la dernière sauvegarde du tour.


## V16.6.23 : correction des choix de parcours en double
- Déduplication des destinations partageant le même état d'arrivée ; fini les choix identiques générés par plusieurs explorations du graphe.
- Si plusieurs arrivées distinctes sont accessibles depuis la même rue, chaque bouton précise la rue d'arrivée et le numéro de case.
- Sélection de drapeaux et animations de mouvement inchangées.


### V16.6.24 : accès à la Py seulement après un arrêt sur un pont
- Traverser un pont sur une route, avec des pas restants, est sans effet : le joueur reste sur la route.
- Terminer le lancer exactement sur le pont prépare le choix de direction pour le lancer suivant.
- Au lancer suivant, le joueur peut choisir une direction routière ou un embranchement de la Py.
- Aucun autre point de la route ne donne accès à la Py.
- Le calcul des parcours et le déplacement animé restent identiques hors de ce choix de pont.


## V16.6.25 : pioche nénuphars
- 40 cartes mélangées sans remise jusqu’à épuisement.
- Tirage seulement à l’arrêt sur un nénuphar.
- La carte remplace investissement, taxe et nettoyage sur cette case.
- 14 événements écologiques positifs, 10 économiques positifs, 10 négatifs, 6 choix ou surprises.
- Récompenses et pénalités plafonnées à 0 pour les pertes.
- Pioche sauvegardée avec la partie ; remise à zéro lors d’une nouvelle partie.
- Une carte à confirmer ou avec choix bloque la fin de tour jusqu’à sa résolution.


## V16.6.26 : interface des événements nénuphars
- La pioche de 40 cartes reste inchangée et sauvegardée localement.
- Les événements s’ouvrent dans une fenêtre centrée avec illustrations locales, gains/pertes explicites et boutons de décision.
- Les parcours et les enchères ne sont pas modifiés.
- Ajustement des champs de cartes économiques de V16.6.25 : les dons, subventions, recettes touristiques, mécénat et travaux affectent bien les Pyons (et non les points éco).


## V16.6.27 : crue de la Py étendue au tronçon
- Une carte « Crue de la Py » touche toutes les propriétés du segment où elle est tirée (de pont à pont, ou d’une extrémité à un pont).
- Chaque propriétaire distinct possédant au moins une case sur ce segment paie une seule fois 1 Pyon, dans la limite de ses ressources.
- Le tireur conserve les dégâts de la carte (−2 Pyons et −2 éco), et paie éventuellement 1 Pyon supplémentaire s’il est aussi propriétaire du tronçon.
- Les propriétés et investissements restent intacts ; aucun dégât hors du segment.
- Les sauvegardes et les autres cartes restent compatibles.


## V16.6.28 : monopoles entre deux nénuphars
- Les cases de la Py strictement entre deux nénuphars successifs d’une même section forment un groupe. Un groupe est un monopole si **toutes** ses cases appartiennent à un seul et même joueur.
- Les nénuphars, les ponts et les intervalles incomplets aux deux extrémités ne comptent pas.
- Sur chacune de ces cases, la taxe volontaire est **doublée en Pyons** (la taxe éco reste de 1 point). Le partage entre commune et propriétaire conserve la règle existante.
- Le propriétaire gagne **1 point éco** à chaque arrêt sur une de ses cases appartenant au monopole, une fois par arrivée. Le simple passage ne donne rien.
- L’avantage est recalculé après tout changement de propriété ; il ne s’applique plus si une case du groupe change de propriétaire.
- La sauvegarde reste compatible, sans changer le moteur de déplacement.


## V16.6.29 : projets participatifs collectifs et nettoyage sur cases investies
- Carte « Projet participatif » : tous les joueurs répondent à tour de rôle, joueur ayant tiré la carte en premier ; chacun peut payer 4 Pyons pour recevoir 6 points éco, ou refuser. Le joueur actif ne change qu’après la dernière réponse.
- Nettoyage sur case vierge : 0 Pyon, +4 points éco, prochain tour sauté, participation gratuite de 1 Pyon en propriété.
- Nettoyage sur case déjà investie : moitié de la taxe de passage en Pyons arrondie au supérieur, minimum 1 Pyon, 0 point éco à payer, +2 points éco, prochain tour sauté ; la propriété ne change pas.
- Taxe de nettoyage répartie entre la commune et le propriétaire comme la taxe de passage.
- Si un joueur ne peut se permettre aucune action sur une case investie, « Passer sans action » évite de bloquer la partie.


## V16.6.30 : propriété en couleur et choix du personnage
- Les cases ordinaires investies de la Py sont remplies entièrement de la couleur du personnage propriétaire (plus de simple point jaune).
- Les cases sans propriétaire restent bleu foncé ; les nénuphars conservent leur visuel d’événement.
- Écran de sélection de 2 à 8 personnages avant une nouvelle partie, avec aperçu de chacune des 8 illustrations. Un personnage ne peut pas être choisi deux fois.
- Le personnage sélectionné, la couleur du tracé et la propriété des terrains correspondent désormais.
- La sauvegarde mémorise l’identité du personnage choisi ; les sauvegardes antérieures sont restaurées avec les personnages habituels.


## V16.6.31 · Son des nénuphars
Le fichier local `assets/sounds/nenuphar.mp3` (fourni par le joueur) se déclenche une fois lors de chaque arrivée sur un nénuphar, au tirage de la carte événement. Le simple passage sur un nénuphar ne déclenche pas ce son. Une politique de lecture automatique du navigateur peut, selon ses réglages, bloquer le son.


## V16.6.33 : victoire mixte
- Fin de partie : 20 tours par joueur, y compris les tours sautés ; classement après le dernier joueur de la 20e manche.
- Score final sur 100 : écologie 50 %, patrimoine actuel 30 %, Pyons restants 20 %. Chaque composante est relative au meilleur joueur (si tous sont à zéro, la composante vaut zéro).
- Patrimoine : somme des mises du propriétaire actuel sur ses cases de la Py. Les investissements d'anciens propriétaires, les ponts gratuits et le pot commun ne comptent pas. Les monopoles ne donnent aucun bonus final.
- En cas de même score : plus de points éco, puis plus de patrimoine, sinon victoire partagée.
- Écran final : classement, détail par catégorie, nouvelle partie et carte 3D. Le classement peut être rouvert.
- Sauvegardes V16.6.10 à V16.6.31 compatibles ; la fin de partie et le classement sont sauvegardés.


## V16.6.34 : projets communaux (vote et financement)
- Vote une fois à la fin des manches 5, 10, 15 et 20, si le pot communal a au moins 10 Pyons.
- Proposition d'un projet aléatoire parmi cinq, sans reproposer un projet déjà réalisé.
- Vote majoritaire strict, chaque joueur a une voix. Les votes se déroulent à tour de rôle dans une fenêtre.
- Contribution libre après un vote favorable, avec pot communal utilisé en premier. Les promesses ne sont débitées que si la somme suffit ; sinon annulation et zéro prélèvement.
- Projet réalisé une seule fois : nettoyage de la Py (20 Pyons, +3 éco à tous), haies (15, +2), restauration des berges (30, prévention d'une crue), biodiversité (25, +5), restauration des chemins (20, +2).
- Sauvegarde du projet en cours, des votes, des promesses, des projets déjà réalisés et de la protection restante.
- Le classement final après 20 tours intervient une fois le vote de la manche 20 résolu.


## V16.6.35 : règle asymétrique des ponts

- **Sur la route :** rejoindre une case de pont interrompt immédiatement le déplacement. Le choix route/Py intervient au lancer suivant.
- **Sur la Py :** passer sur un pont avec des pas restants propose immédiatement de continuer le cours de la Py ou de sortir sur la route, sans consommer de pas supplémentaires pour la bifurcation. Le joueur n'est pas obligé de finir son trajet sur le pont.
- Si le lancer se termine exactement sur le pont depuis la Py, choix reporté au prochain lancer.
- Aux deux extrémités sans pont (Les bunkers, Ossuaire de Navarin), le demi-tour automatique reste en place.
- Règles des événements, enchères, projets communaux, sauvegarde et victoire inchangées.


## V16.6.36 : décision aux ponts sur la Py
- En traversant un pont sur la Py avec des pas restants : le choix entre continuer sur la Py et sortir sur la route est toujours proposé. Les alternatives restent distinctes même en cas d’arrivée identique.
- En tombant exactement sur un pont : fin du déplacement et aucun choix. Le lancer suivant reprend automatiquement sur la Py (direction conservée depuis la Py ; vers l’est par défaut depuis une route).
- Depuis la route, le pont reste un arrêt obligatoire.


## V16.6.38 - Six cartes « Partir pêcher » et reprise des ponts
- Pioche de **46 cartes**, dont **6** cartes « Partir pêcher ». Mélange sans répétition avant épuisement.
- Sauvegardes V16.6.37 compatibles : les cinq nouvelles cartes sont insérées parmi les cartes non encore tirées.
- À chaque début de tour sur un pont, le marqueur de reprise sur la Py est vérifié et réparé si nécessaire.
- Au lancer, départ obligatoire sur la Py depuis un pont, sans nouvel embranchement préalable.
- Si la section de Py envisagée ne permet aucun déplacement, une autre section raccordée est essayée.
- En cas de défaut de parcours, le lancer est annulé et les dés peuvent être relancés, au lieu de bloquer la partie.
- Aucune modification des enchères, événements existants, financements ou score final.


## V16.6.39 · Destination visible après un arrêt sur un pont
- Le lancer au tour suivant calcule le trajet obligatoire sur la Py.
- La destination et le drapeau sont toujours affichés, y compris lorsqu’il n’y a qu’une seule possibilité.
- Le joueur valide le drapeau ou le bouton « Reprendre sur la Py » avant l’animation.
- En fin d’animation, les actions nénuphar / investissement habituelles sont exécutées.
- Les passages sur un pont avec des cases restantes conservent les choix route / Py.


## V16.6.40 · Musique de fond
- Nouveau fichier local : `assets/sounds/fond_musical.mp3`.
- Musique en boucle, activée par défaut après la première interaction avec la page (restriction standard des navigateurs).
- Bouton « Couper la musique » / « Activer la musique » dans le panneau de déplacement.
- Volume de 0 à 100 %, initialement 25 %, indépendant du son de nénuphar.
- Volume et état actif/inactif mémorisés dans le navigateur, sans effet sur la sauvegarde de la partie.


## V16.6.41 : déplacements sur ponts et sortie de pêche
- Depuis une route, passer sur un pont ne stoppe pas le mouvement. Les dés sont consommés entièrement si le parcours le permet.
- Si le lancer termine exactement sur un pont, le joueur choisit les deux sens de la Py au lancer suivant : aval (ouest) ou amont (est).
- Premier tour : le joueur démarre sur un pont et choisit les deux sens de la Py après son premier lancer.
- Depuis la Py, franchir un pont en cours de lancer continue à proposer la rivière ou la route.
- Pêche : 5 poissons, dé favorable ou 10 Pyons libèrent immédiatement ; le jeu lance les dés au même tour et propose trois sorties : Voie du Captage, Py aval, Py amont.
- Une tentative échouée passe le tour, sans déplacement.


## V16.6.42 : pêche plus rapide et pièges
- Poissons réduits à 43 px, visibles entre 0,65 et 1,05 seconde avant de disparaître.
- Apparition continue dans l'étang, avec un court intervalle entre les cibles.
- Environ 1 apparition sur 3 est un piège : sirène, botte ou algues.
- Cliquer sur un piège retire 1 poisson attrapé (plancher 0).
- Objectif inchangé : 5 poissons en moins de 30 secondes. Aucun changement aux règles de libération ni aux déplacements.

## V16.6.43 : panneau de droite réorganisé
- Les boutons Lancer les dés / Terminer mon tour / Passer mon tour et les propositions de choix sont groupés dans une zone fixe, tout en haut du panneau.
- Les propositions utilisent des boutons plus grands et défilent à l'intérieur de leur propre zone si elles sont nombreuses.
- Informations des joueurs, configuration des dés, musique, historique et commandes secondaires sont regroupés sous les choix dans une partie défilante indépendante.
- Aucun changement des règles économiques, des déplacements, de la pêche ou des événements.


## V16.6.44 : commandes sous forme d’images
- Les boutons « Lancer les dés » et « Terminer mon tour » utilisent respectivement des images de dés et de drapeau à damier.
- Pictogrammes et fonds colorés lorsque le bouton est utilisable, grisés lorsqu'il ne l'est pas.
- Libellés conservés pour lecteurs d’écran et infobulles au survol.
- Aucune règle modifiée, commandes à la même place.


### V16.6.45 : pictogrammes bois
Les deux commandes principales utilisent désormais des médaillons illustrés (dés en bois et drapeau de fin de tour), assortis au style du pont. La couleur disparaît automatiquement lorsque le bouton est désactivé.


## V16.6.46 : correction des fins de partie prématurées
- Fin de partie uniquement si chaque joueur a effectivement terminé 20 tours, y compris les tours passés.
- Le numéro de manche seul ne peut plus déclencher le classement final.
- Migration des sauvegardes antérieures : personnages, ressources et propriétés conservés, mais compteur de 20 tours repris à zéro pour éviter la fin de partie prématurée.
- Une fin de tour n'est comptée qu'après le bond de fin de tour.
- Tests syntaxiques et tests ciblés du comptage effectués.


## V16.6.47 : choix sans ascenseur
- Les boutons des trajets et des actions apparaissent directement sous les deux pictogrammes.
- La zone des choix n'a plus d'ascenseur, ni de hauteur maximale.
- Pour plusieurs choix, le panneau s'élargit et les boutons se répartissent sur plusieurs colonnes.
- Les informations et réglages, placés dessous, défilent indépendamment.
- Aucun changement des règles de jeu.


## V16.6.48 : panneau gauche repliable
- Le panneau de gauche est fermé au lancement et réduit au bouton « Carte & réglages ».
- Un clic ouvre le panneau et donne accès à tous les réglages et à la légende ; un second clic le referme.
- Les informations techniques ne sont masquées visuellement qu’en mode fermé.
- Le panneau de droite et toutes les règles du jeu restent inchangés.


## V16.6.49 : panneau droit compact
Le panneau droit ne montre par défaut que les commandes de dés, les choix et actions, et le résultat du lancer. L’icône ⚙ donne accès aux informations secondaires (joueurs, paramètres, musique, historique), lesquelles se replient sans affecter la partie. Les choix restent directement sous les pictogrammes.


## V16.6.52 : déplacement automatique en cas de trajet unique
- Après le lancer, si une seule arrivée est calculée, le pion part immédiatement avec son animation.
- Les choix d'investissement, d'enchère, de taxe et de nettoyage n'apparaissent qu'une fois le pion arrivé.
- Si plusieurs itinéraires sont possibles, le joueur continue à choisir son trajet avant l'animation.
- Les événements nénuphars continuent à se déclencher uniquement à l'arrivée.
- Aucun changement aux règles économiques ou au calcul des itinéraires.


V16.6.52 : simplification des choix de trajet ; boutons numérotés 1/2/3 ; pictogramme de pont sur les arrivées de pont ; numéros visibles sur la carte et dans la liste des choix.


V16.6.52 : nouvelles cartes nénuphars (batraciens, observatoire, concours de pêche, montée des eaux, sondage communal), bandeau supérieur joueurs (Pyons / Éco / Patrimoine), panneau droit simplifié, informations non essentielles regroupées dans le panneau gauche, dés affichés en images D6.


## V16.6.55
- Drapeaux d'arrivée numérotés dans leur toile (sans pastille flottante).
- Libellés de parcours uniformisés entre liste et carte : pont + route ; route + case ; Py + tronçon + case.
- Transition de caméra entre deux joueurs : recul cadrant les deux personnages puis zoom sur le suivant.
- Cases Py sans investissement : contour blanc fin, intérieur transparent ; propriétés colorées selon leur détenteur.


V16.6.55 : correction critique de l’ordre d’initialisation JavaScript. Le panneau des informations n’appelle plus byId avant la déclaration.


## V16.6.55 : repérage des arrivées au survol
- Au passage du pointeur sur un bouton numéroté de trajet, le drapeau correspondant bondit et pulse sur la carte.
- Même repérage au focus clavier; arrêt de l’effet à la sortie du bouton.
- Les autres drapeaux ne sont pas affectés et le clic de validation est inchangé.


## V16.6.56 : acquisition automatique des cases Py vierges
À l'arrivée sur une case ordinaire sans propriétaire, le joueur en devient automatiquement propriétaire pour 0 Pyon et 0 point éco et gagne +1 point éco. La mise financière reste nulle et une enchère future démarre à 1 Pyon. Sur les propriétés existantes, les actions habituelles restent disponibles. Ponts et nénuphars exclus.


### V16.6.59 : entretien de sa propre case Py
Quand le joueur termine sur une case Py ordinaire dont il est déjà propriétaire, l’entretien est automatique : +1 point éco, 0 Pyon dépensé, aucun bouton de choix économique. Les cases vierges, adverses, les nénuphars et les ponts conservent leurs règles. Le bonus de monopole existant reste indépendant.


## V16.6.59
- Les pastilles de prévisualisation de trajet disparaissent étape par étape pendant le déplacement animé.
- Carte animée de transfert entre deux joueurs : avatars, noms, donneur, destinataire, quantité et motif. Déclenchée pour les dons, la solidarité, la part propriétaire des taxes et des nettoyages.
- Les règles économiques, les données locales et les images restent inchangées.


## V16.6.81
Les cartes de transferts entre joueurs restent affichées 7 secondes avec texte lisible pendant la quasi-totalité de la durée.


### V16.6.81 : choix des cases Py sur les cartes
Une carte d’attribution propose désormais les cases vierges de la Py dans un rayon de 150 m de la position du pion. Le joueur choisit chaque case une par une, dans la limite de la récompense. Aucune propriété adverse n’est confisquée ni indemnisée. S’il n’existe plus de case libre proche, le joueur peut aller sur une propriété adverse et lancer une enchère aux conditions habituelles. Il peut refuser.


### V16.6.81 : enchères non refusables
Le propriétaire ne peut pas annuler une enchère lancée par un adversaire. Il peut surenchérir, ou ne pas surenchérir et laisser l'enchérisseur courant gagner. Règles de coût inchangées.


- V16.6.81 : médaillons joueurs du haut agrandis, avatars plus grands, points et classements Pyons / Éco / Patrimoine visibles en direct.


- V16.6.81 : ajout des cartes nénuphars “Tu aperçois…” avec photo animée et +10 éco, et de la carte “Tu acquiers toutes les cases libres adjacentes autour de toi”.


V16.6.81 : médaillons du haut inspirés du schéma fourni, avatars agrandis, 3 compteurs iconographiques (monnaie, écologie, patrimoine) et rangs directs. Les textes des écrans de jeu et des cartes remplacent les noms de ressources par des pictogrammes. Infobulles explicatives.

V16.6.81 : les cases Py libres dans les 150 m clignotent et sont cliquables directement sur la carte pendant les attributions des cartes nénuphars. Chaque acquisition actualise la sélection ; les boutons restent disponibles.

V16.6.81 : médaillons portrait adaptés automatiquement aux 2 à 8 joueurs ; affichage sans défilement horizontal. Réglages en bas à droite, repliés en roue crantée dorée.

V16.6.81 : avatars agrandis dans les médaillons portrait, hauteur adaptée selon le nombre de joueurs, scores et classements conservés.

V16.6.81 : le pictogramme du nénuphar apparaît dans le choix de trajet quand la destination exacte est une case événement.

V16.6.81 : musique d’ambiance coupée par défaut. Réglage manuel conservé et mémorisé séparément des anciennes préférences.


## Correctif V16.6.81
- Classement final simplifié : seulement 3 catégories visibles (écologie, patrimoine, monnaie) + total pondéré.
- Affichage du rang de chaque joueur pour chaque catégorie dans le tableau final.


## V16.6.81
- Saisie des noms des joueurs au début de la partie avec contrôle des doublons.
- Photographies de découvertes sourcées depuis Wikimedia Commons, crédits et licences affichés sur les cartes.
- Cadrage d’image `object-fit:contain` pour voir l’espèce entière.
- Photos Wikimedia téléchargeables avant usage hors ligne avec `python3 telecharger_photos_wikimedia.py` ; fallback local existant sinon.


V16.6.81 : les cartes de récompense de cases Py s’affichent avant leur sélection interactive sur la carte. Rangs et catégories correctement alignés dans la fiche du joueur actif.


V16.6.81 : toutes les cartes attribuant des cases Py affichent d’abord leur événement ; les boutons de destinations ne contiennent plus de noms de rues, seulement numéro et pictos de catégorie / pont / nénuphar. Noms conservés sur carte et en infobulle.


V16.6.81 : panneau actif simplifié (tour uniquement, dés en images sans répétition textuelle), en-tête des choix masqué quand aucun choix, bond de fin de tour sans affichage intempestif de « Passer mon tour ».


V16.6.81 : affichage du classement général calculé en direct au-dessus de chaque avatar (50 % écologie, 30 % patrimoine, 20 % monnaie), égalités identiques au classement final.


## V16.6.81
- Les pastilles temporaires ne sont plus recréées après l’arrivée du personnage.
- Les pancartes et drapeaux de destination disparaissent dès qu’un trajet est validé.
- Les pastilles encore à parcourir s’effacent progressivement pendant l’animation.


## V16.6.81
Le passage au joueur suivant nécessite toujours le clic explicite sur « Terminer mon tour ». Les choix d’investissement, de nettoyage, de taxe, les enchères et les cartes événement ne déclenchent plus de fin de tour automatique.


V16.6.81 : sélection obligatoire du nombre de joueurs avant la sélection des noms et avatars ; panneau du joueur actif repositionné en bas à droite au-dessus des réglages.
