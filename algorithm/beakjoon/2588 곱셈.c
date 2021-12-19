#include <stdio.h>
int main(){
  int A,B,C[3];
  scanf("%d",&A);
  for(int i=0;i<3;i++){
    scanf("%1d", &C[i]);
  }
  B = C[0]*100 + C[1]*10 + C[2];
  printf("%d\n",A*C[2]);
  printf("%d\n",A*C[1]);
  printf("%d\n",A*C[0]);
  printf("%d\n",A*B);
}