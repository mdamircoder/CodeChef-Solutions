#include<iostream>
using namespace std;
int main()
{
	int t, a[100000], b[100000];
	cin >> t;
	for(int i=0; i<t; i++)
	{
		int n, way_1=0, way_2=0;
		cin >> n;
		for(int j=0; j<n; j++)
			cin >> a[j];
		for(int j=0; j<n; j++)
			cin >> b[j];
		for(int j=0; j<n; j++)
		{
			if(j%2==0)
			{
				way_1 = way_1 + a[j];
				way_2 = way_2 + b[j];
			}
			else
			{
				way_1 = way_1 + b[j];
				way_2 = way_2 + a[j];
			}
		
		}
		if(way_1<way_2)
			cout << way_1 << endl ;
		else
			cout << way_2 << endl ;
	
	}
	return 0;
} 
/*========================================================================
Here are two Task arrays : A and B (Each element, task[i], corresponds to time taken by i-th subtask) .
Each array is of size N (N subtasks in each task).

Xenny and Yana will have to complete N subtasks out of total 2N subtasks, alternatively, in minimum time.
Who starts first, doesn't matter. We just need to minimise the total time.
--------------------------------------------------------------------------
Starting with A[0]
Suppose Xenny starts with A[0], then Yana does B[1], then Xenny does A[2], then Yana does B[3] ....and so on... 
i.e.
	Total time in this case = A[0] + B[1] + A[2] + B[3] + A[4] + ...
							= { A[0] + A[2] + ...} + { B[1] + B[3] + ... }
If Yana starts with A[0], the time remains same.
-------------------------------------------------------------------------
Similarly, if Starting with B[0]
Suppose Xenny starts with B[0], then Yana does A[1], then Xenny does B[2], then Yana does A[3] ....and so on... 
i.e.
	Total time in this case = B[0] + A[1] + B[2] + A[3] + B[4] + ...
							= { B[0] + B[2] + ...} + { A[1] + A[3] + ... }
If Yana starts with B[0], the time remains same.

=========================================================================
So who starts first, doesnot matter. It only matters whether they start by Task A or Task B.
=========================================================================

There are two ways - total time taken by them, are :

Time ( Way_1 ) = { A[0] + A[2] + ...} + { B[1] + B[3] + ... }
			   = { Summation ( A[i] ) when i is even } + { Summation ( B[j] ) when j is odd }
			   
Time ( Way_2 ) = { B[0] + B[2] + ...} + { A[1] + A[3] + ... }
               = { Summation ( A[i] ) when i is odd } + { Summation ( B[j] ) when j is even }
               
The minimum of Time ( Way_1 ) and Time ( Way_2 ) will be the answer.
=========================================================================
*/
