# Bloom Filter Algorithm: Detailed Explanation and Implementation

## 1. What is a Bloom Filter?

A Bloom filter is a **space-efficient probabilistic data structure** used to test whether an element is a member of a set. It is "probabilistic" because it can tell you one of two things:

1.  The item is **definitely not** in the set.
2.  The item is **probably** in the set.

This means that **false positives are possible** (it might say an item is in the set when it isn't), but **false negatives are not** (if it says an item is not in the set, it's guaranteed to be absent).

The main advantage of a Bloom filter is its incredible **space efficiency**. It can store a representation of a very large set of items using only a small, fixed-size amount of memory.

## 2. How It Works: The Core Components

A Bloom filter consists of two main things:

1.  **A Bit Array:** A contiguous block of memory (like a Python list or a C array) of `m` bits, initially all set to `0`.
2.  **Hash Functions:** A set of `k` different and independent hash functions. These functions take an item as input and produce a hash value, which is then mapped to an index in the bit array.

### The Operations

**a) Adding an Item (`add`)**

When you want to add an item to the filter:

1.  You run the item through each of the `k` hash functions.
2.  This produces `k` different hash values.
3.  You use these hash values as indices in the bit array and set the bits at those positions to `1`.

![Bloom Filter Add Operation](https://miro.medium.com/v2/resize:fit:1400/1*0bZf_--O2p-A5bA1c2a_TA.gif)

**b) Checking for an Item (`check`)**

When you want to check if an item is in the filter:

1.  You run the item through the same `k` hash functions.
2.  This again produces `k` hash values (indices).
3.  You check the bits at these `k` indices in the bit array.
    *   If **any** of the bits at these indices is `0`, the item is **definitely not** in the set. Why? Because if it had been added, all of its corresponding bits would have been set to `1`.
    *   If **all** of the bits at these indices are `1`, the item is **probably** in the set. It's only "probably" because those bits might have been set to `1` by other items that were added. This is the source of false positives.

![Bloom Filter Check Operation](https://miro.medium.com/v2/resize:fit:1400/1*2zX2x2da_3Z5g3V2YvD7sA.gif)

## 3. Implementation in Python

Here is the Python implementation of the Bloom Filter algorithm:

```python
import math
import hashlib

class BloomFilter:
    """
    A space-efficient probabilistic data structure, that is used to test whether
    an element is a member of a set. False positive matches are possible, but
    false negatives are not.
    """

    def __init__(self, num_items, false_positive_prob):
        """
        Initializes a Bloom Filter.

        Args:
            num_items (int): The approximate number of items that the filter will contain.
            false_positive_prob (float): The desired false positive probability.
        """
        if not (0 < false_positive_prob < 1):
            raise ValueError("False positive probability must be between 0 and 1")
        if not num_items > 0:
            raise ValueError("Number of items must be greater than 0")

        self.num_items = num_items
        self.false_positive_prob = false_positive_prob

        # Calculate optimal size of the bit array (m) and number of hash functions (k)
        self.size = self._calculate_size(num_items, false_positive_prob)
        self.hash_count = self._calculate_hash_count(self.size, num_items)

        # Initialize the bit array (using a standard Python list of 0s)
        self.bit_array = [0] * self.size

    def _calculate_size(self, n, p):
        """Calculates the optimal size (m) of the bit array."""
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def _calculate_hash_count(self, m, n):
        """Calculates the optimal number of hash functions (k)."""
        k = (m / n) * math.log(2)
        return int(k)

    def _get_hashes(self, item):
        """
        Generates k different hash values for an item.
        We use two hash functions (SHA256 and MD5) and combine them to
        generate k hashes, a common technique to avoid needing k separate
        hash algorithms.
        """
        hashes = []
        # Use two different hash functions for better distribution
        h1 = int(hashlib.sha256(item.encode()).hexdigest(), 16)
        h2 = int(hashlib.md5(item.encode()).hexdigest(), 16)

        for i in range(self.hash_count):
            # Kirsch-Mitzenmacher optimization: (h1 + i * h2) % size
            combined_hash = (h1 + i * h2) % self.size
            hashes.append(combined_hash)
        return hashes

    def add(self, item):
        """
        Adds an item to the Bloom Filter.
        This involves hashing the item k times and setting the corresponding
        bits in the bit array to 1.
        """
        for digest in self._get_hashes(item):
            self.bit_array[digest] = 1

    def check(self, item):
        """
        Checks if an item is possibly in the set.

        Returns:
            bool: False if the item is definitely not in the set.
                  True if the item is *probably* in the set.
        """
        for digest in self._get_hashes(item):
            if self.bit_array[digest] == 0:
                return False  # Definitely not in the set
        return True  # Probably in the set

    def __contains__(self, item):
        """Allows using the 'in' keyword."""
        return self.check(item)

# --- Example Usage ---
if __name__ == "__main__":
    # Configuration
    num_items_to_store = 1000
    desired_fp_prob = 0.01  # 1% chance of false positives

    # 1. Create the Bloom Filter
    bloom = BloomFilter(num_items_to_store, desired_fp_prob)
    print(f"Bloom Filter created.")
    print(f"Optimal size (m): {bloom.size} bits")
    print(f"Optimal hash functions (k): {bloom.hash_count}")
    print("-" * 20)

    # 2. Add some items to the filter
    animals_to_add = ["cat", "dog", "lion", "tiger", "elephant", "giraffe", "zebra"]
    for animal in animals_to_add:
        bloom.add(animal)
    print(f"Added {len(animals_to_add)} items to the filter.")
    print("-" * 20)

    # 3. Check for items
    items_to_check = ["cat", "dog", "bird", "fish"]
    print("Checking for item membership:")
    for item in items_to_check:
        if item in bloom:
            if item in animals_to_add:
                print(f"'{item}' is in the set. (Correct)")
            else:
                # This is a potential false positive
                print(f"'{item}' is in the set. (False Positive!)")
        else:
            print(f"'{item}' is not in the set. (Correct)")

    # 4. Demonstrate false positive rate
    print("-" * 20)
    print("Demonstrating false positive rate...")
    num_test_items = 10000
    false_positives = 0
    for i in range(num_test_items):
        test_item = f"item-{i}"
        if test_item not in animals_to_add:
            if test_item in bloom:
                false_positives += 1

    fp_rate = (false_positives / num_test_items) * 100
    print(f"Tested {num_test_items} random items not in the set.")
    print(f"False positives found: {false_positives}")
    print(f"Actual False Positive Rate: {fp_rate:.4f}%")
    print(f"Desired False Positive Rate: {desired_fp_prob * 100:.4f}%")
```

## 4. Usages in Various Fields

Bloom filters are used in many systems where performance and space are critical.

**a) Databases (e.g., Google BigTable, Apache Cassandra)**

