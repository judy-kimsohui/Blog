# DFS

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# DFS는 "앞으로 찾아야 가야할 노드"와 "이미 방문한 노드"를 기준으로 데이터를 탐색한다.
# "앞으로 찾아야 가야할 노드"라면 계속 검색을 하는 것이고,
# "이미 방문한 노드"면 무시하거나 따로 저장

# "스택/큐"를 활용할 수도 있고, "재귀함수를 통해 구현할 수도 있다.

# [스택, 큐](https://sunho-doing.tistory.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
# 스택 : 먼저 들어온 데이터가 나중에 나가는 방식, 박스 쌓기
# 큐 : 먼저 들어온 데이터가 먼저 나가는 방식, 줄서기 : deque append(), pop()과 더불어 appendleft(), popleft() 
# appendleft(), popleft() 메소드는 각각 시간복잡도가 O(1)