#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long arr[1000005];
int main() {
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
  	
  	cin>>arr[i];
  }
  long long cur=1;
  long long ans=1;
  for(int i=1;i<t;i++){
  	if(arr[i]>=arr[i-1]){
  		cur++;
  		ans=max(ans,cur);
	  }
  	else{
  		//ans=max(ans,cur);
  		cur=1;
	  }
  }
  cout<<ans<<endl;
  
  
  
  
  
  
}
