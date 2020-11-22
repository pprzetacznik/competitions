#include <stdio.h>

using ll = long long int;
const ll prime = 140737488355333;
const ll d = 256;
ll h = 1;

ll update_hash(ll prev_hash, char new_char) {
  ll tmp = ((prev_hash*d) + (ll)new_char) % prime;
  while (tmp < 0)
    tmp += prime;
  return tmp;
}

ll update_hash_reversed(ll prev_hash, char new_char, ll h) {
  ll tmp = (prev_hash + (ll)new_char*h) % prime;
  while (tmp < 0)
    tmp += prime;
  return tmp;
}

int main() {
  ll hash_head = 0;
  ll hash_tail = 0;
  char buffer;
  int n;
  scanf("%d\n", &n);
  while ((buffer = getchar_unlocked()) != '\n' && buffer != EOF) {
    if (buffer <= 'z' && buffer >= 'a') {
      hash_head = update_hash_reversed(hash_head, buffer, h);
      h *= d;
      h %= prime;
      hash_tail = update_hash(hash_tail, buffer);
    }
  }
  if (hash_head != hash_tail) {
    printf("NIE\n");
    return 0;
  }
  printf("TAK\n");
  return 0;
}
