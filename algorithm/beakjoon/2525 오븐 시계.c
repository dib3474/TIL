#include <stdio.h>

int main() {
  int h,m,c;
  scanf("%d %d",&h,&m);
  scanf("%d", &c);
  
  if((m+c)%60 > 0){
  	h += (m+c)/60;
  	m = (m+c)%60;
  }
  else{
  	h += (m+c)/60;
  	m = 0;
  }
  if(h>=24){
  	h %= 24;
  }
  
  printf("%d %d", h, m);
}
