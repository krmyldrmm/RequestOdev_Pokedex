import requests
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import urllib.request
import io

# WINDOW
window = Tk()
window.minsize(width=1024, height=768)
window.title("Pokédex")
# WINDOW

# BACKGROUND PHOTO
bg = PhotoImage(file='backg.png')
label1 = Label(window, image=bg)
label1.place(x=0,
             y=0,
             relwidth=1,
             relheight=1)
# BACKGROUND PHOTO

# POKEMON NAME LABEL
pokemon_name_label = Label(window,
                           text="Type the name of the pokémon you want to search for in the box below.",
                           font='Futura 20 italic',
                           bg="#456AA2"
                           )
pokemon_name_label.pack()
# POKEMON NAME LABEL

# POKEMON NAME ENTRY
search_pokemon_entry = Entry(window)
search_pokemon_entry.pack(pady=10)
search_pokemon_entry.config(width=30,
                            font='Futura 24',
                            justify=CENTER,
                            highlightbackground="#456AA2")
# POKEMON NAME ENTRY


def button_clicked():
    entry = search_pokemon_entry.get()
    if entry == "":
        messagebox.showerror(title="Error", message="Please enter the box")
    else:
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{entry.lower()}"
            url_species = f"https://pokeapi.co/api/v2/pokemon-species/{entry.lower()}"

            response = requests.get(url)
            response_species = requests.get(url_species)

            image_url = response.json()["sprites"]["other"]["official-artwork"]["front_default"]
            with urllib.request.urlopen(image_url) as u:
                raw_data = u.read()
            # self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
            image = Image.open(io.BytesIO(raw_data))
            image = ImageTk.PhotoImage(image)

            name_label.config(text='Pokemon Name = ' + response.json()["name"],
                              bg="#456AA2", font='Futura 20 bold')
            name_label.place(x=0, y=120)
            type_label.config(text='Pokemon Type = ' + response.json()["types"][0]["type"]["name"],
                              bg="#456AA2", font='Futura 20 bold')
            type_label.place(x=0, y=150)
            if len(response.json()["abilities"]) == 2:
                ability_label.config(text="Ability 1 = " + response.json()["abilities"][0]["ability"]["name"],
                                     bg="#456AA2",
                                     font="Futura 20 bold")
                ability_label.place(x=0, y=180)
                ability_label2.config(text="Ability 2 = " + response.json()["abilities"][1]["ability"]["name"],
                                      bg="#456AA2",
                                      font="Futura 20 bold")
                ability_label2.place(x=0, y=210)
            else:
                ability_label.config(text="Ability = " + response.json()["abilities"][0]["ability"]["name"],
                                     bg="#456AA2",
                                     font="Futura 20 bold")
                ability_label2.place_forget()
                ability_label.place(x=0, y=180)
            if len(response.json()["abilities"]) == 2:
                habitat_label.config(text="Habitat = " + response_species.json()["habitat"]["name"],
                                     bg="#456AA2",
                                     font="Futura 20 bold")
                habitat_label.place(x=0, y=240)
                habitat_label2.place_forget()
            else:
                habitat_label2.config(text="Habitat = " + response_species.json()["habitat"]["name"],
                                      bg="#456AA2",
                                      font="Futura 20 bold", )
                habitat_label2.place(x=0, y=210)
                habitat_label.place_forget()

            image_label.config(image=image, bg="#456AA2")
            image_label.image = image
            image_label.place(x=10, y=300)

        except requests.exceptions.JSONDecodeError:
            messagebox.showerror(title="Error", message="Pokemon not found")

        search_pokemon_entry.delete(0, END)


# POKEMON SEARCH BUTTON
pokemon_search = Button(text="Search",
                        fg="black",
                        highlightbackground="#456AA2",
                        command=button_clicked)
pokemon_search.pack()
# POKEMON SEARCH BUTTON

# LABELS INSIDE FUNCTION
name_label = Label(text="", bg="#456AA2")
name_label.place_forget()

type_label = Label(text="", bg="#456AA2")
type_label.place_forget()

ability_label = Label(text="", bg="#456AA2")
ability_label.place_forget()

ability_label2 = Label(text="", bg="#456AA2")
ability_label2.place_forget()

habitat_label = Label(text="", bg="#456AA2")
habitat_label.place_forget()

habitat_label2 = Label(text="", bg="#456AA2")
habitat_label2.place_forget()

image_label = Label()
image_label.place_forget()
# LABELS INSIDE FUNCTION

search_pokemon_entry.focus_set()

window.mainloop()
