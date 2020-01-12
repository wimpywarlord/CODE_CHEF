n,q=map(int,input().split())
arr=list(map(int,input().split()))
for j in range(q):
    l,r=map(int,input().split())
    check=arr[l-1]
    bigf=0
    smallf=0
    bigger=0
    smaller=0
    for i in range(l,r):
        if bigf==0:
            if check<arr[i]:
                bigf=1
                smallf=0
                bigger=bigger+1    
        if smallf==0:
            if check>arr[i]:
                smallf=1
                bigf=0
                smaller=smaller+1
        check=arr[i]
    if (bigger==smaller):
        print("YES")
    else:
        print("NO")
'''
/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int no_of_elements,qqq;
    cin>>no_of_elements>>qqq;
    int arr[100003];
    for (int i = 0; i < no_of_elements; i++) {
        cin>>arr[i];
        //cout<<arr[i];
    }
    for (int i = 0; i < qqq; i++) {
        int l,r;
        cin>>l>>r;
        int check = arr[l-1];
        int biggerflag = 0;
        int smallerflag = 0;
        int bigger=0;
        int smaller=0;
        for (int j = l; j < r ; j++) {
            if (check < arr[j])
            {
                if (biggerflag==0)
                {
                    biggerflag=1;
                    smallerflag=0;
                    bigger=bigger+1;
                }
            }
            if(check>arr[j])
            {
                if(smallerflag==0)
                {
                    smallerflag=1;
                    biggerflag=0;
                    smaller=smaller+1;
                }
            }
            check=arr[j];
        }
        if(bigger==smaller)
        {
            //cout<<b<<s;
            cout<<"YES"<<endl;
        }
        else
        {
            //cout<<b<<s;
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
'''
