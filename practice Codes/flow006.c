// Author : Dhruv B Kakadiya

//sum of digits
#include<stdio.h>
int main(){

int t,a,sum;
scanf("%d",&t);
while(t--){
  sum=0;
  scanf("%d",&a);
  while(a>0){
  sum+=a%10;
  a/=10;
}
printf("%d\n",sum);
      
}

return 0;

}