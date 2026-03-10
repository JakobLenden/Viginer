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
    neue_zahl = zahl + verschiebe_zahl
    
    if neue_zahl > ord('Z'):
        neue_zahl -= 26
        
    return chr(neue_zahl)

def verschluesseln():

    klartext = entry_klartext.get("1.0", "end-1c").upper()
    schluessel = entry_schluessel.get().upper()
    
    fehler = False
    if not klartext.strip():
        entry_klartext.configure(fg_color="#8B0000", border_color="#FF0000") # Dunkelrot
        fehler = True
    if not schluessel.strip():
        entry_schluessel.configure(fg_color="#8B0000", border_color="#FF0000")
        fehler = True

    if fehler:
        messagebox.showwarning("Fehlende Eingabe", "Bitte fülle die rot markierten Felder aus!")
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


def check_eingabe(event=None):
    # WICHTIG: Da es eine Textbox ist, brauchen wir Start- und Endparameter
    inhalt = entry_klartext.get("1.0", "end-1c").strip() 
    if inhalt:
        # Wird sofort GRÜN
        entry_klartext.configure(fg_color="#0b6f2e", border_color="#08461b")
    else:
        # Zurück zu Grau
        entry_klartext.configure(fg_color=["#F9F9FA", "#343638"], border_color=["#979DA2", "#565B5E"])
    pruefe_eingabe()

def check_eingabes(event):
    # 1. Farbe des Schlüsselfelds anpassen
    if entry_schluessel.get().strip():
        # Grün, wenn Text drin ist
        entry_schluessel.configure(fg_color="#0b6f2e", border_color="#08461b")
    else:
        # Zurück auf Standard-Werte (None setzt CTK-Defaults)
        entry_schluessel.configure(fg_color=["#F9F9FA", "#343638"], border_color=["#979DA2", "#565B5E"])
    
    # 2. Direkt prüfen, ob der Haupt-Button grün werden darf
    pruefe_eingabe()

def pruefe_eingabe(event=None):
    # Auch hier: Textbox braucht Parameter, Entry nicht
    text_klar = entry_klartext.get("1.0", "end-1c").strip()
    text_key = entry_schluessel.get().strip()
    
    if text_klar and text_key:
        button.configure(fg_color="#225124", hover_color="#45a049") 
    else:
        button.configure(fg_color=["#212121", "#212122"], hover_color=["#101111", "#0F0F0F"])
#  GUI Setup 

root = ctk.CTk()
root.title("Vigenère Verschlüsselung")
root.geometry("500x300")
ctk.set_appearance_mode("dark")  # "dark" oder "light"

# Widgets

ctk.CTkLabel(root, text="Klartext:", corner_radius=40).pack(pady=5)
entry_klartext = ctk.CTkTextbox(root, height=50)
entry_klartext.pack(pady=5)
entry_klartext.bind("<KeyRelease>", check_eingabe)
entry_klartext.bind("<KeyRelease>", pruefe_eingabe, add="+")


ctk.CTkLabel(root, text="Schlüssel:", corner_radius=40).pack(pady=5)
entry_schluessel = ctk.CTkEntry(root)
entry_schluessel.pack(pady=5)
entry_schluessel.bind("<KeyRelease>", check_eingabes)
entry_schluessel.bind("<KeyRelease>", pruefe_eingabe, add="+")

button = ctk.CTkButton(root, text="Verschlüsseln", command=verschluesseln, fg_color=["#212121", "#212122"], hover_color=["#101111", "#0F0F0F"], text_color="white", corner_radius=40)
button.pack(pady=20)


label_ergebnis = ctk.CTkLabel(root, text="", font=("Courier", 15, "bold"))
label_ergebnis.pack(pady=10)
btn_copy = ctk.CTkButton(root, text="In Zwischenablage kopieren", command=in_zwischenablage_kopieren, fg_color="#0532BA", hover_color="#191d6a", text_color="white", corner_radius=40)
btn_copy.pack(pady=5)

root.mainloop()