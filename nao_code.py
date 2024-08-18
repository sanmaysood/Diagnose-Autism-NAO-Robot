from naoqi import *
import time
import sys

IP = "192.168.26.16"
PORT = 9559

# Creating all the proxies
manager = ALProxy("ALBehaviorManager", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)
player = ALProxy("ALAudioPlayer", IP, PORT)
speech = ALProxy("ALSpeechRecognition", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)


front_head_touch_detected = False
middle_head_touch_detected = False
back_head_touch_detected = False

gotWord = False
wordFound = None


class ReactToTouch(ALModule):

    def __init__(self,name):
        ALModule.__init__(self,name)
        global memory
        memory.subscribeToEvent("TouchChanged", "ReactToTouch", "onTouched")

    @classmethod

    def onTouched(self, strVarName, value):
       
        global back_head_touch_detected
        global front_head_touch_detected
        global middle_head_touch_detected

        memory.unsubscribeToEvent("TouchChanged", "ReactToTouch")


        # Check each touch sensor
        for p in value:

            # doubt regarding indexing of p
            touched = p[1]
            touch_sensor = p[0]

            if touched:

                if touch_sensor == "Head/Touch/Front":
                    # Set a flag for front head touch detection
                    # positive button
                    front_head_touch_detected = True

                elif touch_sensor == "Head/Touch/Middle":
                    # Set a flag for middle head touch detection
                    # continue button
                    middle_head_touch_detected = True

                elif touch_sensor == "Head/Touch/Rear":
                    # Set a flag for back head touch detection
                    # repeat button
                    back_head_touch_detected = True

                else:
                    continue


        memory.subscribeToEvent("TouchChanged", "ReactToTouch","onTouched")
        print("front head flag ")
        print(front_head_touch_detected)
        print("middle head flag")
        print(middle_head_touch_detected)
        print("back head flag")
        print(back_head_touch_detected)

        


# Module for subscribing to voice recognition event

class voiceModule(ALModule):

    def __init__(self, name):
        ALModule.__init__(self,name)
        global memory
        memory.subscribeToEvent("WordRecognized", "voiceModule", "onWordRecognized")

    @classmethod

    # Function called when the word is recognized
    def onWordRecognized(self, strVarName, value):

        global memory
        global gotWord
        global wordFound


        memory.unsubscribeToEvent("WordRecognized", "voiceModule")

        if not gotWord:
            wordFound = value[0]
            gotWord = True
            print(wordFound)

        memory.subscribeToEvent("WordRecognized", "voiceModule", "onWordRecognized")



# Function for body parts activity
def body_parts():

    global player
    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected

    f = player.loadFile("/home/nao/Desktop/audio/" + 'body_intro.mp3')
    player.play(f)
    time.sleep(1)


    #Head
    while True:
        manager.runBehavior("behaviours/head")
        f = player.loadFile("/home/nao/Desktop/audio/" + 'head.mp3')
        player.play(f)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'headAsk.mp3')
        player.play(f)

        # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
        while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)
       
        if front_head_touch_detected:
            # Positive button action
            manager.runBehavior("finalcode-048bcc/body_positive")
            front_head_touch_detected = False
            break

        elif middle_head_touch_detected:
            # Negative button action
            manager.runBehavior("finalcode-048bcc/body_negative")
            middle_head_touch_detected = False
            break

        elif back_head_touch_detected:
            # Repeat button action
            f = player.loadFile("/home/nao/Desktop/audio/" + 'tryAgain1.mp3')
            player.play(f)
            back_head_touch_detected = False
            continue
        

    # Eyes
    while True:
        manager.runBehavior("behaviours/eyes")
        f = player.loadFile("/home/nao/Desktop/audio/" + 'eyes.mp3')
        player.play(f)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'eyesAsk.mp3')
        player.play(f)

        # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
        while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)
       
        if front_head_touch_detected:
            # Positive button action
            manager.runBehavior("finalcode-048bcc/body_positive")
            front_head_touch_detected = False
            break

        elif middle_head_touch_detected:
            # Negative button action
            manager.runBehavior("finalcode-048bcc/body_negative")
            middle_head_touch_detected = False
            break

        elif back_head_touch_detected:
            # Repeat button action
            f = player.loadFile("/home/nao/Desktop/audio/" + 'tryAgain1.mp3')
            player.play(f)
            back_head_touch_detected = False
            continue
        

    # Chest
    while True:
        manager.runBehavior("behaviours/chest")
        f = player.loadFile("/home/nao/Desktop/audio/" + 'chest.mp3')
        player.play(f)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'chestAsk.mp3')
        player.play(f)

        # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
        while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)
       
        if front_head_touch_detected:
            # Positive button action
            manager.runBehavior("finalcode-048bcc/body_positive")
            front_head_touch_detected = False
            break

        elif middle_head_touch_detected:
            # Negative button action
            manager.runBehavior("finalcode-048bcc/body_negative")
            middle_head_touch_detected = False
            break

        elif back_head_touch_detected:
            # Repeat button action
            f = player.loadFile("/home/nao/Desktop/audio/" + 'tryAgain1.mp3')
            player.play(f)
            back_head_touch_detected = False
            continue
    
    #Arms
    while True:
        manager.runBehavior("behaviours/Hands")
        f = player.loadFile("/home/nao/Desktop/audio/" + 'Hands.mp3')
        player.play(f)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'handsAsk.mp3')
        player.play(f)

        # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
        while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)
       
        if front_head_touch_detected:
            # Positive button action
            manager.runBehavior("finalcode-048bcc/body_positive")
            front_head_touch_detected = False
            break

        elif middle_head_touch_detected:
            # Negative button action
            manager.runBehavior("finalcode-048bcc/body_negative")
            middle_head_touch_detected = False
            break

        elif back_head_touch_detected:
            # Repeat button action
            f = player.loadFile("/home/nao/Desktop/audio/" + 'tryAgain1.mp3')
            player.play(f)
            back_head_touch_detected = False
            continue




