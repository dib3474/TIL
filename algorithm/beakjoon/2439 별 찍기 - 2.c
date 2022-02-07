#include <stdio.h>

int main() {
  int T, i;
  scanf("%d", &T);
  for(i = 1; i<=T; i++){
    int t = T-i;
    for(; t > 0; t--){
      printf(" ");
    }
    for(int j = 1; j<=i; j++){
      printf("*");
    }
    printf("\n");
  }
}