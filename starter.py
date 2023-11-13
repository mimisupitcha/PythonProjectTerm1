import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk #for importing images
from collections import Counter #counting the letter in self.score list

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
        self.button_enneagram = tk.Button(master, text="Start the Enneagram Test!", command=self.enneagram_test)
        self.button_enneagram['font'] = ['Arial', 20]

        # Placing the widgets in the window
        self.label_welcome.pack(pady=20)
        self.label_slogan.pack(pady=2.5)
        self.label_pic_enneagram = tk.Label(master, image=self.pic_enneagram_resized)
        self.label_pic_enneagram.pack(pady=25)
        self.textbox_intro.pack(pady=15)
        self.intro_paragraph.pack(padx=10, pady=10)
        self.button_enneagram.pack(pady=25)


    def enneagram_test(self):
        # Withdraw the current window
        self.master.iconify()

        # Open a new window
        new_window = tk.Toplevel(self.master)
        enneagram_question_app = EnneagramQuestion(new_window)

class Question:
    def __init__(self, choice_a, choice_b, score_a, score_b):
        # a question consist of 2 choices, and what type the questions contribute to
        self.choice_a = choice_a  # "I've been romantic and imaginative."
        self.choice_b = choice_b  # "I've been pragmatic and down to earth."
        self.score_a = score_a  # "E"
        self.score_b = score_b  # "B"

