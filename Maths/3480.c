#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
 
typedef unsigned long long ull;
 
int main() {
	ull n; scanf("%llu", &n);
	if (n==1) {printf("1");return 0;}

	// 埃式筛法：寻找出小于根号n的所有质数
	ull root = (ull)sqrt(n);
	char* is_prime = malloc(sizeof(char)*root);
	memset(is_prime, (char)1, root);
	is_prime[0] = is_prime[1] = 0;
	for (ull i=2; i<=root; i++) {
		ull sq = (ull)i*i;
		if (sq > root) break;
		for (ull j=sq; j<=root; j+=i) {
			is_prime[j]=0;
		}
	}
	ull m=1;

	ull n2=n;
	for (ull i=2; i<=root; i++) {
		int count=0;
		if (is_prime[i]) {
			while (n2 % i ==0) {
				n2 /= i;
				count++;
			}
			if (count%2==1) {
				m*= i;
			}
		}
	}

	if (n2!=1) {
		m*=n2;
	}
	
	printf("%llu", m);
	return 0;
}
