from collections import deque

N = int(input())
card_list = deque([i for i in range(1, N+1)])

while(len(card_list) > 1):
    card_list.popleft()
    num_move = card_list.popleft()
    card_list.append(num_move)

print(card_list[0])