# TriAliasTB

TriAliasTB est un utilitaire Windows libre qui trie les alias (identités supplémentaires) de Thunderbird par ordre alphabétique, sans modifier l’ordre des comptes de messagerie.

**Version : v1.0.6** — interface en français.

## Téléchargement

Téléchargez **`TriAliasTB.exe`** depuis la [Release v1.0.6](https://github.com/al1outils/TriAliasTB/releases/tag/v1.0.6). L’EXE est autonome : Python n’a pas besoin d’être installé sur le PC.

## Nouveautés de la v1.0.6

- Détection de l’emplacement réel du Bureau Windows, y compris lorsqu’il est déplacé vers un autre disque.
- Fenêtre redimensionnable, avec une taille minimale pour préserver la lisibilité.
- Utilisation de l’icône officielle dans l’EXE et dans l’interface.
- Kit de construction nettoyant les anciens dossiers `build` et `dist` avant compilation.

## Avertissement Microsoft Defender SmartScreen

Lors du premier téléchargement et lancement de `TriAliasTB.exe`, Microsoft Defender SmartScreen peut afficher un avertissement indiquant que l’application est « non reconnue ». Cela peut se produire parce que le fichier n’a pas encore acquis de réputation auprès de Microsoft.

Si vous avez téléchargé l’EXE depuis la Release officielle et souhaitez le lancer, cliquez sur **Informations complémentaires**, puis sur **Exécuter quand même**. Les écrans et options peuvent varier selon la configuration de Windows.

## Fonctionnalités

- Détection des profils Thunderbird déclarés dans `profiles.ini`.
- Tri des alias par adresse e-mail, sans déplacer l’identité principale.
- Conservation de l’ordre des comptes de messagerie.
- Sauvegarde automatique de `prefs.js` avant toute écriture.
- Détection automatique de l’état ouvert/fermé de Thunderbird.
- Voyant d’état vert/rouge et actualisation automatique.
- Ouverture du dossier du profil sélectionné.
- Proposition de création d’un raccourci sur le Bureau au premier lancement.
- Application portable : aucun enregistrement dans le Registre Windows.

## Compatibilité vérifiée

- Windows 10 22H2
- Windows 11 25H2

Les tests fonctionnels de la v1.0.6, notamment le lancement, le raccourci avec un Bureau déplacé et le redimensionnement, ont été effectués par le mainteneur sur ces deux versions de Windows.

## Utilisation

1. Fermez complètement Thunderbird.
2. Lancez `TriAliasTB.exe`.
3. Si la question apparaît, choisissez si vous souhaitez créer un raccourci sur le Bureau.
4. Sélectionnez le profil Thunderbird à examiner.
5. Vérifiez le nombre de **Boîtes à trier**.
6. Cliquez sur **Trier les alias**, puis confirmez.
7. Attendez le message de fin.

Le bouton de tri est désactivé tant que Thunderbird est ouvert. Si aucun tri n’est nécessaire, le programme l’indique sans modifier `prefs.js`.

## Sauvegarde et fonctionnement

Avant chaque écriture, le programme crée une copie de `prefs.js`, par exemple `prefs.js.bak_YYYYMMDD_HHMMSS`. Seules les lignes d’association des identités aux comptes sont réécrites. L’identité principale reste en première position.

La configuration liée à la proposition de raccourci est enregistrée dans `TriAliasTB.ini`, dans le dossier du programme. Le fichier `.ico` sert à la construction et n’a pas à être distribué séparément aux utilisateurs.

**Précaution :** fermez toujours Thunderbird avant le tri. Conservez vos propres sauvegardes habituelles de profil Thunderbird.

## Dépannage rapide

- **Le bouton de tri est désactivé :** vérifiez que Thunderbird est complètement fermé ; l’état est actualisé automatiquement.
- **Le profil attendu n’apparaît pas :** vérifiez qu’il est déclaré dans le fichier `profiles.ini` utilisé par Thunderbird.
- **SmartScreen affiche un avertissement :** vérifiez que le fichier provient bien de la Release officielle avant de décider de l’exécuter.

## Fichiers du projet

Le dépôt contient le code Python, les fichiers de construction, la documentation et les licences. L’EXE destiné aux utilisateurs est joint aux fichiers de la Release.

- Dépôt : https://github.com/al1outils/TriAliasTB
- Release v1.0.6 : https://github.com/al1outils/TriAliasTB/releases/tag/v1.0.6

## Licence

MIT. Voir `LICENSE` et `LICENSE.fr.md`.

---

Développé par **Al1 Outils** — https://toutlibre.com
