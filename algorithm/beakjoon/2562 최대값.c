#include <stdio.h>

int main() {
  int a, max = 0, count = 0;
  for(int i = 0; i < 9; i++){
    scanf("%d", &a);
    if(a > max){
      max = a;
      count = i;
    }
  }
  printf("%d\n%d", max, count);
}