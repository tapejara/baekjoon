#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    if(n / 2 >= m / 2) {
        printf("%d", m / 2);
    }
    else{
        printf("%d", n / 2);
    }
}