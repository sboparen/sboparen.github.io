#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int main() {
    int n, *arr = malloc(INT_MAX);
    size_t i, arr_sz = 0;
    while(scanf("%d", &n) > 0)
        arr[arr_sz++] = n;
    for(i=0; i<arr_sz; i++)
        printf("%d\n", arr[i]);
    for(i=0; i<arr_sz; i++)
        printf("%d\n", arr[i]);
    return 0;
}
