#include <stdio.h>

int main() {
    int a;
    int b;
    int c;
    while(1) {
        scanf("%d %d",&a, &b);
        if(a == 0 && b == 0) {
            break;
        }
        c = a + b;
        printf("%d \n", c);
    }
}