from itertools import chain, combinations
from collections import defaultdict

# Function to generate candidate itemsets of size k
def generate_candidates(itemsets, k):
    candidates = set()
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union_set = itemset1.union(itemset2)
            if len(union_set) == k and union_set not in candidates:
                candidates.add(union_set)
    return candidates

# Function to prune candidate itemsets using the Apriori property
def prune(itemsets, candidates, k):
    pruned_candidates = set()
    for candidate in candidates:
        subsets = list(combinations(candidate, k - 1))
        if all(subset in itemsets for subset in subsets):
            pruned_candidates.add(candidate)
    return pruned_candidates

# Function to calculate the support of a candidate itemset in the transactions
def calculate_support(transactions, candidate):
    count = 0
    for transaction in transactions:
        if candidate.issubset(transaction):
            count += 1
    return count

# Main Apriori algorithm
def apriori(transactions, min_support):
    # Initialize single-item itemsets
    itemsets = [frozenset([item]) for item in set(chain(*transactions))]
    k = 2
    frequent_itemsets = []

    while itemsets:
        # Generate candidate itemsets of size k
        candidates = generate_candidates(itemsets, k)
        # Prune candidates using the Apriori property
        candidates = prune(itemsets, candidates, k)

        # Count support for each candidate itemset
        item_counts = defaultdict(int)
        for candidate in candidates:
            support = calculate_support(transactions, candidate) / len(transactions)
            if support >= min_support:
                item_counts[candidate] = support

        # Add frequent itemsets of size k to the result
        frequent_itemsets.extend(item_counts.items())
        itemsets = [itemset for itemset, _ in item_counts.items()]
        k += 1

    return frequent_itemsets

# Example Data (Replace this with your own dataset)
transactions = [
    {'A', 'B', 'C'},
    {'A', 'B', 'C'},
    {'A', 'B', 'C'},
    {'B', 'C'},
    {'A', 'C'},
    {'A', 'B', 'D'},
    {'B', 'C'},
    {'A', 'C'},
    {'A', 'B', 'D'},
    {'B', 'C'},
    {'A', 'C'},
    {'A', 'B', 'D'},
    {'B', 'C'},
    {'A', 'C'},
    {'A', 'B', 'D'},
    {'A', 'B', 'C', 'D'},
    {'A', 'B', 'C'},
]

# Set the minimum support
# Run Apriori algorithm
min_support=.33
frequent_itemsets = apriori(transactions, min_support)

# Display the results
if len(frequent_itemsets) == 0:
    print('No frequent itemsets found.')
else:
    for itemset, support in frequent_itemsets:
        print(f"Itemset: {itemset}, Support: {support}")

    # Add debug prints
    print("Generated Itemsets:")
    print(itemsets)
    print("Generated Candidates:")
    print(candidates)


# Itemset: frozenset({'A'}), Support: 0.4444444444444444
# Itemset: frozenset({'B'}), Support: 0.6111111111111112
# Itemset: frozenset({'C'}), Support: 0.7222222222222222
# Itemset: frozenset({'D'}), Support: 0.2777777777777778
# Itemset: frozenset({'A', 'B'}), Support: 0.3333333333333333
# Itemset: frozenset({'A', 'C'}), Support: 0.5
# Itemset: frozenset({'A', 'D'}), Support: 0.2777777777777778
# Itemset: frozenset({'B', 'C'}), Support: 0.6111111111111112
# Itemset: frozenset({'B', 'D'}), Support: 0.2222222222222222
# Itemset: frozenset({'C', 'D'}), Support: 0.16666666666666666
# Itemset: frozenset({'A', 'B', 'C'}), Support: 0.2777777777777778
