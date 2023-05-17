
def get_process_to_assign_resources(_curr_resource_info, _curr_process_waiting_list):
    # Implement deadlock avoidance algorithm based on banker's algorithm
    # If there is no process to pick, return [-1, None]
    # Else, return [1, picked_processes]
    # Where, the picked processes contains list of processes

    picked_processes = []
    is_resource_cannot_be_assigned = False
    
    # Implement deadlock avoidance algorithm based on banker's algorithm
    for i in range(0, len(_curr_process_waiting_list)):
        allow = False
        j = 0
        while j < 5:
            if _curr_resource_info[j] < _curr_process_waiting_list[i].req_resources[j]:
                break
            j += 1
        else:
            allow = True
        
        if allow == True:
            picked_processes.append(_curr_process_waiting_list[i])
            for k in range(0, 5):
                _curr_resource_info[k] -= _curr_process_waiting_list[i].req_resources[k]

    if len(picked_processes) > 0:
        return [1, picked_processes]
    elif is_resource_cannot_be_assigned:
        return [-1, None]
    else:
        return [0, None]