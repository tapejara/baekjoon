#include <stdio.h>

int main() {
    int count = 0;
    int n,v,i;
    
    scanf("%d",&n);
    int arr[100] = {};
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    };
    scanf("%d", &v);
    for(i = 0; i < n; i++) {
        if(arr[i] == v) {
            count ++;
        };
    };
    printf("%d", count);
}