# Function for frog jumps activity
def frog_jumps():
    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected

    while True:

        manager.runBehavior("finalcodeup-ff769a/frog_jumps")

        # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
        while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)

        if front_head_touch_detected:
            # Positive button action
            manager.runBehavior("finalcode-048bcc/clapping")
            front_head_touch_detected = False
            break

        elif middle_head_touch_detected:
            # Negative button action
            manager.runBehavior("finalcode-048bcc/negative")
            middle_head_touch_detected = False
            break

        elif back_head_touch_detected:
            # Repeat button action
            f = player.loadFile("/home/nao/Desktop/audio/" + 'tryAgain1.mp3')
            player.play(f)
            back_head_touch_detected = False
        
        

# Function for rolly polly activity
def rhyme():
    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected
    
    while True:
        f = player.loadFile("/home/nao/Desktop/audio/" + 'dance.mp3')
        player.play(f)
        time.sleep(1)
        manager.runBehavior('behaviours/rolly_polly')

        # Wait for the middle head touch sensor (Continue button) or rear head touch sensor (Repeat button) to be activated
        while not (middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)

        if back_head_touch_detected:
            # Repeat button action
            back_head_touch_detected = False
            continue

        else:
            # Continue button action
            manager.runBehavior("finalcode-048bcc/clapping")
            middle_head_touch_detected = False
            break

        
# Function for cards matching activity
def cardsMatch():
    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected
    while True:
        f = player.loadFile("/home/nao/Desktop/audio/" + 'giveCard.mp3')
        player.play(f) 
        manager.runBehavior("finalcode-048bcc/grab")

        # Wait for touch on middle head touch sensor (Continue button)
        while not middle_head_touch_detected:
            time.sleep(0.1)

        # Reset touch sensor flag for the next iteration
        middle_head_touch_detected = False

        while True:
            # Run the "card_matching" behavior
            manager.runBehavior("finalcode-048bcc/card_matching")

            # Wait for either the middle head touch sensor (Continue button) or rear head touch sensor (Repeat button) to be activated
            while not (middle_head_touch_detected or back_head_touch_detected):
                time.sleep(0.1)

            # Determine which touch sensor was activated
            if middle_head_touch_detected:
                # Continue button action: Break out of the loop to continue
                middle_head_touch_detected = False
                break

            elif back_head_touch_detected:
                # Repeat button action: Run the "repeat" behavior
                manager.runBehavior("finalcode-048bcc/repeat")
                # Reset the touch sensor flags for the next iteration
                back_head_touch_detected = False
                continue

        manager.runBehavior("finalcode-048bcc/return_card")

        # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
        while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)

        if front_head_touch_detected:
            # Positive button action
            manager.runBehavior("sanmay-e0b42a/fist_bump")
            front_head_touch_detected = False
            break

        elif middle_head_touch_detected:
            # Negative button action
            manager.runBehavior("finalcode-048bcc/negative")
            middle_head_touch_detected = False
            break

        elif back_head_touch_detected:
            # Repeat button action
            back_head_touch_detected = False
            continue
            


