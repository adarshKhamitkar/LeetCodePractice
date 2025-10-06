import heapq

employees = [['id', 'emp_name', 'department_id', 'salary'],
             [1, 'John Doe', 1, 50000],
             [2, 'Jane Smith', 2, 60000],
             [3, 'Jim Beam', 1, 55000],
             [4, 'Jill Johnson', 2, 65000],
             [5, 'Jack Doe', 1, 52000],
             [6, 'Jackson', 2, 62000],
             [7, 'Jim Beamson', 3, 57000],
             [8, 'Jill Johndottr', 3, 67000],
             [9, 'Jack Stagg', 2, 54000],
             [10, 'Jill Smithson', 3, 64000]]

departments = [['department_id', 'dept_name'],
              [1, 'HR'],
              [2, 'IT'],
              [3, 'Finance'],
              [4, 'Marketing'],
              [5, 'Sales'],
              [6, 'Engineering'],
              [7, 'Customer Service'],
              [8, 'Legal']]

emp_headers = employees[0]
dept_headers = departments[0]

emps_dict = []
depts_dict = []

for emp in employees[1:]:
    emp_dict = {emp_headers[i]: emp[i] for i in range(len(emp_headers))}
    emps_dict.append(emp_dict)

for dept in departments[1:]:
    dept_dict = {dept_headers[i]: dept[i] for i in range(len(dept_headers))}
    depts_dict.append(dept_dict)

dept_map = {row['department_id']: row for row in depts_dict}

merged_dict = []

for emp_row in emps_dict:
    emp_dept_id = emp_row['department_id']
    if emp_dept_id in dept_map:
        merged = emp_row.copy()

        for k,v in dept_map[emp_dept_id].items():
            merged[k] = v

        merged_dict.append(merged)

_heap, _sorted = [], []

for row in merged_dict:
    heapq.heappush(_heap,((-1)*row['salary'],row))

while _heap:
    _sorted.append(heapq.heappop(_heap)[1])

print(_sorted)

# [{'id': 1, 'emp_name': 'John Doe', 'department_id': 1, 'salary': 50000, 'dept_name': 'HR'}, 
#  {'id': 5, 'emp_name': 'Jack Doe', 'department_id': 1, 'salary': 52000, 'dept_name': 'HR'}, 
#  {'id': 9, 'emp_name': 'Jack Stagg', 'department_id': 2, 'salary': 54000, 'dept_name': 'IT'}, 
#  {'id': 3, 'emp_name': 'Jim Beam', 'department_id': 1, 'salary': 55000, 'dept_name': 'HR'}, 
#  {'id': 7, 'emp_name': 'Jim Beamson', 'department_id': 3, 'salary': 57000, 'dept_name': 'Finance'}, 
#  {'id': 2, 'emp_name': 'Jane Smith', 'department_id': 2, 'salary': 60000, 'dept_name': 'IT'}, 
#  {'id': 6, 'emp_name': 'Jackson', 'department_id': 2, 'salary': 62000, 'dept_name': 'IT'}, 
#  {'id': 10, 'emp_name': 'Jill Smithson', 'department_id': 3, 'salary': 64000, 'dept_name': 'Finance'}, 
#  {'id': 4, 'emp_name': 'Jill Johnson', 'department_id': 2, 'salary': 65000, 'dept_name': 'IT'}, 
#  {'id': 8, 'emp_name': 'Jill Johndottr', 'department_id': 3, 'salary': 67000, 'dept_name': 'Finance'}]


# [{'id': 8, 'emp_name': 'Jill Johndottr', 'department_id': 3, 'salary': 67000, 'dept_name': 'Finance'},
#  {'id': 4, 'emp_name': 'Jill Johnson', 'department_id': 2, 'salary': 65000, 'dept_name': 'IT'}, 
#  {'id': 10, 'emp_name': 'Jill Smithson', 'department_id': 3, 'salary': 64000, 'dept_name': 'Finance'}, 
#  {'id': 6, 'emp_name': 'Jackson', 'department_id': 2, 'salary': 62000, 'dept_name': 'IT'}, 
#  {'id': 2, 'emp_name': 'Jane Smith', 'department_id': 2, 'salary': 60000, 'dept_name': 'IT'}, 
#  {'id': 7, 'emp_name': 'Jim Beamson', 'department_id': 3, 'salary': 57000, 'dept_name': 'Finance'}, 
#  {'id': 3, 'emp_name': 'Jim Beam', 'department_id': 1, 'salary': 55000, 'dept_name': 'HR'}, 
#  {'id': 9, 'emp_name': 'Jack Stagg', 'department_id': 2, 'salary': 54000, 'dept_name': 'IT'}, 
#  {'id': 5, 'emp_name': 'Jack Doe', 'department_id': 1, 'salary': 52000, 'dept_name': 'HR'}, 
#  {'id': 1, 'emp_name': 'John Doe', 'department_id': 1, 'salary': 50000, 'dept_name': 'HR'}]
