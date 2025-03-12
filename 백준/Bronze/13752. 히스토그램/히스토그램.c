#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int i;
    for(i = 0; i < n; i++) {
        int j;
        scanf("%d", &j);
        int k;
        for(k = 0; k < j; k++) {
            printf("=");
        }
        printf("\n");
    }
}