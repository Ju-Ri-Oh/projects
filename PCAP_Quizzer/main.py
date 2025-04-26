import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QButtonGroup
from PyQt5.QtCore import QTimer
from collections import Counter
from itertools import chain
import random
from question_bank import total_sample
from groupchart import show_groupchart

# initialize some variables used for the results screen / calculations
user_answers = {}
question_category = []
question_subcategory = []
category_correct = []
subcategory_correct = []
category_percentage = {}
result = ''
category_correct_count = {}
lowest_category = ''
lowest_percentage = ''
question_options = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(480, 470, 75, 23))
        self.next_button.setObjectName("next_button")
        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(230, 470, 75, 23))
        self.previous_button.setObjectName("previous_button")
        self.chart_button = QtWidgets.QPushButton(self.centralwidget)
        self.chart_button.setGeometry(QtCore.QRect(260, 200, 75, 23))
        self.chart_button.setObjectName("chart_button")
        #self.test_button = QtWidgets.QPushButton(self.centralwidget) # This is just for debugging purposes
        #self.test_button.setGeometry(QtCore.QRect(550, 470, 75, 23))
        #self.test_button.setObjectName("test_button")
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(60, 40, 651, 231))
        self.question.setObjectName("question")
        self.copyright_label = QtWidgets.QLabel(self.centralwidget)
        self.copyright_label.setGeometry(QtCore.QRect(680, 540, 121, 20))
        self.copyright_label.setObjectName("copyright_label")
        self.radio_button_a = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_a.setGeometry(QtCore.QRect(80, 300, 450, 40))
        self.radio_button_a.setObjectName("radio_button_a")
        self.radio_button_b = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_b.setGeometry(QtCore.QRect(80, 340, 450, 40))
        self.radio_button_b.setObjectName("radio_button_b")
        self.radio_button_c = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_c.setGeometry(QtCore.QRect(80, 380, 450, 40))
        self.radio_button_c.setObjectName("radio_button_c")
        self.radio_button_d = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_d.setGeometry(QtCore.QRect(80, 420, 450, 40))
        self.radio_button_d.setObjectName("radio_button_d")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 540, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(730, 0, 60, 20))
        self.timer_label.setObjectName("timer_label")
        self.explanation_label = QtWidgets.QLabel(self.centralwidget)
        self.explanation_label.setGeometry(QtCore.QRect(470, 290, 251, 161))
        self.explanation_label.setObjectName("explanation_label")
        self.worstcategory_label = QtWidgets.QLabel(self.centralwidget)
        self.worstcategory_label.setGeometry(QtCore.QRect(60, 175, 500, 46))
        self.worstcategory_label.setObjectName("worstcategory_label")
        self.backtrack_info_label = QtWidgets.QLabel(self.centralwidget)
        self.backtrack_info_label.setGeometry(QtCore.QRect(500, 13, 210, 46))
        self.backtrack_info_label.setObjectName("backtrack_info_label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(710, 30, 90, 22))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuPCAP_Quizzer = QtWidgets.QMenu(self.menubar)
        self.menuPCAP_Quizzer.setObjectName("menuPCAP_Quizzer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPCAP_Quizzer.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.chart_button.setText(_translate("MainWindow", "Chart"))
        self.question.setText(_translate("MainWindow", "                          question"))
        self.copyright_label.setText(_translate("MainWindow", "(c) Hauke Juri Schnepel"))
        self.backtrack_info_label.setText(_translate("MainWindow", "<b><font color='red' size='4'>ATTENTION!</font></b> <br>You can backtrack the questions  <b>HERE →</b>"))
        self.radio_button_a.setText(_translate("MainWindow", "RadioButton"))
        self.radio_button_b.setText(_translate("MainWindow", "RadioButton"))
        self.radio_button_c.setText(_translate("MainWindow", "RadioButton"))
        self.radio_button_d.setText(_translate("MainWindow", "RadioButton"))
        self.timer_label.setText(_translate("MainWindow", "TextLabel"))
        self.menuPCAP_Quizzer.setTitle(_translate("MainWindow", "PCAP Quizzer"))

class QuizApp(QMainWindow):
    def __init__(self, questions):
        super(QuizApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.question_bank = questions
        self.questions = random.sample(self.question_bank, 40)  # Randomly select n questions from the question databank
        self.current_question_index = 0
        self.answers = []
        self.remaining_time = (len(self.questions) * 90)  # 90 seconds time per question
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.ui.progressBar.setValue(0)
        self.quiz_finished = False
        self.ui.explanation_label.setWordWrap(True)
        self.ui.chart_button.clicked.connect(lambda: show_groupchart(self.questions, category_correct))
        self.ui.chart_button.hide()
        self.ui.backtrack_info_label.hide()
        #self.ui.test_button.clicked.connect(self.clear_radio_buttons) # debugging purposes

        # Creates Dropdown menu to show results of questions and allows backtracking
        for index, question in enumerate(self.questions):
            self.ui.comboBox.addItem(translate_func("MainWindow", f"Question {index + 1}:"))

        # Hide ComboBox and Explanation Label before show result
        self.ui.comboBox.hide()
        self.ui.explanation_label.hide()
        self.ui.worstcategory_label.hide()

        # Create a button group for radio buttons
        self.radioButtonGroup = QButtonGroup(self)  # Create the button group in the QuizApp instance
        # Add radio buttons to the button group
        self.radioButtonGroup.addButton(self.ui.radio_button_a)
        self.radioButtonGroup.addButton(self.ui.radio_button_b)
        self.radioButtonGroup.addButton(self.ui.radio_button_c)
        self.radioButtonGroup.addButton(self.ui.radio_button_d)

        # Connect Next / Previous buttons to functions
        self.ui.next_button.clicked.connect(self.next_question)
        self.ui.previous_button.clicked.connect(self.prev_question)

        self.ui.next_button.clicked.connect(self.update_progress)
        self.ui.previous_button.clicked.connect(self.update_progress)

        self.question_labels = []

        self.start_quiz()


    def clear_radio_buttons(self):
        '''Clears the checked state of all radio buttons in the group.'''
        self.radioButtonGroup.setExclusive(False) # Temporarily allow no buttons to be checked
        for button in self.radioButtonGroup.buttons():
            button.setChecked(False)
        self.radioButtonGroup.setExclusive(True) # Re-enable exclusive behavior

    def start_quiz(self):
        '''Shuffles the questions to give a new, random order every time'''
        random.shuffle(self.questions) # Redundant?
        for question in self.questions:
            options = random.sample(question['options'], len(question['options']))
            question_options.append(options)
        self.show_question()

    def show_question(self):
        '''Presents the current questions by updating existing labels'''
        self.clear_radio_buttons()
        question = self.questions[self.current_question_index]
        explanation = self.questions[self.current_question_index]
        self.ui.question.setText(f"{self.current_question_index + 1}. {question['question']}")
        self.ui.explanation_label.setText(f"<b>Explanation:</b> <br> <br>{explanation['explanation']}") # HTML text formatting for bold and newline
        
        options = question_options[self.current_question_index]
        
        # Update radio buttons and set text directly from the question's options
        for i, option in enumerate(options, start=97):
            radio_button = getattr(self.ui, f"radio_button_{chr(i)}")
            radio_button.setText(option)

        # Clear existing labels
        self.clear_question_labels()

        # Hide previous button on the first question and next button on the last to avoid going out of bounds
        if self.current_question_index == 0 or self.quiz_finished:
            self.ui.previous_button.hide()
        else:
            self.ui.previous_button.show()

        if self.current_question_index == len(self.questions) - 1:
            self.ui.next_button.setText('Finish')
        elif self.quiz_finished:
            self.ui.next_button.hide()
        else:
            self.ui.next_button.show()

        if not self.quiz_finished: 
            self.timer.start(1000)  # Update timer every second

        self.ui.worstcategory_label.hide()

        if self.quiz_finished:
            correct_answer = self.questions[self.current_question_index]['correct_answer']
            user_answer = user_answers.get(self.current_question_index +1, None)

            options = question_options[self.current_question_index]

            for i, option in enumerate(options, start=97):
                radio_button = getattr(self.ui, f"radio_button_{chr(i)}")
                if option == correct_answer:
                    checkmark_label = QLabel("✔️", self)
                    checkmark_label.setStyleSheet("font-size: 20px; color: green;")
                    checkmark_label.move(radio_button.x() - 20, radio_button.y() + 25)
                    checkmark_label.setObjectName(f"checkmark_label_{chr(i)}")
                    checkmark_label.show()
                    self.question_labels.append(checkmark_label)
                elif option != correct_answer:
                    x_mark_label = QLabel("❌", self)
                    x_mark_label.setStyleSheet("font-size: 20px; color: red;")
                    x_mark_label.move(radio_button.x() - 25, radio_button.y() + 25)
                    x_mark_label.setObjectName(f"x_mark_label_{chr(i)}")
                    x_mark_label.show()
                    self.question_labels.append(x_mark_label)

                # Add an arrow label next to the selected answer
                if user_answer == option:
                    arrow_label = QLabel("➡️", self)
                    arrow_label.setGeometry(radio_button.x() - 40, radio_button.y() + 30, 20, 20)  # Adjust the position as needed
                    arrow_label.setStyleSheet("font-size: 20px; color: blue;")
                    arrow_label.setObjectName(f"arrow_label_{chr(i)}")
                    arrow_label.show()
                    self.question_labels.append(arrow_label)

    def clear_question_labels(self):
        '''Clears the labels for checkmark, X mark, and arrow for the current question'''
        for label in self.question_labels:
            label.deleteLater()
        self.question_labels = []

    def next_question(self):
        '''Goes to the next question; updates current question index, saves selected answer'''
        self.timer.stop()

        if self.ui.radio_button_a.isChecked():  # If radio button is checked, save into dictionary via question index as key
            user_answers[self.current_question_index +1] = self.ui.radio_button_a.text()
        elif self.ui.radio_button_b.isChecked():
            user_answers[self.current_question_index +1] = self.ui.radio_button_b.text()
        elif self.ui.radio_button_c.isChecked():
            user_answers[self.current_question_index +1] = self.ui.radio_button_c.text()
        elif self.ui.radio_button_d.isChecked():
            user_answers[self.current_question_index +1] = self.ui.radio_button_d.text()
        else:
            pass

        # Get information of current question's category & subcategory, save it into dictionary (e.g. 5: ['miscellaneous'])
        question_category.append(self.questions[self.current_question_index]['category'])
        question_subcategory.append(self.questions[self.current_question_index]['subcategory'])

        self.current_question_index += 1    # Update question index to show next question

        if self.current_question_index < len(self.questions):   # Shows question unless current question goes beyond the total range, then show results instead
            self.show_question()
        else:
            self.show_results()


    def prev_question(self):
        '''Goes to the previous question; updates current question index '''
        self.timer.stop()
        self.current_question_index -= 1
        if self.current_question_index >= 0:
            self.show_question()

    def update_timer(self):
        '''Updates the timer every second'''
        if self.remaining_time > 0:
            self.remaining_time -= 1
            minutes, seconds = divmod(self.remaining_time, 60)
            self.ui.timer_label.setText(f"Time: {minutes:02d}:{seconds:02d}")
        else:
            self.timer.stop()
            self.show_results()

    
    def update_progress(self):
        '''Updates the progress bar based on the current question'''
        if self.ui.progressBar.value() != 100:
            self.ui.progressBar.setValue(int(self.current_question_index / len(self.questions) * 100))  # 2.5% per question assuming 40 total
        else:
            pass


    def backtrack_questions(self, index):
        '''Allows to navigate back through the answered questions via ComboBox dropdown menu'''
        self.timer.stop()
        self.current_question_index = index
        self.show_question()
        self.ui.chart_button.setGeometry(QtCore.QRect(720, 70, 75, 22))
        self.ui.backtrack_info_label.hide()


    def show_results(self):
        '''Calculates total correctly answered questions, gives that information and shows which ones are correct/false'''        
        total = 0
        global result
        global category_correct
        global subcategory_correct
        self.quiz_finished = True

        self.ui.chart_button.show()
        self.ui.chart_button.raise_()
        self.ui.backtrack_info_label.show()

        # Compare user answer to correct answer and color-code questions of the ComboBox accordingly
        for key, value in user_answers.items():
            if value == self.questions[key-1]['correct_answer']:
                total += 1
                category_correct.append(self.questions[key - 1]['category'][0])
                subcategory_correct.append(self.questions[key-1]['subcategory'][0])
                self.ui.comboBox.setItemData(key-1, QtGui.QColor('green'), QtCore.Qt.TextColorRole)  # Set text color to green for correct answer
            else:
                self.ui.comboBox.setItemData(key-1, QtGui.QColor('red'), QtCore.Qt.TextColorRole)  # Set text color to red for incorrect answer


        if (total / len(self.questions) * 100 ) >= 70:
            result = 'passed'
        else:
            result = 'failed'

        # Set up label for percentage of correct answers and fail/pass the exam
        percentage_correct = total / len(self.questions) * 100
        rounded_percentage = round(percentage_correct, 2)  # Round to 2 decimal places to avoid floating-point arithmetic inaccuracies
        self.ui.question.setText(f"You have answered {rounded_percentage}% of the questions correctly \nYou {result} the PCAP exam. ")

        # Hide buttons to avoid IndexError
        self.ui.previous_button.hide()
        self.ui.next_button.hide()

        # Show buttons / labels for result screen
        self.ui.comboBox.show()
        self.ui.explanation_label.show()
        self.ui.explanation_label.raise_()
        self.ui.worstcategory_label.show()

        self.ui.comboBox.activated.connect(self.backtrack_questions)
        print(category_correct, subcategory_correct) # DELETE LATER

        # Get percentage of correct categories/subcategories vs total categories/subcategories
        flattened_categories = list(chain.from_iterable(question_category))
        flattened_subcategories = list(chain.from_iterable(question_subcategory))
        category_count = Counter(flattened_categories)
        subcategory_count = Counter(flattened_subcategories)
        print('Categories: ', category_count, 'Subcategories: ', subcategory_count)

        category_correct_count = Counter(category_correct)
        subcategory_correct_count = Counter(subcategory_correct)
        print('Correct Categories: ', category_correct_count, 'Correct Subcategories: ', subcategory_correct_count)

        category_percentage = {}
        for category, correct_count in category_correct_count.items():
            total_count = category_count.get(category, 0)  # If category not found, default to 0
            if total_count != 0:  # Avoid division by zero
                percentage = round((correct_count / total_count) * 100)
            else:
                percentage = 0 # Avoid empty entry
            category_percentage[category] = percentage

        subcategory_percentage = {}
        for subcategory, correct_count in subcategory_correct_count.items():
            total_count = subcategory_count.get(subcategory, 0)  # If subcategory not found, default to 0
            if total_count != 0:  # Avoid division by zero
                percentage = round((correct_count / total_count) * 100)
            else:
                percentage = 0
            subcategory_percentage[subcategory] = percentage

        # add categories that weren't answered correctly with 0 percent as value
        category_percentage = {category: round((category_correct_count.get(category, 0) / category_count.get(category, 1)) * 100) for category in category_count}
        subcategory_percentage = {subcategory: round((subcategory_correct_count.get(subcategory, 0) / subcategory_count.get(subcategory, 1)) * 100) for subcategory in subcategory_count}
        print('Category Percentages:', category_percentage)
        print('Subcategory Percentages:', subcategory_percentage)

        lowest_category = None
        lowest_percentage = 100  # Initialize with a high value to ensure any percentage is lower

        for category, percentage in category_percentage.items():
            if percentage < lowest_percentage:
                lowest_percentage = percentage
                lowest_category = category
        self.ui.worstcategory_label.setText(f'Your lowest Category was: <b>{lowest_category}</b> with a percentage of <b>{lowest_percentage}%</b> correct answers <br>Check out your chart for more info! &rarr;')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    question_bank = total_sample
    translate_func = QtCore.QCoreApplication.translate
    quiz_app = QuizApp(question_bank)
    quiz_app.show()
    sys.exit(app.exec_())
