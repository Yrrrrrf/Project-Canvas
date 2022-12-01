import tkinter as tk




class ExampleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, width=512, height=512, cursor="cross")
        self.canvas.pack(fill="both", expand=1)

        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)

    def on_button_press(self, event):
        # find rectangle items under mouse cursor
        items = [x for x in self.canvas.find_withtag("current") if self.canvas.type(x) == "rectangle"]
        if items:
            # item found, use it as the "current" item
            self.start = self.canvas.coords(items[0])[:2]
            self.current = items[0]
        else:
            # no item found, create new "current" rectangle item
            self.start = event.x, event.y
            self.current = self.canvas.create_rectangle(*self.start, *self.start, width=5)

    def on_move_press(self, event):
        # resize the "current" item
        self.canvas.coords(self.current, *self.start, event.x, event.y)

ExampleApp().mainloop()