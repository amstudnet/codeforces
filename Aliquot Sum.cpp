#include<iostream>  
#include<vector>  
#include<sstream>
 #include<cstring>  
#include<algorithm>  
#include<cmath>  
#define ll long long 
using namespace std;

const ll maxn=1000010;
long long prime[maxn];
long long ans[maxn];
int main(){
	for(int i=1;i<maxn;++i){
		for(int j=2*i;j<maxn;j+=i){
			prime[j]+=i;
		}
	}
	ll t,n,sum;
	cin>>t;
	while(t--){
		int x;
		cin>>x;
		
		if(prime[x]==x)cout<<"perfect\n";
		else if(prime[x]>x)cout<<"abundant\n";
		else cout<<"deficient\n";
		}

		
		
	
}  
