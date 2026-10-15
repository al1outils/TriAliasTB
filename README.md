# TriAliasTB

TriAliasTB is a free Windows utility that sorts Thunderbird email aliases (additional identities) alphabetically without changing the order of mail accounts.

**Version: v1.0.6** — the application interface is in French.

## Download

Download **`TriAliasTB.exe`** from the [v1.0.6 GitHub Release](https://github.com/al1outils/TriAliasTB/releases/tag/v1.0.6). The executable is standalone; Python does not need to be installed on the user's PC.

## What's new in v1.0.6

- Detects the actual Windows Desktop location, including when it is moved to another drive.
- Resizable window with a minimum size to preserve readability.
- Official icon used by the executable and the application window.
- Build script removes old `build` and `dist` folders before compiling.

## Microsoft Defender SmartScreen warning

When `TriAliasTB.exe` is downloaded and launched for the first time, Microsoft Defender SmartScreen may warn that the application is “unrecognized”. This can happen because the file has not yet built a reputation with Microsoft.

If you downloaded the executable from the official Release and decide to run it, click **More info**, then **Run anyway**. Windows screens and options may vary by configuration.

## Features

- Detects Thunderbird profiles listed in `profiles.ini`.
- Sorts aliases by email address while keeping the primary identity first.
- Preserves the order of mail accounts.
- Automatically backs up `prefs.js` before writing.
- Automatically detects whether Thunderbird is running.
- Green/red status indicator with automatic refresh.
- Opens the selected profile folder.
- Offers to create a Desktop shortcut on first launch.
- Portable application; it does not write to the Windows Registry.

## Verified compatibility

- Windows 10 22H2
- Windows 11 25H2

The maintainer tested v1.0.6 on both Windows versions, including launch, shortcut creation with a redirected Desktop, and window resizing.

## How to use

1. Close Thunderbird completely.
2. Launch `TriAliasTB.exe`.
3. If prompted, choose whether to create a Desktop shortcut.
4. Select the Thunderbird profile to inspect.
5. Check the number of **Mailboxes to sort**.
6. Click **Trier les alias** (Sort aliases), then confirm.
7. Wait for the completion message.

The sort button is disabled while Thunderbird is running. If no sorting is required, the application reports this without modifying `prefs.js`.

## Backup and portable operation

Before each write operation, the program creates a copy of `prefs.js`, for example `prefs.js.bak_YYYYMMDD_HHMMSS`. Only the account-to-identity association lines are rewritten. The primary identity remains first.

The setting related to the first-run shortcut prompt is stored in `TriAliasTB.ini` in the program folder. The `.ico` file is used for building and does not need to be distributed separately to end users.

**Important:** always close Thunderbird before sorting. Keep your usual Thunderbird profile backups.

## Quick troubleshooting

- **The sort button is disabled:** make sure Thunderbird is fully closed; the status refreshes automatically.
- **The expected profile is missing:** check that it is listed in the `profiles.ini` file used by Thunderbird.
- **The shortcut was not created:** the application displays an error and lets you retry at the next launch.
- **SmartScreen displays a warning:** verify that the file came from the official Release before deciding to run it.

## Project files

The repository contains the Python source, build files, documentation, and license files. The user-facing executable is attached to the Release.

- Repository: https://github.com/al1outils/TriAliasTB
- v1.0.6 Release: https://github.com/al1outils/TriAliasTB/releases/tag/v1.0.6

## License

MIT. See `LICENSE` and `LICENSE.fr.md`.

---

Developed by **Al1 Outils** — https://toutlibre.com
