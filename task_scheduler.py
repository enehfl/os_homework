

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
    if _curr_process is not None:
        return selected_idx
    if len(_process_ready_queue) > 0:
        selected_idx = 0

    return selected_idx


def round_robin(_curr_process, _process_ready_queue, _curr_process_run_tick=-1, _time_quantum=-1):
    selected_idx = -1
    # Select process to run


    return selected_idx


def shortest_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    if _curr_process is not None:
        return selected_idx
    if len(_process_ready_queue) > 0:
        if len(_process_ready_queue) == 1:
            selected_idx = 0
        else:
            for i in range(len(_process_ready_queue) - 1):
                if _process_ready_queue[i].req_run_time <= _process_ready_queue[i + 1].req_run_time:
                    selected_idx = i
                else:
                    selected_idx = i + 1

    return selected_idx


def shortest_remaining_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    if len(_process_ready_queue) > 0:
        if len(_process_ready_queue) == 1:
            min = 0
        else:
            for i in range(len(_process_ready_queue) - 1):
                if _process_ready_queue[i].req_run_time <= _process_ready_queue[i + 1].req_run_time:
                    min = i
                else:
                    min = i + 1

        if _curr_process is None:
            selected_idx = min
        else:
            if _curr_process.get_remaining_time() <= _process_ready_queue[min].req_run_time:
                return selected_idx
            else:
                selected_idx = min

    return selected_idx