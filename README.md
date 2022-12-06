# Systemes d'Information Avancés - Projet TP

## Auteur
Clément GRENOT / KeyIsLying / clementgrenot@gmail.com

## Description
Concevoir un système de transaction éléctroniques avec une intégrité garantie, accessible par le protocole HTTP

## Tchaî V1
### Enregistrer une transaction.
Il est possible d'enregistrer une transaction à l'aide d'une requête HTTP. <br />
<p>
En utilisant une requête via le CMD:<br />
- curl -X localhost:5000/new_Transac/<débité>/<crédité>/<montant>
</p><p>
Ou en utilisant directement la barre de recherche du navigateur:<br />
- localhost:5000/new_Transac/<débité>/<crédité>/<montant>
</p>
Il suffit de modifier le nom des variables dans l'URL par les noms de variables souhaitées.<br />
Ex : localhost:5000/new_Transac/Utilisateur1/Utilisateur2/30

### Afficher la liste de toutes les transactions dans l'ordre chronologique.
Il est possible d'afficher la liste des transaction à l'aide d'un requête HTTP. <br />
<p>
En utilisant une requête via le CMD:<br />
- curl -X localhost:5000/
</p><p>
Ou en utilisant directement la barre de recherche du navigateur:<br />
- localhost:5000/
</p>

### Afficher une liste des transactions dans l'ordre chronologique liées à une personne donnée.
Il est possible d'afficher une liste de transaction d'un utilisateur à l'aide d'une requête HTTP. <br />
<p>
En utilisant une requête via le CMD:<br />
- curl -X localhost:5000/historique/<utilisateur>
</p><p>
Ou en utilisant directement la barre de recherche du navigateur:<br />
- localhost:5000/historique/<utilisateur>
</p>
Il suffit de modifier le nom de la variable "utilisateur" dans l'URL par le nom d'un utilisateur deja enregistré dans la liste.<br />
Ex : localhost:5000/historique/Utilisateur1

### Afficher le solde du compte de la personne données
Il est possible de calculer et d'afficher le solde d'un utilisateur à l'aide d'une requête HTTP. <br/>
<p>
En utilisant une requête via le CMD:<br/>
- curl -X localhost:5000/solde/<utilisateur
</p><p>
Ou en utilisant directement la barre de recherche du navigateur:<br/>
- localhost:5000/solde/<utilisateur>
</p>
il suffit de modifier le nom de la variable "utilisateur" dans l'URL par le nom d'un uitilisateur déja enregistré dans la liste. <br/>
Ex : localhost:5000/historique/Utilisateur1

### Attaquer le système en modifiant directement le fichier de données, en changeant le montant d'une transaction.


## Tchaî V2
### Intégrer une nouvelle structure de transaction
Nous ajoutons maintenant le hash d’une transaction dans son tuplet : (P1, P2, t, a, h), où a est égal à la
somme d’argent transférée de la personne P1 à la personne P2 au moment t et h correspond au hash
du tuple (P1, P2, t, a).

[...]

### Vérification de l'intégrité des données
Vérifier l’intégrité des données en recalculant les hashs à partir des données et en les comparant
avec les hashs stockés précédemment.

[...]

### Réexecuter l'attaque précedente et vérifier qu'elle n'est plus possible

[...]

## Tchaî V3

## Tchaî Cryptographique (V4)