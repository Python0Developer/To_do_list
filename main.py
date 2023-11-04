tasks=['Sending Emails']
print(tasks)
wanted_task = input('What you would like to do 1-add,2-remove,3-modify,4-getting out: ')
if int(wanted_task) == 1 :
    add_response = input('Write the task you want to add: ')
    tasks.append(add_response)
    print(f"task {add_response} added to tasks")
    print(tasks)
elif int(wanted_task) == 2 :
    print(tasks)
    remove_response = int(input('What do you want to remove 0 for the first task: '))
    tasks.pop(remove_response)
    print(f'task{remove_response} has been removed')
    print(tasks)
elif int(wanted_task) == 3 :
    print(tasks)
    user_modify = input('What you would like to modify 0 for the first task:')
    user_new_task = input('Write what do you want to take the task: ')
    user_new_task.replace(tasks)
    print(f'task {user_new_task} has been modified')
    print(tasks)
else :
    print('You are now out')
