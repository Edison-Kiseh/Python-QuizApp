from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random
import sqlite3
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
        self.button_help.move(90,0)#The move method is used for positioning content on the screen. The first argument is the width and the second is the height
        self.button_help.clicked.connect(self.help_page)
        self.button_help.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )

        self.label = QLabel('Welcome to PyQuiz!', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 50px;")
        self.label.move(230,110)

        
        self.label2 = QLabel('Click on the button below to start the game!', self)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("font-size: 20px;")
        self.label2.move(250, 450)
        
        #start button
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
        
    def second_Page(self):#basically switching to another page is just hiding the current page and displaying that page
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

        self.back_btn = QPushButton('<- Go back', self)#go back button
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )

        self.label = QLabel('Enter your name to continue...', self)
        self.label.setStyleSheet('font-size: 30px;')
        self.label.move(250,250)
        
        self.text_field = QLineEdit(self)#text field to enter name
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
            print(f'Your name: Anonymous{random_number}')#in case the user doesn't enter their name a random one is generated for them          
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

        #the quiz categories
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

    #This is our attempt at resetting the quiz after the user completes it and hits the play again button. It doesn't seem to reset for some reason
    def reset_quiz(self):
        # Resetting the quiz-related variables in the Quiz class (window4)
        window4.current_question = 0
        window4.score = 0
        window4.answered_questions = 0
        window4.score_tracker = 0

        # Resetting quiz-related variables in this class
        #self.category = None

        # Reloading questions for the selected category
        window4.set_category(self.category)

        
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
        quiz_info.show()
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

#This is the page that is displayed before the quiz page for the user to enter their quiz name and so on
class QuizInfoWindow(QWidget):
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

        self.quiz_name_label = QLabel('Enter quiz name', self)
        self.quiz_name_label.setGeometry(350, 150, 400, 30)
        self.quiz_name_label.setStyleSheet('font-size: 25px')
        
        self.quiz_name_input = QLineEdit(self)
        self.quiz_name_input.move(250,205)
        self.quiz_name_input.setFixedWidth(400)
        self.quiz_name_input.setStyleSheet('height: 40px')

        self.submit_btn = QPushButton('Submit', self)
        self.submit_btn.clicked.connect(self.submit)
        self.submit_btn.setEnabled(False)#meaning that the button is not clickable
        self.submit_btn.move(350,500)
        self.submit_btn.setFixedWidth(200)
        self.submit_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; height: 40px; font-size: 17px; font-weight: bold;}'
        )
        
        self.quiz_name_input.textChanged.connect(self.check_fields)

        self.show()

    def check_fields(self):#function to check if all the input fields have a value before enabling the submit button
        enable_button = bool(self.quiz_name_input.text())
        self.submit_btn.setEnabled(enable_button)
        self.submit_btn.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 40px; font-size: 17px; font-weight: bold;}'
            'QPushButton:hover {background-color: #767B91;}'
        )

    def submit(self):
        quiz_name = self.quiz_name_input.text()

        self.hide()
        quiz_create.show()

    def back(self):
        self.hide()
        window3.show()
        print('back')
            

class QuizCreationApp(QMainWindow):#The quiz creation page
    def __init__(self):
        super(QuizCreationApp, self).__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)
        
        self.back_btn = QPushButton('<- Go back', self)
        self.back_btn.clicked.connect(self.back)
        self.back_btn.setStyleSheet(
            'QPushButton {background-color: #767B91; color: white; font-size: 14px; font-weight: bold;}'
            'QPushButton:hover {background-color: #E1E5EE; color: black}'
        )
        self.back_btn.setFixedWidth(100)

        self.quiz_list = []
        self.current_question_index = 0
        self.max_questions = 10#fixing the required number of custom questions to be 10 else it becomes quite chaotic in case of abuse
        self.question_counter = 0

        self.init_ui()

    def init_ui(self):
        # Widgets
        self.question_label = QLabel('Enter your question here:', self)
        self.question_label.setStyleSheet('font-size: 20px')
        self.question_label.setGeometry(100, 250, 400, 30)

        self.question_text = QLineEdit(self)
        self.question_text.setFixedWidth(400)
        self.question_text.move(330,250)

        self.ans1_label = QLabel('Answer 4:', self)
        self.ans1_label.move(280,520)
        self.answer1_label = QLineEdit(self)
        self.answer1_label.move(380,520)
        self.answer1_label.setFixedWidth(200)

        self.ans2_label = QLabel('Answer 3:', self)
        self.ans2_label.move(280,470)
        self.answer2_label = QLineEdit(self)
        self.answer2_label.move(380,470)
        self.answer2_label.setFixedWidth(200)
        
        self.ans3_label = QLabel('Answer 2:', self)
        self.ans3_label.move(280,420)
        self.answer3_label = QLineEdit(self)
        self.answer3_label.move(380,420)
        self.answer3_label.setFixedWidth(200)
        
        self.ans4_label = QLabel('Answer 1:', self)
        self.ans4_label.move(280,370)
        self.answer4_label = QLineEdit(self)
        self.answer4_label.move(380,370)
        self.answer4_label.setFixedWidth(200)

        self.ans1_label.setStyleSheet('font-size: 20px')
        self.ans2_label.setStyleSheet('font-size: 20px')
        self.ans3_label.setStyleSheet('font-size: 20px')
        self.ans4_label.setStyleSheet('font-size: 20px')


        self.question_text.setStyleSheet('background-color: white;')
        self.answer1_label.setStyleSheet('background-color: white;')
        self.answer2_label.setStyleSheet('background-color: white;')
        self.answer3_label.setStyleSheet('background-color: white;')
        self.answer4_label.setStyleSheet('background-color: white;')


        self.correct_label = QLabel('Which of these answers is correct?', self)
        self.correct_label.setGeometry(320, 600, 400, 30)
        self.correct_label.setStyleSheet('font-size: 15px')
        
        self.correct_input = QLineEdit(self)
        self.correct_input.move(550,600)
        self.correct_input.setStyleSheet('background-color: white;')
        self.correct_input.setFixedWidth(40)

        self.next_btn = QPushButton('Next question',self)
        self.next_btn.move(350,650)
        self.next_btn.setFixedWidth(200)
        self.next_btn.setStyleSheet(
            'QPushButton {background-color: #2A324B; color: white; height: 40px; font-size: 17px; font-weight: bold;}'
            'QPushButton:hover {background-color: #767B91;}'
        )

        self.next_btn.clicked.connect(self.next_question)

    def next_question(self):
        if self.question_counter >= self.max_questions:
            print("You have reached the maximum limit of questions.")
            return
        # Check if all fields are filled
        if not all(field.text() for field in [self.question_text,
                                               self.answer1_label,
                                               self.answer2_label,
                                               self.answer3_label,
                                               self.answer4_label,
                                               self.correct_input]):
            print("Please fill in all fields before proceeding.")
            return

        # Incrementing the question counter
        self.question_counter += 1
        
        # Storing the current quiz and answers in the list
        current_quiz = {
            'question': self.question_text.text(),
            'answers': [
                self.answer1_label.text(),
                self.answer2_label.text(),
                self.answer3_label.text(),
                self.answer4_label.text()
            ],
            'correct_index': int(self.correct_input.text()) - 1  #since indexes start from 0
        }
        self.quiz_list.append(current_quiz)

        # Clearing the fields for the next question
        self.question_text.clear()
        self.answer1_label.clear()
        self.answer2_label.clear()
        self.answer3_label.clear()
        self.answer4_label.clear()
        self.correct_input.clear()

        # Printing the stored list
        print("Stored Quiz List:", self.quiz_list)

        self.show()

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
        

