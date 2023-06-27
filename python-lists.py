if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(0,N):    
        un_split_cmd = str(input())
        command = un_split_cmd.split()
        if 'append' in command:
            my_list.append(int(command[1]))
        elif 'insert' in command:
            my_list.insert(int(command[1]),int(command[2]))
        elif 'print' in command:
            print(my_list)
        elif 'sort' in command:
            my_list.sort()
        elif 'pop' in command:
            my_list.pop()
        elif 'remove' in command:
            my_list.remove(int(command[1]))
        elif 'reverse' in command:
            my_list.reverse()
            
        
