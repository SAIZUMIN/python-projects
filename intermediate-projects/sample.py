task = ['Do Homework', 'Practice Coding', 'Study Python']

task.append('Learn Git')
print(task)

task.remove('Do Homework')
print(task)


print(len(task))

for i in range(len(task)):
    print(f'{i+1}. {task[i]}')