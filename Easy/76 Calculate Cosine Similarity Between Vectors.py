# Task: Implement Cosine Similarity
# In this task, you need to implement a function 
# cosine_similarity(v1, v2) that calculates the 
# cosine similarity between two vectors. 
# Cosine similarity measures the cosine of 
# the angle between two vectors, indicating their directional similarity.

# Input:
# v1 and v2: Numpy arrays representing the input vectors.
# Output:
# A float representing the cosine similarity.

# Constraints:
# Both input vectors must have the same shape.
# Input vectors cannot be empty or have zero magnitude.

# Example:
# Input:
# import numpy as np

# v1 = np.array([1, 2, 3])
# v2 = np.array([2, 4, 6])
# print(round(cosine_similarity(v1, v2), 3))
# Output:
# 1.0
# Reasoning:
# The cosine similarity between v1 and v2 is 1.0, 
# indicating perfect similarity (vectors point in the same direction).

import numpy as np

def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    if v1.shape != v2.shape:
        raise ValueError("Lỗi")
    if v1.size == 0:
        raise ValueError("Vector không được rỗng")
    
    numerator = 0
    deno_a = 0
    deno_b = 0
    for i in range (len(v1)):
        numerator = numerator + (v1[i] * v2[i])
        deno_a = deno_a + (v1[i] * v1[i])
        deno_b = deno_b + (v2[i] * v2[i])

    deno = (deno_a**0.5) * (deno_b ** 0.5)
    if deno == 0:
        raise ValueError("Mẫu 0")
    
    return numerator / deno

# Tối ưu numpy
# def cosine_similarity(v1, v2):
#     v1 = np.asarray(v1) -> asarray chuyển thành array numpy nếu chưa là array numpy
#     v2 = np.asarray(v2)

#     if v1.shape != v2.shape:
#         raise ValueError("Hai vector phải có cùng kích thước")

#     norm_product = np.linalg.norm(v1) * np.linalg.norm(v2)
#                       linalg.norm Tính độ dài vector (vector magnitude).
#                       căn của a[1]^2 + a[2]^2 + ... + a[n]^2

#     if norm_product == 0:
#         raise ValueError("Vector không được rỗng hoặc có độ dài bằng 0")

#     return np.dot(v1, v2) / norm_product
