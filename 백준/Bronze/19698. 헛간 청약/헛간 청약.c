#include <stdio.h>
int main() {
    int n, w, h, l;
    scanf("%d %d %d %d", &n, &w, &h, &l);
    if((w / l) * (h / l) >= n) {
        printf("%d", n);
    }
    else {
    printf("%d", (w / l) * (h / l));
    }
}