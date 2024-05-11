import cv2
import mediapipe as mp
import numpy as np
import time
import os
from PIL import Image 


# Function used to convert the image to ascii
def imageToAscii(image): 
    # image.show()
    
    width, height = image.size
    image = image.resize((width//4, height//4))
    # image.show() 
    ascii_1 = "."
    ascii_2 = ","
    ascii_3 = "-"
    ascii_4 = "^"
    ascii_5 = "="
    ascii_6 = "+"
    ascii_7 = "/"
    ascii_8 = "$"
    ascii_9 = "#"

    #convert to array
    img_array = np.asarray(image)
    img_shape = img_array.shape
    img_rows, img_col = img_shape[0], img_shape[1]
    print(img_rows)
    print(img_col)
    buffer = [[0]*img_col]*img_rows
    color_values = [0,0,0]
    color_average = 0

    for i in range(len(img_array)):
        for j in range(len(img_array[i])):
            for z in range(len(img_array[i][j])):
                color_values[z] = img_array[i][j][z]
            color_average = int(sum(color_values)/len(color_values))
            if color_average < 30:
                buffer[i][j] = ascii_1
            elif color_average > 30 and color_average < 60:
                buffer[i][j] = ascii_2
            elif color_average > 60 and color_average < 90:
                buffer[i][j] = ascii_3
            elif color_average > 90 and color_average < 120:
                buffer[i][j] = ascii_4
            elif color_average > 120 and color_average < 150:
                buffer[i][j] = ascii_5
            elif color_average > 150 and color_average < 180:
                buffer[i][j] = ascii_6
            elif color_average > 180 and color_average < 210:
                buffer[i][j] = ascii_7
            elif color_average > 210 and color_average < 240:
                buffer[i][j] = ascii_8
            else:
                buffer[i][j] = ascii_9

    for i in range(len(buffer)):
        for j in range(len(buffer[i])):
            print(buffer[i][j], end="")
        print("")

    # print(buffer)
    # print("")
    # print(img_array)
    # print(img_array.shape)
    # print("")
    

    


# function to display prompt 
def displayPrompt(): 
    # Display Prompt
    print("")
    print("Choose from the following options:")
    print("")
    print("1.  Use an image in current directory.")
    print("2.  Use an image captured by Camera.")
    print("")
    print("Please return 1 or 2")
    print("") 
    # Scan in the user input
    user_input = int(input(""))

    return user_input

# main function 
def main(): 
    #Display the prompt 
    # os.system("clear")
    # user_input = displayPrompt() 
    # print(type(user_input))
    # 
    # # Check if input is what is needed
    # while user_input not in [1,2]:
    #     print("")
    #     print("Error: Return 1 or 2")   # Return error
    #     print("")
    #     time.sleep(1)                   # Sleeep
    #     os.system("clear")
    #     user_input = displayPrompt()    # Ask prompt again 

    # # if user image input:
    # if user_input == 1:
    #     os.system("clear")
    #     
    #     #Take in users input
    #     print("1.  Use an image in current directory.")
    #     print("")
    #     print("")
    #     print("Please enter the file name of the image:")
    #     image_user_input = input()
    #     image_is_not_good = True 
    #     while image_is_not_good: 
    #         try:
    #             image = Image.open(image_user_input) 
    #             image_is_not_good = False 
    #         except FileNotFoundError:
    #             print("")
    #             print("Error: No Such file in directory, please try again.")
    #             time.sleep(1)
    #             os.system("clear")
        
        # convert image to black and white 
        image = Image.open("test.jpeg") 
        # # print out properites
        # print(image.format) 
        # print(image.size)
        # print(image.mode)
        imageToAscii(image)

    # else:
    #     #TODO Capture image funtion 
    #     pass


    

if __name__ == '__main__':
    main()
