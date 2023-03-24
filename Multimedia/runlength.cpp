#include<iostream>
#include<string.h>
#include<vector>
using namespace std;

string run_enc(string s)
{	
	int co=1,t=1;
	char c=s[0];
	string o;
	o.push_back(s[0]);
	for(int i=1;i<=s.length();i++)
	{
		if(c==s[i])
		{	
			co++;
		}
		else
		{
			o+=to_string(co); 
			t++;
			o.push_back(s[i]);
			t++;
			c=s[i];
			co=1;
		}
	}
	return o;
}

int main()
{
	string s,o;
	cout<<"Enter the string  ";
	cin>>s;
	o=run_enc(s);
	cout<<o<<endl;
	return 0;
}
