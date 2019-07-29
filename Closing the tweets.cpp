#include<iostream>
#include<iterator>
#include<map>
#include<string>
#include<iomanip>
#include<string.h>
// for <streamsize>
#include<ios>

// for numeric_limits
#include<limits>

 using namespace std;

 int main()
 {
     map<string,int> my_map;
     int n,k;
     char click[10];
     cin>>n;
     cin>>k;
     for(int i=0;i<n;i++)
     {
         my_map.insert(pair<string,int>("CLICK "+to_string(i+1),0));
     }

     map<string,int>::iterator itr;
     for(itr=my_map.begin();itr!=my_map.end();itr++)
     {
        cout<<itr->first<<"*"<<itr->second<<'\n';
     }

     for(int i=0;i<k;i++)
     {

         cin>>click;
         cin.ignore(numeric_limits<streamsize>::max(),'\n');
         if(strcmp(click,"CLOSEALL")==0)
         {
             cout<<"$";
             map<string,int>::iterator itr;
            for(itr=my_map.begin();itr!=my_map.end();itr++)
            {
                itr->second=0;
                cout<<"&";
            }
         }
         else{
            cout<<"!";
            map<string,int>::iterator itr;
            for(itr=my_map.begin();itr!=my_map.end();itr++)
            {
                cout<<itr->first<<itr->second;
                if(strcmp(itr->first,click)==0)
                {
                    if(itr->second==0)
                    {
                        itr->second=1;
                        cout<<"#";
                    }
                    else{
                    itr->second=0;
                    cout<<"%";
                    }
                }

            }
         }
     }
     for(itr=my_map.begin();itr!=my_map.end();itr++)
     {
        cout<<itr->first<<"*"<<itr->second<<'\n';
     }

     return 0;
 }
