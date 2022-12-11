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
Le programme enregistre en clair toutes les transactions dans un fichier <i>.csv </i> externe. <br/>
Ainsi, on peut facilement modifier n'importe quelle variable opperant sur une transaction ; emetteur, recepteur ou montant. <br/>
La modification d'une de ces variables dans le fichier <i>.csv </i> fait que la modification a directement lieu sur la transaction : <br/>
Ex : Si l'on modifie le montant de la transaction dans le fichier de sauvegarde, lors de n'importe quelle requête permettant d'afficher la transaction, la modification apparaitra. Ainsi, le solde ainsi que l'historique des deux utilisateurs seront touchés.

## Tchaî V2
### Intégrer une nouvelle structure de transaction
Nous ajoutons maintenant le hash d’une transaction dans son tuplet : (P1, P2, t, a, h), où a est égal à la
somme d’argent transférée de la personne P1 à la personne P2 au moment t et h correspond au hash
du tuple (P1, P2, t, a).

Dans cette nouvelle version du programme, il est capable de hasher les informations liées à une transaction ; à savoir l'emetteur, le recepteur, le montant et maintenant la date et heure de la transaction. </br>
Pour chiffrer ces transactions, j'utilise la bibliothèque python <i>hashlib</i> qui me permet d'utiliser la fonction de hashage <i>sha256</i>. L'utilisation de cette méthode permet de ne pas réinventer un fonction de hashage et permet l'utilisation d'une fonction reconnu et sécuritaire.</br>
Pour utiliser cette fonction sur une variable de type tuple, il faut d'abord convertir cette variable sous forme de chaine de caractères. Il faut par la suite définir un langage d'encodage de cette chaine ; ici elle sera encodé en langage <i>UTF-8</i>.
<br/><br/>
Ainsi, notre nouvelle structure de transaction est opérationelle.

[...]

### Vérification de l'intégrité des données
Vérifier l’intégrité des données en recalculant les hashs à partir des données et en les comparant
avec les hashs stockés précédemment.

Maintenant que la structure des transactions à été modifié, il nous faut vérifier l'intégrité de nos données pour prévenir d'une éventuelle attaque.<br/>
Pour ce faire, nous allons récupérer le hash stocké dans notre base de donnée et le comparer avec un hash nouvellement calculé à partir des mêmes données en entrée.<br/>
<p>
- Si les deux hashs sont identiques, la transaction est valide.<br/>
- Sinon, il y a non validité dans les données.</p>
Ainsi, lorsque l'on souhaite afficher le tableau de bord, l'intégralité des transactions va etre vérifiée. 
<p>
- Si toute les transactions sont valides, on indique que les données sont intègres.
- Si l'une des transaction n'est pas valide, on indique que les données ne sont pas intègres.
</p>

### Réexecuter l'attaque précedente et vérifier qu'elle n'est plus possible
Maintenant que nous vérifions l'intégritée des données, l'attaque précédente n'est plus possible ; à savoir modifier une ou plusieurs données d'une transaction.<br/>
En effet, lorsqu'une donnée est modifié, la valeur du hash, elle, n'est pas recalculée, donc lors de l'affichage des transactions, il sera indiqué que l'intégritée des données n'est pas valide.
### Attaquer le système en supprimant une transaction
En modifiant directement le fichier de données, en supprimant une ligne correspondant à une transaction, rien ne se passe, l'intégrité des données est toujours valide et le solde des utilisateurs est mis à jour en accord avec la disparition de cette transaction.<br/>
En théorie, l'intégrité des données ne devrait plus etre valide, or ici ce n'est pas le cas.<br/>
Pour ce qui est du risque de double dépense, nous ne sommes pas confronté à ca problème.

## Tchaî V3
### Modifier la méthode de calcul du hash
A partir de maintenant, la valeur du hash d'une nouvelle transaction va, en plus des valeurs de la transaction en cours, prendre la valeur du hash de la transaction précédente.<br/>
Ainsi, lors d'une nouvelle transaction, nous executons notre fonction de hashage sur 5 variables : emetteur, recepteur, montant, date/heure et le hash précédent.<br/>
Cela peux poser un porblème lorsque la liste de transaction est vide et que l'on souhaite créer notre première transaction. Ainsi nous ajoutons une exeption lors de la première et plaçons comme valeur de hash précédente la valeur 0.<br/>
Ex de première transaction : Personne1, Personne2, montant, date et heure, HASH(calculé avec les valeurs ci-avant et le hash précédent, ici '0').<br/>

### Réexecuter les attaques précédentes
Lorsque nous décidons d'attaquer directement notre fichier en modifiant une valeur, la fonction de vérification va détecter une anomalie est afficher que l'integrité des données n'est pas valide.<br/>
Lorsque nous décidons d'attaquer directement notre fichier en supprimant une transaction, la fonction de vérification va égualement détecter une anomalie est afficher le même message.
### Attaquer le système en ajoutant une transaction
Maintenant, testons une nouvelle attaque. Celle_ci consiste en l'ajout d'un transaction directement dans le fichier de données.
Si le hash entré dans la <i>nouvelle transaction</i> ne respecte pas le hash de la transaction précédente, la vérification des données va détecter l'anomalie est afficher que l'intégrité des données n'est pas valide.<br/>
Si le hash est correcte et respecte lors de son calcul la valeur du hash précédent, la vérification ne va pas détecter d'anomalie et va afficher que l'intégrité des données ets valide.
