#include <stdio.h>
int main() {
    int n,x,i,j;
    int count = 0;
    scanf("%d %d",&n, &x);
    for(i = 0; i < n; i++) {
        scanf("%d", &j);
        if(j < x) {
            printf("%d ", j);
        }
    }
}