#include <stdio.h>
int main(){
  int N;
  scanf("%d", &N);
  if(N%4==0){
      if(!(N%100==0)) printf("1");
      else if(N%400==0) printf("1");
      else printf("0");
  }
  else printf("0");
}