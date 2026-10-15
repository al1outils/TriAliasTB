# Changelog.fr

Toutes les évolutions importantes de TriAliasTB sont documentées dans ce fichier.

## v1.0.6

### Corrections

- Correction de la détection du dossier Bureau Windows lorsqu’il est déplacé ou redirigé, y compris vers un autre disque.
- Amélioration de la fiabilité de la création du raccourci grâce à la détection de l’emplacement réel du Bureau Windows.

### Améliorations

- Fenêtre redimensionnable avec une taille minimale.
- Icône officielle intégrée à l’EXE et disponible pour l’interface.
- Le script de construction supprime les anciens dossiers `build` et `dist` avant compilation.
- Le fichier `.ico` est retiré du dossier de distribution `dist` après compilation ; seul `TriAliasTB.exe` est destiné à l’utilisateur final.

### Compatibilité

- Fonctionnement de la v1.0.6 validé par le mainteneur sous Windows 10 22H2 et Windows 11 25H2.
- Le tri des alias conserve le comportement validé depuis les versions antérieures.

## v1.0.4 (2026-09-20)

### Ajouts

- Détection automatique de l'état de Thunderbird.
- Réactivation automatique du bouton de tri après fermeture de Thunderbird.
- Création automatique d'un raccourci Bureau au premier lancement.

### Améliorations

- Suppression du bouton **Analyser**.
- Suppression de la barre d'état.
- Message d'état unique à côté du voyant.
- Remplacement de **« À trier »** par **« Boîtes à trier »**.
- Meilleure gestion du cas où aucun tri n'est nécessaire.

### Compatibilité

- Validation Windows 10 22H2.
- Validation Windows 11 25H2.
- Fonctionnement autonome, sans dépendance externe.
