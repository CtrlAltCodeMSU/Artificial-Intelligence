#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// BFS: Returns the shortest path from 'start' to 'goal' if one exists
vector<int> bfsPath(const vector<vector<int>> &graph, int start, int goal)
{
  int n = graph.size();
  vector<bool> visited(n, false);
  vector<int> parent(n, -1);
  queue<int> q;

  q.push(start);
  visited[start] = true;

  bool found = false;
  while (!q.empty() && !found)
  {
    int current = q.front();
    q.pop();

    if (current == goal)
    {
      found = true;
      break;
    }

    for (int neighbor : graph[current])
    {
      if (!visited[neighbor])
      {
        visited[neighbor] = true;
        parent[neighbor] = current;
        q.push(neighbor);
      }
    }
  }

  vector<int> path;
  if (found)
  {
    int current = goal;
    while (current != -1)
    {
      path.push_back(current);
      current = parent[current];
    }
    reverse(path.begin(), path.end());
  }

  return path;
}

// DFS Utility function (recursive)
bool dfsUtil(const vector<vector<int>> &graph, int current, int goal,
             vector<bool> &visited, vector<int> &path)
{
  visited[current] = true;
  path.push_back(current);

  if (current == goal)
  {
    return true;
  }

  for (int neighbor : graph[current])
  {
    if (!visited[neighbor])
    {
      if (dfsUtil(graph, neighbor, goal, visited, path))
        return true;
    }
  }

  path.pop_back();
  return false;
}

// DFS: Returns a path from 'start' to 'goal' (not necessarily the shortest)
vector<int> dfsPath(const vector<vector<int>> &graph, int start, int goal)
{
  int n = graph.size();
  vector<bool> visited(n, false);
  vector<int> path;
  dfsUtil(graph, start, goal, visited, path);
  return path;
}

int main()
{
  // Define a sample graph using an adjacency list.
  // For example, graph[0] contains the list of nodes connected to node 0.
  // Graph structure:
  // 0 - 1 - 2
  // |   |
  // 3 - 4
  vector<vector<int>> graph = {
      {1, 3},    // Neighbors of node 0
      {0, 2, 4}, // Neighbors of node 1
      {1},       // Neighbors of node 2
      {0, 4},    // Neighbors of node 3
      {1, 3}     // Neighbors of node 4
  };

  int start = 0;
  int goal = 2;

  // Perform BFS
  vector<int> pathBFS = bfsPath(graph, start, goal);
  cout << "BFS Path from " << start << " to " << goal << ": ";
  for (int node : pathBFS)
  {
    cout << node << " ";
  }
  cout << "\n";

  // Perform DFS
  vector<int> pathDFS = dfsPath(graph, start, goal);
  cout << "DFS Path from " << start << " to " << goal << ": ";
  for (int node : pathDFS)
  {
    cout << node << " ";
  }
  cout << "\n";

  return 0;
}
