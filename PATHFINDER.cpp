#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int a[4][4]=
{
{1,0,0,0},
{1,0,0,0},
{1,1,2,1},
{0,1,1,0}
};
/*{
{1,1,0,1},
{1,0,1,0},
{1,1,1,0},
{0,0,1,1}
};*/
int q[4][4]={{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};

using namespace std;
int path(int i,int j)
{
	if(a[i][j]==2)
	{
		q[i][j]=2;
		return 1;	
	}	
	if(a[i][j]==1)
	{
		q[i][j]=1;
		if(path(i,j+1)==1)return 1;
		if(path(i+1,j)==1)return 1;
		if(path(i+1,j+1)==1)return 1;
		/*if(path(i-1,j-1)==1)return 1;
		if(path(i-1,j)==1)return 1;
		if(path(i,j-1)==1)return 1;
		if(path(i-1,j+1)==1)return 1;
		if(path(i+1,j-1)==1)return 1;*/
		q[i][j]=0;
	}
	return 0;
}
int main()
{
	int i=0,j=0;
	
	path(i,j);
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cout<<q[i][j]<<"\t";
		}
		cout<<"\n";
	}
	return 0;	
} 
