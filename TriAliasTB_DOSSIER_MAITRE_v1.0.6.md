# TriAliasTB — DOSSIER MAÎTRE

**Version de référence du projet : v1.0.6**  
**Date de mise à jour : 2026-10-11**

## ÉTAT DE RÉFÉRENCE DU PROJET

| Élément                                | État                                                                                  |
|----------------------------------------|---------------------------------------------------------------------------------------|
| ---                                    | ---                                                                                   |
| Dernière version fonctionnelle validée | **v1.0.6**                                                                            |
| Dernière version publiée               | **v1.0.6**                                                                            |
| Validation de v1.0.6                   | Confirmée par l’utilisateur sous Windows 10 et Windows 11                             |
| Moteur de tri                          | Validé depuis v0.6, inchangé dans v1.0.6                                              |
| Interface graphique                    | Validée ; fenêtre redimensionnable depuis v1.0.6                                      |
| Langue officielle                      | Français                                                                              |
| Compatibilité testée                   | Windows 10 22H2 et Windows 11 25H2                                                    |
| Sauvegarde                             | Obligatoire avant toute écriture dans `prefs.js`                                      |
| Thunderbird                            | Doit être fermé avant le tri                                                          |
| Détection des profils                  | Via `profiles.ini`, quel que soit leur emplacement                                    |
| Dernier fichier Python                 | `TriAliasTB_v1.0.6.py`                                                                |
| Icône officielle                       | `TriAliasTB.ico`, version confirmée par l’utilisateur                                 |
| Fichier final pour les utilisateurs    | Un seul fichier : `TriAliasTB.exe`                                                    |
| Publication GitHub                     | Release/tag **v1.0.6 publiée** ; v1.0.4 conservée dans l’historique          |
| Publication ToutLibre                  | Article consacré à la v1.0.6 publié ; présentation à conserver pour cette version     |
| Prochaine étape                        | Préparer la v1.1 bilingue (français/anglais) à partir de la v1.0.6 |
Ce document constitue la référence officielle du projet. En cas de contradiction avec une ancienne conversation, il fait foi.

---

# 1. Présentation du projet

**TriAliasTB** est un utilitaire Windows destiné à trier les alias de Thunderbird par ordre alphabétique, sans modifier l’ordre des boîtes mail.

Mainteneur : **Al1 Outils**

- Site : https://toutlibre.com
- GitHub : `al1outils`
- Dépôt : https://github.com/al1outils/TriAliasTB

---

# 2. Objectif

Créer un outil simple, sûr, open source et compatible Windows 10/11. La distribution finale doit être portable et facile à utiliser, sans exiger que Python soit installé sur le PC de l’utilisateur.

---

# 3. Vocabulaire officiel

| Terme               | Signification                        |
|---------------------|--------------------------------------|
| ---                 | ---                                  |
| Boîte mail          | Compte Thunderbird                   |
| Alias               | Identité supplémentaire              |
| Identité principale | Première identité du compte          |
| Fournisseur         | Orange, OVH, Gmail, Infomaniak, etc. |
---

# 4. Règles du projet

1. Ne jamais modifier l’ordre des boîtes mail.
2. Conserver l’identité principale en première position.
3. Trier uniquement les alias.
4. Effectuer le tri sur `useremail` (adresse e-mail).
5. Le nom d’affichage (`fullName`) peut devenir `contact` ou toute autre valeur sans perturber le tri.
6. Sauvegarder `prefs.js` avant toute écriture.
7. Thunderbird doit être fermé avant toute modification.
8. Obtenir les profils via `profiles.ini`, quel que soit leur emplacement.
9. Ne jamais écraser une version validée ; chaque version livrée doit être conservée comme fichier complet.

---

# 5. Architecture Thunderbird

- Détection des profils via `profiles.ini`.
- Réécriture limitée aux lignes `mail.account.accountX.identities=`.
- Conservation systématique de l’identité principale.
- Sauvegarde de `prefs.js` avant écriture.
- L’ordre des comptes/boîtes mail ne doit pas être modifié.

