#include <stdio.h>

int main() {
    int n;
    int i;
    int j;
    int k;
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        for(j = 0; j < n - i - 1; j++) {
            printf(" ");
        }
        for(j = 0; j < i; j++) {
            printf("*");
        }
        printf("* \n");
    }
}