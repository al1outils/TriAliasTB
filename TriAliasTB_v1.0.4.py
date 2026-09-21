#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TriAliasTB v1.0.4
Interface Windows (Français)

- Moteur v0.6 conservé
- Sauvegarde automatique
- Tri réel des alias
- Détection de Thunderbird ouvert
"""

from pathlib import Path
import os
import re
import shutil
import subprocess
import configparser
from datetime import datetime
import sys

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# --------------------------------------------------
# Langue
# --------------------------------------------------

T = {
    "title": "TriAliasTB v1.0.4",
    "sort": "Trier les alias",
    "quit": "Quitter",
    "open": "Ouvrir le dossier",
    "confirm": "Une sauvegarde de prefs.js sera créée avant le tri.\n\nContinuer ?",
}

# --------------------------------------------------
# Expressions régulières
# --------------------------------------------------

PREF_RE = re.compile(r'^user_pref\("([^"]+)",\s*"(.*)"\);$')

IDENTITY_LINE_RE = re.compile(
    r'^(user_pref\("mail\.account\.(account\d+)\.identities",\s*")(.*?)("\);.*)$'
)

# --------------------------------------------------
# Thunderbird
# --------------------------------------------------

def thunderbird_root():
    return Path(os.getenv("APPDATA")) / "Thunderbird"


def thunderbird_running():
    try:
        txt = subprocess.check_output(
            ["tasklist"],
            text=True,
            creationflags=0x08000000
        )
        return "thunderbird.exe" in txt.lower()
    except Exception:
        return False


def list_profiles():

    root = thunderbird_root()
    ini = root / "profiles.ini"

    if not ini.exists():
        return []

    cp = configparser.ConfigParser(interpolation=None)
    cp.read(ini, encoding="utf-8")

    profiles = []

    for section in cp.sections():

        if not section.startswith("Profile"):
            continue

        path = cp[section].get("Path", "")

        if cp[section].get("IsRelative", "1") == "1":
            profile = root / path
        else:
            profile = Path(path)

        if profile.exists():
            profiles.append(profile)

    return profiles

# --------------------------------------------------
# Lecture prefs.js
# --------------------------------------------------

def parse_prefs(prefs_file):

    prefs = {}

    with prefs_file.open(
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        for line in f:

            m = PREF_RE.match(line.strip())

            if m:
                prefs[m.group(1)] = m.group(2)

    return prefs


def build_accounts(prefs):

    accounts = {}

    for key, value in prefs.items():

        if key.startswith("mail.account.account") and key.endswith(".identities"):

            account = key.split(".")[2]
            ids = [i for i in value.split(",") if i]

            accounts[account] = ids

    return accounts

# --------------------------------------------------
# Analyse
# --------------------------------------------------

def analyse_profile(profile):

    prefs_file = profile / "prefs.js"

    if not prefs_file.exists():
        return None

    prefs = parse_prefs(prefs_file)
    accounts = build_accounts(prefs)

    total_ids = sum(len(v) for v in accounts.values())
    changed = []

    for account, ids in accounts.items():

        if len(ids) <= 1:
            continue

        principal = ids[0]
        aliases = ids[1:]

        aliases_sorted = sorted(
            aliases,
            key=lambda i: prefs.get(
                f"mail.identity.{i}.useremail",
                ""
            ).lower()
        )

        if aliases != aliases_sorted:
            changed.append(account)

    return {
        "prefs": prefs,
        "accounts": accounts,
        "boxes": len(accounts),
        "identities": total_ids,
        "changed": changed,
    }

# --------------------------------------------------
# Sauvegarde
# --------------------------------------------------

def backup_prefs(prefs_file):

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup = prefs_file.with_name(
        f"prefs.js.bak_{stamp}"
    )

    shutil.copy2(prefs_file, backup)

    return backup

# --------------------------------------------------
# Tri réel
# --------------------------------------------------

def rewrite_accounts(profile):

    prefs_file = profile / "prefs.js"

    result = analyse_profile(profile)

    prefs = result["prefs"]
    accounts = result["accounts"]

    new_accounts = {}

    for account, ids in accounts.items():

        if len(ids) <= 1:
            new_accounts[account] = ids
            continue

        principal = ids[0]

        aliases = sorted(
            ids[1:],
            key=lambda i: prefs.get(
                f"mail.identity.{i}.useremail",
                ""
            ).lower()
        )

        new_accounts[account] = [principal] + aliases

    backup = backup_prefs(prefs_file)

    lines = prefs_file.read_text(
        encoding="utf-8",
        errors="ignore"
    ).splitlines(True)

    out = []

    for line in lines:

        m = IDENTITY_LINE_RE.match(line)

        if m:

            account = m.group(2)

            if account in new_accounts:

                out.append(
                    f'{m.group(1)}{",".join(new_accounts[account])}{m.group(4)}\n'
                )

                continue

        out.append(line)

    prefs_file.write_text(
        "".join(out),
        encoding="utf-8"
    )

    return backup
    
    # --------------------------------------------------
# Interface graphique
# --------------------------------------------------

class TriAliasTBGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("TriAliasTB v1.0.4 - Al1 Outils")
        self.root.resizable(False, False)

        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(100, lambda: self.root.attributes("-topmost", False))
        self.root.focus_force()

        try:
            self.root.iconbitmap("TriAliasTB.ico")
        except Exception:
            pass


        self.profiles = list_profiles()
        self.current_profile = None

        self.build_ui()
        self.load_profiles()
        self.update_thunderbird_state()

    def build_ui(self):

        top = ttk.Frame(self.root, padding=10)
        top.grid(sticky="nsew")

        state_frame = ttk.Frame(top)
        state_frame.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.state_canvas = tk.Canvas(state_frame, width=16, height=16, highlightthickness=0)
        self.state_canvas.pack(side="left", padx=(0, 6))

        self.state_light = self.state_canvas.create_oval(2, 2, 14, 14, fill="gray", outline="black")

        self.state_label = ttk.Label(state_frame, text="")
        self.state_label.pack(side="left")

        self.profile_list = tk.Listbox(top, width=36, height=8)
        self.profile_list.grid(row=1, column=0, rowspan=4, sticky="ns")
        self.profile_list.bind("<<ListboxSelect>>", self.on_select)

        info = ttk.Frame(top)
        info.grid(row=1, column=1, padx=(12, 0), sticky="nw")

        self.profile_name = ttk.Label(info, text="Profil :")
        self.profile_name.grid(sticky="w")

        self.profile_boxes = ttk.Label(info, text="Boîtes mail :")
        self.profile_boxes.grid(sticky="w")

        self.profile_ids = ttk.Label(info, text="Identités :")
        self.profile_ids.grid(sticky="w")

        self.profile_changed = ttk.Label(info, text="Boîtes à trier :")
        self.profile_changed.grid(sticky="w")

        ttk.Label(info, text="Chemin du profil :").grid(sticky="w", pady=(10, 0))

        self.path_var = tk.StringVar()

        self.path_entry = ttk.Entry(
            info,
            textvariable=self.path_var,
            width=52,
            state="readonly"
        )
        self.path_entry.grid(sticky="we")

        self.log = scrolledtext.ScrolledText(
            top,
            width=70,
            height=10,
            state="disabled"
        )
        self.log.grid(row=5, column=0, columnspan=2, pady=10)

        buttons = ttk.Frame(top)
        buttons.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.sort_button = ttk.Button(
            buttons,
            text=T["sort"],
            command=self.do_sort
        )
        self.sort_button.pack(side="left")

        ttk.Button(
            buttons,
            text=T["open"],
            command=self.open_folder
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons,
            text=T["quit"],
            command=self.root.destroy
        ).pack(side="right")

    def write_log(self, text):

        self.log.configure(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def load_profiles(self):

        self.profile_list.delete(0, "end")

        for p in self.profiles:
            self.profile_list.insert("end", p.name)

        if self.profiles:
            self.profile_list.selection_set(0)
            self.on_select()

    def update_thunderbird_state(self):
        running=thunderbird_running()
        if running:
            self.state_canvas.itemconfig(self.state_light,fill="red")
            self.state_label.config(text="Tri impossible — fermez d'abord Thunderbird.")
            self.sort_button.config(state="disabled")
        else:
            self.state_canvas.itemconfig(self.state_light,fill="green")
            self.state_label.config(text="Tri possible — Thunderbird est fermé.")
            self.sort_button.config(state="normal")
        self.root.after(2000,self.update_thunderbird_state)

    def on_select(self, event=None):

        self.update_thunderbird_state()

        sel = self.profile_list.curselection()

        if not sel:
            return

        self.current_profile = self.profiles[sel[0]]

        self.refresh_current()

    def refresh_current(self):

        if not self.current_profile:
            return

        result = analyse_profile(self.current_profile)

        if result is None:
            return

        self.profile_name.config(
            text=f"Profil : {self.current_profile.name}"
        )

        self.profile_boxes.config(
            text=f"Boîtes mail : {result['boxes']}"
        )

        self.profile_ids.config(
            text=f"Identités : {result['identities']}"
        )

        self.profile_changed.config(
            text=f"Boîtes à trier : {len(result['changed'])}"
        )

        self.path_var.set(str(self.current_profile))

    def open_folder(self):

        if self.current_profile:
            os.startfile(self.current_profile)

    def do_sort(self):

        self.update_thunderbird_state()

        if thunderbird_running():

            messagebox.showwarning(
                "Thunderbird ouvert",
                "Fermez Thunderbird avant de lancer le tri."
            )

            return

        if not self.current_profile:
            return

        result=analyse_profile(self.current_profile)
        if result and len(result["changed"])==0:
            messagebox.showinfo("Information","Rien à trier. Tous les alias sont déjà dans l'ordre.")
            return

        if not messagebox.askyesno(
            "Confirmation",
            T["confirm"]
        ):
            return

        backup = rewrite_accounts(self.current_profile)

        self.write_log(f"Profil : {self.current_profile.name}")
        self.write_log(f"Sauvegarde : {backup.name}")
        self.write_log("Tri terminé.\n")

        self.refresh_current()

        messagebox.showinfo(
            "Terminé",
            "Les alias ont été triés avec succès."
        )


# --------------------------------------------------
# Premier lancement
# --------------------------------------------------

def app_folder():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

def ensure_first_run():
    ini=app_folder()/"TriAliasTB.ini"
    cp=configparser.ConfigParser()
    if ini.exists():
        cp.read(ini,encoding="utf-8")
        if cp.has_section("General") and cp.get("General","ShortcutPrompted",fallback="0")=="1":
            return
    if messagebox.askyesno("Premier lancement","Créer un raccourci sur le Bureau ?"):
        try:
            from win32com.client import Dispatch
            desktop=Path.home()/"Desktop"
            link=Dispatch("WScript.Shell").CreateShortCut(str(desktop/"TriAliasTB.lnk"))
            exe=app_folder()/ "TriAliasTB.exe"
            target=exe if exe.exists() else Path(sys.executable if getattr(sys,"frozen",False) else __file__)
            link.TargetPath=str(target)
            ico=app_folder()/ "TriAliasTB.ico"
            if ico.exists():
                link.IconLocation=str(ico)
            link.WorkingDirectory=str(app_folder())
            link.save()
        except Exception:
            pass
    cp["General"]={"ShortcutPrompted":"1"}
    with ini.open("w",encoding="utf-8") as f:
        cp.write(f)


# --------------------------------------------------
# Programme principal
# --------------------------------------------------

def main():

    root = tk.Tk()

    ensure_first_run()
    TriAliasTBGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()