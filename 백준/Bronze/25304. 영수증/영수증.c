#include <stdio.h>

int main() {
    int total;
    int n;
    int i;
    int a;
    a = 0;
    int j;
    int k;
    scanf("%d", &total);
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        scanf("%d %d", &j, &k);
        a += j * k;
    }
    if(a == total) {
        printf("Yes");
    }
    else {
        printf("No");
    }
}