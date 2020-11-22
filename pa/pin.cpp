#include <iostream>
#include <vector>

using namespace std;

/*

a,b,c
a+b+c=n
a,a*n,a*n*m
a+a*n+a*n*m=Z
a(1+n)+anm=Z
a(1+n+nm)=Z
a(1+n(1+m))=Z

*/

vector<int>* get_dividers(int n, int limit=0) {
  vector<int>* dividers = new vector<int>();
  dividers->push_back(1);
  if (n % 2 == 0)
    dividers->push_back(2);
  int max_n = n + 1;
  if (limit)
    max_n = limit;
  for (int i = 3; i < max_n; ++i) {
    if (n % i == 0)
      dividers->push_back(i);
  }
  return dividers;
}

void print_int_vector(vector<int>* container) {
  for (vector<int>::const_iterator i = container->begin(); i != container->end(); ++i)
    cout << *i << endl;
}

int main() {
  int n;
  int results = 0;
  cin >> n;
  vector<int>* a_dividers = get_dividers(n, n/3);
  for (vector<int>::const_iterator i = a_dividers->begin(); i != a_dividers->end(); ++i) {
    int a = *i;
    int n2 = n/a - 1;
    vector<int>* b_dividers = get_dividers(n2, n2/2);
    for (vector<int>::const_iterator j = b_dividers->begin(); j != b_dividers->end(); ++j) {
      int p1 = *j;
      int b = p1*a;
      int c = n - a - b;
      if (p1 > 1 && c > b) {
        results++;
      }
    }
  }
  cout << results << endl;
  return 0;
}
