#!/usr/bin/env python3
import matplotlib.pyplot as plt

# Sample data (assuming consistent formatting with previous data)
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
age = [24, 27, 29, 30, None, 31, 32, 33, 33, 34, 34, None, 36, 57, None, 38, 39, None]
uric_acid = [None, 5.6, None, 5.9, 6.0, None, 7.7, 65, 5.199, 6.3, 6.4, 58, 6.5, 5.6, 6.3, 6.9, 6.1, None]
blood_pressure = [92, 95, 96.33, 97.33, 101, 96.00, 102, 84.67, 93, None, 102, 98.33, 93.33, 88.00, 103.33, 100.3, 92.67, 87.33]

# Filter out rows with missing index values (assuming index is in column 0)
filtered_data = [row for row in zip(index, age, uric_acid, blood_pressure) if row[0] is not None]
index, age, uric_acid, blood_pressure = zip(*filtered_data)

# Check if there are enough data points for each column to create a graph
if len(age) < 2 or len(uric_acid) < 2 or len(blood_pressure) < 2:
    print("Insufficient data to create graphs.")
else:
    plt.figure(figsize=(10, 6))

    # Age on x-axis, Blood Pressure and Uric Acid on y-axis
    plt.plot(age, blood_pressure, marker='o', label='Blood Pressure Level', linestyle='-')
    plt.plot(age, uric_acid, marker='s', label='Uric Acid', linestyle='-')
    plt.xlabel('Age')
    plt.ylabel('Blood Pressure Level / Uric Acid')
    plt.title('Blood Pressure Level & Uric Acid vs Age')
    plt.legend()

    # Connect the dots
    plt.plot(age, blood_pressure, marker='o', label='Blood Pressure Level', linestyle='-')
    plt.plot(age, uric_acid, marker='s', label='Uric Acid', linestyle='-')

    plt.tight_layout()
    plt.show()