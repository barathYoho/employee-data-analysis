
import numpy as np

# 1. Create a NumPy array 
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print("Marks Array:")
print(marks)

print("Shape:", marks.shape)
print("Data Type:", marks.dtype)
print("Size:", marks.size)

# 2. Slice 
print("\nFirst two students, last subject:")
print(marks[:2, -1])

# 3. Calculate averages
student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)
print("\nStudent averages:", np.round(student_avg, 2))
print("Subject averages:", subject_avg)

# 4. Broadcasting: Add 5 grace marks
grace_marks = marks + 5
print("\nMarks after adding grace marks:")
print(grace_marks)

# 5. Weighted scores using np.dot()
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("\nWeighted scores:", weighted_scores)

# 6. Reshape
arr = np.arange(12)
reshaped_arr = arr.reshape(3, 4)
print("\nOriginal array:")
print(arr)
print("Reshaped 3x4 array:")
print(reshaped_arr)
