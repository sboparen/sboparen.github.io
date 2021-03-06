---
layout: post
title: Codec in 1K
date: 2012-01-11
priority: 1
---
My submission for the 20th
[International Obfuscated C Code Contest](http://ioccc.org/).
Exactly one kilobyte of C code that can function as some kind of
"codec".

<!--more-->

I approached this more as a code golf contest than as an obfuscated
code contest.
All development was done with the program in this "obfuscated" form.
My favourite part is the code reuse accomplished by the definition of `M`.

<a href="1k-codec.c">
<img src="/icons/32px/c.png" alt="(C source code) ">1k-codec.c</a>

```
#include<stdio.h>
#include<stdlib.h>
#define B 4<<17
#define F(i,n)for(i=0;i<n;i++)
#define M(a,b,c)F(i,A)v[s[i]=i]=0;F(i,a){b q=s[c];F(j,c+1)r=s[j],s[j]=q,q=r;}
#define T t[i]
#define W(a)s[y+7>>3]=0,s[y/8]+=(a)<<y%8,y++;
unsigned char s[B],t[B],u[B],q,r;
unsigned z[B],v[B],w[256][B],c,d,i,j,m,x,y;
int C(int*a,int*b){F(i,c)if(x=z[*a+i]-z[*b+i])return x;}
int main(int A,char**Y){
while(*(*Y)++)A=256;while(47-*--*Y)x=1&**Y;
if((c=1+fread(s,1,8<<x*14,stdin))<2)exit(0);
if(x){
F(i,c)z[v[i]=i]=s[i];z[c-1]=A;qsort(v,c,sizeof c,C);
F(i,c)v[i]?(T=s[v[i]-1]):(d=i);
M(c,F(x,A&&T-s[x]);T=x;,x)
y=64;F(i,c){x=T+1;F(j,8&&x>=2<<j)W(0)while(j+1)W(1&x>>j--)}
y=y+7>>3;F(i,4)s[i]=y-8>>8*i,s[4+i]=d>>8*i;
}else{
y=c=d=j=m=x=0;
F(i,4)c+=s[i]<<8*i,x+=s[4+i]<<8*i;c%=B;fread(s,1,c,stdin);
F(i,8*c){q=s[i/8]>>i%8&1;j+=!m;m=m||q;if(m){d+=d+q;if(!--j)t[y++]=d-1,m=d=0;}}
y+=!y;M(y,c=T;T=,c)
F(i,y)if(i-x)w[T][v[T]++]=i;
F(j,A){d=0;F(i,y)if(i-x&&T==j)u[m]=j,v[m++]=d++;}
x%=y--;F(i,y)s[i]=t[x=w[u[x]][v[x]]];
}main(fwrite(s,1,y,stdout),Y);}
```

## Example Usage (contains spoilers)

```
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$ curl http://en.wikipedia.org/wiki/Data_compression >input
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  186k    0  186k    0     0   235k      0 --:--:-- --:--:-- --:--:--  235k
$ wc -c input
191101 input
$ gcc 1k-codec.c -o compress 2>/dev/null
$ ./compress <input >input.z
$ wc -c input.z
51149 input.z
$ cp compress decompress
$ ./decompress <input.z >input2
$ diff -qs input input2
Files input and input2 are identical
```
