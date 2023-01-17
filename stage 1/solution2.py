def solution(f_in, f_out):
    list_str = [x for x in f_in]
    N = int(list_str[0])
    log_list = [list(map(int, list_str[i * 2 + 2].split())) for i in range (N)] #список логов
    for logs in log_list:
        for sec in logs:
            i = logs.count(sec)
            i -= i % 2
            while i > 0:
                logs.remove(sec)
                i -= 1
                
    result = log_list[0] # первый лог, результат будет меняться
    for i in range(1, N):
        pos1 = 0
        pos2 = 0
        upd = []
        while (pos1 != len(result) and pos2 != len(log_list[i])):
            if result[pos1] >= log_list[i][pos2 + 1]:
                pos2 += 2
            elif result[pos1 + 1] <= log_list[i][pos2]:
                pos1 += 2
            else:
                upd.append(max(result[pos1], log_list[i][pos2]))
                upd.append(min(result[pos1 + 1], log_list[i][pos2 + 1]))
                pos1 += 2
                pos2 += 2
        result = upd
    last_string = " ".join(list(map(str, result)))
    print(len(result))
    if len(last_string) > 0:
        print(last_string)

if __name__ == "__main__":
    import sys
    solution(sys.stdin, sys.stdout)