import time

def speed_typing_test():
    # prompt user to start the test
    input("Press Enter to start the typing test...")
    
    # set up the test
    test_string = "The quick brown fox jumps over the lazy dog"
    print("Type the following text:\n")
    print(test_string + "\n")
    
    # track the start time
    start_time = time.time()
    
    # ask the user to type the text
    user_input = input()
    
    # track the end time
    end_time = time.time()
    
    # calculate and display the results
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    wpm = words_typed / (time_taken / 60)
    
    print("You typed", words_typed, "words in", round(time_taken, 2), "seconds.")
    print("That's a speed of", round(wpm, 2), "words per minute!")

# run the test
speed_typing_test()
