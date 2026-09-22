# TriAliasTB --- DOSSIER MAÎTRE

**Version du projet : v1.0.4**

**Date de mise à jour : 2026-09-20**

## ÉTAT FIGÉ DU PROJET

> À partir de la v1.0, les éléments ci-dessous constituent l'état de
> référence du projet.

  Élément                  État
  ------------------------ -------------------------------------------
  Version actuelle         **v1.0.4**
  Moteur de tri            Validé (v0.6)
  Interface graphique      Validée
  Langue officielle        Français
  Compatibilité            Windows 10 / Windows 11
  Sauvegarde               Obligatoire avant écriture
  Thunderbird              Doit être fermé avant le tri
  Détection des profils    Via `profiles.ini`
  Dernier fichier Python   `TriAliasTB_v1.0.4.py`
  Icône officielle         Flèche de tri
  Prochaine étape          Validation finale puis publication GitHub

Ce document constitue la référence officielle du projet.

En cas de contradiction avec une ancienne conversation, ce document fait
foi.

------------------------------------------------------------------------

# 1. Présentation du projet

**TriAliasTB** est un utilitaire Windows destiné à trier les alias de
Thunderbird par ordre alphabétique, sans modifier l'ordre des boîtes
mail.

Mainteneur : **Al1 Outils**

-   Site : https://toutlibre.com
-   GitHub : `al1outils`

------------------------------------------------------------------------

# 2. Objectif

Créer un outil simple, sûr, open source et compatible Windows 10/11.

------------------------------------------------------------------------

# 3. Vocabulaire officiel

  Terme                 Signification
  --------------------- --------------------------------------
  Boîte mail            Compte Thunderbird
  Alias                 Identité supplémentaire
  Identité principale   Première identité
  Fournisseur           Orange, OVH, Gmail, Infomaniak, etc.

------------------------------------------------------------------------

# 4. Règles du projet

1.  Ne jamais modifier l'ordre des boîtes mail.
2.  Conserver l'identité principale en première position.
3.  Trier uniquement les alias.
4.  Le tri est effectué sur `useremail` (adresse e-mail).
5.  Le nom d'affichage (`fullName`) peut devenir `contact` (ou tout
    autre choix) sans perturber le tri.
6.  Sauvegarder `prefs.js` avant toute écriture.
7.  Thunderbird doit être fermé avant toute modification.
8.  Les profils sont obtenus via `profiles.ini`, quel que soit leur
    emplacement.

------------------------------------------------------------------------

# 5. Architecture Thunderbird

-   Détection via `profiles.ini`.
-   Réécriture limitée aux lignes `mail.account.accountX.identities=`.
-   Conservation systématique de l'identité principale.

------------------------------------------------------------------------

# 6. Configuration validée

-   Windows 11 25H2.
-   Windows 10 22H2.
-   Python utilisé pour le développement.
-   Deux profils Thunderbird réels (Infomaniak et Orange).

------------------------------------------------------------------------

# 7. Portabilité

TriAliasTB est une application portable.

-   N'écrit rien dans le Registre Windows.
-   Ne crée rien dans `%APPDATA%` ni `%LOCALAPPDATA%`.
-   Les seules écritures permanentes concernent `prefs.js`, sa
    sauvegarde et `TriAliasTB.ini` dans le dossier du programme.

------------------------------------------------------------------------

# 8. Tests validés

  Test                                         Résultat
  -------------------------------------------- ----------
  Détection des profils                        OK
  Lecture de `prefs.js`                        OK
  Sauvegarde automatique                       OK
  Tri réel des alias                           OK
  Conservation identité principale             OK
  Réécriture ciblée                            OK
  Interface graphique                          OK
  Voyant vert/rouge                            OK
  Icône personnalisée                          OK
  EXE autonome sans Python installé            OK
  Création du raccourci au premier lancement   OK

------------------------------------------------------------------------

# 9. État actuel

## Version actuelle

**v1.0.4**

## Fonctionnalités disponibles

-   Détection automatique des profils.
-   Analyse automatique.
-   Sauvegarde automatique.
-   Tri réel des alias.
-   Interface Tkinter en français.
-   Journal intégré.
-   Ouverture du dossier du profil.
-   Voyant vert/rouge.
-   Icône personnalisée.
-   Raccourci Bureau proposé au premier lancement.
-   Fenêtre au premier plan au lancement.

Le moteur de tri validé en v0.6 est désormais figé.

------------------------------------------------------------------------

# 10. Journal du projet

## Séances 1 à 5

-   Définition du besoin.
-   Architecture.
-   Détection des profils.
-   Validation de l'identité principale.
-   Simulation du tri.

## Séance 6

-   Validation complète du moteur.

## Séance 7

-   Première interface graphique.

## Séance 8

-   Voyant vert/rouge validé.

## Séance 9

-   Icône officielle.
-   Intégration de l'icône dans la fenêtre et l'EXE.

## Séance 9.1

-   Premier lancement : proposition de créer un raccourci sur le Bureau.
-   Création de `TriAliasTB.ini` dans le dossier du programme.
-   Aucune écriture dans le Registre ni dans `%APPDATA%`.

## Séance 10

-   Suppression de la dépendance `winshell`.
-   Création du raccourci via `pywin32`.
-   Fenêtre au premier plan au lancement.
-   Validation Windows 10 22H2 et Windows 11 25H2.
-   Validation de l'EXE autonome sans Python installé.

------------------------------------------------------------------------

# 11. Feuille de route

## v1.0.1

-   Suppression du bouton « Analyser » devenu inutile.
-   L'analyse reste automatique au chargement du profil et après le tri.

## v1.0.2

-   Correction du comportement du bouton « Trier les alias » lorsque
    aucun tri n'est nécessaire.
-   Si aucun compte ne nécessite de tri :
    -   aucune sauvegarde de `prefs.js` n'est créée ;
    -   aucune modification n'est effectuée ;
    -   un message informe l'utilisateur que rien n'est à trier.

## v1.0.3

-   Actualisation automatique de l'état de Thunderbird.
-   Réactivation automatique du bouton après fermeture de Thunderbird.
-   Plus besoin de relancer TriAliasTB.

## v1.0.4

-   Suppression de la barre d'état inférieure.
-   Message unique à côté du voyant.
-   Actualisation automatique de l'état de Thunderbird (2 s).
-   « Boîtes à trier » remplace « À trier ».

## v1.1 Internationalisation (projet)

-   Interface disponible en français et en anglais.
-   Un seul code source avec gestion des textes par dictionnaire (LANG / TEXT).
-   Choix de la langue dans l’application.
-   Un seul EXE gérant les deux langues.
-   Mise à jour de la documentation correspondante.

------------------------------------------------------------------------

# 12. Méthode de développement

-   Une séance = un livrable.
-   Une version = un fichier complet.
-   Ne jamais écraser une version validée.
-   Le dossier maître fait foi.

------------------------------------------------------------------------

# 13. Kit de reprise

Fichiers à joindre :

-   `TriAliasTB_DOSSIER_MAITRE_v1.0.4.md`
-   `TriAliasTB_v1.0.4.py`

Message de reprise :

> « Nous reprenons TriAliasTB à partir de la v1.0.4. Le dossier maître
> fait foi. »
------------------------------------------------------------------------

# 14. Publication

-   README.fr.md
-   README.md
-   LICENSE MIT
-   CHANGELOG.md
-   `.gitignore`
-   Dépôt GitHub
-   Publication ToutLibre