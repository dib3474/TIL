#include <stdio.h>

int main() {
  int number;
  scanf("%d", &number);
  int N = number;
  int i=0;
  do{
    if(N/10==0){
      N = N*10 + N;
    }
    else {
      int A, B;
      A = N/10;
      B = N%10;
      N = B*10 + ((A+B)%10);
    }
    i++;
  } while(number != N);
  printf("%d", i);
}