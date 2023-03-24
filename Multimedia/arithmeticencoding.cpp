#include<iostream>
#include<vector>
#include<string.h>
using namespace std;
int main()
{
	int n;
	cout<<"Enter the number of characters  ";
	cin>>n;
	vector <float> p;
	vector <char> c;
	p.push_back(0);
	cout<<"Enter the characters along with their probability ";
	char t1;
	float t2;
	for(int i=0;i<n;i++)
	{
		cin>>t1;
		c.push_back(t1);
		cin>>t2;
		p.push_back(t2+p[i]);		
	}
	cout<<"Enter the string you want to encode  ";
	string s;
	cin>>s;
	float u=1,l=0;
	for(int i=0;i<s.length();i++)
	{	
		int j;
		for(j=0;;j++)
		{
			if(s[i]==c[j])
			{	//cout<<"Char found at "<<j<<endl;
				break;
			}	
		}
		float d=u-l;
		//cout<<"Current d is "<<d<<endl;
		u=d*p[j+1]+l;
		l=d*p[j]+l;
	}
	cout<<"Lower Limit:  "<<l<<endl<<"Upper Limit:  "<<u<<endl;
	return 0;
}

void balance(node *root, int data)
{
	
}