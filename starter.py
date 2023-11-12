import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class EnneaFinanceExplorer:
    def __init__(self, master):
        self.master = master
        self.master.title("EnneaFinance Explorer")
        self.master.geometry("1200x1000")
        self.master.resizable(height=True, width=True)

        # Load and resize the image
        pic_enneagram = Image.open("images/enneagram_homepage.png")
        resized_image = pic_enneagram.resize((575, 400))
        self.pic_enneagram_resized = ImageTk.PhotoImage(resized_image)

        # Create labels for program descriptions
        self.label_welcome = tk.Label(master, text="Welcome to EnneaFinance Explorer!")
        self.label_slogan = tk.Label(master, text='"Discover your type, Shape your wealth"')
        self.label_welcome['font'] = ['Arial', 20, 'bold']
        self.label_slogan['font'] = ['Arial', 15, 'italic', 'bold']
        self.label_slogan['bg'] = 'light blue'
        self.label_slogan['fg'] = 'blue'

        # Create a text box with Program's Intro paragraph
        self.textbox_intro = tk.LabelFrame(master, text="Welcome Message", width=600)
        self.intro_paragraph = tk.Message(self.textbox_intro,
                                          text="Our unique program designed to blend the insights of Enneagram typing with the world of finance. Discover how your Enneagram type influences your financial decisions, uncover patterns in your saving behavior, and receive tailored advice on investments that align with your individual traits.",
                                          aspect=500)

        # Create a button to initiate the Enneagram test
        self.button_enneagram = tk.Button(master, text="Begin Your Enneagram Test", command=self.what_is_enneagram)
        self.button_enneagram['font'] = ['Arial', 20]

        # Placing the widgets in the window
        self.label_welcome.pack(pady=20)
        self.label_slogan.pack(pady=10)
        self.label_pic_enneagram = tk.Label(master, image=self.pic_enneagram_resized)
        self.label_pic_enneagram.pack(pady=25)
        self.textbox_intro.pack(pady=25)
        self.intro_paragraph.pack(padx=10, pady=10)
        self.button_enneagram.pack(pady=25)

    def what_is_enneagram(self):
        # Withdraw the current window
        self.master.iconify()

        # Open a new window
        new_window = tk.Toplevel(self.master)
        enneagram_question_app = EnneagramQuestion(new_window)


class EnneagramQuestion:
    def __init__(self, master):
        self.master = master
        master.title("EnneaFinance Explorer - Enneagram Question")
        master.geometry("800x600")
        master.resizable(height=True, width=True)
        self.type = []

        # Create buttons for the options
        self.button_1 = tk.Button(master, text="I've been romantic and imaginative.", command=self.on_click_button_1)
        self.button_2 = tk.Button(master, text="I've been pragmatic and down to earth.", command=self.on_click_button_2)
        self.button_3 = tk.Button(master, text="Button 3", command=self.on_click_button_3, state=tk.DISABLED)
        self.button_4 = tk.Button(master, text="Button 4", command=self.on_click_button_4, state=tk.DISABLED)
        self.button_none = tk.Button(master, text="Neither Choices", command=self.none_button)

        self.button_1['font'] = ['Arial', 15]
        self.button_2['font'] = ['Arial', 15]
        self.button_3['font'] = ['Arial', 15]
        self.button_4['font'] = ['Arial', 15]
        self.button_none['font'] = ['Arial', 15]

        # Create a text box for the question
        self.textbox_question = tk.LabelFrame(master, text="Question", width=600)
        self.question_text = tk.Message(self.textbox_question,
                                        text="Choose the best answer for you:",
                                        aspect=500)

        # Place the widgets in the window
        self.textbox_question.pack(pady=25)
        self.question_text.pack(padx=10, pady=10)
        self.button_1.pack(pady=25)
        self.button_2.pack(pady=25)
        self.button_3.pack(pady=25)
        self.button_4.pack(pady=25)
        self.button_none.pack(pady=25)

    def on_click_button_1(self):
        # Replace button_1 with button_3, enable button_3, and update the question text
        self.button_1.destroy()
        self.button_1 = self.button_3
        self.button_1.configure(command=self.on_click_button_3)
        self.button_3['state'] = tk.NORMAL
        self.button_2.destroy()
        self.button_2 = self.button_4
        self.button_2.configure(command=self.on_click_button_4)
        self.button_4['state'] = tk.NORMAL
        self.update_question_text("Your answer: I've been romantic and imaginative.")

    def on_click_button_2(self):
        # Replace button_2 with button_4, enable button_4, and update the question text
        self.button_2.destroy()
        self.button_2 = self.button_4
        self.button_2.configure(command=self.on_click_button_4)
        self.button_4['state'] = tk.NORMAL
        self.update_question_text("Your answer: I've been pragmatic and down to earth.")

    def on_click_button_3(self):
        messagebox.showinfo("Message", "Your answer: Button 3")
        self.type.append('C')

    def on_click_button_4(self):
        messagebox.showinfo("Message", "Your answer: Button 4")
        self.type.append('D')

    def none_button(self):
        messagebox.showinfo("Message", "Job la")

    def update_question_text(self, new_text):
        # Update the question text
        self.question_text.configure(text=new_text)


def main():
    root = tk.Tk()
    ennea_finance_explorer_app = EnneaFinanceExplorer(root)
    root.mainloop()


if __name__ == '__main__':
    main()
