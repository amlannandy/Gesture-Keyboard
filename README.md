# Gesture-Keyboard

The gesture keyboard module consists of an Arduino Nano micro-processor with an MPU-6050 attached to it, which is turned on and off by a switch. Keeping the button pressed, one has to draw the alpha-numeric character they want to type. It captures the movement of the module through its 6 axis(accelerometer + gyro) and compares it against the 1500+ samples that we have recorded beforehand and predicts the correct character.

We use pyGARL (Python Gesture Analysis and Recognition Library), a Python library which uses SVM (Support Vector Machine) algorithms to analyze the samples that we have recorded and normalizes the data. When the module records a movement, it matches it against the normalized data and predicts the correct one.
