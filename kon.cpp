#include <iostream>
#include <math.h>

using ull = unsigned long long int;
using namespace std;

typedef struct big_num {
  int log10 = 0;
  int size = 1;
  ull numbers[12000];
} big_num;

void print_big_num(big_num* a) {
  printf("%llu", a->numbers[0]);
  for (int i = 1; i < a->size; ++i) {
    printf("%018llu", a->numbers[i]);
  }
  printf("\n");
}

bool is_bigger_or_equal(big_num* a, big_num* b) {
  if (a->size > b->size)
    return true;
  if (a->size == b->size) {
    for (int i = 0; i < a->size-1; ++i) {
      if (a->numbers[i] > b->numbers[i])
        return true;
    }
    if (a->numbers[a->size - 1] >= b->numbers[b->size - 1])
      return true;
  }
  return false;
}

int compare_diff_major_bigger_than_current(big_num* a, ull current, int current_log10) {
  int segment_magnitude = (a->log10) % 18;
  int offset_magnitude = current_log10 - segment_magnitude + 1;

  ull tmp = a->numbers[0] % (ull)pow(10, segment_magnitude + 1);
  if (current_log10 < segment_magnitude) {
    tmp /= (ull)pow(10, segment_magnitude - current_log10);
  }
  if (offset_magnitude > 0 && a->size > 1) {
    tmp *= (ull)pow(10, offset_magnitude - 1);
    tmp += a->numbers[1] / (ull)pow(10, 18-offset_magnitude + 1);
  }
  if (tmp > current)
    return 1;
  else if (tmp < current)
    return -1;
  return 0;
}

void lift(big_num* a, int magnitude) {
  int blocks = magnitude / 18;
  int offset = magnitude % 18;
  ull offset_pow = pow(10, offset);
  a->size += blocks;
  if (offset > 0) {
    ull tmp = 0;
    ull tmp_prev = 0;
    for (int i = a->size - 1; i >= 0; --i) {
      tmp = 0;
      for (int j = 0; j < offset; ++j) {
        a->numbers[i] *= 10;
        tmp *= 10;
        tmp += a->numbers[i] / (ull)1e18;
        a->numbers[i] = a->numbers[i] % (ull)1e18;
      }
      a->numbers[i] += tmp_prev;
      tmp_prev = tmp;
    }
    if (tmp > 0) {
      a->size++;
      for (int i = a->size - 1; i > 0; --i) {
        a->numbers[i] = a->numbers[i-1];
      }
      a->numbers[0] = tmp;
    }
  }
  a->log10 += magnitude;
}

bool check_mod_part_is_almost_full(big_num* a, int magnitude) {
  int blocks = magnitude / 18;
  int offset = magnitude % 18;
  ull offset_pow = pow(10, offset);
  for (int i = a->size - 1; i >= a->size - blocks; --i) {
    if (a->numbers[i] != (ull)1e18-1) {
      return false;
    }
  }
  if ((a->numbers[a->size - blocks - 1] % offset_pow) + 1 == offset_pow) {
    return true;
  }
  return false;
}

void increase_by_mod_part_plus_one(big_num* a, big_num* b, int magnitude) {
  int blocks = magnitude / 18;
  int offset = magnitude % 18;
  ull offset_pow = pow(10, offset);
  for (int i = a->size - 1; i > a->size - blocks - 1; --i) {
    a->numbers[i] = b->numbers[i];
  }
  a->numbers[a->size - blocks - 1] += b->numbers[a->size - blocks - 1] % offset_pow;
  ull tmp = 0;
  a->numbers[a->size - 1] += 1;

  tmp = a->numbers[a->size - 1] / (ull)1e18;
  int i = a->size - 1;
  while(tmp) {
    a->numbers[i] = a->numbers[i] % (ull)1e18;
    --i;
    tmp = a->numbers[i] / (ull)1e18;
  }
}

int main() {
  int n;
  cin >> n;
  big_num *prev = new big_num;
  big_num *current = new big_num;
  ull counter = 0;
  cin >> prev->numbers[0];
  prev->size = 1;
  prev->log10 = floor(log10(prev->numbers[0]));
  for (int i = 1; i < n; ++i) {
    cin >> current->numbers[0];
    ull current_bak = current->numbers[0];
    current->size = 1;
    current->log10 = floor(log10(current->numbers[0]));
    int current_bak_log10 = current->log10;
    if (is_bigger_or_equal(prev, current)) {
      int log_diff = prev->log10 - current->log10;
      lift(current, log_diff);
      counter += log_diff;
      if (is_bigger_or_equal(prev, current)) {
        int comparison = compare_diff_major_bigger_than_current(prev, current_bak, current_bak_log10);
        if (comparison > 0 || check_mod_part_is_almost_full(prev, log_diff)) {
          lift(current, 1);
          counter++;
        } else if (comparison == 0) {
          increase_by_mod_part_plus_one(current, prev, log_diff);
        }
      }
    }
    big_num* tmp = prev;
    prev = current;
    current = tmp;
    for (int i = 0; i < current->size; ++i)
      current->numbers[i] = 0;
    current->size = 1;
  }
  cout << counter << endl;
  return 0;
}
