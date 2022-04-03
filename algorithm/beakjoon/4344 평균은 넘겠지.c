#include <stdio.h>

int main(){
	int c;
	scanf("%d", &c);
	
	for(int i=0; i < c; i++){
    int n, cnt = 0, sum = 0;
    scanf("%d", &n);
    int a[n];
    for(int j=0; j < n; j++){
      scanf("%d", &a[j]);
		  sum += a[j];
    }
    for(int k=0; k < n; k++){
		  if (a[k] > (float)sum/n){
			  cnt += 1;
		  }
	  }
		printf("%.3f%%\n", (float)(cnt/n)*100);
	}
}
