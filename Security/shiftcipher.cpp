#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	cout<<"Enter the key  ";
	int k;
	cin>>k;
	cout<<"\nEnter the string  ";
	string is,os;
	cin>>is;
	if(k==0)
	{
		os=is;
		cout<<os;
		return 0;
	}
	cout<<endl;
	for(int i=0;i<is.length();i++)
	{
		int t=(is[i]+k-97)%26;
		os[i]=t+97;	
		cout<<os[i];
	}
	//cout<<os;
	return 0;
}