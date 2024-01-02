def dfs(graph, start, end, color, visited):
    if start == end:
        return True
    visited.add(start)
    for neighbor, edge_color in graph[start]:
        if neighbor not in visited and edge_color == color:
            if dfs(graph, neighbor, end, color, visited):
                return True
    return False

def process_queries(n, edges, queries):
    # 그래프 구성
    graph = {i: set() for i in range(1, n + 1)}
    for u, v, c in edges:
        graph[u].add((v, c))
        graph[v].add((u, c))

    # 쿼리 처리
    results = []
    for u, v in queries:
        colors = set()
        for _, color in graph[u]:
            if dfs(graph, u, v, color, set()):
                colors.add(color)
        results.append(len(colors))

    return results

# 파일 입출력을 사용하여 데이터 읽기 및 결과 저장
def read_input_and_process():
    with open("input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        edges = [tuple(map(int, file.readline().split())) for _ in range(m)]
        q = int(file.readline())
        queries = [tuple(map(int, file.readline().split())) for _ in range(q)]

    results = process_queries(n, edges, queries)

    with open("output.txt", "w") as file:
        for result in results:
            file.write(str(result) + "\n")

# 함수 실행
read_input_and_process()
