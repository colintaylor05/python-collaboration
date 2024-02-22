def addtasks():
    num = int(input("how many tasks do you want to do:"))
    tasks = {}
    for i in range(num):
        task = str(input(f"what is task {i + 1}:"))

        tasks[i + 1] = task +" (incomplete)"
    print("this is your todo list")
    for key, value in tasks.items():
        print(key, ':', value)
    return tasks


def newtasks(tasks):
    num = int(input("how many tasks do you want to add:"))
    start = len(tasks) + 1
    newtasks = {}
    for i in range(num):
        task = str(input(f"what is task {start + i}:"))
        newtasks[start + i] = task+" (incomplete)"
    return newtasks

def deletetasks(tasks):
    Del = input("what task would you like to delete:")
    keydelete = []
    for key, value in tasks.items():
        if value == Del:
            keydelete.append(key)
    for key in keydelete:
        del tasks[key]

def completetask(tasks):
        numb=int(input("what number task did you complete:"))
        for i,value in tasks.items():
            if i == numb:
                tasks[i]= tasks[i].replace("incomplete" , "complete")
def main():
    tasks = addtasks()
    new = input("do you want to add a task(y/n):")
    if new == 'y':
        newtask = newtasks(tasks)
        tasks.update(newtask)
        print("this is the new todo list")
        for key, value in tasks.items():
            print(key, ':', value)
    Del = input("do you want to delete a task(y/n):")
    
    if Del == 'y':
        deletetasks(tasks)
    print("this is the new todo list")

    complete=input("do you want to mark any tasks complete(y/n):")
    if complete == 'y':
        completetask(tasks)
    for key, value in tasks.items():
        print(key, ':', value)


main()