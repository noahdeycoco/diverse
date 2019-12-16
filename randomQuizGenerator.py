# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
import os

# The quiz data. Keys are states and values are their capitals.

capitals = {
 'Alabama': 'Montgomery',
 'Alaska': 'Juneau',
 'Arizona': 'Phoenix',
 'Arkansas': 'Little Rock',
 'California': 'Sacramento',
 'Colorado': 'Denver',
 'Connecticut': 'Hartford',
 'Delaware': 'Dover',
 'Florida': 'Tallahassee',
 'Georgia': 'Atlanta',
 'Hawaii': 'Honolulu',
 'Idaho': 'Boise',
 'Illinois': 'Springfield',
 'Indiana': 'Indianapolis',
 'Iowa': 'Des Moines',
 'Kansas': 'Topeka',
 'Kentucky': 'Frankfort',
 'Louisiana': 'Baton Rouge',
 'Maine': 'Augusta',
 'Maryland': 'Annapolis',
 'Massachusetts': 'Boston',
 'Michigan': 'Lansing',
 'Minnesota': 'Saint Paul',
 'Mississippi': 'Jackson',
 'Missouri': 'Jefferson City',
 'Montana': 'Helena',
 'Nebraska': 'Lincoln',
 'Nevada': 'Carson City',
 'New Hampshire': 'Concord',
 'New Jersey': 'Trenton',
 'New Mexico': 'Santa Fe',
 'New York': 'Albany',
 'North Carolina': 'Raleigh',
 'North Dakota': 'Bismarck',
 'Ohio': 'Columbus',
 'Oklahoma': 'Oklahoma City',
 'Oregon': 'Salem',
 'Pennsylvania': 'Harrisburg',
 'Rhode Island': 'Providence',
 'South Carolina': 'Columbia',
 'South Dakota': 'Pierre',
 'Tennessee': 'Nashville',
 'Texas': 'Austin',
 'Utah': 'Salt Lake City',
 'Vermont': 'Montpelier',
 'Virginia': 'Richmond',
 'Washington': 'Olympia',
 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison',
 'Wyoming': 'Cheyenne'}


def create_dir():
    try:
        if os.path.isdir('quiz/'):
            print('\'quiz/\' already exists.')
            return
        else:
            os.mkdir('quiz/')
            print('A new file has been created to: ' +
                  str(os.path.realpath('quiz/')))
    except Exception:
        print('An error occured: ' + str(Exception))


def create_quiz():
    try:
        # Generate 35 quiz files.
        for quizNum in range(35):
            # TODO: Create the quiz and answer key files.
            quizFile = open('quiz/capitalsquiz%s.txt' % (quizNum + 1), 'w')
            answerKeyFile = open('quiz/capitalsquiz_answers%s.txt' %
                                 (quizNum + 1), 'w')
            # TODO: Write out the header for the quiz.
            quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
            quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' %
                           (quizNum + 1))
            quizFile.write('\n\n')
            # TODO: Shuffle the order of the states.
            states = list(capitals.keys())
            random.shuffle(states)

        print(str(len([name for name in os.listdir('quiz/') if
              os.path.isdir('quiz/')])) + ' files has been created.')
        return states
    except Exception:
        print('An error occured: ' + str(Exception))


def answer_quiz():
    try:
        # Loop through all 50 states, making a question for each.
        for questionNum in range(1, 50):
            # Get right and wrong answers.
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)
            # Question and answer options to the quiz file.
            correctCapital = [key for key, value in capitals.items()
                              if value == correctAnswer]
            for quizNum in range(35):
                quizFile = open('quiz/capitalsquiz%s.txt' % (quizNum + 1), 'a')
                answerKeyFile = open('quiz/capitalsquiz_answers%s.txt' %
                                     (quizNum + 1), 'a')
                quizFile.write('\n\n%s. What is the capital ' % (questionNum) +
                               ' of %s between ' % (''.join(correctCapital)) +
                               ' these answers : \n')
                for i in range(4):
                    quizFile.write('\t %s. ' % ('ABCD'[i]) +
                                   '%s' % (answerOptions[i]))

                answerKeyFile.write('%s. %s\n' % (questionNum, 'ABCD'[
                                    answerOptions.index(correctAnswer)]))
        print('All questions has been written as well as the answers.')
    except Exception:
        print('An error occured: ' + str(Exception))


if __name__ == '__main__':
    create_dir()
    # create_quiz()
    states = create_quiz()
    answer_quiz()
