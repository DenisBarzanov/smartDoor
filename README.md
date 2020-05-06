# Smart Door Lock

The project consists of a raspberry pi, a linear 12V actuator, 2 relays and two nMOSFETs 
The raspberry pi commands the transistors, which control the actuator and power the relays.
## Image
![Project image](https://lh3.googleusercontent.com/N7hNGYE4esqmywIHXbgOugEUkQujYg5YNEru3TXx3LZqplen-LH_G4zHsjaH2YCORZMTuUF2eCo5TnvamNLUyTbhyVVTmkKnR6pmUsMwsWSXHsEV-M5QrXJsaQLMciu7fnCmZ8DOWdXrhZpL4satATBX6lQxf8U)

## Schematic
![schematic image](https://i.ibb.co/bXktv73/Schematic-Lock-controller-2020-05-06-17-44-32.png "Schematic image")

<br/>
It uses two trigger SPDT relays in a reverse polarity configuration to reverse the power of the actuator to retract it.

![Reverse polarity relays](https://i.pinimg.com/originals/90/30/9d/90309d2d122e52f8f27ab058eae3af24.gif)

Other than that it uses the face recognition code from [this tutorial](https://maker.pro/raspberry-pi/projects/how-to-create-a-facial-recognition-door-lock-with-raspberry-pi). 

[Video](https://photos.app.goo.gl/HcvL9oxe5uwYwL7U7)