---

# 6. Configuration de validation

- Windows 11 25H2.
- Windows 10 22H2.
- Python utilisé pour le développement et la construction de l’EXE.
- Deux profils Thunderbird réels utilisés lors des essais (Infomaniak et Orange).
- Essais de v1.0.6 réalisés avec le Bureau Windows déplacé sur un autre disque.

Chemins de Bureau ayant servi aux essais de v1.0.6 :

- Windows 11 : emplacement personnalisé sur le disque D:.
- Windows 10 : emplacement personnalisé sur le disque D:.

---

# 7. Portabilité et distribution

TriAliasTB est une application portable.

- N’écrit rien dans le Registre Windows.
- Ne crée rien dans `%APPDATA%` ni `%LOCALAPPDATA%`.
- Les écritures permanentes liées au programme concernent `prefs.js`, sa sauvegarde et `TriAliasTB.ini` dans le dossier du programme.
- L’EXE final est autonome et a été testé sans Python installé.
- La distribution utilisateur de v1.0.6 doit contenir uniquement `TriAliasTB.exe`. Le fichier `.ico` est nécessaire à la construction, mais n’a pas à être fourni séparément à l’utilisateur final.

## Gestion du Bureau et du raccourci — v1.0.6

La v1.0.4 ne trouvait pas correctement le Bureau lorsque celui-ci avait été déplacé vers un chemin non standard sur le disque D:. La v1.0.6 utilise l’API Windows `SHGetFolderPathW` avec `CSIDL_DESKTOPDIRECTORY` pour obtenir l’emplacement réel du Bureau.

Si la création du raccourci échoue, l’application signale l’erreur et ne marque pas la demande de raccourci comme terminée ; une nouvelle tentative reste donc possible au lancement suivant.

## Fenêtre — v1.0.6

Fenêtre redimensionnable : l’utilisateur peut l’agrandir ou la réduire, tout en conservant une taille minimale qui permet de voir correctement les éléments de l’interface.

## Icône — v1.0.6

- L’icône officielle correcte est utilisée pour l’icône intégrée à l’EXE et pour l’interface.
- Le SPEC PyInstaller pointe explicitement vers le fichier `TriAliasTB.ico` situé dans le dossier du kit.
- L’icône est également ajoutée aux données du bundle afin que l’icône de fenêtre soit disponible pendant l’exécution.
- Le BAT nettoie les anciens dossiers `build` et `dist` avant la compilation.
- Le BAT supprime `dist\TriAliasTB.ico` après la compilation : l’utilisateur final ne reçoit que `TriAliasTB.exe`.
- SHA-256 de l’icône officielle confirmée : `37980fcd7669b04dcff300bdc5755e5bc0b419b2a1aa5f728f4f24da1407a81f`.

---

# 8. Tests validés

| Test                                                | Résultat                         |
|-----------------------------------------------------|----------------------------------|
| ---                                                 | ---                              |
| Détection des profils                               | OK                               |
| Lecture de `prefs.js`                               | OK                               |
| Sauvegarde automatique                              | OK                               |
| Tri réel des alias                                  | OK                               |
| Conservation de l’identité principale               | OK                               |
| Réécriture ciblée                                   | OK                               |
| Interface graphique                                 | OK                               |
| Voyant vert/rouge                                   | OK                               |
| Icône personnalisée                                 | OK                               |
| EXE autonome sans Python installé                   | OK                               |
| Création du raccourci au premier lancement          | OK                               |
| v1.0.6 sous Windows 10 22H2                         | OK, confirmé par l’utilisateur   |
| v1.0.6 sous Windows 11 25H2                         | OK, confirmé par l’utilisateur   |
| Création du raccourci avec le Bureau déplacé sur D: | OK sous Windows 10 et Windows 11 |
| Redimensionnement de la fenêtre v1.0.6              | OK                               |
| Kit de construction corrigé avec l’icône officielle | Confirmé par l’utilisateur       |
**Limite de vérification :** la validation fonctionnelle de v1.0.6 et du kit final est rapportée par l’utilisateur. La compilation Windows n’a pas été exécutée dans l’environnement de préparation du présent document.

