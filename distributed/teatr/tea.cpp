#include "message.h"
#include "teatr.h"
#include "bits/stdc++.h"
#include <vector>

using ll = long long;
using namespace std;

const int const_max_element = 1000000;
vector<int> numbers_list;
vector<int> cumulative_numbers_list(const_max_element);
ll conflict_counter = 0;

ll count_conflicts_with_merge_sort(vector<int> &numbers_list, vector<int> &helper_list, int p, int q, int r) {
  for (int k = p; k <= r; ++k) {
    helper_list[k] = numbers_list[k];
  }
  int i = p;
  int j = q + 1;
  ll conflict_counter = 0;
  for (int k = p; k <= r; ++k) {
    if ((i <= q) && helper_list[i] <= helper_list[j] || (j > r)) {
      numbers_list[k] = helper_list[i];
      ++i;
    } else {
      numbers_list[k] = helper_list[j];
      conflict_counter += (q - i) + 1;
      ++j;
    }
  }
  return conflict_counter;
}

ll count_conflicts_with_merge_sort(vector<int> &numbers_list, vector<int> &helper_list, int p, int r) {
  ll conflict_counter = 0;
  if (p < r) {
    int q = (p + r) / 2;
    conflict_counter += count_conflicts_with_merge_sort(numbers_list, helper_list, p, q);
    conflict_counter += count_conflicts_with_merge_sort(numbers_list, helper_list, q+1, r);
    conflict_counter += count_conflicts_with_merge_sort(numbers_list, helper_list, p, q, r);
  }
  return conflict_counter;
}

// ll count_conflicts(vector<int> &numbers_list) {
//   vector<int> helper_list(numbers_list.size());
//   return count_conflicts_with_merge_sort(numbers_list, helper_list, 0, numbers_list.size() - 1);
// }

ll bit_tree_sum_smaller(vector<int> &bit_tree, int index) {
  int sum = 0;
  while (index > 0) {
    sum += bit_tree[index - 1];
    index -= index & (-index);
  }
  return sum;
}

void bit_tree_increase_counter(vector<int> &bit_tree, int index) {
  while (index <= bit_tree.size()) {
    bit_tree[index - 1]++;
    index += index & (-index);
  }
}

ll count_conflicts(vector<int> &bit_tree, vector<int> &numbers_list) {
  ll conflict_counter = 0;
  for (int i = numbers_list.size() - 1; i >= 0; --i) {
    conflict_counter += bit_tree_sum_smaller(bit_tree, numbers_list[i] - 1);
    bit_tree_increase_counter(bit_tree, numbers_list[i]);
  }
  return conflict_counter;
}

void count_cumulative_numbers_list(vector<int> &bit_tree, vector<int> &cumulative_numbers_list, int size) {
  for (int i = 1; i < bit_tree.size(); ++i) {
    cumulative_numbers_list[i] = bit_tree[i-1];
    int prev_index = i - (-i & i);
    if (prev_index)
      cumulative_numbers_list[i] += cumulative_numbers_list[prev_index];
  }
  for (int i = 0; i < bit_tree.size(); ++i) {
    cumulative_numbers_list[i] = size - cumulative_numbers_list[i];
  }
}

int main() {
  int node_id = MyNodeId();
  int number_of_nodes = NumberOfNodes();
  int n = GetN();
  int node_n_length = n / number_of_nodes + 1;
  if (n % number_of_nodes == 0)
    node_n_length = n / number_of_nodes;

  for (int i = node_id * node_n_length; (i < (node_id + 1) * node_n_length) && (i < n); ++i) {
    numbers_list.push_back(GetElement(i));
  }
  if (numbers_list.size() > 0) {
    vector<int> bit_tree(const_max_element);
    conflict_counter = count_conflicts(bit_tree, numbers_list);
    count_cumulative_numbers_list(bit_tree, cumulative_numbers_list, numbers_list.size());
    for (int i = (node_id + 1) * node_n_length; i < n; ++i) {
      int tmp = GetElement(i);
      conflict_counter += cumulative_numbers_list[tmp];
    }
  }

  if (node_id != 0) {
    PutLL(0, conflict_counter);
    Send(0);
  } else {
    for (int i = 1; i < number_of_nodes; ++i) {
      Receive(i);
      conflict_counter += GetLL(i);
    }
    cout << conflict_counter << endl;
  }
  return 0;
}
