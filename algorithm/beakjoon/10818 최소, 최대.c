#include <stdio.h>

int main() {
  int N, a, max=-1000001, min=1000001;
  scanf("%d", &N);
  for(int i=0; i<N; i++){
    scanf("%d", &a);
    if(a > max){
      max = a;
    }
    if(a < min){
      min = a;
    }
  }
  printf("%d %d", min, max);
}