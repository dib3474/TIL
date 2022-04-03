#include <stdio.h>

int main(){
	int n, max=0;
	scanf("%d", &n);
	float d[n], result;
	for(int i=0; i<n; i++){
		scanf("%f", &d[i]);
		if(d[i] > max){
			max = d[i];
		}
	}
	for(int i=0; i<n; i++){
		d[i] = (d[i]/max) * 100;
		result += d[i];
  }
  printf("%f", result/n);
}
