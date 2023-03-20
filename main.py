# python3
import heapq

def parallel_processing(n, j, data):
    treads = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(n):
        heapq.heappush(treads, (0,i))
    swaps = []
    for i in range(j):
        data_time = data[i]
        start_time, tread = heapq.heappop(treads)
        swaps.append((tread, start_time))
        heapq.heappush(treads, (start_time + data_time, tread))
    return swaps

def main():
    try:
        n, j = map(int, input().split())
        data = list(map(int, input().split()))
    except ValueError:
        return
    
    result = parallel_processing(n, j, data)
    total = result[-1][1]
    print(total)
    for i in range(len(result)):
        print(x[i][0], result[i][1])



if __name__ == "__main__":
    main()
