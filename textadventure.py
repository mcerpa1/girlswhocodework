#Beginning of Game
start = '''You hear the annoying alarm clock, but you barely have the strength
to get out of bed. You see the bus mosing down the street out of the foggy
window and wonder if it's worth going. The true question is to ditch or not
to ditch.'''


print(start)

#Go to School or Ditch
done = False

while not done:
    print("Type 'Go' to go to school or 'Ditch' to go to the city.")
    user_input = input()

    if user_input == "Go":
        print("You barely make it to the bus and ponder was it really worth it.")
        done = True
    #Go to School
        pause = False
        while not pause:
            print('''You end up at school unfortunatley, but forgot first period
            was with the old, infuriating teacher. Once you get to class, you
            hear the groans of the other students as they tell you there is a
            pop quiz. Do you cheat or not? Type 'Yes' to cheat or 'No' to use
            your brain.''')

            user_input = input()
            if user_input == "Yes":
                print('''The teacher was looking at her a computer when a
                student yells out that you were using your phone to cheat...

                THE END''')
                pause = True
            elif user_input == "No":
                print('''As she is handing out the quiz, someone from the office
                enter the room. The women calls your name and says you are
                leaving early.

                THE END''')
                pause = True
            else:
                print("Wrong option")
                pause = False

    #Ditch School
    elif user_input == "Ditch":
        print('''You chose to ditch and leave through the back door to head to the
        city.''')
        done = True
            #after user input is "ditch school"
        xy = False
        while not xy:
            print('''When you escape through the backdoor, you want to meet your
            friends but don't know if it worth it to take the shortcut or not.
            Type 'Yes' for the the short cut and 'No'to go the long way.''')
            user_input = input()
            if user_input == "Yes":
                print('''As you are going through the shortcut, there is an
                officer looking straight out you. He calls you over...
                and makes you back to school.

                THE END''')
                xy = True
            elif user_input == "No":
                print('''Along the long way, you found a street festival taking
                place. You texted all your friends to meet you there.

                THE END''')
                xy = True
            else:
                print("Wrong option")
                xy = False 
    else:
        print("Wrong option")
        done = False
