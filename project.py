import cv2
import numpy as np
import time
import os
from PIL import Image 


# Function used to convert the image to ascii
def imageToAscii(image): 
    # image.show()
    
    width, height = image.size
    image = image.resize((width//5, height//10))
    # image.show() 
    ascii_1 = "."
    ascii_2 = "-"
    ascii_3 = "="
    ascii_4 = "+"
    ascii_5 = "/"
    ascii_6 = "$"
    ascii_7 = "#"

    #convert to array
    img_array = np.asarray(image)
    img_shape = img_array.shape
    img_rows, img_col = img_shape[0], img_shape[1]
    # print(img_rows)
    # print(img_col)
    buffer = [['']*img_col for _ in range(img_rows)]
    color_values = [0,0,0]
    color_average = 0

    for i in range(len(img_array)):
        for j in range(len(img_array[i])):
            for z in range(len(img_array[i][j])):
                color_values[z] = img_array[i][j][z]
            color_average = int(sum(color_values)/len(color_values))
            if color_average < 40:
                buffer[i][j] = ascii_1
            elif color_average < 80:
                buffer[i][j] = ascii_2
            elif color_average < 120:
                buffer[i][j] = ascii_3
            elif color_average < 160:
                buffer[i][j] = ascii_4
            elif color_average < 200:
                buffer[i][j] = ascii_5
            elif color_average < 240:
                buffer[i][j] = ascii_6
            else:
                buffer[i][j] = ascii_7

    for row in buffer:
        print(''.join(row))
    

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

# function to ask user which image file from directory
def imageFromDirectory():
    os.system("clear")
    
    #Take in users input
    print("1.  Use an image in current directory.")
    print("")
    print("")
    print("Please enter the file name of the image:")
    image_user_input = input()
    image_is_not_good = True 
    while image_is_not_good: 
        try:
            image = Image.open(image_user_input) 
            image_is_not_good = False 
        except FileNotFoundError:
            print("")
            print("Error: No Such file in directory, please try again.")
            time.sleep(1)
            os.system("clear")
    
    # convert image to black and white 
    image = Image.open(image_user_input) 
    imageToAscii(image)

# function to caputre image from camera
def imageFromCamera():
    os.system("clear")

    #open the camera to capture images 
    webcam = cv2.VideoCapture(0)
    camera_on = True
    while camera_on:
        check, frame = webcam.read()
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key == ord(" "):
            cv2.imwrite(filename="image.jpeg", img=frame)
            webcam.release()
            cv2.destroyAllWindows()
            image = Image.open("image.jpeg")
            width, height = image.size
            image = image.resize((width//2, height//2))
            camera_on = False
            imageToAscii(image)
        elif key == ord("q"):
            print("Camera Disabled")
            webcam.release()
            print("Program ending")
            cv2.destroyAllWindows()
            camera_on = False
            break


# main function 
def main(): 
    #Display the prompt 
    os.system("clear")
    user_input = displayPrompt() 
    print(type(user_input))
    
    # Check if input is what is needed
    while user_input not in [1,2]:
        print("")
        print("Error: Return 1 or 2")   # Return error
        print("")
        time.sleep(1)                   # Sleeep
        os.system("clear")
        user_input = displayPrompt()    # Ask prompt again 

    # if user image input:
    if user_input == 1:
        imageFromDirectory()
    else:
        imageFromCamera()


if __name__ == '__main__':
    main()
