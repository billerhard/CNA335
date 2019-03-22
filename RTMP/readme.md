Scripting version of the CNA350 project. Scripts go here, instructions on how to set up servery things go there.

Reference for rpi rgb led matrix (specifically 64x64 using adafruit hat) https://github.com/hzeller/rpi-rgb-led-matrix

For my particular HW setup, I used *HARDWARE_DESC=adafruit-hat make* to build the code.

Steps to follow to get this to work:
1. Clone the linked repository.
2. Make (build) the code using the above command.
3. Use the binaries in the examples-api-use directory to familiarize yourself with how the code works to make the display.
4. Tweak options passed to the scripts to make it work better

For my demos, I used a command similar to *sudo ./demo --led-rows=64 --led-cols=64 --led-multiplexing=1*

Don't be surprised if you run into a lot of problems. My 64x64 acted like a 32x64, with 16x0x16x0 strips displaying.
Also had some problems with ghosting/brightness, probably related to random noise on the pi board.
