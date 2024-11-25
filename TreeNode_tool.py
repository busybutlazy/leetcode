class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def tree_maker(li_of_node):
    l=len(li_of_node)
    for i in range(l):
        # if not li_of_node[i]:
        #     continue
        li_of_node[i]=TreeNode(li_of_node[i])

    for i in range(l):
        if not li_of_node[i]:
            continue
        left=i*2+1
        right=i*2+2
        if left < len(li_of_node):
            li_of_node[i].left=li_of_node[left]
        if right < len(li_of_node):
            li_of_node[i].right=li_of_node[right]
    return li_of_node[0]



def tree_to_list(head):
    que=[head]
    result=[]
    tmp=None
    while que:
        tmp=que.pop(0)
        if tmp:
            result.append(tmp.val)
            if tmp.left:
                que.append(tmp.left)
            if tmp.right:
                que.append(tmp.right)    
    return result


def tree_printer(head):
    li=tree_to_list(head)
    length=len(li)
    level=1
    for i in range(length):
        if level==i+1:
            print("*")
            level*=2
        for _ in range((length-level)//2+2):
            print('{:^7}'.format(""),end="")
        if li[i]:
            print('{:^7}'.format(li[i]),end="")
        else:
            print('{:^7}'.format("None"),end="")

def rotate(subroot:TreeNode,direction:bool)->TreeNode:
            """
            direction=True meaning switch right as new root
            """
            if direction:
                new_head=subroot.right
                new_head.left,subroot.right=subroot,new_head.left
            else:
                new_head=subroot.left
                new_head.right,subroot.left=subroot,new_head.right
            return new_head