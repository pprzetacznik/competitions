#include <iostream>

using uc = unsigned char;
using ll = long long int;
using namespace std;

const ll prime = 140737488355333;
const ll d = 256;
ll h = 1;
const int max_length = 4166670;
uc table[max_length];
int table_length = 0;
int table_length_in_bits = 0;

void append(uc* table, uc buffer) {
  int segment = table_length_in_bits / 8;
  int offset = table_length_in_bits % 8;
  uc tmp1 = buffer-'a';
  uc tmp1_mask = 224;
  uc tmp2 = tmp1;
  uc tmp2_mask = tmp1_mask;
  for (int i = 0; i < offset; ++i) {
    tmp1 *= 2;
    tmp1_mask *= 2;
    tmp1_mask += 1;
  }
  for (int i = 0; i < 8 - offset; ++i) {
    tmp2 /= 2;
    tmp2_mask /= 2;
    tmp2_mask += 128;
  }
  table[segment] &= tmp1_mask;
  table[segment] += tmp1;
  if (offset > 3) {
    table[segment+1] &= tmp2_mask;
    table[segment+1] += tmp2;
  }
  table_length++;
  table_length_in_bits += 5;
}

char get(uc* table, int i) {
  int table_length_in_bits = i*5;
  int segment = table_length_in_bits / 8;
  int offset = table_length_in_bits % 8;
  uc tmp1 = table[segment];
  uc tmp2 = table[segment+1];
  for (int i = 0; i < offset; ++i)
    tmp1 /= 2;
  for (int i = 0; i < 8 - offset; ++i)
    tmp2 *= 2;
  if (offset > 3)
    tmp1 += tmp2;
  tmp1 %= 32;
  return (uc)(tmp1 + 'a');
}

ll calculate_hash_reversed(uc* table) {
  ll t = 0;
  for (int i = max_length*8/5 - 1; i >= 0; --i) {
    t = (d*t + (ll)get(table, i)) % prime;
  }
  return t;
}

ll calculate_hash(uc* table) {
  ll t = 0;
  for (int i = 0; i < max_length*8/5; ++i) {
    t = (d*t + (ll)get(table, i)) % prime;
  }
  return t;
}

ll update_hash(ll prev_hash, uc new_char, uc prev_char) {
  ll tmp = ((prev_hash*d) - ((ll)prev_char*h) + (ll)new_char) % prime;
  while (tmp < 0)
    tmp += prime;
  // return tmp % prime;
  return tmp;
}

void print_table() {
  for (int i = 0; i < table_length; ++i) {
    cout << get(table, i);
  }
  cout << endl;
}

int main() {
  for (int i = 0; i < max_length*8/5; ++i) {
    h *= d;
    h %= prime;
  }
  ll hash_head = 0;
  ll hash_tail = 0;
  char buffer;
  int n;
  cin >> n;
  int n_loaded = 0;

  while (cin.get(buffer)) {
    if (buffer <= 'z' && buffer >= 'a') {
      if (n_loaded < max_length*8/5) {
          append(table, buffer);
      } else if (n_loaded < 2*max_length*8/5) {
        if (n_loaded == (max_length*8/5)) {
          hash_head = calculate_hash_reversed(table);
          hash_tail = calculate_hash(table);
          table_length = 0;
          table_length_in_bits = 0;
        }
        hash_tail = update_hash(hash_tail, (uc)buffer, get(table, n_loaded % (max_length*8/5)));
        append(table, buffer);
      } else {
        hash_tail = update_hash(hash_tail, (uc)buffer, get(table, n_loaded % (max_length*8/5)));
      }
      n_loaded++;
    }
  }
  if (hash_head != hash_tail) {
    cout << "NIE" << endl;
    return 0;
  } else {
    if (n_loaded < 3*max_length*8/5) {
      int first, last, palindrom_length;
      if (n_loaded < max_length*8/5) {
        // the whole string is in the memory,
        // let's check everything
        first = 0;
        last = n_loaded-1;
        palindrom_length = n_loaded / 2;
      } else if (n_loaded < 2*max_length*8/5) {
        // the last part of the memory contains the middle of the palindrome
        first = table_length;
        last = max_length*8/5 - 1;
        palindrom_length = (last - first) / 2 + 1 - (n_loaded % 2);
      } else {
        // the first part of the memory contains the middle of the palindrome
        first = 0;
        palindrom_length = n_loaded/2 - (max_length*8/5);
        last = 2*palindrom_length - 1 + (n_loaded % 2);
      }
      for (int i = 0; i < palindrom_length; ++i) {
        if (get(table, i+first) != get(table, last-i)) {
          cout << "NIE" << endl;
          return 0;
        }
      }
    } else {
      cout << "OUT OF RANGE" << endl;
      return 0;
    }
  }
  cout << "TAK" << endl;
  return 0;
}
