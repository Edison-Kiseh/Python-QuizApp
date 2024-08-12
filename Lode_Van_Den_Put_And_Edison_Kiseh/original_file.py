from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random
from random import shuffle

class Window(QWidget):#the welcome page
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle("PyQuiz")

        # window size
        self.setFixedSize(900, 700)

        #nav bars
        self.button_about = QPushButton('about', self)
        self.button_about.clicked.connect(self.about_page)
        self.button_about.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE;  color: black}'
        )

        #self.button_about.setStyleSheet('border: none; padding-top: 10px; margin-left: 0px')
        
        self.button_help = QPushButton('help', self)
        self.button_help.move(90,0)
        self.button_help.clicked.connect(self.help_page)
        self.button_help.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )

        self.label = QLabel('Welcome to PyQuiz!', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 50px;")
        self.label.move(230,110)

        page_text = QTextEdit(self)
        page_text.setPlainText(self.highscores())
        page_text.setFixedWidth(250)
        page_text.setFixedHeight(200)
        page_text.move(325, 220)
        page_text.setStyleSheet('font-size: 21px; background-color: white;')
        page_text.setAlignment(Qt.AlignCenter)
        
        self.label2 = QLabel('Click on the button below to start the game!', self)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("font-size: 20px;")
        self.label2.move(250, 450)
        
        
        self.button_start = QPushButton('Start' , self)
        self.button_start.setFixedWidth(200)
        self.button_start.move(350,500)
        self.button_start.clicked.connect(self.second_Page)

        self.button_start.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 40px; font-size: 20px;}'
            'QPushButton:hover {background-color: #767B91;}'
        )

    def highscores(self):
        return "Highscores\n\n- Dummy 1:  100\n\n- Dummy 2:  75\n\n- Dummy 3:  50"
        
    def second_Page(self):
        self.hide()
        window2.show()
        print('Switched to page 2')

    def about_page(self):
        self.hide()
        about.show()
        print('about page')

    def create_quiz(self):
        self.hide()
        quiz_create.show()
        print('create quiz')

    def help_page(self):
        self.hide()
        help_page.show()
        print('Help page')
        
class Window2(QWidget): #username input page
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle("PyQuiz")

        # window size
        self.setFixedSize(900, 700)

        self.back_btn = QPushButton('<- Go back', self)
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )

        self.label = QLabel('Enter your name to continue...', self)
        self.label.setStyleSheet('font-size: 30px;')
        self.label.move(250,250)
        
        self.text_field = QLineEdit(self)
        self.text_field.setPlaceholderText('Enter your name')
        self.text_field.setStyleSheet('height: 35px; font-size: 20px; background-color: white')
        self.text_field.setFixedWidth(500)
        self.text_field.move(200,320)
        self.value = self.text_field.text()

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.move(375,400)
        self.submit_button.clicked.connect(self.on_submit)
        self.submit_button.setFixedWidth(150)
        self.submit_button.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 40px; font-size: 20px;}'
            'QPushButton:hover {background-color: #767B91;}'
        )

    def on_submit(self):
        self.value = self.text_field.text()
        if(self.value == ''):
            random_number = random.randint(1,1000)
            print(f'Your name: Anonymous{random_number}')            
        else:
            print(f'Your name: {self.value}')

        self.third_Page()

    def third_Page(self):
        self.hide()
        window3.show()
        print('Switched to page 3')

    def back(self):
        self.hide()
        window.show()
        print('back')
            

