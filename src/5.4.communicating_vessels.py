def interleave(*iterables):
    # - Takes multiple iterables and combines them by alternating elements
    # - Creates iterators for each input to track position
    # - Uses list(iterators) to safely modify while iterating
    # - Appends items until all iterators are exhausted
    # - Returns combined list
    iterators = [iter(it) for it in iterables]  # Convert all to iterators
    result = []
    while iterators:  # Keep going until all iterators are done
        for it in list(iterators):  # Safe iteration with copy
            try:
                result.append(next(it))  # Get next item
            except StopIteration:
                iterators.remove(it)  # Remove exhausted iterators
    return result

def generator_interleave(*iterables):
    # - Generator version of interleave
    # - Same logic but yields items one at a time
    # - More memory efficient for large inputs
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in list(iterators):
            try:
                yield next(it)  # Yield instead of append
            except StopIteration:
                iterators.remove(it)

if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))  
    print(list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))))  