class EnneagramQuestion:
    def __init__(self, master):
        self.master = master
        self.master.title("Enneagram Type Indicator-RHETI Sampler")
        self.master.geometry("1200x1000")
        self.master.resizable(height=True, width=True)

        #self.scores = {i: 0 for i in "ABCDEFGHI"}
        self.scores = []

        self.questions = [
            Question("I've been romantic and imaginative.", "I've been pragmatic and down to earth.", "E", "B"),
            Question("I have tended to take on confrontations.", "I have tended avoid confrontations", "G", "A"),
            Question("I have typically been diplomatic, charming, and ambitious.", "I have typically been direct, formal, and idealistic.", "C", "D"),
            Question("I have tended to be focused and intense.", "I have tended to be spontaneous and fun-loving.", "H", "I"),
            Question("I have been a hospitable person and have enjoyed welcoming new friends into mylife.", "I have been a private person and have not mixed much with others.", "F", "E"),
            Question("Generally, it's been easy to 'get a rise' out of me.", "Generally, it's been difficult to 'get a rise' out of me.", "B", "A"),
            Question("I've been more of a 'street-smart' survivor.", "I've been more of a 'high-minded' idealist .", "G", "D"),
            Question("I have needed to show affection to people.", "I have preferred to maintain a certain distance with people.", "F", "H"),
            Question("When presented with a new experience, I've usually asked myself if it would be useful to me.", "When presented with a new experience, I've usually asked myself if it would be enjoyable.", "C", "I"),
            Question("I have tended to focus too much on myself.", "I have tended to focus too much on others.", "E", "A"),
            Question("Others have depended on my insight and knowledge.", "Others have depended on my strength and decisiveness.", "H", "G"),
            Question("I have come across as being too unsure of myself.", "I have come across as being too sure of myself.", "B", "D"),
            Question("I have been more relationship-oriented than goal-oriented.", "I have been more goal-oriented than relationship-oriented.", "F", "C"),
            Question("I have not been able to speak up for myself very well.", "I have been outspoken—I've said what others wished they had the nerve to say.", "E", "I"),
            Question("It's been difficult for me to stop considering alternatives and do something definite.", "It's been difficult for me to take it easy and be more flexible.", "H", "D"),
            Question("I have tended to be hesitant and procrastinating.", "I have tended to be bold and domineering.", "B", "G"),
            Question("My reluctance to get too involved has gotten me into trouble with people.", "My eagerness to have people depend on me has gotten me into trouble with them.", "A", "F"),
            Question("Usually, I have been able to put my feelings aside to get the job done.", "Usually, I have needed to work through my feelings before I could act.", "C", "E"),
            Question("Generally, I have been methodical and cautious.", "Generally, I have been adventurous and taken risks.", "B", "I"),
            Question("I have tended to be a supportive, giving person who enjoys the company of others.", "I have tended to be a serious, reserved person who likes discussing issues.", "F", "D"),
            Question("I've often felt the need to be a 'pillar of strength.'", "I've often felt the need to perform perfectly", "G", "C"),
            Question("I've typically been interested in asking tough questions and maintaining my independence.", "I've typically been interested in maintaining my stability and peace of mind.", "H", "A"),
            Question("I've been too hard-nosed and sceptical.", "I've been too soft-hearted and sentimental.", "B", "F"),
            Question("I've often worried that I'm missing out on something better.", "I've often worried that if I let down my guard, someone will take advantage of me.", "I", "G"),
            Question("My habit of being 'stand-offish' has annoyed people.", "My habit of telling people what to do has annoyed people.", "E", "D"),
            Question("Usually, when troubles have gotten to me, I have been able to 'tune them out.'", "Usually, when troubles have gotten to me, I have treated myself to something I've enjoyed.", "A", "I"),
            Question("I have depended upon my friends and they have known that they can depend on me.", "I have not depended on people; I have done things on my own.", "B", "C"),
            Question("I have tended to be detached and preoccupied.", "I have tended to be moody and self-absorbed.", "H", "E"),
            Question("I have liked to challenge people and 'shake them up'.", "I have liked to comfort people and calm them down", "G", "F"),
            Question("I have generally been an outgoing, sociable person.", "I have generally been an earnest, self-disciplined person.", "I", "D"),
            Question("I've usually been shy about showing my abilities.", "I've usually liked to let people know what I can do well.", "A", "C"),
            Question("Pursuing my personal interests has been more important to me than having comfort and security.", "Having comfort and security has been more important to me than pursuing my personal interests.", "H", "B"),
            Question("When I've had conflict with others, I've tended to withdraw.", "When I've had conflict with others, I've rarely backed down.", "E", "G"),
            Question("I have given in too easily and let others push me around.", "I have been too uncompromising and demanding with others.", "A", "D"),
            Question("I've been appreciated for my unsinkable spirit and great sense of humour.", "I've been appreciated for my quiet strength and exceptional generosity.", "I", "F"),
            Question("Much of my success has been due to my talent for making a favourable impression.", "Much of my success has been achieved despite my lack of interest in developing 'interpersonal skills.'", "C", "H"),


            # add your questions!
        ]
        self.question_index = 0

        self.textbox_question = tk.LabelFrame(self.master, text= "Instruction", width= 600)
        self.instruction = tk.Message(self.textbox_question, text = "Choose the sentence that best describes you or is important to you in most of the time. If neither sentence fits well or if both are equally relevant, you can choose the 'Neither of the choices' option. ", width = 750)
        self.label_a = tk.Label(self.master)
        self.label_b = tk.Label(self.master)
        self.button_a = tk.Button(self.master, text="sentence 1", command=self.button_a_press)
        self.button_b = tk.Button(self.master, text="sentence 2", command=self.button_b_press)
        self.button_neither = tk.Button(self.master, text="neither of the choices", command= self.button_none_press)

        #place the labels
        self.textbox_question.pack(pady=10,padx= 300, side = "top", fill='x')
        self.instruction.pack(pady=10)
        self.label_a.pack(pady=20)
        self.button_a.pack()
        self.label_b.pack(pady=20)
        self.button_b.pack()
        self.button_neither.pack(pady=40)

        self.set_question()


        
        #self.master.mainloop()

    def set_question(self):
        question = self.questions[self.question_index]
        self.label_a.config(text=question.choice_a, font= ['Arial',28, 'bold'])
        self.label_b.config(text=question.choice_b, font= ['Arial',28, 'bold'])

    def button_a_press(self):
        # plus the type to score
        question = self.questions[self.question_index]
        self.scores.append(question.score_a)
        self.change_question()

    def button_b_press(self):
        # plus the type to score
        question = self.questions[self.question_index]
        #self.scores[question.score_b] += 1
        self.scores.append(question.score_b)
        self.change_question()

    def button_none_press(self):
        self.change_question()


    def change_question(self):
        self.question_index += 1
        if self.question_index == len(self.questions):
            # If it's the last question, close the current window and open a new one
            self.master.iconify()  # Close the current window
            new_window = tk.Toplevel(self.master)
            enneagram_question_app = LastThreeChoice(new_window, self.get_top_three_letters())
        else:
            self.set_question()
    

    def get_top_three_letters(self):
        #print(self.scores)
        if not self.scores:
            messagebox.showinfo("Please Review Your Answers", 'Please read the questions carefully and answer again')
            self.master.destroy()
            self.run_again()
        else:
            self.letter_counts = Counter(self.scores)
            self.top_three_letters = [letter for letter, count in self.letter_counts.most_common(3)]
            return self.top_three_letters

    def run_again(self):
        # Add code here to reset or reinitialize any necessary variables or states
        # ...
        self.master = tk.Tk()  # Reinitialize the Tkinter window
        main()



 


