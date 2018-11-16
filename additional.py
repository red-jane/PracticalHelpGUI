import numpy as np
import tkinter as tk
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

SCALER_FONT = "Arial 11"
SCALER_BACKGROUND = "#ffbe4f"
SCALER_FOREGROUND = "black"


class Plot:
    """
    A class which represents the plotting app
    """

    def __init__(self):
        """
        (None) Initialise the plotting class
        """
        self.plot = tk.Toplevel()
        self.plot.title("Fern Visualiser")
        self.plot.geometry("1400x1000")
        self.plot.config(bg="white")

        # the figure plot widget
        self.widget = None
        # create title

        # the title header frame
        self.message_frame = tk.Frame(self.plot, height=150, bg="#0c457d")
        self.message_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.N)
        self.message = tk.Message(
            self.message_frame, text="Fern Plotting", width=300
        )
        self.message.config(
            bg="#0ea7b5",
            fg="white",
            font=("Arial", 30, "bold underline"),
            justify=tk.LEFT,
            bd=0,
        )
        self.message.pack(side=tk.TOP, fill=tk.X, pady=30, anchor=tk.N)  # , ipady=20

        # create the sliders' frame
        self.scale_frame = tk.Frame(self.plot, bg="white")
        self.scale_frame.pack(side=tk.LEFT, fill=tk.X, anchor=tk.N, padx=20, pady=20)

        # the scaler for the probability of the first affine transform rule
        self.scaler1 = tk.Scale(
            self.scale_frame,
            from_=1,
            to=100,
            length=200,
            label="P (transform 1): ",
            orient=tk.HORIZONTAL,
        )
        self.scaler1.config(
            font=SCALER_FONT, bg=SCALER_BACKGROUND, fg=SCALER_FOREGROUND
        )
        self.scaler1.set(1)
        self.scaler1.pack(side=tk.TOP, anchor=tk.W, pady=20)

        # the scaler for the probability of the second affine transform rule
        self.scaler2 = tk.Scale(
            self.scale_frame,
            from_=1,
            to=100,
            length=200,
            label="P (transform 2): ",
            orient=tk.HORIZONTAL,
        )
        self.scaler2.config(
            font=SCALER_FONT, bg=SCALER_BACKGROUND, fg=SCALER_FOREGROUND
        )
        self.scaler2.set(85)
        self.scaler2.pack(side=tk.TOP, anchor=tk.W)

        # the scaler for the probability of the third affine transform rule
        self.scaler3 = tk.Scale(
            self.scale_frame,
            from_=1,
            to=100,
            length=200,
            label="P (transform 3): ",
            orient=tk.HORIZONTAL,
        )
        self.scaler3.config(
            font=SCALER_FONT, bg=SCALER_BACKGROUND, fg=SCALER_FOREGROUND
        )
        self.scaler3.set(7)
        self.scaler3.pack(side=tk.TOP, anchor=tk.W, pady=20)

        # the scaler for the probability of the fourth affine transform rule
        self.scaler4 = tk.Scale(
            self.scale_frame,
            from_=1,
            to=100,
            length=200,
            label="P (transform 4): ",
            orient=tk.HORIZONTAL,
        )
        self.scaler4.config(
            font=SCALER_FONT, bg=SCALER_BACKGROUND, fg=SCALER_FOREGROUND
        )
        self.scaler4.set(7)
        self.scaler4.pack(side=tk.TOP, anchor=tk.W)

        # the scaler for the number of iterations for the plot
        self.scaler5 = tk.Scale(
            self.scale_frame,
            from_=10000,
            to=50000,
            length=200,
            label="Number of iterations: ",
            orient=tk.HORIZONTAL,
        )
        self.scaler5.config(
            font=SCALER_FONT, bg=SCALER_BACKGROUND, fg=SCALER_FOREGROUND
        )
        self.scaler5.set(20000)
        self.scaler5.pack(side=tk.TOP, anchor=tk.W, pady=20)

        # the button to activate the plotting
        self.button = tk.Button(
            self.scale_frame, text="Plot", command=self.plot_fractal
        )
        self.button.config(
            font="Arial 13",
            bg="#e8702a",
            fg=SCALER_FOREGROUND,
            relief=tk.GROOVE,
            anchor=tk.N,
            activebackground="#ffb16f",
            activeforeground="white",
        )
        self.button.pack(side=tk.TOP, expand=1, ipadx=7, anchor=tk.N)

        # the string variable to alert users when the plot is being prepared
        self.printing_var = tk.StringVar()
        self.printing = tk.Label(
            self.scale_frame, textvariable=self.printing_var, bg="white"
        )
        self.printing.config(font="Arial 14", pady=5)
        self.printing.pack(side=tk.TOP, fill=tk.X)

        # the option variable to attach to the tk.radiobuttons
        self.option = tk.StringVar()

        # the frame for the radio buttons
        self.radio = tk.Frame(self.plot, bg="white")
        self.radio.pack(side=tk.LEFT, anchor=tk.N)

        # the different fractals for users to choose
        self.choice1 = tk.Radiobutton(
            self.radio, text="Barnsley Fern", variable=self.option, value="Barnsley Fern"
        )
        self.choice1.config(
            bg="#6bd2db", font=SCALER_FONT, command=self.choose, relief=tk.GROOVE
        )
        self.choice1.pack(side=tk.TOP, anchor=tk.W, pady=40, padx=10)

        self.choice2 = tk.Radiobutton(
            self.radio,
            text="Fishbone Fern",
            variable=self.option,
            value="Fishbone Fern",
        )
        self.choice2.config(
            bg="#6bd2db", font=SCALER_FONT, command=self.choose, relief=tk.GROOVE
        )
        self.choice2.pack(side=tk.TOP, anchor=tk.W, pady=40, padx=10)

        self.choice3 = tk.Radiobutton(self.radio, text="Leptosporangiate Fern", variable=self.option, value="Leptosporangiate Fern")
        self.choice3.config(bg='#6bd2db', font=SCALER_FONT, command=self.choose, relief=tk.GROOVE)
        self.choice3.pack(side=tk.TOP, anchor=tk.W, pady=40, padx=10)

        self.choice4 = tk.Radiobutton(self.radio, text="Thelypteridaceae Fern", variable=self.option, value="Thelypteridaceae Fern")
        self.choice4.config(bg='#6bd2db', font=SCALER_FONT, command=self.choose, relief=tk.GROOVE)
        self.choice4.pack(side=tk.TOP, anchor=tk.W, pady=40, padx=10)

    def choose(self):
        """
        (str) Adjust the default settings for scalers and returns the 
        value of the option variable when an user clicks a radio button
        """
        value = self.option.get()
        if value == "Fishbone Fern":
            # set the default values of each slider
            self.scaler1.set(2)
            self.scaler2.set(84)
            self.scaler3.set(7)
            self.scaler4.set(7)
        elif value == "Barnsley Fern":
            self.scaler1.set(1)
            self.scaler2.set(85)
            self.scaler3.set(7)
            self.scaler4.set(7)
        elif value == "Thelypteridaceae Fern":
            self.scaler1.set(1)
            self.scaler2.set(93)
            self.scaler3.set(3)
            self.scaler4.set(3)
        else:
            self.scaler1.set(2)
            self.scaler2.set(84)
            self.scaler3.set(7)
            self.scaler4.set(7)
        return self.option.get()

    def plot_fractal(self):
        """
        (None) Collects the user's choice and plot a fractal accordingly
        """
        shape = self.choose()
        if shape == "Barnsley Fern":
            self.barnsley()
        elif shape == "Thelypteridaceae Fern":
            self.thelypteridaceae()
        elif shape == "Fishbone Fern":
            self.fishbone()
        else:
            self.leptosporangiate()

    def get_values(self):
        """
        (flt, flt, flt, flt, int) Returns a sequence of numbers to be used for the plot
        """
        # get the chosen probabilities given by the user
        # divide by 100 for the probability format(betwwen 0 and 1)
        p1, p2, p3, p4, iteration = (
            self.scaler1.get() / 100,
            self.scaler2.get() / 100,
            self.scaler3.get() / 100,
            self.scaler4.get() / 100,
            self.scaler5.get(),
        )

        # calculate the total for the normalisation
        total = p1 + p2 + p3 + p4

        # normalise the given probabilities to ensure 4 probabilities will add up to 1
        normalised1, normalised2, normalised3, normalised4 = (
            p1 / total,
            p2 / total,
            p3 / total,
            p4 / total,
        )
        return normalised1, normalised2, normalised3, normalised4, iteration

    def barnsley(self):
        """
        (None) Plot the barnsley fractal
        """
        self.printing_var.set("Plotting...")
        # collect the given variables from the user
        input1, input2, input3, input4, iteration = self.get_values()

        # a 1x2 starting matrix
        p = np.matrix([[0], [0]])

        # the rules for 4 affine transformations
        transform1 = lambda p: np.matrix([[0.00, 0.00], [0.00, 0.16]]) * p
        transform2 = lambda p: np.matrix([[0.85, 0.04], [-0.04, 0.85]]) * p + np.matrix([[0.00], [1.60]])
        transform3 = lambda p: np.matrix([[0.20, -0.26], [0.23, 0.22]]) * p + np.matrix([[0.00], [1.60]])
        transform4 = lambda p: np.matrix([[-0.15, 0.28], [0.26, 0.24]]) * p + np.matrix([[0.00], [0.44]])

        # initialise the plot with a matrix of zeros for faster iteration
        pts = np.zeros((iteration, 2))
        # accumulated probabilities
        accumulated = input1 + input2
        second_accumulated = accumulated + input3

        # plot according to given inputs
        for i in range(iteration):
            probability = random.random()
            if probability <= input1:
                p = transform1(p)
            elif probability <= accumulated:
                p = transform2(p)
            elif probability <= second_accumulated:
                p = transform3(p)
            else:  # 0.07
                p = transform4(p)

            # flattern the matrix to be an 1D 1xiteration matrix for plotting
            pts[i] = p.A1

        # if a plot already exist, destroy and create a new one
        if self.widget:
            self.widget.destroy()

        # create a scatter plot
        fig = Figure(figsize=(8, 8))
        a = fig.add_subplot(111)  # 1x1 plot, first subplot
        # s is the size of the scatter point
        a.scatter(*zip(*pts), s=0.5, color="#386b30", label="Barnsley Fern")

        # draws the plot on a tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.plot)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP)
        canvas.draw()

        self.printing_var.set("Done!")

    def fishbone(self):
        """
        (None) Plot the fishbone fractal fern
        """

        self.printing_var.set("Plotting...")

        # collect data
        input1, input2, input3, input4, iteration = self.get_values()

        # starting matrix
        p = np.matrix([[0], [0]])

        # rules
        transform1 = lambda p: np.matrix([[0.00, 0.00], [0.00, 0.25]]) * p + np.matrix([[0.00], [-0.4]])
        transform2 = lambda p: np.matrix([[0.95, 0.002], [-0.002, 0.93]]) * p + np.matrix([[-0.002], [0.5]])
        transform3 = lambda p: np.matrix([[0.035, -0.11], [0.27, 0.01]]) * p + np.matrix([[-0.05], [0.005]])
        transform4 = lambda p: np.matrix([[-0.04, 0.11], [0.27, 0.01]]) * p + np.matrix([[0.047], [0.06]])

        pts = np.zeros((iteration, 2))

        accumulated = input1 + input2
        second_accumulated = accumulated + input3

        for i in range(iteration):
            probability = random.random()
            if probability <= input1:
                p = transform1(p)
            elif probability <= accumulated:
                p = transform2(p)
            elif probability <= second_accumulated:
                p = transform3(p)
            else:  # 0.07
                p = transform4(p)

            # flattern the matrix to be an 1D 1xiteration matrix for plotting
            pts[i] = p.A1

        if self.widget:
            self.widget.destroy()

        fig = Figure(figsize=(8, 8))
        a = fig.add_subplot(111)  # 1x1 plot, first subplot
        a.scatter(*zip(*pts), s=0.5, color="#a36032", label="Fishbone Fern")

        canvas = FigureCanvasTkAgg(fig, master=self.plot)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP)
        canvas.draw()
        self.printing_var.set("Done!")

    def leptosporangiate(self):
        """
        (None) Plot the leptosporangiate fractal fern
        """

        self.printing_var.set("Plotting...")

        # collect data
        input1, input2, input3, input4, iteration = self.get_values()

        # starting matrix
        p = np.matrix([[0], [0]])

        # rules
        transform1 = lambda p: np.matrix([[0.00, 0.00], [0.00, 0.25]]) * p + np.matrix([[0.00], [-0.14]])
        transform2 = lambda p: np.matrix([[0.85, 0.020], [-0.02, 0.83]]) * p + np.matrix([[0.00], [1.0]])
        transform3 = lambda p: np.matrix([[0.09, -0.28], [0.3, 0.11]]) * p + np.matrix([[0.00], [0.6]])
        transform4 = lambda p: np.matrix([[-0.09, 0.28], [0.3, 0.09]]) * p + np.matrix([[0.00], [0.7]])

        pts = np.zeros((iteration, 2))

        accumulated = input1 + input2
        second_accumulated = accumulated + input3

        for i in range(iteration):
            probability = random.random()
            if probability <= input1:
                p = transform1(p)
            elif probability <= accumulated:
                p = transform2(p)
            elif probability <= second_accumulated:
                p = transform3(p)
            else:  # 0.07
                p = transform4(p)

            # flattern the matrix to be an 1D 1xiteration matrix for plotting
            pts[i] = p.A1

        if self.widget:
            self.widget.destroy()

        fig = Figure(figsize=(8, 8))
        a = fig.add_subplot(111)  # 1x1 plot, first subplot
        a.scatter(*zip(*pts), s=0.5, color="#780000", label="Leptosporangiate fern")

        canvas = FigureCanvasTkAgg(fig, master=self.plot)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP)
        canvas.draw()
        self.printing_var.set("Done!")

    def thelypteridaceae(self):
        """
        (None) Plot the thelypteridaceae fractal fern
        """

        self.printing_var.set("Plotting...")

        # collect data
        input1, input2, input3, input4, iteration = self.get_values()

        # starting matrix
        p = np.matrix([[0], [0]])

        # rules
        transform1 = lambda p: np.matrix([[0.00, 0.00], [0.00, 0.25]]) * p + np.matrix([[0.00], [-0.4]])
        transform2 = lambda p: np.matrix([[0.95, 0.005], [-0.005, 0.93]]) * p + np.matrix([[-0.002], [0.5]])
        transform3 = lambda p: np.matrix([[0.035, -0.2], [0.16, 0.04]]) * p + np.matrix([[-0.09], [0.02]])
        transform4 = lambda p: np.matrix([[-0.04, 0.2], [0.16, 0.04]]) * p + np.matrix([[0.083], [0.12]])

        pts = np.zeros((iteration, 2))

        accumulated = input1 + input2
        second_accumulated = accumulated + input3

        for i in range(iteration):
            probability = random.random()
            if probability <= input1:
                p = transform1(p)
            elif probability <= accumulated:
                p = transform2(p)
            elif probability <= second_accumulated:
                p = transform3(p)
            else:  # 0.07
                p = transform4(p)

            # flattern the matrix to be an 1D 1xiteration matrix for plotting
            pts[i] = p.A1

        if self.widget:
            self.widget.destroy()

        fig = Figure(figsize=(8, 8))
        a = fig.add_subplot(111)  # 1x1 plot, first subplot
        a.scatter(*zip(*pts), s=0.5, color="#540d4d", label="Thelypteridaceae Fern")

        canvas = FigureCanvasTkAgg(fig, master=self.plot)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP)
        canvas.draw()
        self.printing_var.set("Done!")