nums = [1, 2, 2, 3, 3, 3, 10, 5, 2, 8, 4, 1]

def bucket_sort(nums):
    """
    Bucket Sort
    """
    buckets = [[] for _ in range(10)]
    for num in nums:
        buckets[num // 10].append(num)
    for bucket in buckets:
        bucket.sort()
    return buckets