# Function for pointing activity
def pointing():
    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected

    while True:

        while True:
            f = player.loadFile("/home/nao/Desktop/audio/" + 'reinforce1.mp3')
            player.play(f)
            manager.runBehavior('behaviours/wave_left')

            # Wait for the middle head touch sensor (Continue button) or rear head touch sensor (Repeat button) to be activated
            while not (middle_head_touch_detected or back_head_touch_detected):
                time.sleep(0.1)

            if back_head_touch_detected:
                back_head_touch_detected = False
                continue

            else:
                middle_head_touch_detected = False
                break
    

        while True:
            # Point left
            f = player.loadFile("/home/nao/Desktop/audio/" + 'pleft.mp3')
            manager.runBehavior("behaviours/pleft")
            player.play(f)
            manager.runBehavior("behaviours/pleft_front")
            f = player.loadFile("/home/nao/Desktop/audio/" + 'objectNames.mp3')
            player.play(f)

            # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
            while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
                time.sleep(0.1)

            if front_head_touch_detected:
                # Positive button action
                manager.runBehavior("sanmay-e0b42a/High5")
                front_head_touch_detected = False
                break

            elif middle_head_touch_detected:
                # Negative button action
                manager.post.runBehavior("behaviours/point_left")
                f = player.loadFile("/home/nao/Desktop/audio/" + 'pleftNegative.mp3')
                player.play(f)
                time.sleep(1)
                middle_head_touch_detected = False
                break

            elif back_head_touch_detected:
                # Repeat button action
                back_head_touch_detected = False
                continue


        while True:
            # Point right
            manager.runBehavior("behaviours/point_right")
            f = player.loadFile("/home/nao/Desktop/audio/" + 'pright.mp3')
            player.play(f)
            manager.stopBehavior("behaviours/point_right")
            manager.runBehavior("behaviours/pright_front")
            f = player.loadFile("/home/nao/Desktop/audio/" + 'objectNames.mp3')
            player.play(f)
            time.sleep(1.0)

            # Wait for the front head touch sensor (Positive button), middle head touch sensor (Negative button), or rear head touch sensor (Repeat button) to be activated
            while not (front_head_touch_detected or middle_head_touch_detected or back_head_touch_detected):
                time.sleep(0.1)

            if front_head_touch_detected:
                # Positive button action
                manager.runBehavior("sanmay-e0b42a/High5")
                front_head_touch_detected = False
                break

            elif middle_head_touch_detected:
                # Negative button action
                manager.post.runBehavior("behaviours/point_right")
                f = player.loadFile("/home/nao/Desktop/audio/" + 'prightNegative.mp3')
                player.play(f)
                time.sleep(1)
                middle_head_touch_detected = False
                break

            elif back_head_touch_detected:
                # Repeat button action
                back_head_touch_detected = False
                continue

        break



# Function for peekaboo activity
def peekaboo():

    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected

    while True:
        # namecall
        while True:

            f = player.loadFile("/home/nao/Desktop/audio/" + 'reinforce1.mp3')
            player.play(f)
            manager.runBehavior('behaviours/wave_left')

            # Wait for the middle head touch sensor (Continue button) or rear head touch sensor (Repeat button) to be activated
            while not (middle_head_touch_detected or back_head_touch_detected):
                time.sleep(0.1)

            if back_head_touch_detected:
                # Repeat button action
                back_head_touch_detected = False
                continue

            else:
                middle_head_touch_detected = False
                break

    
        f = player.loadFile("/home/nao/Desktop/audio/" + 'giveCard.mp3')
        player.play(f)
        manager.runBehavior("finalcode-048bcc/peekaboo_grab")

        # Wait for the middle head touch sensor (Continue button) to be activated
        while not middle_head_touch_detected:
            time.sleep(0.1)

        manager.runBehavior("finalcode-048bcc/close_hand")

        manager.runBehavior("behaviours/peek")
        time.sleep(2)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'peekaboo.mp3')
        player.play(f)
        time.sleep(3)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'Booh.mp3')
        manager.runBehavior("behaviours/boo")
        player.play(f)
        time.sleep(4)
        f = player.loadFile("/home/nao/Desktop/audio/" + 'giveCardback.mp3')
        player.play(f)


        middle_head_touch_detected = False
        back_head_touch_detected = False


        # Wait for the middle head touch sensor (Continue button) or rear head touch sensor (Repeat button) to be activated
        while not (middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)

        if back_head_touch_detected:
            back_head_touch_detected = False
            continue

        else:
            middle_head_touch_detected = False
            break



