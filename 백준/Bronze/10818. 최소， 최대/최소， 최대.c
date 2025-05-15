#include <stdio.h>

int main() {
    int n, i, j;
    int min = 1000000;
    int max = -1000000;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &j);
        if(j < min) {
            min = j;
        }
        if(j > max) {
            max = j;
        }
    }
    printf("%d %d", min, max);
}