---

# 9. État actuel et fonctionnalités

## Version fonctionnelle de référence

**v1.0.6 — version française publiée et figée.**

La Release GitHub v1.0.6 est publiée. La v1.0.4 reste disponible dans l’historique des Releases.

## Fonctionnalités disponibles

- Détection automatique des profils.
- Analyse automatique.
- Sauvegarde automatique.
- Tri réel des alias par adresse e-mail.
- Conservation de l’identité principale.
- Interface Tkinter en français.
- Journal intégré.
- Ouverture du dossier du profil.
- Voyant vert/rouge.
- Icône personnalisée correcte.
- Proposition de créer un raccourci Bureau au premier lancement.
- Détection de l’état de Thunderbird et actualisation automatique.
- Fenêtre au premier plan au lancement.
- Fenêtre redimensionnable.
- Prise en charge du Bureau déplacé vers un autre disque pour la création du raccourci.

Le moteur de tri validé en v0.6 est figé et n’a pas été modifié par les changements de v1.0.6.

---

# 10. Journal du projet

## Séances 1 à 5

- Définition du besoin.
- Architecture.
- Détection des profils.
- Validation de l’identité principale.
- Simulation du tri.

## Séance 6

- Validation complète du moteur.

## Séance 7

- Première interface graphique.

## Séance 8

- Voyant vert/rouge validé.

## Séance 9

- Icône officielle.
- Intégration de l’icône dans la fenêtre et l’EXE.

## Séance 9.1

- Premier lancement : proposition de créer un raccourci sur le Bureau.
- Création de `TriAliasTB.ini` dans le dossier du programme.
- Aucune écriture dans le Registre ni dans `%APPDATA%`.

## Séance 10 — v1.0.4

- Suppression de la dépendance `winshell`.
- Création du raccourci via `pywin32`.
- Fenêtre au premier plan au lancement.
- Validation Windows 10 22H2 et Windows 11 25H2.
- Validation de l’EXE autonome sans Python installé.
- Publication GitHub v1.0.4 le 22/09/2026.
- Article ToutLibre v1.0.4 publié le 05/10/2026.

## Séance 11 — correctif du Bureau et v1.0.6

- Découverte d’une limite de v1.0.4 : la création du raccourci échouait lorsque le Bureau avait été déplacé vers un chemin non standard sur D:.
- La v1.0.5 a servi d’étape de correction intermédiaire et n’est pas la version de référence actuelle.
- La v1.0.6 utilise `SHGetFolderPathW` pour trouver le Bureau Windows réel.
- En cas d’échec de création du raccourci, l’application affiche une erreur et permet de réessayer au lancement suivant.
- La fenêtre est redimensionnable : l’utilisateur peut l’agrandir ou la réduire, tout en conservant une taille minimale qui permet de voir correctement les éléments de l’interface.
- Le kit de construction utilise l’icône officielle confirmée par l’utilisateur et nettoie les anciens dossiers de compilation.
- L’EXE final conserve son icône sans fichier `.ico` séparé dans la distribution finale.
- La v1.0.6 et le kit corrigé ont été validés par l’utilisateur sous Windows 10 et Windows 11.

---

# 11. Historique des versions et feuille de route

## v1.0.1

- Suppression du bouton « Analyser » devenu inutile.
- L’analyse reste automatique au chargement du profil et après le tri.

## v1.0.2

- Correction du comportement du bouton « Trier les alias » lorsque aucun tri n’est nécessaire.
- Si aucun compte ne nécessite de tri, aucune sauvegarde de `prefs.js` n’est créée, aucune modification n’est effectuée, et un message informe l’utilisateur que rien n’est à trier.

## v1.0.3

- Actualisation automatique de l’état de Thunderbird.
- Réactivation automatique du bouton après fermeture de Thunderbird.
- Plus besoin de relancer TriAliasTB.

