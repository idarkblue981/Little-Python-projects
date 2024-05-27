from sys import exit

def print_success(message):
    print(message)

def main():
    help_panel = """
            Operation Description        |        Type
                                         |
        Add a task                       |    Add
        Remove a task                    |    Remove
        Remove all the tasks             |    Remove All
        Mark a task as complete          |    Completed
        Mark all the tasks as complete   |    Completed All
                                         |
        List all the tasks               |    List All
        List the completed task          |    List Completed
        List the uncompleted tasks       |    List Uncompleted
                                         |
        Count all tasks                  |    Count All
        Count completed tasks            |    Count Completed
        Count uncompleted tasks          |    Count Uncompleted
                                         |
        See help panel                   |    Help Panel
        Exit program                     |    Exit
        """

    uncompleted_tasks = []
    completed_tasks = []
    print(help_panel)

    while True:
        try:
            list_operations = ['Add', 'Remove', 'Remove All', 'Completed', 'Completed All', 
                               'List All', 'List Completed', 'List Uncompleted', 
                               'Count All', 'Count Completed', 'Count Uncompleted', 
                               'Help Panel', 'Exit']
            
            operation = input('Enter Operation: ')
            
            # Operation does not exist
            if operation not in list_operations:
                raise ValueError('Invalid operation name!')
            
            # Add operation
            if operation == 'Add':
                add_task = input('Enter task: ')
                uncompleted_tasks.append(add_task)
                print_success('Task added successfully.')

            # Remove operation
            elif operation == 'Remove':
                remove_task = input('Enter task name: ')
                if remove_task in uncompleted_tasks:
                    uncompleted_tasks.remove(remove_task)
                    print_success('Task removed successfully.')
                elif remove_task in completed_tasks:
                    completed_tasks.remove(remove_task)
                    print_success('Task removed successfully.')
                else:
                    raise ValueError('Task not found!')

            # Remove All operation
            elif operation == 'Remove All':
                uncompleted_tasks.clear()
                completed_tasks.clear()
                print_success('All tasks removed successfully.')

            # Completed operation
            elif operation == 'Completed':
                completed_task = input('Enter task name: ')
                if completed_task in uncompleted_tasks:
                    uncompleted_tasks.remove(completed_task)
                    completed_tasks.append(completed_task)
                    print_success('Task marked as completed successfully.')
                else:
                    raise ValueError('Task not found in uncompleted tasks!')

            # Completed All operation
            elif operation == 'Completed All':
                if not uncompleted_tasks:
                    raise ValueError('No uncompleted tasks to mark as completed!')
                completed_tasks.extend(uncompleted_tasks)
                uncompleted_tasks.clear()
                print_success('All tasks marked as completed successfully.')

            # List All operation
            elif operation == 'List All':
                if not uncompleted_tasks and not completed_tasks:
                    raise ValueError('There are no tasks!')
                print('Uncompleted tasks:')
                print(*uncompleted_tasks, sep='\n')
                print('Completed tasks:')
                print(*completed_tasks, sep='\n')

            # List Completed operation
            elif operation == 'List Completed':
                if not completed_tasks:
                    raise ValueError('There are no completed tasks!')
                print('Completed tasks:')
                print(*completed_tasks, sep='\n')
                
            # List Uncompleted operation
            elif operation == 'List Uncompleted':
                if not uncompleted_tasks:
                    raise ValueError('There are no uncompleted tasks!')
                print('Uncompleted tasks:')
                print(*uncompleted_tasks, sep='\n')
                
            # Count All operation
            elif operation == 'Count All':
                total = len(uncompleted_tasks) + len(completed_tasks)
                print(f'Total tasks: {total}.')
            
            # Count Completed operation
            elif operation == 'Count Completed':
                total = len(completed_tasks)
                print(f'Total completed tasks: {total}.')

            # Count Uncompleted operation
            elif operation == 'Count Uncompleted':
                total = len(uncompleted_tasks)
                print(f'Total uncompleted tasks: {total}.')

            # Help operation
            elif operation == 'Help Panel':
                print(help_panel)
            
            # Exit operation
            elif operation == 'Exit':
                exit()

        except ValueError as ve:
            print(ve)

if __name__ == '__main__':
    main()