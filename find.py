import numpy as np

def find_nearest(array, value):
    array = np.asarray(array)
    new_array = array - value
    # print(new_array)
    norm_array = np.empty(len(new_array[0]))
    for i in range(len(new_array[0])):
        norm_array[i] = new_array[0][i] ** 2 + new_array[1][i] ** 2
    # print(norm_array)
    idx = norm_array.argmin()
    return idx

# # array = np.random.random((2, 10))
# array = [
#     [1, 2, 3, 4, 5],
#     [1, 4, 5, 5, 6]
# ]
# print(array)
# # [ 0.21069679  0.61290182  0.63425412  0.84635244  0.91599191  0.00213826
# #   0.17104965  0.56874386  0.57319379  0.28719469]

# value = np.array(
#     [
#         [5],
#         [6]
#     ]
# )

# print(find_nearest(array, value))
# # 0.568743859261