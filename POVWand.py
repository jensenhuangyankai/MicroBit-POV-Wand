from microbit import *
import utime
import math
letters = {
"a" : ['99999:', '90009:', '90009:', '99999:', '90009'],
"b" : ['99999:', '90009:', '99990:', '90009:', '99999'],
"c" : ['99999:', '90000:', '90000:', '90000:', '99999'],
"d" : ['99990:', '90009:', '90009:', '90009:', '99990'],
"e" : ['99999:', '90000:', '99990:', '90000:', '99999'],
"f" : ['99999:', '90000:', '99900:', '90000:', '90000'],
"g" : ['99999:', '90000:', '90099:', '90009:', '99999'],
"h" : ['90009:', '90009:', '99999:', '90009:', '90009'],
"i" : ['99999:', '00900:', '00900:', '00900:', '99999'],
"j" : ['00099:', '00009:', '00009:', '90009:', '99999'],
"k" : ['90009:', '90090:', '99900:', '90090:', '90009'],
"l" : ['90000:', '90000:', '90000:', '90000:', '99999'],
"m" : ['90009:', '99099:', '90909:', '90009:', '90009'],
"n" : ['90009:', '99009:', '90909:', '90099:', '90009'],
"o" : ['09990:', '90009:', '90009:', '90009:', '09990'],
"p" : ['99990:', '90009:', '99990:', '90000:', '90000'],
"q" : ['99999:', '90009:', '90009:', '99999:', '00900'],
"r" : ['99990:', '90009:', '99990:', '90009:', '90009'],
"s" : ['99999:', '90000:', '99999:', '00009:', '99999'],
"t" : ['99999:', '00900:', '00900:', '00900:', '00900'],
"u" : ['90009:', '90009:', '90009:', '90009:', '99999'],
"v" : ['90009:', '90009:', '09090:', '09090:', '00900'],
"w" : ['90009:', '90009:', '90909:', '90909:', '09090'],
"x" : ['90009:', '09090:', '00900:', '09090:', '90009'],
"y" : ['90009:', '90009:', '09090:', '00900:', '00900'],
"z" : ['99999:', '00090:', '00900:', '09000:', '99999'],
"space" : ['00000:', '00000:', '00000:', '00000:', '00000'],
}
phrase = "LMAO" # <<< CHANGE THIS VALUE FOR DIFFERENT WORDS
phrase = phrase.lower()
counter = 0
dirCount = 0
x = accelerometer.get_x()
y = accelerometer.get_y()
z = accelerometer.get_z()
initial_acceleration = math.sqrt(x**2 + y**2 + z**2)
while True:
    for letter in phrase:
        accelDiff = 0
        displayList = []
        for col in range(5):
            tempString = ''
            for row in letters[letter]:
                tempString += row[col]
            displayList.append(tempString)
    
        #print(displayList)
        newDisplayString = ""
        for line in displayList:
            for dot in line:
                if counter < 4:
                    newDisplayString += "00"+dot+"00" + ":"
                    counter += 1
                else:
                    newDisplayString += "00"+dot+"00"
                    counter = 0
            #print(newDisplayString)
            dirChange = False
            x = accelerometer.get_x()
            y = accelerometer.get_y()
            z = accelerometer.get_z()
            
            acceleration = math.sqrt(x**2 + y**2 + z**2)
            
            accelDiff = acceleration - initial_acceleration
            print(accelDiff)
            
            utime.sleep_ms(200)
            display.show(Image(newDisplayString))
            if accelDiff > 200:
                dirChange = True
                dirCount += 1
            if (dirCount = 2):
                display.clear()
            newDisplayString = ""
            utime.sleep_ms(400)
            display.clear()
            if dirCount == 2:
                dirCount = 0
    display.clear()
    utime.sleep_ms(300)