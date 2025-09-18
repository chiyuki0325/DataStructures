#include <stdio.h>

typedef unsigned long long llu;

llu C(llu a, llu b);

int main() {
  llu k;
  scanf("%llu", &k);

  for (llu n = 1; n <= k; n++) {
    llu places = C(2, n * n);
    places -= 4 * (n - 2) * (n - 1);
    printf("%llu\n", places);
  }
  return 0;
}

llu C(llu a, llu b) {
  // a < b
  // C 2 6 = 6*5 / 1*2
  llu result = 1;
  for (llu i = b; (b - i) < a; i--) {
    result *= i;
  }
  for (llu i = 1; i <= a; i++) {
    result /= i;
  }
  return result;
}
