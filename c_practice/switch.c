#include <stdio.h>

int main()
{
    int slices = 3;

    switch(slices)
    {
        case 1:
            printf("you did a great job!");
            break;
        case 2:
            printf("you did an ok job");
            break;
        case 3:
            printf("you did a bad job");
            break;
    }
    return 0;
}