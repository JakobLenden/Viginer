import tkinter as tk
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
    """Berechnet das neue Zeichen basierend auf dem Schlüsselzeichen."""
    verschiebe_zahl = ord(schluessel_zeichen) - ord('A')
    zahl = ord(zeichen)
    neue_zahl = zahl + verschiebe_zahl
    
    if neue_zahl > ord('Z'):
        neue_zahl -= 26
        
    return chr(neue_zahl)

def verschluesseln():
    """Hauptfunktion für den Button-Klick."""
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
            # Nur Buchstaben verschlüsseln
            schluessel_zeichen = schluessel[zaehler % laenge_schluessel]
            verschluesseltes_zeichen = verschiebung(s, schluessel_zeichen)
            ergebnis += verschluesseltes_zeichen
            zaehler += 1
        else:
            # Leerzeichen/Sonderzeichen einfach übernehmen
            ergebnis += s
    
    # Ergebnis im Label anzeigen
    label_ergebnis.config(text=f"Verschlüsselt: {ergebnis}", fg="green")

#  GUI Setup 

root = tk.Tk()
root.title("Vigenère Verschlüsselung")
root.geometry("500x300")

# Widgets
tk.Label(root, text="Klartext:").pack(pady=5)
entry_klartext = tk.Entry(root)
entry_klartext.pack(pady=5)

tk.Label(root, text="Schlüssel:").pack(pady=5)
entry_schluessel = tk.Entry(root)
entry_schluessel.pack(pady=5)

btn_start = tk.Button(root, text="Verschlüsseln", command=verschluesseln, bg="lightblue")
btn_start.pack(pady=20)

label_ergebnis = tk.Label(root, text="", font=("Courier", 12, "bold"))
label_ergebnis.pack(pady=10)
btn_copy = tk.Button(root, text="In Zwischenablage kopieren", command=in_zwischenablage_kopieren)
btn_copy.pack(pady=5)

root.mainloop()