*   **Usage:** To reduce disk lookups for non-existent rows or columns.
*   **Example:** Before performing a costly disk read to find a specific row key, the database first checks a Bloom filter that contains all the row keys stored on that disk.
    *   If the filter says the key is **not present**, the database can immediately tell the client "not found" without ever touching the disk. This saves a huge amount of I/O.
    *   If the filter says the key **is present**, the database then performs the disk read. It might be a false positive, but this is acceptable as it avoids the vast majority of unnecessary reads.

**b) Networking (e.g., Content Delivery Networks - CDNs)**

*   **Usage:** To avoid caching "one-hit wonders" or web pages that are requested only once.
*   **Example:** A web cache (like Varnish or Squid) can use a Bloom filter to track all requested URLs. When a new request comes in, it's added to the filter. A second request for the same URL will find all bits set. The cache can then decide to store the content only on the *second* request. This prevents the cache from being filled with objects that will never be requested again.

**c) Security and Cryptocurrencies**

*   **Usage:** To check for malicious URLs, weak passwords, or previously seen data without storing the data itself.
*   **Example (Google Chrome):** Chrome uses a Bloom filter to implement its Safe Browsing feature. It downloads a small Bloom filter representing a huge list of malicious URLs. When you navigate to a URL, Chrome checks it against the filter.
    *   If the check is negative, the site is safe.
    *   If the check is positive (a "probable" match), Chrome sends a more detailed request to Google's servers for a full check. This protects user privacy as the full URL is only sent when necessary.
*   **Example (Bitcoin):** Bitcoin clients use Bloom filters to receive transactions relevant to their wallet without revealing their full public keys to network peers, enhancing privacy.

## 5. Bloom Filters with Other Data Structures

While a Bloom filter is fundamentally based on a **bit array**, the *concept* can be extended or used in conjunction with other data structures, though this is less common.

**a) Bloom Filters and Trees (e.g., Merkle-Bloom Trees)**

This is a more advanced and less common use case. You wouldn't typically implement the filter *itself* with a tree, but you can combine them.

*   **Concept:** Imagine a large, distributed system where data is stored in a tree-like structure (like a Merkle tree). Each node in the tree could have its own Bloom filter that represents all the data stored in the branches below it.
*   **Usage:** When searching for an item, you start at the root. You check the Bloom filter at the root.
    *   If the root's filter says the item is **not present**, you know it's not in the entire tree, and the search stops.
    *   If it says the item **is present**, you then check the Bloom filters of its children. You only traverse down the path where the filters continue to return "probably present."
*   **Benefit:** This can be much faster than traversing the entire tree, as you prune entire subtrees from your search at each level. This is useful in peer-to-peer networks or distributed file systems.

A direct implementation using a tree instead of a bit array is not standard because it defeats the core purpose of a Bloom filter: **O(1) time complexity for adds and checks**. A tree-based structure would introduce logarithmic complexity (`O(log n)`), which is less efficient. The power of a Bloom filter comes from its direct, constant-time access to bits in an array.
