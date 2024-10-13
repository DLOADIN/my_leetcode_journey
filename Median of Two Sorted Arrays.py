def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Calculate the total length
    total_length = len(nums1) + len(nums2)

    # Initialize the low and high pointers
    low = 0
    high = len(nums1)

    while low <= high:
        # Calculate the partition point for nums1
        partitionX = (low + high) // 2

        # Calculate the partition point for nums2
        partitionY = (total_length + 1) // 2 - partitionX

        # Calculate the max and min values for both partitions
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == len(nums1) else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == len(nums2) else nums2[partitionY]

        # Check if the partition is correct
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Calculate the median
            if total_length % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        # Adjust the partition points
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1