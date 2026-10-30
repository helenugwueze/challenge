def reverse_first(queue, K):
    if K <= 0 or K > len(queue):
        return queue
    stack = []
    for _ in range(K):
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    for _ in range(len(queue) -K):
        queue.append(queue.pop(0))
    return queue

qu1 = [10, 20, 30, 40, 50]
print(reverse_first(qu1, 3))