class Window3(QWidget):#quiz category page
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)
        
        self.back_btn = QPushButton('<- Go back', self)
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )


        self.label = QLabel('Choose your preferred option', self)
        self.label.setStyleSheet('font-size: 40px;')
        self.label.move(190,120)

        self.btn1 = QPushButton('Animals', self)
        self.btn1.setFixedWidth(450)
        self.btn1.move(225,275)
        self.btn1.clicked.connect(lambda: self.select_category('Animals'))
        
        self.btn2 = QPushButton('General Knowledge', self)
        self.btn2.setFixedWidth(450)
        self.btn2.move(225,350)
        self.btn2.clicked.connect(lambda: self.select_category('General Knowledge'))

        self.btn3 = QPushButton('Science', self)
        self.btn3.setFixedWidth(450)
        self.btn3.move(225,425)
        self.btn3.clicked.connect(lambda: self.select_category('Science'))

        self.btn4 = QPushButton('Create my own quiz', self)
        self.btn4.setFixedWidth(450)
        self.btn4.move(225,500)
        self.btn4.clicked.connect(self.create_quiz)

        self.btn1.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 50px; font-size: 25px; font-weight: bold;}'
            'QPushButton:hover {background-color: #767B91;}'
        )
        self.btn2.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 50px; font-size: 25px; font-weight: bold;}'
            'QPushButton:hover {background-color: #767B91;}'
        )
        self.btn3.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 50px; font-size: 25px; font-weight: bold;}'
            'QPushButton:hover {background-color: #767B91;}'
        )
        self.btn4.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 50px; font-size: 25px; font-weight: bold;}'
            'QPushButton:hover {background-color: #767B91;}'
        )

    def select_category(self, category):
        self.category = category
        window4.set_category(category)  # Pass the selected category to the quiz window
        self.fourth_page()

    def reset_quiz(self):
        # Reset quiz-related variables
        window4.current_question = 0
        window4.score = 0
        window4.answered_questions = 0
        window4.score_tracker = 0
        self.category = None
        window4.set_category(None)
        #window4.shuffle(questions)  
        window4.load_question()

        

    def fourth_page(self):
        self.hide()
        window4.show()
        print('back')

    def back(self):
        self.hide()
        window2.show()
        print('back')

    def create_quiz(self):
        self.hide()
        quiz_create.show()
        print('create your quiz')
        

class About(QWidget): #about page
    def __init__(self):
        super().__init__()
              
        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)
        
        self.back_btn = QPushButton('<- Go back', self)
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )


        label = QLabel('About page', self)
        label.setStyleSheet('font-size: 40px')
        label.move(350, 50)

        page_text = QTextEdit(self)
        page_text.setPlainText(self.text())
        page_text.setFixedWidth(700)
        page_text.setFixedHeight(500)
        page_text.move(100, 140)
        page_text.setStyleSheet('font-size: 18px; background-color: white;')
        
            
    def text(self):
        return 'PyQuiz is a simple quiz application which was developped for a python project by two 2nd year students in Thomas more de nayer. This application provides multiple topics for quizzes and allows you to make the choice for yourself on which quiz to take.When a wrong answer is chosen, the quiz clearly indicates that the choice was wrong and give the right answer. It also possesses a point recording system which records your points based on the correct answers you\'ve gotten. Based on your performance, you have the chance of making it to the highscores page which displays the top 3 scorers of the quiz. Questions and the answers are stored in an SQLite database alongside the names of the users.' 

    def back(self):
        self.hide()
        window.show()
        print('back')
            

class QuizCreationApp(QMainWindow): #the window where a user can create their own quizzes
    def __init__(self):
        super(QuizCreationApp, self).__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)
        
        self.back_btn = QPushButton('<- Go back', self)
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )


        self.questions = []
        self.current_question_index = 0

        self.init_ui()

    def init_ui(self):
        # Widgets
        self.question_label = QLabel('Question:')
        self.question_text = QLineEdit()

        self.answers_group = QGroupBox('Answers:')
        self.answers_layout = QVBoxLayout(self.answers_group)
        self.add_answer_button = QPushButton('Add Answer')
        self.add_answer_button.clicked.connect(self.add_answer)

        self.submit_button = QPushButton('Submit Quiz')
        #self.submit_button.clicked.connect(self.submit_quiz)

        # Layout
        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(self.question_label)
        central_layout.addWidget(self.question_text)
        central_layout.addWidget(self.answers_group)
        central_layout.addWidget(self.add_answer_button)
        central_layout.addWidget(self.submit_button)

        self.setCentralWidget(central_widget)

        # Initialize the first question
        self.add_answer()

    def add_answer(self):
        answer_text = QLineEdit()
        radio_button = QRadioButton()
        layout = QHBoxLayout()
        layout.addWidget(radio_button)
        layout.addWidget(answer_text)
        self.answers_layout.addLayout(layout)

    def back(self):
        self.hide()
        window3.show()
        print('back')


