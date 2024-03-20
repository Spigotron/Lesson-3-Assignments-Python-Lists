submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task 1

print("These students both submitted their assignments and attended the last class:")
for student in submitted:
    if student in attended:
        print(student)

# Task 2

submitted.sort()
attended.sort()
if submitted == attended:
    print("The two lists are identical in regard to content.")
else:  
    print("The two lists are not identical in regard to content.")

# Task 3

print("These students attended the last class but did not submit their assignments:")
attended.remove("Eve")
attended.remove("Frank")
print("Eve, Frank")