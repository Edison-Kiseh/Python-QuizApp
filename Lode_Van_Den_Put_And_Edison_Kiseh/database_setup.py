# database_setup.py

import sqlite3

class QuizDatabase:
    def __init__(self, database_name='quiz_database.db'):
        self.database_name = database_name

    def create_database(self):
        # Connect to SQLite database (or create if it doesn't exist)
        conn = sqlite3.connect(self.database_name)

        # Create a cursor object
        cursor = conn.cursor()

        # Create a table for questions if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                correct_option INTEGER
            )
        ''')

        # Insert questions into the table based on category
        self.insert_questions(cursor, 'Animals', [
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
        ])

        self.insert_questions(cursor, 'General Knowledge', [
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
        ])

        self.insert_questions(cursor, 'Science', [
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
        ])

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def insert_questions(self, cursor, category, questions):
        # Insert questions into the table for the specified category
        for question_data in questions:
            cursor.execute('''
                INSERT INTO questions (category, question, option1, option2, option3, option4, correct_option)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                category,
                question_data['question'],
                question_data['options'][0],
                question_data['options'][1],
                question_data['options'][2],
                question_data['options'][3],
                question_data['correct_option']
            ))
    
if __name__ == "__main__":
    # Run this script independently to create the database and fill it with questions
    quiz_db = QuizDatabase()
    quiz_db.create_database()
