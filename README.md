🐍 Python List Operations Example
📜 Description
This script demonstrates basic list operations in Python, including:
✅ Creating an empty list
✅ Adding elements
✅ Inserting at specific positions
✅ Extending with another list
✅ Removing elements
✅ Sorting
✅ Finding the index of a value

🖥 Code Overview
1️⃣ Create an Empty List
python
Copy code
my_list = []
2️⃣ Append Elements
python
Copy code
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
Now:

csharp
Copy code
[10, 20, 30, 40]
3️⃣ Insert at a Specific Index
python
Copy code
my_list.insert(1, 15)
Now:

csharp
Copy code
[10, 15, 20, 30, 40]
4️⃣ Extend with Another List
python
Copy code
my_list.extend([50, 60, 70])
Now:

csharp
Copy code
[10, 15, 20, 30, 40, 50, 60, 70]
5️⃣ Remove the Last Element
python
Copy code
my_list.pop()
Now:

csharp
Copy code
[10, 15, 20, 30, 40, 50, 60]
6️⃣ Sort the List
python
Copy code
my_list.sort()
Now:

csharp
Copy code
[10, 15, 20, 30, 40, 50, 60]
7️⃣ Find and Print Index of 30
python
Copy code
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
Output:

yaml
Copy code
Index of 30: 3
📌 How to Run
Save the code into a file, e.g., list_operations.py

Run the script in your terminal:

bash
Copy code
python list_operations.py
📚 Methods Used
Method	Description
.append()	Add an element to the end of the list
.insert()	Insert an element at a given index
.extend()	Add multiple elements from another list
.pop()	Remove and return the last element
.sort()	Sort the list in ascending order
.index()	Find the index of a specific element

