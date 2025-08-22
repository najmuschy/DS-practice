def unionArray(nums1, nums2):
    size1 =len(nums1)
    size2 = len(nums2)
    i=0
    j=0
    result = []
    last= 0
    while i<size1 and j<size2 :

        if nums1[i]<=nums2[j] :
            if nums1[i]!=last:
                last = nums1[i]
                result.append(nums1[i])
                i+=1
            else:
                i+=1
        elif nums2[j]<nums1[i] :
            if nums2[j]!=last:
                last = nums2[j]
                result.append(nums2[j])
                j+=1
            else:
                j+=1
    
    if i==len(nums1):
        while j!=len(nums2):
            if nums2[j]!=last:
                result.append(nums2[j])
                j+=1
            else:
                j+=1

    if j==len(nums2):
        while i!=len(nums1):
            if nums1[i]!=last:
                result.append(nums1[i])
                i+=1
            else:
                i+=1               
    return result

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]

print(unionArray(nums1, nums2))