class Help(QWidget): #for the help the page
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)

        self.back_btn = QPushButton('<- Go back', self)
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )


        label = QLabel('Help page', self)
        label.setStyleSheet('font-size: 40px')
        label.move(350, 50)

        page_text = QTextEdit(self)
        page_text.setPlainText(self.text())
        page_text.setFixedWidth(700)
        page_text.setFixedHeight(500)
        page_text.move(100, 140)
        page_text.setStyleSheet('font-size: 18px; background-color: white;')
        
            
    def text(self):
        return "How to play:\n\nIt is pretty simple and playable to anyone. Once you enter (or not) enter your name, all you have to do is select the category of the quiz you wish to take then 10 random questions will be generated on this subject alongside possible answers. You also have the option of adding your own quiz by clicking on the create my own quiz button which will then demand you to enter the questions alongside their answers. \n\nHow the point system works: \n\n- Each question answered correctly on first try awards the user 10 points\n- If the question is answered on the second try, you are awarded 7 points\n- If it is guessed in the third try then you gain only 3 point\n- In the case where it is gotten in the fourth try, then you don\'t gain any points. \n\nIt's also important to note that users who don't enter their name get registered as anonymous"

    def back(self):
        self.hide()
        window.show()
        print('back')
        

class Quiz(QWidget):  # the quiz

    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)        
        
        self.category = None

    def set_category(self, category):
        self.category = category
        if category == 'Animals':
            # List of questions for the Animals category
            self.questions = [
                {
                    'question': 'What is the largest mammal on Earth?',
                    'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Gorilla'],
                    'correct_option': 1
                },
                {
                    'question': 'Which of the following birds is known for imitating human speech?',
                    'options': ['Eagles', 'Penguin', 'Parrot', 'Owl'],
                    'correct_option': 2
                },
                {
                    'question': 'What is the primary diet of a koala?',
                    'options': ['Insects', 'Fish', 'Bamboo shoots', 'Eucalyptus leaves'],
                    'correct_option': 3
                },
                {
                    'question': 'Which big cat is known for its distinctive black and orange stripes?',
                    'options': ['Tiger', 'Panther', 'Leopard', 'Cheetah'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the only mammal capable of sustained flight?',
                    'options': ['Flying Squirrel', 'Pegasus', 'Bat', 'Albatross'],
                    'correct_option': 2
                },
                {
                    'question': 'Which animal is known as the "King of the Jungle"?',
                    'options': ['Lion', 'Elephant', 'Giraffe', 'Cheetah'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the largest living species of turtle?',
                    'options': ['Leatherback Turtle', 'Green Sea Turtle', 'Loggerhead Turtle', 'Hawksbill Turtle'],
                    'correct_option': 0
                },
                {
                    'question': 'Which mammal lays eggs instead of giving birth to live young?',
                    'options': ['Platypus', 'Kangaroo', 'Dolphin', 'Bat'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the world\'s largest bird?',
                    'options': ['Eagle', 'Ostrich', 'Penguin', 'Sparrow'],
                    'correct_option': 1
                },
                {
                    'question': 'Which animal is known for its ability to regrow lost body parts?',
                    'options': ['Lizard', 'Starfish', 'Salamander', 'Snail'],
                    'correct_option': 2
                },
                            {
                    'question': 'What is the largest land animal?',
                    'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                    'correct_option': 0
                },
                {
                    'question': 'Which animal is known for its ability to change color?',
                    'options': ['Chameleon', 'Octopus', 'Cuttlefish', 'Camel'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the only continent where lemurs are found in the wild?',
                    'options': ['Africa', 'Asia', 'North America', 'Madagascar'],
                    'correct_option': 3
                },
                {
                    'question': 'Which bird is known for its long migrations, often flying thousands of miles?',
                    'options': ['Penguin', 'Albatross', 'Hummingbird', 'Swan'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the largest species of bear?',
                    'options': ['Panda Bear', 'Grizzly Bear', 'Polar Bear', 'Black Bear'],
                    'correct_option': 2
                },
                {
                    'question': 'Which animal is considered the fastest land mammal?',
                    'options': ['Cheetah', 'Lion', 'Gazelle', 'Leopard'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the largest species of big cat?',
                    'options': ['Lion', 'Tiger', 'Leopard', 'Jaguar'],
                    'correct_option': 1
                },
                {
                    'question': 'Which marine animal is known for its bioluminescence?',
                    'options': ['Dolphin', 'Whale Shark', 'Anglerfish', 'Sea Turtle'],
                    'correct_option': 2
                },
                {
                    'question': 'Which snake is the longest venomous snake in the world?',
                    'options': ['Rattlesnake', 'King Cobra', 'Black Mamba', 'Python'],
                    'correct_option': 2
                },
                {
                    'question': 'What is the collective term for a group of owls?',
                    'options': ['Herd', 'Flock', 'Parliament', 'Pack'],
                    'correct_option': 2
                }
            ]
            
        elif category == 'General Knowledge':
            self.questions = [
                {
                    'question': 'What is the capital of France?',
                    'options': ['London', 'Paris', 'Berlin', 'Rome'],
                    'correct_option': 1
                },
                {
                    'question': 'Which planet is known as the Red Planet?',
                    'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
                    'correct_option': 0
                },
                {
                    'question': 'In which year did the Titanic sink?',
                    'options': ['1912', '1905', '1920', '1899'],
                    'correct_option': 0
                },
                {
                    'question': 'Who wrote "Romeo and Juliet"?',
                    'options': ['Charles Dickens', 'William Shakespeare', 'Jane Austen', 'Mark Twain'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the largest ocean on Earth?',
                    'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                    'correct_option': 3
                },
                {
                    'question': 'Which element has the chemical symbol "O"?',
                    'options': ['Osmium', 'Oxygen', 'Gold', 'Lead'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the square root of 64?',
                    'options': ['4', '6', '8', '10'],
                    'correct_option': 2
                },
                {
                    'question': 'Who painted the Mona Lisa?',
                    'options': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet'],
                    'correct_option': 2
                },
                {
                    'question': 'Which country is known as the Land of the Rising Sun?',
                    'options': ['China', 'Japan', 'South Korea', 'Vietnam'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the largest mammal on Earth?',
                    'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Gorilla'],
                    'correct_option': 1
                },
                {
                    'question': 'Which planet is known as the "Morning Star" or "Evening Star"?',
                    'options': ['Venus', 'Mars', 'Jupiter', 'Mercury'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the largest desert in the world?',
                    'options': ['Sahara Desert', 'Arabian Desert', 'Antarctica', 'Gobi Desert'],
                    'correct_option': 2
                },
                {
                    'question': 'Who was the first President of the United States?',
                    'options': ['Thomas Jefferson', 'John Adams', 'George Washington', 'Abraham Lincoln'],
                    'correct_option': 2
                },
                {
                    'question': 'What is the currency of Japan?',
                    'options': ['Yuan', 'Won', 'Yen', 'Ringgit'],
                    'correct_option': 2
                },
                {
                    'question': 'Which famous scientist formulated the theory of relativity?',
                    'options': ['Isaac Newton', 'Niels Bohr', 'Albert Einstein', 'Galileo Galilei'],
                    'correct_option': 2
                },
                {
                    'question': 'In what year did World War II end?',
                    'options': ['1945', '1939', '1941', '1942'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the capital of Australia?',
                    'options': ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'],
                    'correct_option': 2
                },
                {
                    'question': 'Which famous landmark is located in Agra, India?',
                    'options': ['Eiffel Tower', 'Great Wall of China', 'Taj Mahal', 'Pyramids of Giza'],
                    'correct_option': 2
                },
                {
                    'question': 'Who wrote "To Kill a Mockingbird"?',
                    'options': ['J.K. Rowling', 'Harper Lee', 'George Orwell', 'Ernest Hemingway'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the chemical symbol for gold?',
                    'options': ['Au', 'Ag', 'Fe', 'Cu'],
                    'correct_option': 0
                }
                
            ]
            
        elif category == 'Science':
            self.questions = [
                {
                    'question': 'What is the chemical symbol for gold?',
                    'options': ['Au', 'Ag', 'Fe', 'Cu'],
                    'correct_option': 0
                },
                {
                    'question': 'Which gas makes up the majority of Earth\'s atmosphere?',
                    'options': ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'],
                    'correct_option': 2
                },
                {
                    'question': 'What is the smallest unit of life?',
                    'options': ['Cell', 'Atom', 'Molecule', 'Organism'],
                    'correct_option': 0
                },
                {
                    'question': 'Which planet is known as the "Red Planet"?',
                    'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the powerhouse of the cell?',
                    'options': ['Mitochondria', 'Nucleus', 'Endoplasmic Reticulum', 'Ribosome'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the process by which plants make their own food?',
                    'options': ['Photosynthesis', 'Respiration', 'Fermentation', 'Transpiration'],
                    'correct_option': 0
                },
                {
                    'question': 'Which element has the chemical symbol "O"?',
                    'options': ['Osmium', 'Oxygen', 'Gold', 'Lead'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the largest organ in the human body?',
                    'options': ['Heart', 'Brain', 'Skin', 'Liver'],
                    'correct_option': 2
                },
                {
                    'question': 'What is the speed of light in a vacuum?',
                    'options': ['300,000 km/s', '150,000 km/s', '500,000 km/s', '1,000,000 km/s'],
                    'correct_option': 0
                },
                {
                    'question': 'Which scientist is known for the theory of general relativity?',
                    'options': ['Isaac Newton', 'Albert Einstein', 'Niels Bohr', 'Stephen Hawking'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the chemical formula for water?',
                    'options': ['H2O', 'CO2', 'O2', 'NaCl'],
                    'correct_option': 0
                },
                {
                    'question': 'In the periodic table, what is the symbol for helium?',
                    'options': ['He', 'H', 'Li', 'Ne'],
                    'correct_option': 0
                },
                {
                    'question': 'Which force keeps planets in orbit around the Sun?',
                    'options': ['Gravity', 'Magnetism', 'Friction', 'Tension'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the process by which solid changes directly into a gas?',
                    'options': ['Sublimation', 'Condensation', 'Evaporation', 'Melting'],
                    'correct_option': 0
                },
                {
                    'question': 'Which metal is liquid at room temperature?',
                    'options': ['Gold', 'Silver', 'Mercury', 'Copper'],
                    'correct_option': 2
                },
                {
                    'question': 'What is the main component of Earth\'s core?',
                    'options': ['Iron', 'Nickel', 'Gold', 'Platinum'],
                    'correct_option': 0
                },
                {
                    'question': 'What is the unit of electric current?',
                    'options': ['Volt', 'Ampere', 'Ohm', 'Watt'],
                    'correct_option': 1
                },
                {
                    'question': 'Which gas is responsible for the greenhouse effect?',
                    'options': ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Methane'],
                    'correct_option': 1
                },
                {
                    'question': 'What is the chemical formula for glucose?',
                    'options': ['C6H12O6', 'H2O', 'CO2', 'NaCl'],
                    'correct_option': 0
                },
                {
                    'question': 'Who is known as the father of modern physics?',
                    'options': ['Isaac Newton', 'Galileo Galilei', 'Albert Einstein', 'Niels Bohr'],
                    'correct_option': 2
                }
            ]


        shuffle(self.questions)#shuffle the questions and make them different each time a quiz is started
        
        self.current_question = 0
        self.score = 0
        self.answered_questions = 0
        self.score_tracker = 0

        self.create_widgets()

    def create_widgets(self):
        layout = QVBoxLayout()

        # a QLabel to display the current score
        self.score_label = QLabel()
        self.score_label.setStyleSheet('font-size: 20px; color: blue; margin-left: 730px; font-weight: bold')
        layout.addWidget(self.score_label)
        
        self.question_label = QLabel()
        self.question_label.setStyleSheet('font-size: 30px; margin-bottom: 175px;')
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.question_label)

        self.option_buttons = []

        for i in range(4):
            button = QPushButton()

            button.clicked.connect(lambda state, x=i: self.next_question(x))
            self.option_buttons.append(button)
            button.setFixedWidth(700)
        
            button.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 40px; font-size: 25px; font-weight: bold; height: 60px; border-radius: 10px; border: 1px solid black; font-size: 25px; margin-bottom: 10px; margin-left: 200px}'
            'QPushButton:hover {background-color: #767B91;}'
            )
            layout.addWidget(button)
            
        self.setLayout(layout)
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.setText(question_data['question'])

        options = question_data['options']
        for i in range(4):
            self.option_buttons[i].setText(options[i])

        #the score label
        self.score_label.setText(f"Score: {self.score}")

    def next_question(self, selected_option):
        question_data = self.questions[self.current_question]
        if selected_option == question_data['correct_option']:
            # Awarding points based on how many tries it took to find the right answer
            if self.score_tracker == 0:
                self.score += 10
                self.score_tracker = 0
                self.answered_questions += 1
            elif self.score_tracker == 1:
                self.score += 7
                self.score_tracker = 0
            elif self.score_tracker == 2:
                self.score += 3
                self.score_tracker = 0
            else:
                self.score += 0
                self.score_tracker = 0

            for i in range(4):
                self.option_buttons[i].setEnabled(True)
                self.option_buttons[i].setFixedWidth(700)
                self.option_buttons[i].setStyleSheet(
                'QPushButton {background-color: #2A324B; color: white; height: 40px; font-weight: bold; font-size: 25px; height: 60px; border-radius: 10px; border: 1px solid black; font-size: 25px; margin-bottom: 10px; margin-left: 200px}'
                'QPushButton:hover {background-color: #767B91;}'
                )
                          
            self.current_question += 1

        else:
            self.option_buttons[selected_option].setEnabled(False)
            self.option_buttons[selected_option].setFixedWidth(700)
            self.option_buttons[selected_option].setStyleSheet(
                'height: 60px; border-radius: 10px; border: 1px solid black; font-size: 25px; margin-bottom: 10px; margin-left: 200px; color: red; background-color: #C7CCDB;')

            self.score_tracker += 1

        if self.current_question < 10:#len(self.questions):
            self.load_question()
        else:
            # self.show_result()
            self.hide()
            results_window.show()
            results_window.display_result(self.answered_questions, 10, self.score)

class ShowResults(QWidget):
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)

        self.results_label = QLabel(self)
        self.results_label.setStyleSheet('font-size: 40px')
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.play_again_button = QPushButton('Play again', self)
        self.play_again_button.clicked.connect(self.play_again)
        self.play_again_button.setStyleSheet('QPushButton{height: 70px; font-size: 30px; font-weight: bold; background-color: #2A324B; color: white;}'
                                             'QPushButton:hover {background-color: #767B91;}')
        self.play_again_button.setFixedWidth(300)

        # Layout for results and play again button
        layout = QVBoxLayout()
        layout.addWidget(self.results_label)
        layout.addWidget(self.play_again_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def play_again(self):
        self.hide()
        # Reset the quiz and go back to the categories page
        window3.reset_quiz()
        window3.show()

    def display_result(self, answered_questions, total_questions, score):
        '''if score >= 90:
           self.results_comment.setText('Outstanding performance!')
        elif score >= 75:
            self.results_comment.setText('Great job!')
        elif score >= 50:
            self.results_comment.setText('Good job')
        else:
            self.results_comment.setText('Poor performance!')'''
        self.results_label.setText(f'Your final score is {score} / 100.')
        

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window2 = Window2()
    window3 = Window3()
    window4 = Quiz()
    about = About()
    help_page = Help()
    quiz_create = QuizCreationApp()
    results_window = ShowResults()

    window.setStyleSheet('background-color: #E1E5EE')
    window2.setStyleSheet('background-color: #E1E5EE')
    window3.setStyleSheet('background-color: #E1E5EE')
    window4.setStyleSheet('background-color: #E1E5EE')
    about.setStyleSheet('background-color: #E1E5EE')
    help_page.setStyleSheet('background-color: #E1E5EE')
    quiz_create.setStyleSheet('background-color: #E1E5EE')
    results_window.setStyleSheet('background-color: #E1E5EE')
        
    window.show()
    window4.hide()
    #results_window.hide()

    app.setWindowIcon(QIcon('quiz.png'))
    
    sys.exit(app.exec_())

