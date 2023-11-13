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
        self.letter_counts = Counter(self.scores)
        self.top_three_letters = [letter for letter, count in self.letter_counts.most_common(3)]
        return self.top_three_letters
    


class LastThreeChoice:
    def __init__(self, master, top_three_letters):
        self.master = master
        self.master.title("Enneagram Type Indicator-RHETI Sampler")
        self.master.geometry("1200x1000")
        self.master.resizable(height=True, width=True)
        self.check_top3_letters(top_three_letters)

    
    def check_top3_letters(self, top_three_letters):
        # Sort the letters based on their frequency in descending order
        sorted_letters = sorted(top_three_letters) #, key=lambda letter: top_three_letters.count(letter), reverse=True)
        self.labelChooseType = tk.Label(self.master, text= 'To confirm your results, read the short type descriptions below and choose the one that best describes you', font=['Arail', 20, 'bold'], fg='blue')
        self.labelChooseType.pack(padx=60)
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
        self.Type_title = tk.Label(self.master, text='TYPE 1 & THEIR FINANCIAL BEHAVIOUR', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='brown1')
        self.brief= tk.Message(self.brief_box, text = 'Ones have a propensity to save versus spend, and want to make sure they have enough money for the future.', width = 800,font=['Arial', 18] ,fg= 'brown1')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Most likely to say they save what they earn and rarely spend. Owens projects the One’s drive to “do the right thing” prompts them to save for a rainy day instead of buying themselves a new toy.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'When they treat themselves, Ones spend the most on travel and clothing, but are also the type most likely to spend on fitness and wellness—perhaps an indicator of their desire to keep their bodies and minds in good working order.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description3 = tk.Message(self.description_box, text = 'Most types said their biggest money stressor was spending too much when they shouldn’t. This wasn’t the biggest worry for Ones, however— 33% stressed most about having enough for future goals like retirement or their kids’ college.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Let go of the All-Or-Nothing thinking and embrace the middle ground. You can save money and spend on yourself too.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'If you think the stock market is a bad place because it supports morally wrong companies, perhaps the best strategy is to pick and choose companies that are morally right to you. For example, if you don’t want to invest in SPY because it includes oil companies, maybe pick one or two companies you believe in and invest in them instead. I also like the idea of not investing in companies but rather, investing in yourself. Your education, your small business ideas, and your family and friends.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Set aside a small amount of money each week dedicated to yourself. If you budget it as ‘Fun Money’, it is accounted for and you will feel less guilt when you buy something for yourself. Although, I can’t guarantee the guilt goes away completely', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=20)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=20)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.description3.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=20)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
    def press_chooseType2(self):
        self.clear_widgets()
        self.Type_title = tk.Label(self.master, text='TYPE 1 & THEIR FINANCIAL BEHAVIOUR', font= ['Arial', 30, 'bold'])
        self.brief_box = tk.LabelFrame(self.master)
        self.breif_title = tk.Message(self.brief_box, text = 'In General...', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='brown1')
        self.brief= tk.Message(self.brief_box, text = 'Ones have a propensity to save versus spend, and want to make sure they have enough money for the future.', width = 800,font=['Arial', 18] ,fg= 'brown1')
       
        self.description_box = tk.LabelFrame(self.master)
        self.description_title = tk.Message(self.description_box, text ='Their Financial Behaviour', width= 800,  justify="center", font= ['Arial',28,'bold'], fg ='cornflowerblue')
        self.description1 = tk.Message(self.description_box, text = 'Most likely to say they save what they earn and rarely spend. Owens projects the One’s drive to “do the right thing” prompts them to save for a rainy day instead of buying themselves a new toy.', width = 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description2 = tk.Message(self.description_box, text = 'When they treat themselves, Ones spend the most on travel and clothing, but are also the type most likely to spend on fitness and wellness—perhaps an indicator of their desire to keep their bodies and minds in good working order.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
        self.description3 = tk.Message(self.description_box, text = 'Most types said their biggest money stressor was spending too much when they shouldn’t. This wasn’t the biggest worry for Ones, however— 33% stressed most about having enough for future goals like retirement or their kids’ college.', width= 800, justify="center", font= ['Arial', 18], fg= 'cornflowerblue')
       
        self.advice_box = tk.LabelFrame(self.master)
        self.advice_title = tk.Message(self.advice_box, text = 'ADVICE', width = 800, justify="center", font= ['Arial',28,'bold'], fg ='cyan4')
        self.advice1 = tk.Message(self.advice_box, text = 'Let go of the All-Or-Nothing thinking and embrace the middle ground. You can save money and spend on yourself too.', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice2 = tk.Message(self.advice_box, text = 'If you think the stock market is a bad place because it supports morally wrong companies, perhaps the best strategy is to pick and choose companies that are morally right to you. For example, if you don’t want to invest in SPY because it includes oil companies, maybe pick one or two companies you believe in and invest in them instead. I also like the idea of not investing in companies but rather, investing in yourself. Your education, your small business ideas, and your family and friends.', width=800, justify='center', font=['Arial',18], fg= 'cyan4')
        self.advice3 = tk.Message(self.advice_box, text = 'Set aside a small amount of money each week dedicated to yourself. If you budget it as ‘Fun Money’, it is accounted for and you will feel less guilt when you buy something for yourself. Although, I can’t guarantee the guilt goes away completely', width = 800, justify='center', font=['Arial',18], fg= 'cyan4')

        self.Type_title.pack()
        self.brief_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=20)
        self.breif_title.pack()
        self.brief.pack()
        self.description_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=20)
        self.description_title.pack()
        self.description1.pack()
        self.description2.pack()
        self.description3.pack()
        self.advice_box.pack(padx = 200,pady = 10, fill= 'x',ipady=10,ipadx=20)
        self.advice_title.pack()
        self.advice1.pack()
        self.advice2.pack()
        self.advice3.pack()
    def press_chooseType3(self):
        self.clear_widgets()
    def press_chooseType4(self):
        self.clear_widgets()
    def press_chooseType5(self):
        self.clear_widgets()
    def press_chooseType6(self):
        self.clear_widgets()
    def press_chooseType7(self):
        self.clear_widgets()
    def press_chooseType8(self):
        self.clear_widgets()
    def press_chooseType9(self):
        self.clear_widgets()
def main():
    root = tk.Tk()
    ennea_finance_explorer_app = EnneaFinanceExplorer(root)
    root.mainloop()



#if __name__ == '__main__':
main()
