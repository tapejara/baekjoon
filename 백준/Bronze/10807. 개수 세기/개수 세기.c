#include <stdio.h>

int main() {
    int i;
    scanf("%d", &i);
    int arr[i];
    for(int k = 0; k < i; k++) {
        scanf("%d", &arr[k]);
    }
    int j;
    scanf("%d", &j);
    int k;
    int count = 0;
    for(k = 0; k < i; k++) {
        if(arr[k] == j) {
            count++;
        }
    }
    printf("%d", count);
}