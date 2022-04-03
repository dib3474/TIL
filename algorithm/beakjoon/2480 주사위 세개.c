#include <stdio.h>
int main(){
	int a,b,c, max, money;
	scanf("%d %d %d", &a, &b, &c);
	max = a;
	if(b > max) max = b;
	if(c > max) max = c;
	if(a==b && b==c) money = 10000 + a*1000;
	else if(a==b) money = 1000 + a*100;
	else if(b==c)	money = 1000 + b*100;
	else if(c==a) money = 1000 + c*100;
	else money = max*100;
	printf("%d", money);
}