class LastThreeChoice:
    def __init__(self, master, top_three_letters):
        self.master = master
        self.master.title("Enneagram Type Indicator-RHETI Sampler")
        self.master.geometry("1200x1000")
        self.master.resizable(height=True, width=True)
        self.check_top3_letters(top_three_letters)

    
    def check_top3_letters(self, top_three_letters):
        # Sort the letters based on their frequency in descending order
        sorted_letters = sorted(top_three_letters)
        self.labelChooseType = tk.Label(self.master, text= '"Discover tailored financial insights by choosing your top three personality types. Click for a detailed analysis if one type fits you."', font=['Arail', 20, 'bold'], fg='blue')
        self.labelChooseType.pack(padx=60, pady= 25)
        for letter in sorted_letters:
            if letter == 'D':
                self.Type1_brief()
            elif letter == 'F':
                self.Type2_brief()
            elif letter == 'C':
                self.Type3_brief()
            elif letter == 'E':
                self.Type4_brief()
            elif letter == 'H':
                self.Type5_brief()
            elif letter == 'B':
                self.Type6_brief()
            elif letter == 'I':
                self.Type7_brief()
            elif letter == 'G':
                self.Type8_brief()
            elif letter == 'A':
                self.Type9_brief()

                

        
    def Type1_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type1',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The REFORMER", font= ['Arail',30,'bold'], width=750)
        self.label_detail = tk.Message(self.frame, text= "The rational, idealistic type. Ones are conscientious and ethical, with a strong sense of right and wrong. They are teachers, crusaders, and advocates for change: always striving to improve things, but afraid of making a mistake. Well-organized, orderly, and fastidious, they try to maintain high standards, but can slip into being critical and perfectionistic. They typically have problems with resentment and impatience. At their Best: wise, discerning, realistic, and noble. Can be morally heroic.", width=750)
        self.button1 = tk.Button(self.frame, text='Choose Type1',command= self.press_chooseType1)
        
        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button1.pack()
    def Type2_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type2',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The HELPER", font= ['Arail',30,'bold'], width=750)
        self.label_detail = tk.Message(self.frame, text= "The caring, interpersonal type. Twos are empathetic, sincere, and warm-hearted. They are friendly, generous, and self-sacrificing, but can also be sentimental, flattering, and people-pleasing. They are well-meaning and driven to be close to others, but can slip into doing things for others in order to be needed. They typically have problems with possessiveness and with acknowledging their own needs. At their Best: unselfish and altruistic, they have unconditional love for others.",width=750)
        self.button2 = tk.Button(self.frame, text='Choose Type2',command=self.press_chooseType2)

        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button2.pack()
        
    def Type3_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type3',pady=10, padx=5) 
        self.label_title = tk.Message(self.frame, text= "The ACHIEVER ", font= ['Arail',30,'bold'], width=750)
        self.label_detail = tk.Message(self.frame, text= "The success-oriented, pragmatic type. Threes are self-assured, attractive, and charming. Ambitious, competent, and energetic, they can also be status-conscious and highly driven for advancement. They are diplomatic and poised, but can also be overly concerned with their image and what others think of them. They typically have problems with workaholism and competitiveness. At their Best: self-accepting, authentic, everything they seem to be—role models who inspire others.", width=750)
        self.button3 = tk.Button(self.frame, text='Choose Type3', command= self.press_chooseType3)        
        
        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button3.pack()
    def Type4_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type4',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The INDIVIDUALIST ", font= ['Arail',30,'bold'], width=750)
        self.label_detail = tk.Message(self.frame, text= "The sensitive, introspective, type. Fours are self-aware, expressive, and reserved. They are emotionally honest, creative, and personal, but can also be moody and self-conscious. Withholding themselves from others due to feeling vulnerable and defective, they can also feel disdainful and exempt from ordinary ways of living. They typically have problems with melancholy, self-indulgence, and self-pity. At their Best: inspired and highly creative, they are able to renew themselves and transform their experiences.", width=750)
        self.button4 = tk.Button(self.frame, text='Choose Type4', command= self.press_chooseType4)       
        
        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button4.pack()
    def Type5_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type5',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The INVESTIGATOR", font= ['Arail',30,'bold'],width=750)
        self.label_detail = tk.Message(self.frame, text= "The intense, cerebral type. Fives are alert, insightful, and curious. They are able to concentrate and focus on developing complex ideas and skills. Independent, innovative, and inventive, they can also become preoccupied with their thoughts and imaginary constructs. They become detached, yet high-strung and intense. They typically have problems with eccentricity, nihilism, and isolation. At their Best: visionary pioneers, often ahead of their time, and able to see the world in an entirely new way.",width=750)
        self.button5 = tk.Button(self.frame, text='Choose Type5', command= self.press_chooseType5)       
        
        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button5.pack()
    def Type6_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type6',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The LOYALIST", font= ['Arail',30,'bold'], width=750)
        self.label_detail = tk.Message(self.frame, text= "The committed, security-oriented type. Sixes are reliable, hard-working, responsible, and trustworthy. Excellent “trouble-shooters,” they foresee problems and foster cooperation, but can also become defensive, evasive, and anxious—running on stress while complaining about it. They can be cautious and indecisive, but also reactive, defiant, and rebellious. They typically have problems with self-doubt and suspicion. At their Best: internally stable and self-reliant, courageously championing themselves and others.", width=750)
        self.button6 = tk.Button(self.frame, text='Choose Type6', command= self.press_chooseType6)              
        
        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button6.pack()
    def Type7_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type7',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The ENTHUSIAST", font= ['Arail',30,'bold'],width=750)
        self.label_detail = tk.Message(self.frame, text= "The busy, variety-seeking type. Sevens are extroverted, optimistic, versatile, and spontaneous. Playful, high-spirited, and practical, they can also misapply their many talents, becoming over-extended, scattered, and undisciplined. They constantly seek new and exciting experiences but can become distracted and exhausted by staying on the go. They typically have problems with impatience and impulsiveness. At their Best: they focus their talents on worthwhile goals, becoming appreciative, joyous, and satisfied.", width=750)
        self.button7 = tk.Button(self.frame, text='Choose Type7', command= self.press_chooseType7)       

        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button7.pack()
    def Type8_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type8',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The CHALLENGER", font= ['Arail',30,'bold'],width=750)
        self.label_detail = tk.Message(self.frame, text= "The powerful, dominating type. Eights are self-confident, strong, and assertive. Protective, resourceful, straight-talking, and decisive, but can also be egocentric and domineering. Eights feel they must control their environment, especially people, sometimes becoming confrontational and intimidating. Eights typically have problems with their tempers and with allowing themselves to be vulnerable. At their Best: self-mastering, they use their strength to improve others' lives, becoming heroic, magnanimous, and inspiring.", width=750)
        self.button8 = tk.Button(self.frame, text='Choose Type8', command= self.press_chooseType8)               

        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button8.pack()
    def Type9_brief(self):
        self.frame = tk.LabelFrame(self.master, text= 'Type9',pady=10, padx=5)
        self.label_title = tk.Message(self.frame, text= "The PEACEMAKER", font= ['Arail',30,'bold'],width=750)
        self.label_detail = tk.Message(self.frame, text= "The easygoing, self-effacing type. Nines are accepting, trusting, and stable. They are usually creative, optimistic, and supportive, but can also be too willing to go along with others to keep the peace. They want everything to go smoothly and be without conflict, but they can also tend to be complacent, simplifying problems and minimizing anything upsetting. They typically have problems with inertia and stubbornness. At their Best: indomitable and all-embracing, they are able to bring people together and heal conflicts.", width=750)
        self.button9 = tk.Button(self.frame, text='Choose Type9', command= self.press_chooseType9)               
        
        self.frame.pack(pady=15,padx= 200, fill='x',ipady=10,ipadx=20)
        self.label_title.pack()
        self.label_detail.pack()
        self.button9.pack()
    def clear_widgets(self):
        # Destroy all widgets in the current window
        for widget in self.master.winfo_children():
            widget.destroy()
    def press_chooseType1(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 1 - THE REFORMER', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Ones have a propensity to save versus spend, and want to make sure they have enough money for the future.', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'A sense of justice and doing things right are the main driver for Reformers. These clients pay close attention to the details and can be highly organized. If you have a client who actually likes talking budgets, they might be Type 1.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'A Reformer’s built-in moral compass and attention to detail can lead to perfectionistic tendencies. Reformers should make sure to budget to give themselves personal spending money to deter feelings of guilt. Defining personal values and creating a financial plan that reflects what they are passionate about will be important to your Reformer clients.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Let go of the All-Or-Nothing thinking and embrace the middle ground. You can save money and spend on yourself too.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'If you think the stock market is a bad place because it supports morally wrong companies, perhaps the best strategy is to pick and choose companies that are morally right to you. For example, if you don’t want to invest in SPY because it includes oil companies, maybe pick one or two companies you believe in and invest in them instead. I also like the idea of not investing in companies but rather, investing in yourself. Your education, your small business ideas, and your family and friends.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Set aside a small amount of money each week dedicated to yourself. If you budget it as ‘Fun Money’, it is accounted for and you will feel less guilt when you buy something for yourself. Although, I can’t guarantee the guilt goes away completely', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
    def press_chooseType2(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 2 - THE HELPER', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Twos aren’t likely to be interested in money for money’s sake,. “They may think of money as a way to care for loved ones or create opportunities to connect, rather than a goal in itself,” she explains. ', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Helpers, as the name suggests, feel happiest when serving others’ needs. They are often providers for their families and don’t hesitate to help friends and spend money to make others happy.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'Helpers may find themselves agreeing to spend when asked, even if it’s not in the budget. To them, emotional currency is more motivating than seeing their savings grow. Helper clients need encouragement to put more emphasis on making rational decisions that serve the long term and do not put them in a bad place. They might need the reminder that it’s important to take financial care of oneself to be able to provide financial care for others. ', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Balance is key. Dedicate one way to show self-care every day in order to avoid burn-out. That could be taking a walk, taking a bubble bath, or reading a book.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'Budget money for spending on others. For example, we have a ‘Gifts and Donations’ category in our budget. Another great title for this category is “Love Language Money”', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Limit the amount of hours you spend at work. When you are off, spend time on yourself instead of with others.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice4 = tk.Message(self.advice_box, text = 'Prioritize yourself when it comes to finances. Understand that spending too much on others can be hurting you. If being loved and liked is your motivator, reframe. Think of how not being financially savvy can make others feel. The people you love don’t want you to hurt. Let those around you motivate you to improve your finances.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice5 = tk.Message(self.advice_box, text = 'Get an accountability partner! 2s are motivated by others and some have reported that it helps to do the weekly budget with a spouse via a ‘date night’. Set challenges and share your goals and successes with each other.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')


        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
        self.advice4.pack()
        self.advice5.pack()

    def press_chooseType3(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 3 - THE ACHIEVER', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Enneagram Threes are often high earners, who see money as a “very important” driver in everything they do. Threes are often concerned with status and outward appearance.', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Achievers are big dreamers with big goals, often found in leadership positions. Feeling successful and having the admiration of others is what drives the Achiever – a corner office will do fine, thanks! It is important they remain connected to their authentic selves instead of focusing on how others perceive them or getting swept up in someone else’s definition of success.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'chievers can easily burn themselves out if they aren’t careful. When this happens, they are too exhausted to make wise money decisions, and may splurge on self-care or “shopping therapy”. Achievers tend to be big spenders and may see money as a status symbol. Help your Achiever clients define what success means to them so they have clear goals in mind. Your Achievers love to see progress and be acknowledged for accomplishing their goals.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'When feeling compelled to spend, ask yourself your true intentions. Is it to impress others or keep up with a trend? The clearer you are on your priorities, the better you are at feeding your inner happiness.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'Define financial success by how much you save as well as how much you earn. This will keep a balance between earning and spending. There is no point in earning more if you go into debt because you spend a lot.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Since type 3s are external-facing, start a blog on saving money or publish your savings goals. If you don’t want to be so public, verbally announce to friends and family what you wish to accomplish. For example, if you want to pay your student debt down by a certain date, inform your social circle. Then you will feel the pressure of success to get it done.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
    def press_chooseType4(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 4 -THE INDIVIDUALISTS', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Though they are the type most likely to say that money isn’t a motivating factor in their decision-making, Fours fell among the spenders of the Enneagram. “Fours may be more guided by their emotions in managing money, spending on the things that appeal to them instead of budgeting or being disciplined,”', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Individualists are the least motivated by money, compared to the other Enneagram Types. They are led by their hearts and are motivated by being true to themselves. Fours are typically emotionally engaged in life and will fully commit to projects and goals they believe in. ', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'Fours often spend money on things that help regulate their emotions and are the least likely to save. Helping your Individualist clients clearly identify long-term life goals that align with their true identity is the strongest motivator and reminder for them to disregard fleeting emotions during daily spending decisions. It is also important that their life and career reflect their personal interests in order to feel fulfilled. If they aren’t there yet, they may be driven to add a career change to their financial plan or devote financial resources to a side hustle or hobby they find meaningful.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Because type 4s like to do things that fuel their soul and creativity, it may be a great idea to create a side hustle out of your passions!', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'You may not want to hear the B-word, but budgeting can be your best friend. Make an event out of it. Buy a pretty notebook, grab colored pens and get creative with your budgeting. Forget the spreadsheet. Make a poster if you have to! If its too daunting, put budgeting on auto-pilot.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
    def press_chooseType5(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 5 - THE INVESTIGATOR', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Despite being one of the types most likely to self-identify as savers, Fives also tend to stress about not having enough money for the future. Ever the rational type, they prize being capable and self-reliant, and finances may be one key way they measure that.', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Investigators tend to be thoughtful, independent savers. Often frugal, they enjoy a nice deep dive into financial strategy and take comfort in knowledge. Investigators may find financial data, reports, and analytics to be the most interesting and engaging methods to communicate about money.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'Even though Investigators tend to be responsible with money, they also tend to be anxious about it. They can struggle with a scarcity mindset and hoard their money, worried that they won’t have enough for bad times. Helping your Investigator clients define what is “enough” in their savings and retirement funds will ease their anxiety and help them enjoy their money instead of simply holding onto it. Money’s no good if you don’t use it!', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Introverted type 5s tend to spend money on information. Use your research skills to learn about finances. Create graphs and charts that will point you towards the right direction in terms of investments. Trust the information you gain and invest your money. Remember this statistic: Historically, the market always goes up.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'Set aside a small amount of money each week dedicated to yourself. If you budget it as ‘Fun Money’, it is accounted for and you will feel less guilt when you buy something for yourself. Although, I can’t guarantee the guilt goes away completely', width=800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
    def press_chooseType6(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 6 - THE LOYALIST', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Sixes stress more about the future than most other types, hypothesizing the anxious Six may worry they won’t have security in the future if they don’t save enough today.', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Hardworking, responsible Loyalists keep things running behind the scenes without needing recognition. They crave stability and find their motivation in close relationships and feeling safe. They often have a mindset of expecting the worst while hoping for the best. ', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'Offset their anxiety when it comes to money management by feeding their love of learning. Help them build confidence by spending extra time on financial education. Having a long-term relationship with a trusted advisor will empower your Loyalist clients and help them feel secure in their decisions, including the decision to trust you with their finances.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'When 6s treat themselves, they tend to spend the most money on the ‘essentials’ like clothing or dining. It is important for 6s to also spend on self-care.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'Type 6s are uncomfortable with promotions and career changes. However, they are typically great at what they do. Have the courage to ask for a promotion. Reframe it as ensuring finance security and wealth in the future. Use financial security as a motivator to earn more.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Type 6s tend to worry about not having enough for retirement or their kid’s college. Perhaps looking into how Bonds can help with paying for both would calm a 6s nerves.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice4 = tk.Message(self.advice_box, text = 'Don’t let fear overcome your finances. Try a set-it-and-forget it strategy with investing and budgeting. Then avoid checking in every single day.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')


        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
        self.advice4.pack()

    def press_chooseType7(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 7 - THE ENTHUSIAST', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Sevens are the adventurers of the Enneagram, so it makes total sense they spend a lot on travel—and they’ve been very pleased with those purchases. Sevens also self-identify as spenders. “Sevens are a little more impulsive,”. “They see a purchase they know can bring them happiness or fun, and feel FOMO if they don’t get it.” ', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Enthusiasts are adventurers who want to experience life to the fullest. Their attention tends to bounce from one thing to another and are prone to spontaneous spending. Enthusiasts can be outgoing and have an exciting outlook on life that is contagious. ', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'Sometimes the happy-go-lucky attitude hides fear and insecurity about their financial future. They’d rather focus on the next fun time than spend time working out their financial issues. Enthusiasts will need help and accountability with balancing instant gratification versus long-term goals. Consider helping them set up automatic processes for bills and savings so they can spend on the here and now without jeopardizing their future.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Use their creativity and idea creation to find ways to get what they want without spending money.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = '7s sometimes suffer from impulse buys. Perhaps create a rule to wait 24 hours before buying something. Sleep on it. Or find ways to borrow items from someone or buy used.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
    def press_chooseType8(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 8 - THE CHALLENGER', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = 'Enneagram Eights tend to be high earners, who are fairly motivated by money. Although Eights aren’t stereotypically image-conscious, they do seek power and control. Owens thinks financial status could be a symbol of power and influence for the Eight—a way to show that they’re on top.  Plus, assertive Eights are likely to prevail in any negotiation about money—meaning higher salaries and better deals.', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Challengers are known to be confident, decisive, and protective. They like to feel in control. Their preferred method of building relationships is to engage in a heated debate on topics they find interesting and relevant. Challengers tend to be one of the highest earning types and will most likely appreciate conversations around investing money to build future wealth.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'When a  Challenger wants something, they usually get it, without considering others during the process. This can show up in their life goals and spending habits. If they have a life partner, it’s likely that their relationship would benefit from an advisor facilitating money conversations so that both parties are reflected in the budget and feel heard. Challengers may come across as intimidating and opinionated, but engaging in intense discussions is a meaningful way to build trust, respect, and a long-term relationship with them.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Fierce 8s are good negotiators. You should use this to their advantage. Type 8s would make great salespeople or could negotiate a better salary for themselves at their current job. No one is going to rip them off and get away with it.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'Listen to other people’s money stories. It isn’t the easiest thing for 8s to do, as they are programmed to think theirs is the best way, but learning from others could pay out in the end.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Sometimes 8s spend money to feel in control. Notice when you are doing that. Instead, reframe it as your money controlling you. To be better in control of money, focus on a budget.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
    def press_chooseType9(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 9 - THE PEACEMAKER', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='antiquewhite4')
        self.brief= tk.Message(self.brief_box, text = '"Laid-back Nines may see money as just a means to an end, motivated to have just enough of it to keep life on an even keel,"."Nines aren’t much for showing off or putting themselves out to gain acclaim, and their attitude towards money follows suit."', width = 800,font=['Arial', 18] ,fg= 'antiquewhite4')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Easygoing, gentle, and supportive, Peacemakers are motivated by keeping the peace and living in harmony with the people in their lives. They usually gravitate toward a simpler lifestyle and their purchases are useful rather than flashy. Peacemakers are happy to go along with someone else’s decisions, or to follow a group, to avoid causing conflict.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'Your Peacemaker clients are prone to decision fatigue and will benefit from building a simple, repeatable budget. Also, directly asking what they want in life might put them in a stressful situation. Peacemakers can struggle to make their own decisions or to even speak up for what they want in financial planning conversations because they may perceive that as causing conflict. A less intimidating approach is to present a hypothetical situation. “If you didn’t have all your current obligations and money wasn’t a factor, what would be your ideal lifestyle?” This is a great way to help Peacemakers overcome their fear of disruption and use their voices in the financial planning process instead of simply taking a supportive role.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Create a vision board of your wants in life. This may spark interest and inspire action. Type 9s are actually very creative people which is why vision boards are a great thing to do. They don’t always have the right words to explain what they want, but they can cut out pictures or images of what they hope for.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'Like type 2s, type 9s will benefit from having a friend hold their hand. Budgeting dates work best for a type 9. Creating finance goals and having an accountability partner is helpful too. Pick someone who is more go-getter than you, not another peacemaker. My husband is actually a Type 9 through and through. It works out really well for us. He lets me (a type 1) formulate the budget, and then he goes through and adds and subtracts from it as needed. I am crucial to getting the job started, but I need him to curate it for me in an intentional way.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'These self-less creatures name gifts as an expenditure that gives them joy. Create a ‘fun money’ category in your budget.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice4 = tk.Message(self.advice_box, text = 'Definitely budget! 9s seek inner peace and having a budget set every month actually calms them down since there is a plan set out for them.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')


        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=10)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
        self.advice4.pack()

def main():
    root = tk.Tk()
    ennea_finance_explorer_app = EnneaFinanceExplorer(root)
    root.mainloop()



#if __name__ == '__main__':
main()
