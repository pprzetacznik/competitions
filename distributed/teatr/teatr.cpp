#include "bits/stdc++.h"

using namespace std;

namespace teatr {

  bool initialized = false;
  int n, type, a, b, mod;
  unsigned long long mul;

  void init() {
    if(initialized) return;
    cin >> n >> type >> a >> b >> mod >> mul;
    initialized = true;
  }

  int GetN() {
    init();
    return n;
  }

  int GetElement(int i) {
    init();
    assert(0 <= i and i < n);
    assert(0 <= i && i < n);
    unsigned long long x = i + 1;
    x = ((x + 1) * mul) >> 32;
    bool done = false;
    if(type == 1 || type == 2) {
      if(x % 100 < (unsigned) a) {
        x = (long long) i * mod / n;
        if(type == 2) {
          x = mod - 1 - x;
        }
        done = true;
      }
    }
    if(!done) { // fake time consumption, to make running times equal
      for(int asdf = 1; asdf <= 2 - (type == 3); ++asdf) {
        x += n / (i / asdf + 1);
      }
    }
    if(type == 3) {
      if((i + a / 3) % a < b) {
        x = mod * 9LL / 10;
      }
    }
    return 1 + x % mod;
  }
}


#ifdef __cplusplus
extern "C" {
#endif
int GetN() {
  return teatr::GetN();
}
int GetElement(int i) {
  return teatr::GetElement(i);
}
#ifdef __cplusplus
}
#endif
