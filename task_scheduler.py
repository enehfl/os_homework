

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
    if _curr_process is not None: #기존에 수행되고 있는 프로세스가 있는지 확인
        return selected_idx
    if len(_process_ready_queue) > 0: #대기 중인 프로세스 중 먼저 도착한 프로세스 선택
        selected_idx = 0

    return selected_idx


def round_robin(_curr_process, _process_ready_queue, _curr_process_run_tick=-1, _time_quantum=-1):
    selected_idx = -1
    # Select process to run
    if len(_process_ready_queue) > 0: #대기 중인 프로세스가 있는지 확인
        if _curr_process is None: #기존에 수행되고 있는 프로세스가 있는지 확인
            selected_idx = 0
        else:
            if _curr_process_run_tick > _time_quantum: #프로세스의 수행시간이 time_quantum보다 크면 교환
                selected_idx = 0

    return selected_idx


def shortest_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    if _curr_process is not None: #기존에 수행되고 있는 프로세스가 있는지 확인
        return selected_idx
    if len(_process_ready_queue) > 0: #대기 중인 프로세스가 있는지 확인
        if len(_process_ready_queue) == 1: #대기 중인 프로세스가 1개
            selected_idx = 0
        else:
            for i in range(len(_process_ready_queue) - 1): #대기 중인 프로세스 중 작업 시간이 가장 짧은 프로세스 선택
                if _process_ready_queue[i].req_run_time <= _process_ready_queue[i + 1].req_run_time:
                    selected_idx = i
                else:
                    selected_idx = i + 1

    return selected_idx


def shortest_remaining_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    if len(_process_ready_queue) > 0: #대기 중인 프로세스가 있는지 확인
        if len(_process_ready_queue) == 1: #대기 중인 프로세스가 1개
            min = 0
        else:
            for i in range(len(_process_ready_queue) - 1): #대기 중인 프로세스 중 작업 시간이 가장 짧은 프로세스 선택
                if _process_ready_queue[i].req_run_time <= _process_ready_queue[i + 1].req_run_time:
                    min = i
                else:
                    min = i + 1

        if _curr_process is None: #기존에 수행되고 있는 프로세스가 있는지 확인
            selected_idx = min
        else:
            if _curr_process.get_remaining_time() <= _process_ready_queue[min].req_run_time: #기존에 수행되고 있는 프로세스의 잔여시간과 위에서 선택한 작업 시간이 가장 짧은 프로세스와 비교 선택
                return selected_idx
            else:
                selected_idx = min

    return selected_idx