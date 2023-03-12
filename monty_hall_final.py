import random
import tkinter as tk

class MontyHallGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Monty Hall Game")
        self.master.geometry("300x200")
        self.prize_door = random.randint(1, 3)
        self.selected_door = None
        self.opened_door = None
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choose a door:")
        self.label.pack()

        self.door1_button = tk.Button(self.master, text="Door 1\n33.3%", command=lambda: self.select_door(1))
        self.door1_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.door2_button = tk.Button(self.master, text="Door 2\n33.3%", command=lambda: self.select_door(2))
        self.door2_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.door3_button = tk.Button(self.master, text="Door 3\n33.3%", command=lambda: self.select_door(3))
        self.door3_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game, state=tk.DISABLED)

    def select_door(self, door):
        self.selected_door = door
        self.open_door()
        self.door1_button.pack_forget()
        self.door2_button.pack_forget()
        self.door3_button.pack_forget()

    def open_door(self):
        doors = [1, 2, 3]
        doors.remove(self.prize_door)
        if self.selected_door in doors:
            doors.remove(self.selected_door)
        self.opened_door = random.choice(doors)
        self.label.config(text=f"Interesting that you selected door {self.selected_door}.\nJust wanted to let you know that behind door {self.opened_door} is a goat.\nDo you want to switch doors?")

        self.switch_button = tk.Button(self.master, text="Switch\n66.7%", command=self.switch_door)
        self.switch_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.stay_button = tk.Button(self.master, text="Stay\n33.3%", command=self.finish_game)
        self.stay_button.pack(side=tk.LEFT, expand=True, padx=10)

    def switch_door(self):
        doors = [1, 2, 3]
        doors.remove(self.opened_door)
        doors.remove(self.selected_door)
        self.selected_door = doors[0]
        self.finish_game()

    def finish_game(self):
        self.switch_button.pack_forget()
        self.stay_button.pack_forget()
        self.restart_button.pack(side=tk.LEFT, padx=10)
        self.restart_button.config(state=tk.NORMAL)
        if self.selected_door == self.prize_door:
            result = "Congratulations, you won!"
        else:
            result = "Sorry, you lost."
        self.label.config(text=f"The prize was behind door {self.prize_door}.\n{result}")

    def restart_game(self):
        self.prize_door = random.randint(1, 3)
        self.selected_door = None
        self.opened_door = None
        self.label.config(text="Choose a door:")
        self.door1_button.pack(side=tk.LEFT, expand=True, padx=10)
        self.door2_button.pack(side=tk.LEFT, expand=True, padx=10)
        self.door3_button.pack(side=tk.LEFT, expand=True, padx=10)
        self.restart_button.pack_forget()
        self.restart_button.config(state=tk.DISABLED)

root = tk.Tk()
game = MontyHallGame(root)
root.mainloop()
