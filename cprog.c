#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // creates an array pointer to traverse the arguments
    int *arrayPtr = NULL;
    arrayPtr = (int *) malloc((argc - 1) * sizeof(int));
    
    // exits if there is an error reading the arguments
    if (arrayPtr == NULL) {
        printf("Halting: Unable to allocate array.\n");
        exit(1);
    }

    // iterate through the arguments
    // prints either 0 or 255 if the current argument value is above/below the threshold
    for (int i = 1; i < argc; i++) {
        arrayPtr[i - 1] = atoi(argv[i]);
        if (arrayPtr[i - 1] > 170) {
            printf("255 ");
        } else {
            printf("0 ");
        }
    }


    // freeing the array pointer
    free(arrayPtr);
    arrayPtr = NULL;
    return 0;
}