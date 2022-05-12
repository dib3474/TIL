#include <stdio.h>

int main(){
	int n, cnt = 0, flag, a;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &a);
		flag = 0;
		if (a==1) continue;
		for(int j=2; j<a; j++){
			if(a%j == 0){
				flag = 1;
				break;
			}
		}
		if(flag == 0) cnt += 1;
	}
	printf("%d", cnt);
}
