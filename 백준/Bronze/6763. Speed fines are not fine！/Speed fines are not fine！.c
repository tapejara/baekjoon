#include <stdio.h>

int main() {
    int n,m;
    scanf("%d", &n);
    scanf("%d", &m);
    if(m <= n) {
        printf("Congratulations, you are within the speed limit!");
    }
    else if(m - n >= 31) {
        printf("You are speeding and your fine is $500.");
    }
    else if(m - n >= 21) {
        printf("You are speeding and your fine is $270.");
    }
    else{
        printf("You are speeding and your fine is $100.");
    }
}