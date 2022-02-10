#include <stdio.h>

int min4(int a, int b, int c, int d){
    int min = a;
    if(b<min) min = b;
    if(c<min) min = c;
    if(d<min) min = d;
    return min;
}

int main() {
    printf("min4(%d, %d, %d, %d) = %d\n", 2, 3, 3, 4, min4(2, 3, 3, 4));
}