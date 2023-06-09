import process

VERSION = 1.1

def get_process_to_assign_resources(_curr_resource_info, _total_resource_info, _curr_process_waiting_list):
    # Implement deadlock avoidance algorithm based on banker's algorithm
    # If there is no process to pick, return [-1, None]
    # Else, return [1, picked_processes]
    # Where, the picked processes contains list of processes

    picked_processes = []
    is_resource_cannot_be_assigned = False
    available_resources = _curr_resource_info
    
    # Implement deadlock avoidance algorithm based on banker's algorithm
    for i in range(len(_curr_process_waiting_list)):
        allow = False
        for j in range(5):
            if available_resources[j] < _curr_process_waiting_list[i].get_required_resource()[j]: #자원 할당 가능한 프로세스 확인
                if _total_resource_info[j] < _curr_process_waiting_list[i].get_required_resource()[j]: #자원을 과도하게 요청하여 자원 할당이 불가능한 프로세스가 있는지 확인
                    is_resource_cannot_be_assigned = True
                break
        else:
            allow = True

        if allow:
            picked_processes.append(_curr_process_waiting_list[i]) #자원 할당이 가능한 프로세스 추가
            break

    if len(picked_processes) > 0:
        return [1, picked_processes]
    elif is_resource_cannot_be_assigned:
        return [-1, None]
    else:
        return [0, None]