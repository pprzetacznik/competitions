#include <iostream>
#include <vector>

using ll = long long;
using namespace std;

void print_char_table(const char* table, const int size) {
  for (int i = 0; i < size+1; ++i) {
    cout << (int)table[i];
  }
  cout << endl;
}

char is_vowel(const char key) {
  static const string vowels = "aeiouy";
  for (char i : vowels) {
    if (key == i)
      return 1;
  }
  return 0;
}

char* get_table_with_vowels(const string input) {
  char* table = new char[input.size()];
  for (int i = 0; i < input.size(); ++i) {
    table[i] = is_vowel(input[i]);
  }
  return table;
}

ll solve(const char* input, const int size) {
  if (size < 3) {
    return 0;
  }
  ll result = 0;
  int last_sequence = 0;
  for (int i = 2; i < size; ++i) {
    if (input[i] == input[i-1] && input[i-1] == input[i-2]) {
      last_sequence = i;
    }
    if (last_sequence > 0)
      result += last_sequence - 1;
  }
  return result;
}

int main() {
  string input;
  cin >> input;
  int size = input.size();
  cout << solve(get_table_with_vowels(input), size) << endl;
  return 0;
}
