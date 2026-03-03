import customtkinter as ctk
from tkinter import messagebox

# Logik-Funktionen 

def in_zwischenablage_kopieren():
    # Wir holen uns den Text aus dem Label (wir müssen den Präfix abschneiden)
    ergebnis_text = label_ergebnis.cget("text").replace("Verschlüsselt: ", "")
    
    if ergebnis_text:
        root.clipboard_clear()  # Zwischenablage leeren
        root.clipboard_append(ergebnis_text)  # Text hinzufügen
        messagebox.showinfo("Kopiert", "Verschlüsselter Text wurde in die Zwischenablage kopiert!")
    else:
        messagebox.showwarning("Fehler", "Kein Text zum Kopieren vorhanden!")

def verschiebung(zeichen, schluessel_zeichen):

    verschiebe_zahl = ord(schluessel_zeichen) - ord('A')
    zahl = ord(zeichen)
    neue_zahl = zahl - verschiebe_zahl
    
    if neue_zahl < ord('A'):
        neue_zahl += 26
        
    return chr(neue_zahl)

def verschluesseln():

    klartext = entry_klartext.get().upper()
    schluessel = entry_schluessel.get().upper()
    
    if not klartext or not schluessel:
        messagebox.showwarning("Fehlende Eingabe", "Bitte Klartext und Schlüssel eingeben!")
        return

    ergebnis = ""
    zaehler = 0
    laenge_schluessel = len(schluessel)

    for s in klartext:
        if 'A' <= s <= 'Z':
            schluessel_zeichen = schluessel[zaehler % laenge_schluessel]
            verschluesseltes_zeichen = verschiebung(s, schluessel_zeichen)
            ergebnis += verschluesseltes_zeichen
            zaehler += 1
        else:
            ergebnis += s
    
    # Ergebnis im Label anzeigen
    label_ergebnis.configure(text=f"Verschlüsselt: {ergebnis}", text_color="white")


def check_eingabe(event):
    # Wir prüfen, ob etwas im Feld steht
    if entry_klartext.get().strip():
        # Wenn Text vorhanden ist -> Hintergrund hellblau (oder jede andere Farbe)
        entry_klartext.configure(fg_color="#0b6f2e", border_color="#08461b")
    else:
        # Wenn leer -> Zurück zum Standard (Dunkelgrau/Grau)
        entry_klartext.configure(fg_color=None, border_color=None)

def check_eingabes(event):
    # Wir prüfen, ob etwas im Feld steht
    if entry_schluessel.get().strip():
        # Wenn Text vorhanden ist -> Hintergrund hellblau (oder jede andere Farbe)
        entry_schluessel.configure(fg_color="#0b6f2e", border_color="#08461b")
    else:
        # Wenn leer -> Zurück zum Standard (Dunkelgrau/Grau)
        entry_schluessel.configure(fg_color=None, border_color=None)

def pruefe_eingabe(event=None):
    # Wir holen den Inhalt beider Felder
    text_klar = entry_klartext.get().strip()
    text_key = entry_schluessel.get().strip()
    
    # Prüfen, ob beide Felder nicht leer sind
    if text_klar and text_key:
        # Button wird grün, wenn alles bereit ist
        button.configure(fg_color="#225124", hover_color="#45a049") 
    else:
        # Zurück zur Standardfarbe (meist blau in CTK)
        button.configure(fg_color=["#212121", "#212122"], hover_color=["#101111", "#0F0F0F"])

#  GUI Setup 

root = ctk.CTk()
root.title("Vigenère Verschlüsselung")
root.geometry("500x300")
ctk.set_appearance_mode("dark")  # "dark" oder "light"

# Widgets

ctk.CTkLabel(root, text="Geheimtext:", corner_radius=40).pack(pady=5)
entry_klartext = ctk.CTkEntry(root)
entry_klartext.pack(pady=5)
entry_klartext.bind("<KeyRelease>", check_eingabe)
entry_klartext.bind("<KeyRelease>", pruefe_eingabe)


ctk.CTkLabel(root, text="Schlüssel:", corner_radius=40).pack(pady=5)
entry_schluessel = ctk.CTkEntry(root)
entry_schluessel.pack(pady=5)
entry_schluessel.bind("<KeyRelease>", check_eingabes)
entry_schluessel.bind("<KeyRelease>", pruefe_eingabe)

button = ctk.CTkButton(root, text="Entschlüsseln", command=verschluesseln, fg_color=["#212121", "#212122"], hover_color=["#101111", "#0F0F0F"], text_color="white", corner_radius=40)
button.pack(pady=20)


label_ergebnis = ctk.CTkLabel(root, text="", font=("Courier", 15, "bold"))
label_ergebnis.pack(pady=10)
btn_copy = ctk.CTkButton(root, text="In Zwischenablage kopieren", command=in_zwischenablage_kopieren, fg_color="#0532BA", hover_color="#191d6a", text_color="white", corner_radius=40)
btn_copy.pack(pady=5)

root.mainloop() 