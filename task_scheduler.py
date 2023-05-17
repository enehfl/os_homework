

def get_process_idx_from_queue(_curr_process, _process_ready_queue, _scheduling_algorithm, _curr_process_run_tick=-1, _time_quantum=-1):
    selected_idx = -1

    if _scheduling_algorithm == "FCFS":
        selected_idx = first_come_first_served(_curr_process, _process_ready_queue)
    elif _scheduling_algorithm == "RR":
        selected_idx = round_robin(_curr_process, _process_ready_queue, _curr_process_run_tick, _time_quantum)
    elif _scheduling_algorithm == "SJF":
        selected_idx = shortest_job_first(_curr_process, _process_ready_queue)
    elif _scheduling_algorithm == "SRJF":
        selected_idx = shortest_remaining_job_first(_curr_process, _process_ready_queue)

    return selected_idx



def first_come_first_served(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run

    return selected_idx


def round_robin(_curr_process, _process_ready_queue, _curr_process_run_tick=-1, _time_quantum=-1):
    selected_idx = -1
    # Select process to run


    return selected_idx


def shortest_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    
    

    return selected_idx


def shortest_remaining_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    
    

    return selected_idx