def danceBeg():
    global manager
    global back_head_touch_detected
    global front_head_touch_detected
    global middle_head_touch_detected

    while True:
        manager.runBehavior("finalcode-048bcc/danceBeg")

        # Wait for the middle head touch sensor (Continue button) or rear head touch sensor (Repeat button) to be activated
        while not (middle_head_touch_detected or back_head_touch_detected):
            time.sleep(0.1)

        if back_head_touch_detected:
            back_head_touch_detected = False
            continue

        else:
            middle_head_touch_detected = False
            break



def main():

    broker = ALBroker("pythonBroker","0.0.0.0",0,IP,9559)

    react_to_touch = ReactToTouch("ReactToTouch")


    global front_head_touch_detected
    global middle_head_touch_detected
    global back_head_touch_detected

    intro = False

    while not (front_head_touch_detected or middle_head_touch_detected):
        time.sleep(0.1)

    if(front_head_touch_detected):
        front_head_touch_detected = False
        intro = True

    else:
        middle_head_touch_detected = False
        intro = False


    if(intro):

        manager.post.runBehavior('behaviours/wave_left')

        f = player.loadFile("/home/nao/Desktop/audio/" + 'namaste.mp3')
        player.play(f)
        time.sleep(1)



        # Greeting the instructor

        # Wait for touch on middle head touch sensor (Continue button)
        while not  middle_head_touch_detected:
            time.sleep(0.1)


        # Reset touch sensor flag for the next iteration
        middle_head_touch_detected = False


        while(manager.isBehaviorRunning("behaviours/wave_left")):
            continue


        manager.post.runBehavior('behaviours/talking4')
        f = player.loadFile("/home/nao/Desktop/audio/" + 'ashwini.mp3')
        player.play(f)
        time.sleep(1)

     
        # Wait for touch on middle head touch sensor (Continue button)
        while not middle_head_touch_detected:
            time.sleep(0.1)



        # Reset touch sensor flag for the next iteration
        middle_head_touch_detected = False

        manager.post.runBehavior('behaviours/wave_left')
        f = player.loadFile("/home/nao/Desktop/audio/" + 'childAsk.mp3')
        player.play(f)
        time.sleep(1)

        # Counter response to the child

        # Wait for touch on middle head touch sensor (Continue button)
        while not middle_head_touch_detected:
            time.sleep(0.1)

        # Reset touch sensor flag for the next iteration
        middle_head_touch_detected = False

        while(manager.isBehaviorRunning("behaviours/talking4")):
            continue

        f = player.loadFile("/home/nao/Desktop/audio/" + 'counter.mp3')
        player.play(f)
        time.sleep(1)

        # Listing the activities
     
        # Wait for touch on middle head touch sensor (Continue button)
        while not middle_head_touch_detected:
            time.sleep(0.1)

        # Reset touch sensor flag for the next iteration
        middle_head_touch_detected = False

        while(manager.isBehaviorRunning("behaviours/wave_left")):
            continue

        manager.post.runBehavior('behaviours/talking3')
        f = player.loadFile("/home/nao/Desktop/audio/" + 'taskList.mp3')
        player.play(f)
        time.sleep(1)



    vocabulary = ["body", "frog", "move", "card", "point", "hide", "start"]
    global speech
    speech.setLanguage("English")
    speech.pause(True)
    speech.setVocabulary(vocabulary, False)

    # Initialize the voice recognition module
    voice_module = voiceModule("voiceModule")
    speech.pause(False)

    global gotWord
    global wordFound

    while True:

        print("sleep")
        time.sleep(15)

        # Use voice recognition to get the activity choice
        gotWord = False
        wordFound = None

        while not gotWord:
            print("hi")
            time.sleep(0.1)
        

        if wordFound == "body":
            body_parts()
            # print("body is called")

        elif wordFound == "frog":
            frog_jumps()
            # print("frog is called")

        elif wordFound == "move":
            rhyme()
            # print("move is called")

        elif wordFound == "card":
            cardsMatch()                                                  
            # print("card is called")

        elif wordFound == "point":
            pointing()
            # print("point is called")

        elif wordFound == "hide":
            peekaboo()
            # print("hide is called")

        elif wordFound == "start":
            danceBeg()
            # print("start is called")

        # Reset the voice recognition flag
        gotWord = False
        manager.runBehavior("behaviours/stand_slow")
        f = player.loadFile("/home/nao/Desktop/audio/" + 'repeat_ques.mp3')
        player.play(f)



if __name__ == "__main__":

    main()