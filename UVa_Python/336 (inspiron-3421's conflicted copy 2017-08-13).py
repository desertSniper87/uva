from collections import defaultdict

# import re


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


# def bfs(graph, start, ttl):
#     # dec_ttl_flag = True
#     q = []
#     r_node = 1
#     visited = {}
#     for g in graph:
#         visited[g] = False
#     visited[start] = True
#     q.append(start)
#     # q2 = [start]
#     # x = 0
#
#     # for i in range(0, ttl):
#     #     q2.extend(graph[start])
#     while (q):
#         print(q)
#         current = q.pop(0)
#         for a in graph[current]:
#             if not visited[a]:
#                 q.append(a)
#                 visited[a]=True
#                 r_node+=1
#                 print("visiting " + a)
#         # print("reducing ttl")
#         # for x in q:
#         #     for g in graph[x]:
#         #         if visited[g]!=True:
#         #             dec_ttl_flag=False
#         # if dec_ttl_flag==True:
#         #     ttl-=1
#         # if ttl==0:
#         #     return r_node
#
#                 ttl-=1
#
#         if ttl>0:

# def packet(graph, start, ttl):
#     visited = {}
#     for g in graph:
#         visited[g] = False
#     # visited[start] = True
#
#     q = [start]
#     q2 = []
#     for i in range(0, ttl):
#         q = q2
#         for s in q:
#             if  visited[s] == False:
#                 q2.extend(s)
#                 q2.extend(graph[s])
#                 visited[s] = True
#     ttl-=1


# def rec_bfs(n, g, v, ttl):
#     # print("ayyy lmao")
#     if (ttl==0):
#         return ttl
#     ttl-=1
#     v[n] = True
#     for x in g[n]:
#         print (" "+ x)
#         rec_bfs(x, g, v, ttl)




if __name__ == '__main__':
    f = open('input336.txt')
    while (True):
        num_of_edges = int(f.readline())
        # num_of_edges = int(input())
        if num_of_edges == 0:
            break
        graph = defaultdict(list)
        edge = 0
        break_edge_loop = 0
        while (True):
            if break_edge_loop == 1:
                break
            line = f.readline().rstrip()
            # line = input().rstrip()
            # #print(line)
            parts = line.split(" ")
            # #print(parts)
            values = remove_values_from_list(parts, "")
            # #print(values)
            it = iter(values)
            v = zip(it, it)
            for i1, i2 in v:
                graph[i1].append(i2)
                graph[i2].append(i1)
                edge += 1
            #print(graph)

            if edge == num_of_edges:
                line = remove_values_from_list(f.readline().rstrip().split(" "), "")
                # line = remove_values_from_list(input().rstrip().split(" "), "")
                #print(line)
                it = iter(line)
                tup = zip(it, it)
                for node, ttl in tup:
                    if node == '0' and ttl == '0':
                        break_edge_loop = 1
                        break
                    # r = len(graph)-bfs(graph, node, int(ttl))
                    # r = len(graph)-packet(graph, node, int(ttl))
                    # print(r)
                    visited = {}
                    for g in graph:
                        visited[g] = False
                    rec_bfs(node, graph, visited, int(ttl))