class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_questions_by_category(self, category):
        query = "SELECT * FROM questions WHERE category = ?"
        self.cursor.execute(query, (category,))
        rows = self.cursor.fetchall()

        questions = []
        for row in rows:
            question_data = {
                'question': row[2],
                'options': [row[3], row[4], row[5], row[6]],
                'correct_option': row[7]
            }
            questions.append(question_data)

        return questions

class Quiz(QWidget):
    def __init__(self, db):
        super().__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)

        self.category = None
        self.db = db

    def set_category(self, category):
        self.category = category
        self.questions = self.get_questions_from_db(category)

        shuffle(self.questions)  # shuffle the questions and make them different each time a quiz is started

        self.current_question = 0
        self.score = 0
        self.answered_questions = 0
        self.score_tracker = 0

        self.create_widgets()

    def get_questions_from_db(self, category):
        return self.db.get_questions_by_category(category)

    def create_widgets(self):
        layout = QVBoxLayout()

        # a QLabel to display the current score
        self.score_label = QLabel()
        self.score_label.setStyleSheet(
            'font-size: 20px; color: blue; margin-left: 730px; font-weight: bold')
        layout.addWidget(self.score_label)

        self.question_label = QLabel()
        self.question_label.setStyleSheet(
            'font-size: 30px; margin-bottom: 175px;')
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.question_label)

        self.option_buttons = []

        for i in range(4):
            button = QPushButton()

            button.clicked.connect(
                lambda state, x=i: self.next_question(x))
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

        # The score label
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

        else:#This here is to disable the button whenever the answer to the question is false
            self.option_buttons[selected_option].setEnabled(False)
            self.option_buttons[selected_option].setFixedWidth(700)
            self.option_buttons[selected_option].setStyleSheet(
                'height: 60px; border-radius: 10px; border: 1px solid black; font-size: 25px; margin-bottom: 10px; margin-left: 200px; color: red; background-color: #C7CCDB;')

            self.score_tracker += 1

        if self.current_question < 10:  # len(self.questions):
            self.load_question()
        else:
            # self.show_result()
            self.hide()
            results_window.show()
            results_window.display_result(
                self.answered_questions, 10, self.score)
            

class ShowResults(QWidget):#The last page displayed to show the score of the user
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('PyQuiz')

        # window size
        self.setFixedSize(900, 700)

        self.results_label = QLabel(self)
        self.results_label.setStyleSheet('font-size: 40px; font-weight: bold;')
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
        self.close()

        # Reset the quiz and go back to the categories page
        window3.reset_quiz()
        window3.show()

    def display_result(self, answered_questions, total_questions, score):
        if score >= 90:
           self.results_comment = 'Outstanding performance!'
        elif score >= 75:
            self.results_comment = 'Great job!'
        elif score >= 50:
            self.results_comment = 'Good job'
        else:
            self.results_comment = 'Poor performance!'
            
        self.results_label.setText(f'Your final score is {score} / 100.\n\n{self.results_comment}')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a connection to the SQLite database
    sqlite_connection = sqlite3.connect("quiz_database.db")

    # Create an instance of the Database class
    database_instance = Database(sqlite_connection)

    window = Window()
    window2 = Window2()
    window3 = Window3()
    window4 = Quiz(database_instance)  # Pass the Database instance
    about = About()
    help_page = Help()
    quiz_create = QuizCreationApp()
    results_window = ShowResults()
    quiz_info = QuizInfoWindow()

    #setting the background-color of the pages 
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
    quiz_info.hide()

    app.setWindowIcon(QIcon('quizz.jpg'))#the quiz logo
    sys.exit(app.exec_())