## v1.0.4 — dernière version publiée

- Suppression de la barre d’état inférieure.
- Message unique à côté du voyant.
- Actualisation automatique de l’état de Thunderbird toutes les 2 secondes.
- « Boîtes à trier » remplace « À trier ».

## v1.0.5 — étape intermédiaire

- Étape de correction du problème lié au chemin du Bureau Windows.
- Remplacée par la v1.0.6 ; ne pas traiter comme version de référence actuelle.

## v1.0.6 — version fonctionnelle validée, publication à effectuer

- Correction de la détection du Bureau Windows lorsqu’il est déplacé.
- Gestion d’erreur en cas d’échec de création du raccourci et nouvelle tentative possible.
- Fenêtre redimensionnable.
- Icône officielle intégrée à l’EXE et disponible dans la fenêtre.
- Kit de construction avec nettoyage des dossiers `build` et `dist`.
- Distribution utilisateur prévue sous la forme d’un seul fichier `TriAliasTB.exe`.
- Tests fonctionnels validés par l’utilisateur sous Windows 10 22H2 et Windows 11 25H2.

## v1.1 — projet d’internationalisation

- Interface disponible en français et en anglais.
- Un seul code source avec gestion des textes par dictionnaire (`LANG` / `TEXT`).
- Choix de la langue dans l’application.
- Un seul EXE gérant les deux langues.
- Mise à jour de la documentation correspondante.

---

# 12. Méthode de développement

- Une séance = un livrable.
- Une version = un fichier complet.
- Ne jamais écraser une version validée.
- Le dossier maître fait foi.
- L’utilisateur valide l’ergonomie et la documentation ; les aspects techniques sont vérifiés avant de déclarer un fichier prêt.
- Ne pas prétendre qu’une compilation ou un test a été exécuté lorsque ce n’est pas le cas.

---

# 13. Kit de reprise

Fichiers à joindre pour reprendre le développement à partir de l’état actuel :

- `TriAliasTB_DOSSIER_MAITRE_v1.0.6.md`
- `TriAliasTB_v1.0.6.py`
- `TriAliasTB_v1.0.6.spec`
- `Construire_EXE_v1.0.6.bat`
- `TriAliasTB.ico` (nécessaire à la construction, pas à distribuer séparément aux utilisateurs finaux)

Message de reprise :

> « Nous reprenons TriAliasTB à partir de la v1.0.6 française, publiée et figée, validée sous Windows 10 22H2 et Windows 11 25H2. La prochaine étape est la préparation de la v1.1 bilingue (français et anglais), à partir du code de référence v1.0.6. Le dossier maître fait foi. »

---

# 14. Publication et documentation

Éléments présents dans le dépôt GitHub, avec la v1.0.6 française comme version publiée de référence :

- `README.fr.md`
- `README.md`
- `LICENSE` / `LICENSE.fr.md`
- `CHANGELOG.md` et fichiers de documentation associés
- `.gitignore`
- Dépôt GitHub : https://github.com/al1outils/TriAliasTB
- Guides PDF français et anglais sous `docs/`
- Article ToutLibre consacré à la v1.0.6

**État des publications :**

- **v1.0.6 française :** publiée sur GitHub et conservée comme version de référence. Ne pas modifier ni remplacer ses fichiers.
- **v1.1 bilingue :** prochaine version à préparer. Elle intégrera le français et l’anglais dans une seule application, avec le français par défaut.

Pour la v1.1, mettre à jour le code source, les fichiers de construction, les guides utilisateurs, le README et les changelogs afin qu’ils correspondent à la nouvelle version et à son contenu.

Sur ToutLibre.com, conserver la présentation de la v1.0.6 et ajouter les nouveautés et améliorations de la v1.1 lorsque celle-ci sera publiée, avec le lien vers sa Release GitHub et les liens directs vers les guides utilisateurs.

Le README doit conserver l’avertissement Microsoft Defender SmartScreen pour une nouvelle application non encore reconnue.
