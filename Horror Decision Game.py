import random
import time

def total_score_increese(score):
    score+=2
    print("your score now is",score) 
    return score       




def total_score_decreese(score):
    score-=2
    print("your score now is",score)
    return score    



def play_game():

    def print_pause(masseg):
        print(masseg)
        time.sleep(2)
    

    
    print_pause('                                                                  WELCOME TO OUR GAME!                                       ')



    print_pause('First we want to know your name ')

    name = input('please enter your name....')

    print('Now we can start!')

    print_pause(name + ", you wake up one day and find your mother and father have gone to your grandmother's and left a paper for you on the shelf next to the bed.")

    print_pause("You got out of bed and you didn't feel any bad, and after you came out of your room, you found the kitchen light on ")
    print_pause("At this moment, will you enter the kitchen or not ? ")


    def kitchen_choice1():
        print('good choice')
        total_score_increese(0)
        print_pause("You made the decision to go to the kitchen, and when you entered, you didn't find anyone")
            
        print_pause("and found the breakfast that your mother had prepared for you ,You heated up that breakfast and ate it, and you were happy and unstressed")
            


    def kitchen_choice2():
        total_score_decreese(0)
        print('Us you like!')
        print_pause("You made the decision not to go to the kitchen, And now you are a bit nervous and now you")
        
        print_pause("Are thinking why your mother did not prepare breakfast for you, So you feel bad and order ")
        print_pause("food for delivery and eat your breakfast while you are nervous")
        


    def kitchine_choice3():
        print_pause("We don't understand you")

    def kitchen_fan():
        while True : 
            kitchen = input(' please answer by yes or no...   ')

            if kitchen == "yes":  
                kitchen_choice1()

            elif kitchen=='no':
                kitchen_choice2()
            if kitchen not in ["yes","no"]:
                continue
            break
        
    kitchen_fan()


            
        



    #start bathroom pragraf

    bathroom_scene = ('You saw a shadow moving outside the bathroom',' you heard a sound in the house, and this sound was somewhat strong ')

    bathroom_random = random.choice(bathroom_scene)

    print_pause("After you had breakfast, you went to the bathroom to take a shower. Buffy, while you were taking a shower")

    print_pause(bathroom_random + ",Then you got scared")
    print_pause("In this case, you have two choices: will you go out ,")
    

    animals = ('cat','dog','monkey')
    the_animal = random.choice(animals)

    def take_showre_choice():
        while True:
            take_shower = input("or will you remain afraid in the bathroom? Answer by yes or no ...    ")
            if take_shower == "yes":
                print('good choice')
                total_score_increese(2)
                print_pause("You chose to get out of the shower and when you do get out you find that it was just your "+ the_animal+ " and ")
                print_pause("nothing else and now you feel relaxed and reassured Then you decided to go to your room")

            elif take_shower == "no":
                print('Us you like!')
                total_score_decreese(2)
                print_pause("You chose not to get out of the bathroom, and now you feel afraid and worried that there was someone outside or not")
                print_pause("And you start finishing quickly to get out of the bathroom and run to your room.")
            if take_shower not in ["yes","no"] :
             continue
            break

    take_showre_choice()

    #start friend scene

    names = ("Mahmoud","Ahmed","Hassan")
    name_random = random.choice(names)

    print_pause("After you went to your room and sat on your bed, you felt a little bored and decided to call a friend of yours called " + name_random + " ,and ")
    time.sleep(1.5)
    print_pause(" you took the phone and called him . Your friend "+name_random +" replied to you and told him that you are alone and invited him ")
    print_pause("to play computer games with you at home He told you he's coming but he'll be a little late because his house is far away")
    print_pause("After you closed with him, you felt that there was a shadow of something moving outside the window, and you felt that someone was watching you")
    print_pause("You felt anxious and afraid because you live on the second floor and no one can look at you from the outside")
    print_pause("After a while, you heard a knock on the back door, and this door is not used by anyone Except in an emergency")
    print_pause("and you looked through the hole in the door and found a short black man with curly hair and in his hand a huge screwdriver.")

    def go_to_freind():
        print_pause("After you decided to go to your friend, and when you approached his house, you noticed that the door was openand ")
        print_pause("you felt that there was no one in the house. Then you approached the door and entered, and found his mother and father killed and dismembered,")
        print_pause(" killed and dismembered, then you heard a voice on the second floor at your friend's room.")

    def you_opned():
        print_pause("You chose to open the door for him, and after he entered, he asked about the electrical panel, so you went to him with it, then he opened it,")
        print_pause("and after you gave him your back, he tried to attack you, and he hit you with a screwdriver on your leg, but you tried to resist him and ")
        print_pause("you ran away from him and went to your room and closed the door on yourself,")
        print_pause("so he tried to enter you and tried to break the door and you found it The window is open, so think quickly,")
        

    def choice_the_room_fan():
        while True:
            choice_the_room = (input(" will you get out of the window or go under your bed ? answer by" "  1  " "or" "  2   "    ))


            if choice_the_room == "1":
                
                total_score_increese(6)
                print_pause("You chose to escape from the window. After you go out, you will find a ladder, but it is a little far from you,")
                print_pause("so you try to reach it, and you actually reach it and go down and run away then you hear the sound of the man ")
                print_pause("breaking the door and entering and not finding you, so he goes out and searches for you in the whole house," )
                print_pause("so you leave the whole area and go to your friend " + name_random)
                go_to_freind()
                
            elif choice_the_room == "2":
                
                total_score_decreese(6)
                print_pause("You chose to hide under the bed. At this moment, the man breaks the door and enters.")
                print_pause("He searches for you and finds you under the bed. He takes you out, and you try to escape from him")
                time.sleep(1)
                print_pause("but to no avail. He hits you twice with the big screwdriver on your head, so you lose consciousness, but before you close your eyes")
                print_pause(" you see another man enter with a knife in his hand, and he ends your life.")
                print_pause("You lost!")
                print_pause("                                              Game over                                       ")
                time.sleep(1.5)

                play_again()
               
            if choice_the_room not in ["1","2"] :
                continue
            break



    def dont_open():
        print_pause("You reply to him that you do not want any electricity maintenance, and he replies to you that ")
        print_pause("he must look into the electricity and insist on entering, so you are afraid of that, so you think a little, then you")
        print_pause("ask for his name to contact the electricity company, but he does not answer you, then you repeat the question, so he says that")
        print_pause("he does not want to enter, and in his voice hesitation And he turns away ")
        print_pause("After that you rest a bit and go out and go to your friend "+ name_random +" Because he was late for the appointment ")

    def door_choice():
        while True:
            door_open = (input('Will you open for him and let him in or not ,  Answer by yes or no ...    '))

            if door_open == "yes":
                
                total_score_decreese(4)
                you_opned()
                choice_the_room_fan()
                

            elif door_open == "no":
                
                total_score_increese(4)

                dont_open()
                go_to_freind()
                

            if door_open not in ["yes","no"]:
                continue
            break

    door_choice()

    #start go to your freind

    def Climb_up():
        
        total_score_decreese(6)
        print_pause("You chose to go up the stairs, then as soon as you go up and look at your friend's room, you find a man holding ")
        print_pause("an ax full of blood,and in his other hand is your friend's head, then he hears your voice and runs towards you")
        print_pause("and grabs you, so you scream, then he puts his hand on your mouth, pulls out the ax and cuts off your head")
        print_pause("You lost!")
        print_pause("                                              Game over                                       ")
        time.sleep(1.5)

        play_again()

    def dont_Climb_up():
        
        total_score_increese(6)
        print_pause("You chose not to go up, and now you feel very afraid and terrified, then you run towards the door to escape,")
        print_pause("then you find a man who comes towards the door and enters, so you try to hide under the furniture, so the man climbs upstairs,")
        print_pause("so you run out of the house quickly in fear, and you reach an old waste bin, so you stop to take a break and look at the box")
        print_pause("and you find The remains of a body and blood, and you look at the face of the body, and you find it your picture !!!! ")
        
        print_pause("At this moment, you wake up to your mother's voice, and it's all a nightmare....... ")
        print_pause("If you have reached this stage, congratulations, you have finished the game ")
        play_again()

    
        


    def climb_house():
        while True:
            Climb_up_the_ladder = (input('At this moment, will you go up to see what is happening, or will you run away? , answer with yes or no...   '))

            if Climb_up_the_ladder =="yes":
                Climb_up()

            elif Climb_up_the_ladder =="no":
                dont_Climb_up()


            if Climb_up_the_ladder not in ["yes","no"] :
                continue
            break

    climb_house()



    

def play_again():
    while True:
        play_again_input = (input("if you want to play again answer by y/n .....   "))

        if play_again_input == 'y':
            play_game()

        elif play_again_input =="n":
            print("                                                     End Game                                             ")
        else:
            print("we dont understand you")
            continue
        break

def start_game():
    while True:
        
        start = (input(" When you be redy write start ...   "))
        if start == "start":
            play_game()
        else:
            print("Try write it again")
            continue
        break

start_game()


