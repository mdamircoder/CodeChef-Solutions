#include<iostream>
#include<math.h>
 
using namespace std;
 
int main()
{
	long long int x, y;
	int t;
	cin >> t;
	while(t--)
	{
		cin >> x >> y;
		long long int n = x+y;
		long long int size = n*(n+1)/2 + 1;
		long long int ans = size + x;
		cout << ans << endl;
	}
} 
