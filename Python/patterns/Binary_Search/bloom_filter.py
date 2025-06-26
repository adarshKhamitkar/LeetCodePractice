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
