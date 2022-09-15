# 파이썬은 기본적으로 최소힙!

from heapq import heappush, heappop

heap = []

heappush(heap, 2)
heappush(heap, 5)
heappush(heap, 7)
heappush(heap, 3)
heappush(heap, 4)
heappush(heap, 6)
print(heap)

while heap:
    print(heappop(heap))

"""
heapq 모듈 이용해서 최대힙은 어떻게 구현할 수 있을까요?
직접 검색을 통해 알아봅시다!
"""