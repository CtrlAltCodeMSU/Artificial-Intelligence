
#include <iostream>
#include <ctime>
using namespace std;
int main() {
   clock_t start = clock();

   long  long sum = 0 ;
   for (int i = 0; i < 100000; i++)
   {
     sum += i ;
   }
   clock_t end = clock();

   double time_done = double (end - start) / CLOCKS_PER_SEC;

   cout << "Total time done: " << time_done << " seconds" << endl;
   
  }