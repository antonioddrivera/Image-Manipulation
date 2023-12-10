# Image-Manipulation
Utilizes C, Haskell, Prolog, and Matlab to manipulate an image and it all run from a single Python script.

The Python script calls the first Matlab script mprog1.m to take image file and convert it from 2D to 1D and written to a text file (input.txt). The image has to be grayscale to start, so the Matlab program converts it automatically.

Then the Python file takes that input.txt file and passes it into the C program via command line argument. It uses a threshold to convert the unsigned chars to 255 or 0 depending on the char is above or below the threshold.
The output is written into another text file.

The Python file also passes input.txt into the Haskell and Prolog programs, where Haskell creates an output file that inverts the color and Prolog flipped the image.

The second Matlab script takes the output files from C, Haskell, and Prolog and converts them back from 1D to 2D matrices. These 2D matricies are then displayed on figure with labels.

Feel free to swap the image out, however in mprog2.m, make sure to change the dimensional size when reshaping the output files.

*For Window Users*
Windows terminal has a limit to the number of characters that an arguement can use. Therefore, the max size I found works is a 92x92 sized file. The file included is 92x92 and works for windows.
*For Mac and Linux Users*
To my knowledge, the limit (if there is one) is much much greater than windows, so you could use a larger file such as 256x256.
