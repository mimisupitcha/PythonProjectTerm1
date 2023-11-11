from tkinter import *

# Create a home page window
homepage = Tk()
homepage.title("EnneaFinance Explorer")
homepage.geometry("1200x1000")
homepage.resizable(height= True, width= True)

# Load the image using Pillow for resizing
from PIL import Image, ImageTk
pic_enneagram = Image.open("/Users/supitchachuchottaworn/Desktop/financial engineering 2023/introduction to programming/PythonProjectTerm1/images/enneagram_homepage.png")
# Resize the image
resized_image = pic_enneagram.resize((575, 400))
pic_enneagram_resized = ImageTk.PhotoImage(resized_image)
labelPicEnneagram = Label(homepage, image = pic_enneagram_resized)

# Create labels for program descriptions
labelWelcome = Label(homepage, text="Welcome to EnneaFinance Explorer!")
labelSlogan = Label(homepage, text='"Discover your type, Shape your wealth"')
labelWelcome['font'] = ['Arial', 20, 'bold']
labelSlogan['font'] = ['Arail', 15, 'italic', 'bold']
labelSlogan['bg'] = 'light blue'
labelSlogan['fg'] = 'blue'

# Create a text box with Program's Intro paragraph
textbox_intro = LabelFrame(homepage, text= "Welcome Message",
                        width= 600)
IntroParagraph = Message(textbox_intro, text = "Our unique program designed to blend the insights of Enneagram typing with the world of finance. Discover how your Enneagram type influences your financial decisions, uncover patterns in your saving behavior, and receive tailored advice on investments that align with your individual traits.",
                        font= ("Arial",18,'italic','bold'),
                        aspect= 500,
                        justify = CENTER,
                        fg = 'bisque4')

# "What is enneagram?" button
button_enneagram = Button(homepage, text = "WHAT IS ENNEAGRAM")
button_enneagram['font'] = ['Arial',20]

button_enneagram.bind("<Button-1>")

# Placing the widget to window
labelWelcome.pack()
labelSlogan.pack(pady = 5)
labelPicEnneagram.pack(pady = 25)
textbox_intro.pack()
IntroParagraph.pack()
button_enneagram.pack(pady = 25)

homepage.mainloop()