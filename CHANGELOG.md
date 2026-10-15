# Changelog

All notable changes to TriAliasTB are documented in this file.

## v1.0.6

### Fixed

- Fixed Windows Desktop-folder detection when the Desktop is moved or redirected, including to another drive.
- Improved shortcut creation reliability by detecting the actual Windows Desktop location.

### Improved

- Resizable window with a minimum size.
- Official icon embedded in the executable and available to the application window.
- Build script removes old `build` and `dist` folders before compiling.
- The `.ico` file is removed from the `dist` distribution folder after compilation; only `TriAliasTB.exe` is intended for end users.

### Compatibility

- The maintainer validated v1.0.6 on Windows 10 22H2 and Windows 11 25H2.
- Alias sorting retains the behavior validated in earlier versions.

## v1.0.4 (2026-09-20)

### Added

- Automatic detection of Thunderbird running state.
- Automatic re-enabling of the **Sort aliases** button after Thunderbird is closed.
- Desktop shortcut proposal on first launch.

### Improved

- Removed the **Analyze** button.
- Removed the bottom status bar.
- Single status message next to the indicator.
- Replaced **"To sort"** with **"Mailboxes to sort"**.
- Improved handling when no mailbox requires sorting.

### Compatibility

- Validated on Windows 10 22H2.
- Validated on Windows 11 25H2.
- Standalone operation with no external dependencies.
