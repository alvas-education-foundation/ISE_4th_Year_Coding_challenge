1)

n = int(input().strip())
X = [int(x) for x in input().strip().split()]

mean = sum(X) / n
variance = sum([((x - mean) ** 2) for x in X]) / n
stddev = variance ** 0.5

print("{0:0.1f}".format(stddev))



2)

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int divisibleSumPairs(int n, int k, int ar_size, int* ar) {
    // Complete this function
    int i,j;
    int counter=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i<j && (ar[i]+ar[j])%k==0){
                counter++;
            }
        }
    }
    return counter;
}

int main() {
    int n; 
    int k; 
    scanf("%i %i", &n, &k);
    int *ar = malloc(sizeof(int) * n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       scanf("%i",&ar[ar_i]);
    }
    int result = divisibleSumPairs(n, k, n, ar);
    printf("%d\n", result);
    return 0;
}


3)

#!/bin/python

import sys

N = int(raw_input())
difference = 0
for i in xrange(N):
    row = raw_input().split()
    difference += (int(row[i]) - int(row[N-1-i]))
print abs(difference)




4)


#include<bits/stdc++.h>
using namespace std;
int ar[1001],result[1001],k = 0,n;
int smal_cal(){

    int cnt = 0,smal = 1001;
    for(int i = 0; i < n; i++){
        if(smal >= ar[i] && ar[i] != 0)smal = ar[i];
        if(ar[i] != 0)cnt++;
    }
    if(cnt != 0)cout << cnt << endl;
    return smal;
}
int main(){

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> ar[i];
    }
    int smal = 1001;
    for(int i = 0; i < n; i++){
        smal = smal_cal();
        for(int j = 0; j < n; j++)if(ar[j] != 0)ar[j]-=smal;
    }
    return 0;
}



5)


#include <iostream>
using namespace std;

int n,a[100],b[200];
int main() {
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int k= 2*i;
            if(a[i]==a[j]||a[i]==a[j]+1)
                b[k]++;
            if(a[i]==a[j]||a[i]==a[j]-1)
                b[k+1]++;
        }
    }
    for(int i=0;i<200;i++)
        if(b[i]>b[0])
            b[0]=b[i];
    cout<<b[0];
    return 0;
}
