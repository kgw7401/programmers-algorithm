#1
# 좌표와 주어진 순서를 가지고 이진 트리 생성
### 전위, 후위 순화 결과 ###

#2
# y좌표 정렬로 만들고 x좌표 비교해서 add

import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, info):
        self.left = None
        self.right = None
        self.num = info[0]
        self.x = info[1]
        self.y = info[2]

def add_node(root, info):
    if root.x < info[1]:
        if not root.right:
            root.right = Node(info)
        else:
            add_node(root.right, info)
    elif root.x > info[1]:
        if not root.left:
            root.left = Node(info)
        else:
            add_node(root.left, info)

def preorder(root, order):
    if root != None:
        order.append(root.num)
        preorder(root.left, order)
        preorder(root.right, order)

def postorder(root, order):
    if root != None:
        postorder(root.left, order)
        postorder(root.right, order)
        order.append(root.num)

def solution(nodeinfo):
    new_nodeinfo = []
    for idx, info in enumerate(nodeinfo):
        new_nodeinfo.append((idx+1, *info))

    new_nodeinfo = sorted(new_nodeinfo, key=lambda x: (-x[2], x[1]))

    root = Node(new_nodeinfo[0])

    for info in new_nodeinfo[1:]:
        add_node(root, info)

    preorderlist = []
    preorder(root, preorderlist)

    postorderlist = []
    postorder(root, postorderlist)

    answer = [preorderlist, postorderlist]
    return answer