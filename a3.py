"""
Assignment 3 - Queue
CSSE1001/7030
Semester 2, 2018
"""

import tkinter as tk
import math
from queue import Queue, QueueItem
import time
import additional

__author__ = "Minh Trang Nguyen 45270532"

class QueueApp:
    """
    A class which represents the queue app.
    """

    def __init__(self, master):
        """
        (None) Initialise the queue app
        Parameter:
            master(root): tkinter main root
        """
        self._master = master
        self._model = Model()
        self._view = View(self._master, self._model)
        self._view.pack(expand=1, fill=tk.BOTH)


class Model:
    """
    A class for storing data for the queue app
    """

    def __init__(self):
        """
        (None) Initialise the Model class
        """
        self.long_queue = Queue()
        self.quick_queue = Queue()

class View(tk.Frame):
    """
    A class for viewing the GUI
    """

    def __init__(self, master, model):
        """
        (None) Initialise the View class
        Parameter:
            master(root): the tkinter master frame
            model(Model): the model class for the queue app
        """
        super().__init__(master, bg="white") 
        self._master = master
        self._master.title("CSSE1001 Queue")
        self._master.geometry("1300x1000")
        self._model = model

        # string variable for the 2 table header displpaying "average wait time"
        self.left_table_header = tk.StringVar()
        self.right_table_header = tk.StringVar()

        # create the menu bar to switch to the additional feature
        self.create_menu_bar(self._master)

        # the important notice bar on top
        self.create_notice_bar(self._master)
        
        # left frame which contains widgets supporting the quick hep functionality
        self._left_frame = tk.Frame(master, bg="white")
        self._left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.create_left_frame(self._left_frame)
        # left table header
        self.create_table(self._left_frame)

        # right frame which contains widgets supporting the long hep functionality
        self._right_frame = tk.Frame(master, bg="white")
        self._right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.create_right_frame(self._right_frame)
        self.create_table(self._right_frame)

        # warning label for the popup 
        self.warning_label = tk.StringVar()

        # frame for the students entry
        self.left_entry_frame = tk.Frame(self._left_frame, bg="white")
        self.left_entry_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.right_entry_frame = tk.Frame(self._right_frame, bg="white")
        self.right_entry_frame.pack(side=tk.TOP, fill=tk.BOTH)


    def create_menu_bar(self, frame):
        """
        (None) The method to create the menubar
        Parameter:
            frame(tk.Frame): the frame to pack the menubar
        """
        menubar = tk.Menu(frame)
        frame.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="SWITCH TO PLOTTING", menu=filemenu)
        filemenu.add_command(label="Open Fern Visualiser", font="Arial 11", command=self.visualise)

    def visualise(self):
        """
        (None) Opens the additional plotting app
        """
        plot_fractal = additional.Plot()

    def create_notice_bar(self, frame):
        """
        (None) The method to create the notice bar
        Parameter: 
            frame(tk.Frame): the tk Frame to pack the notice bar
        """
        self.notice_bar_frame = tk.Frame(frame, height=7, bg="#FEFCEC")
        self.notice_bar_frame.pack(side=tk.TOP, fill=tk.X)

        notice_bar = tk.Text(self.notice_bar_frame, height=7, width=200, bd=0)
        notice_bar.config(bg="#FEFCEC", wrap=tk.WORD, padx=25)
        notice_bar.pack()
        notice_bar.insert(tk.INSERT, "Important\n")

        notice = (
            f"Individual assessment items must be solely your own work. "
            f"While students are encouraged to have high-level conversations about the problems "
            f"they are trying to solve, you must not look at another student's code or copy. "
            f"from it. The university uses sophisticated anti-collusion measures to automatically "
            f"detect similarity between assignment submissions."
        )

        notice_bar.insert("2.0", notice)
        notice_bar.tag_add("bold", "1.0", "2.0")
        notice_bar.tag_config(
            "bold", font="Arial 14 bold", foreground="#C5994F", spacing3=8, spacing1=20
        )
        notice_bar.tag_add("paragraph", "2.0", tk.END)
        notice_bar.tag_config("paragraph", font="Arial 10", justify=tk.LEFT)
        notice_bar.config(state=tk.DISABLED)

    def create_left_frame(self, frame):
        """
        (None) The method to create the quick help frame and its widgets
        Parameter:
            frame(tk.Frame): the frame to pack the left frame in
        """
        short_question = tk.Text(frame, height=1.5, width=60, bd=0)
        short_question.config(spacing1=10, spacing2=30, bg="#DBF3D6")
        short_question.pack(
            side=tk.TOP, padx=25, pady=25, anchor=tk.N, ipadx=30, ipady=30
        )
        short_question.insert("1.0", "Quick Questions\n\n")
        short_question.tag_add("big", "1.0", "1.15")
        short_question.tag_config(
            "big", font="Arial 20 bold", foreground="#1F7B38", justify=tk.CENTER
        )
        short_question.insert("3.0", "< 2 mins with a tutor")
        short_question.tag_add("small", "1.15", tk.END)
        short_question.tag_config(
            "small", font="Arial 11 italic", foreground="grey", justify=tk.CENTER
        )
        short_question.config(state=tk.DISABLED)

        # Create left message widget 
        bullet_point = "\u2022"
        message1 = (
            f"Some example of quick questions:\n\n"
            f"  {bullet_point} Syntax errors\n\n"
            f"  {bullet_point} Interpreting error output\n\n"
            f"  {bullet_point} Assignment/MyPyTutor interpretation\n\n"
            f"  {bullet_point} MyPyTutor submission issues\n"
        )
        quick_message = tk.Message(frame, text=message1, bg="white")
        quick_message.config(font="Arial 11", padx=20, pady=20)
        quick_message.pack(side=tk.TOP, anchor=tk.W)

        # button frame
        left_button_frame = tk.Frame(frame, bg="#3BB653")
        left_button_frame.pack()

        # the button which when pressed opens the quick popup toplevel
        self.quick_button = tk.Button(left_button_frame, text="Request Quick Help")
        self.quick_button.config(
            bg="#9CD2A3",
            fg="white",
            justify=tk.CENTER,
            padx=3,
            pady=3,
            font="Arial 11",
            bd=4,
            relief=tk.FLAT,
            activebackground="#3BB653",
            activeforeground="white",
            command=self.create_quick_popup,
        )
        self.quick_button.pack(side=tk.TOP, anchor=tk.N, padx=3, pady=3)

        # create the students queue frame
        self.left_table_header.set("No students in queue")
        queue_header_quick_frame = tk.Frame(frame, bg="#EFF0F0", pady=3)
        queue_header_quick_frame.pack(fill=tk.BOTH, anchor=tk.N, padx=25, pady=15)
        queue_header_left = tk.Label(
            queue_header_quick_frame, textvariable=self.left_table_header, bg="white"
        )
        queue_header_left.config(justify=tk.LEFT, pady=10, anchor=tk.W, font="Arial 11")
        queue_header_left.pack(
            side=tk.TOP, anchor=tk.W, fill=tk.X, expand=1, ipadx=8, ipady=8
        )

    def create_right_frame(self, frame):
        """
        (None) The method to create the long help frame and its widgets
        Parameter:
            frame(tk.Frame): the frame to pack the right frame in
        """
        # create the long question text widget on the right
        long_question = tk.Text(frame, height=1.5, width=60, bd=0)
        long_question.config(spacing1=10, spacing2=30, bg="#D5EDF9")
        long_question.pack(
            side=tk.TOP, padx=25, pady=25, anchor=tk.N, ipadx=30, ipady=30
        )
        long_question.insert("1.0", "Long Questions\n\n")
        long_question.tag_add("big", "1.0", "1.15")
        long_question.tag_config(
            "big", font="Arial 20 bold", foreground="#186F93", justify=tk.CENTER
        )
        long_question.insert("3.0", "> 2 mins with a tutor")
        long_question.tag_add("small", "1.15", tk.END)
        long_question.tag_config(
            "small", font="Arial 11 italic", foreground="grey", justify=tk.CENTER
        )
        long_question.config(state=tk.DISABLED)

        # create right message widget
        bullet_point = "\u2022"
        message2 = (
            f"Some example of long questions:\n\n"
            f"  {bullet_point} Open ended questions\n\n"
            f"  {bullet_point} How to start a problem\n\n"
            f"  {bullet_point} How to improve code\n\n"
            f"  {bullet_point} Debugging\n\n"
            f"  {bullet_point} Assignment help\n"
        )
        long_message = tk.Message(frame, text=message2, bg="white")
        long_message.config(font="Arial 11", padx=20, pady=20)
        long_message.pack(side=tk.TOP, anchor=tk.W)

        # create 2 button frames for button border
        right_button_frame = tk.Frame(frame, bg="#31C0E2")
        right_button_frame.pack()

        # create Request Long Help button
        long_button = tk.Button(right_button_frame, text="Request Long Help")
        long_button.config(
            bg="#9DD7EA",
            fg="white",
            justify=tk.CENTER,
            padx=3,
            pady=3,
            font="Arial 11",
            bd=4,
            relief=tk.FLAT,
            activebackground="#31C0E2",
            activeforeground="white",
            command=self.create_long_popup,
        )
        long_button.pack(side=tk.TOP, anchor=tk.N, padx=3, pady=3)

        queue_header_long_frame = tk.Frame(frame, bg="#EFF0F0", pady=3)
        queue_header_long_frame.pack(fill=tk.BOTH, padx=25, pady=15, anchor=tk.N)

        # create students queue label displaying "average time"
        queue_header_right = tk.Label(
            queue_header_long_frame, textvariable=self.right_table_header, bg="white"
        )
        queue_header_right.config(
            justify=tk.LEFT, pady=10, anchor=tk.W, font="Arial 11"
        )
        queue_header_right.pack(
            side=tk.TOP, anchor=tk.W, fill=tk.X, expand=1, ipadx=8, ipady=9
        )
        self.right_table_header.set("No students in queue")

    def create_table(self, frame):
        """
        (None) The method to create the table header for the students' queue
        Parameter:
            frame(tk.Frame): main frame for the table
        """
        self.table_header = tk.Frame(frame, bg="white")
        self.table_header.pack(side=tk.TOP, fill=tk.X, anchor=tk.N, padx=25)

        # table labels : #, name, number of question, time
        num_text = tk.Label(self.table_header, text="#    ", bg="white")
        num_text.config(font="Arial 12 bold", justify=tk.LEFT)
        num_text.pack(side=tk.LEFT, anchor=tk.W, ipadx=3, ipady=3)

        name_text = tk.Label(self.table_header, text="Name\t\t", bg="white")
        name_text.config(font="Arial 12 bold", justify=tk.LEFT, anchor=tk.W)
        name_text.pack(side=tk.LEFT, ipadx=3, ipady=3)

        question_col = tk.Label(self.table_header, text="Questions Asked\t", bg="white")
        question_col.config(font="Arial 12 bold", justify=tk.LEFT, anchor=tk.W)
        question_col.pack(side=tk.LEFT, ipadx=3, ipady=3)

        time_col = tk.Label(self.table_header, text="Time")
        time_col.config(font="Arial 12 bold", justify=tk.LEFT, bg="white")
        time_col.pack(side=tk.LEFT, ipadx=3, ipady=3, anchor=tk.W)

        line_frame = tk.Frame(frame, bg="#EFF0F0", height=3)
        line_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.N, padx=25, pady=5)

    def create_long_popup(self):
        """
        (None) Create the popup window for students requesting long help
        """
        prompt = tk.Toplevel()
        prompt.title("Student Name")
        prompt.geometry("500x100")
        prompt.resizable(0, 0)  # disable resizing
        prompt.config(bg="white", relief=tk.FLAT)

        # the entry variable to collect the student's input
        self.long_entry_var = tk.StringVar()

        inner_frame = tk.Frame(prompt)
        inner_frame.pack(side=tk.TOP)
        name_label = tk.Label(inner_frame, text="Please enter your name: ", bg="white")
        name_label.config(font="Arial 13")
        name_label.pack(side=tk.LEFT, anchor=tk.W)
        # create the entry widget for user input
        user_name = tk.Entry(inner_frame, bg="white", font="Arial 13", width="40")
        user_name.config(textvariable=self.long_entry_var)
        user_name.pack(side=tk.RIGHT)

        # the button which sends data to the model 
        ok_button = tk.Button(prompt, text="Submit")
        ok_button.config(
            bg="#186F93",
            fg="white",
            justify=tk.CENTER,
            padx=5,
            pady=5,
            font="Arial 10",
            bd=4,
            relief=tk.GROOVE,
            activebackground="gray",
            activeforeground="white",
            command=lambda: self.submit_data(
                prompt,
                self._model.long_queue,
                self.long_entry_var,
                self.right_entry_frame,
                self._model.quick_queue,
                self.right_table_header
            ),
        )
        ok_button.pack(side=tk.BOTTOM, fill=tk.X)
        # tk label to display the warning label when needed
        warning = tk.Label(prompt, textvariable=self.warning_label, justify=tk.CENTER)
        warning.config(font="Arial 11", bg="white")
        warning.pack(side=tk.BOTTOM, fill=tk.X)
        self.warning_label.set("")

    def create_quick_popup(self):
        """
        (None) Create the popup window
        """
        prompt = tk.Toplevel()
        prompt.title("Student Name")
        prompt.geometry("500x100")
        prompt.resizable(0, 0)  # disable resizing
        prompt.config(bg="white", relief=tk.FLAT)
        self.quick_entry_var = tk.StringVar()
        inner_frame = tk.Frame(prompt)
        inner_frame.pack(side=tk.TOP)
        name_label = tk.Label(inner_frame, text="Please enter your name: ", bg="white")
        name_label.config(font="Arial 13")
        name_label.pack(side=tk.LEFT, anchor=tk.W)
        # create the entry widget for user input
        user_name = tk.Entry(inner_frame, bg="white", font="Arial 13", width="40")
        user_name.config(textvariable=self.quick_entry_var)
        user_name.pack(side=tk.RIGHT)

        ok_button = tk.Button(prompt, text="Submit")
        ok_button.config(
            bg="#186F93",
            fg="white",
            justify=tk.CENTER,
            padx=5,
            pady=5,
            font="Arial 10",
            bd=4,
            relief=tk.GROOVE,
            activebackground="gray",
            activeforeground="white",
            command=lambda: self.submit_data(
                prompt,
                self._model.quick_queue,
                self.quick_entry_var,
                self.left_entry_frame,
                self._model.long_queue,
                self.left_table_header
            )
        )
        ok_button.pack(side=tk.BOTTOM, fill=tk.X)
        self.warning_label.set("")
        warning = tk.Label(prompt, textvariable=self.warning_label, justify=tk.CENTER)
        warning.config(font="Arial 11", bg="white")
        warning.pack(side=tk.BOTTOM, fill=tk.X)

    def create_entry(self, frame, left_num_var, left_name_var, left_question_var, left_time_var):
        """
        (None) Create the table entry for each student
        Parameter:
            frame(tk.Frame): the frame to pack the entry in
            left_num_var(int): the nth student in the queue
            left_name_var(str): the name of the student
            left_question_var(int): the number of questions the student has asked since opening the app
            left_time_var(str): the time the students have been in the queue approximately (string format)
        """
        table_entry = tk.Frame(frame, bg="white", height=3)
        table_entry.pack(side=tk.TOP, fill=tk.X, padx=25, anchor=tk.N)

        person_num = tk.Label(table_entry, text=left_num_var, bg="white", width=3)
        person_num.config(font="Arial 11", justify=tk.LEFT, anchor=tk.W)
        person_num.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W)

        person_name = tk.Label(table_entry, text=left_name_var, bg="white")
        person_name.config(font="Arial 11", justify=tk.LEFT, anchor=tk.W, width=20)
        person_name.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W)

        person_question = tk.Label(table_entry, text=left_question_var, bg="white")
        person_question.config(font="Arial 11", justify=tk.LEFT, anchor=tk.W, width=10)
        person_question.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W)

        person_time = tk.Label(table_entry, text=left_time_var, bg="white")
        person_time.config(font="Arial 11", justify=tk.LEFT)
        person_time.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W, expand=1)

        # the cancel button
        no_button = tk.Button(table_entry, bg="#F6A5A3", relief=tk.GROOVE)
        no_button.config(
            padx=3, width=2, command=lambda: self.cancel_frame(person_name))
        no_button.pack(side=tk.LEFT)

        # the accept button
        yes_button = tk.Button(table_entry, bg="#DBF3D6", relief=tk.GROOVE)
        yes_button.config(
            padx=3, width=2, command=lambda: self.accept_frame(person_name))
        yes_button.pack(side=tk.LEFT)

    def clear_entry(self, frame):
        """
        (None) Clears the children widgets within the given frame
        Parameter:
            frame(tk.Frame): to frame to clear widgets
        """
        list_widgets = frame.pack_slaves()
        for w in list_widgets:
            w.destroy()

    def cancel_frame(self, label):
        """
        (None) Remove a specific student who no longer requires help from the active queue 
        Parameter:
            label(tk.Label): the label which contains the student's name to remove
        """
        # get the students name which stored in the "text" config of the label
        canceled_student = label.cget("text")
        # find whether the students were in the short queue or the long queue and remove them
        if canceled_student in [item.name for item in self._model.long_queue.items]:
            self._model.long_queue.remove_item(canceled_student)
        else:
            self._model.quick_queue.remove_item(canceled_student)

    def accept_frame(self, label):
        """
        (None) Accept a student and increment by 1 the number of question they have asked
        and remove the student from the current active queue
        Parameter:
            label(tk.Label): the label which contains the student's name to remove and to
            update
        """
        accepted_student = label.cget("text")
        if accepted_student in [item.name for item in self._model.long_queue.items]:
            # increment the student's number of question by one 
            self._model.long_queue.database[accepted_student] += 1
            # remove the students from the current active queue
            self._model.long_queue.remove_item(accepted_student)
        else:
            self._model.quick_queue.database[accepted_student] += 1
            self._model.quick_queue.remove_item(accepted_student)


    def update_times(self, start_time):
        """
        (str) Returns the approximate waiting time for the students
        Parameter:
            start_time(float): The recorded start_time given by the time module
        """
        timestamp = time.time() - start_time
        value = math.floor(timestamp / 60)
        if timestamp < 60:
            return "a few seconds ago"
        elif timestamp < 120:
            return "a minute ago"
        elif timestamp < 3600:
            return f"{value} minutes ago"
        elif timestamp < 7200:
            return "1 hour ago"
        else:
            return f"{value} hours ago"

    def set_average_queue(self, variable, queue):
        """
        (None) Refresh the average wait time label and update the students' waiting time
        Parameter:
            variable(tk.StringVar): the string variable to set to the updated value
            queue(Queue): the student's queue to update the average wait time
        """
        # check if anyone is in the active queue
        if queue.items == []:
            variable.set("No students in queue.")
        else:
            avg_time = queue.get_avg_wait_time()
            if avg_time < 60:
                variable.set(f"An average wait time of about a few seconds for {len(queue.items)} students")
            elif avg_time < 120:
                variable.set(f"An average wait time of about {1} minute for {len(queue.items)} students")
            elif avg_time < 3600:
                avg_time = math.floor(avg_time/60)
                variable.set(f"An average wait time of about {avg_time} minutes for {len(queue.items)} students")
            elif avg_time < 7200:
                variable.set(f"An average wait time of about {1} hour for {len(queue.items)} students")
            else:
                avg_time = math.floor(avg_time/60)
                variable.set(f"An average wait time of about {avg_time} hours for {len(queue.items)} students")
        # checking the queue time every few seconds 
        self._master.after(7000, lambda: self.set_average_queue(variable, queue))

    def submit_data(self, prompt, queue, entry_var, frame, other, variable):
        """
        (None) Add the student's name to the main GUI queue
        Parameter:
            prompt(tk.Toplevel): the popup to close
            queue(Queue): the student's queue to add the students to
            entry_var(tk.StringVar): the student's input saved in a tk string variable
            frame(tk.Frame): the frame to pack the students entry widget in
            other(Queue): the other students queue on the main GUI 
            to check if the student's already requested help in the other queue
            variable(tk.StringVar): the tk string variable to update
        """
        # check if the student is addded successfully to the data list
        is_added = queue.add_item(QueueItem(entry_var.get()), other)
        # if added, update the main GUI with the students info
        if is_added:
            self.update_entries(frame, queue, variable)
            # close the popup
            prompt.destroy()
        else:
            # otherwise, display the warning if the student's not added
            self.warning_label.set("You already requested help!")

    def update_entries(self, frame, queue, variable):
        """
        (None) Refresh the students queue according to the data from the queue list
        Parameter:
            frame(tk.Frame): the frame to pack the new entries 
            queue(Queue): the queue (short/long) to add the new entries in
            variable(tk.StringVar): the "average wait time" string variable to update
        """
        # clear the children widgets in frame
        self.clear_entry(frame)
        for row, item in enumerate(queue.items, 1):
            # update the average wait time according to the info from the queue
            self.set_average_queue(variable, queue)
            # get the updated time
            updated_time = self.update_times(item.time)
            # create the entry with the student's information from the Queue database
            self.create_entry(
                frame, row, item.name, queue.database[item.name], updated_time
            )
        # keep updating the table with new info every few seconds 
        self._master.after(7000, lambda: self.update_entries(frame, queue, variable))


def main():
    """
    (None) Main function that calls the tkinter root
    """
    root = tk.Tk()
    app = QueueApp(root)
    root.resizable(0, 0)
    root.mainloop()

if __name__ == "__main__":
    main()
