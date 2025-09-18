#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGroupBox, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
from random import shuffle, randint

class Question():
    def __init__(self, question_text, right_ans, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
questions_list = []
questions_list.append(
    Question('Государственный язык Бразилии?', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(
    Question('Какого цвета нет на флаге Росси?', 'Голубого', 'Белого', 'Красного', 'Синего'))
questions_list.append(
    Question('Что отвечают камни на вопрос:"увыгде?"', 'На обочине', 'В вулкане', 'На острове', 'В мешочке'))

def next_question():
    cor_ques = randint(0, len(questions_list) - 1)
    q = questions_list[cor_ques]
    ask(q)


def click_ok():
    if answer_button.text() == 'Каменный отвечатор':
        check_ans()
    else:
        next_question()

def ask(q: Question):
    shuffle(answers)
    question.setText(q.question_text)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    correct_ans.setText(q.right_ans)
    show_ques()

def check_ans():
    if answers[0].isChecked():
        show_correct('Правильно')
        mw.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно')
    mw.total += 1
    print(f'Статистика\n-Всего вопросов: {mw.total}\n-Правильных ответов: {mw.score}\nРейтинг: {mw.score / mw.total * 100}')

def show_correct(res):
    wrong_ans.setText(res)
    show_res()

def show_res():
    ans_box.hide()
    ans_group.show()
    answer_button.setText('Следующий каменный вопрос')

def show_ques():
    ans_group.hide()
    ans_box.show()

    rad_group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    rad_group.setExclusive(True)

    answer_button.setText('Каменный отвечатор')

def start_test():
    if answer_button.text() == 'Каменный отвечатор':
        show_res()
    else:
        show_ques()

app = QApplication([])

mw = QWidget()

question = QLabel()
question.setText('Каменный вопрос')

answer_button = QPushButton('Каменный отвечатор')

ans_box = QGroupBox('Варианты ответов')

ans1 = QRadioButton('Каменный ответ 1')
ans2 = QRadioButton('Каменный ответ 2')
ans3 = QRadioButton('Каменный ответ 3')
ans4 = QRadioButton('Каменный ответ 4')

answers = [ans1, ans2, ans3, ans4]

rad_group = QButtonGroup()
rad_group.addButton(ans1)
rad_group.addButton(ans2)
rad_group.addButton(ans3)
rad_group.addButton(ans4)

h_layout1 = QHBoxLayout()
layout_group1 = QVBoxLayout()
layout_group2 = QVBoxLayout()

main_layout = QVBoxLayout()
main_layout.setSpacing(25)

layout_group1.addWidget(ans1, alignment = Qt.AlignHCenter)
layout_group1.addWidget(ans2, alignment = Qt.AlignHCenter)
layout_group2.addWidget(ans3, alignment = Qt.AlignHCenter)
layout_group2.addWidget(ans4, alignment = Qt.AlignHCenter)

h_layout1.addLayout(layout_group1)
h_layout1.addLayout(layout_group2)

ans_box.setLayout(h_layout1)

ans_group = QGroupBox('Результат каменного теста')
wrong_ans = QLabel('Правильно/Неправильно')
correct_ans = QLabel('Правильный ответ')

layout_result = QVBoxLayout()
layout_result.addWidget(wrong_ans, alignment = Qt.AlignLeft)
layout_result.addWidget(correct_ans, stretch= 2, alignment = Qt.AlignCenter)

ans_group.setLayout(layout_result)
ans_group.hide()

main_layout.addWidget(question, alignment = Qt.AlignHCenter)
main_layout.addWidget(ans_box)
main_layout.addWidget(ans_group)
main_layout.addWidget(answer_button, alignment = Qt.AlignHCenter)

mw.setLayout(main_layout)

answer_button.clicked.connect(click_ok)
mw.total = 0
mw.score = 0
next_question()


mw.resize(400, 300)
mw.show()
app.exec_()