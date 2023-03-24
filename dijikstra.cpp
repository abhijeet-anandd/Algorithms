#include <iostream>
#include<climits>
using namespace std;

void print( int * distance, int V)
{
    cout<<endl;
  for( int i=0 ;i<V; i++)
  {
      cout << i <<" " << distance[i] << endl;
  }
}

void dijikstra(int ** edges, int V)
{
  bool * takenSource = new bool [V]{};

  int * distance = new int [V];
   for(int i=0 ;i<V; i++)
     distance[i] = INT_MAX;

  //lets take 0 as first source and parent of 0 is -1 and  weight is 0
   distance[0] = 0;
  int src ;

  for(int i=0; i<V-1 ;i++)
  {
    int tempDistance = INT_MAX;

    for(int j=0; j<V; j++)
   {
     if(takenSource[j] == false && distance[j] < tempDistance)
     {
       src = j;
       tempDistance = distance[j];
     }
   }

    takenSource[src] = true;   /// marked as taken parent


    for(int j=0 ;j<V; j++)
    {
      if(takenSource[j] == false && edges[src][j] > 0 && edges[src][j] + distance[src] < distance[j] )
      {
        distance[j] = edges[src][j] + distance[src];
      }
    }

  }
  print(distance,V);

 delete []takenSource;
 delete []distance;
}

int main()
{
  int V ,E;
  cout<<"Enter no of V and E: ";
  cin >> V >> E;

  int ** edges = new int * [V];
  for(int i=0 ;i<V; i++)
   edges[i] = new int [V];

  cout<<"Enter the source-destination-weight: ";
  for( int i =0 ;i<E; i++)
  {
    int source, dest, weight;
    cin >>  source >> dest >> weight;

    edges[source][dest] = weight;
    edges[dest][source] = weight;
  }

   dijikstra(edges, V);

  for(int i=0; i<V ;i++)
    delete []edges[i];
  delete []edges;
  return 0;
}
