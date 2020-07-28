# Definition for a Node.
class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def __init__(self):
        self.visited = {}

    def copy_random(self,head):
        if not head:
            return None
        #if we already have processed the current node, return the cloned version of it
        if head in self.visited:
            return self.visited[head]

        #create a new node with the same value as old node
        node = Node(head.val, None, None)

        #save this value in the hashmap
        self.visited[head] = node

        #recuesively copy the remaining linkedlist starting once from the next pointer and then from the random pointer
        #we have 2 independent recursive calls
        #update the next and random pointers for the new node created
        node.next = self.copy_random(head.next)
        node.random = self.copy_random(head.random)

        return node

class Solution2(object):
    def __init__(self):
        self.visited = {}

    def get_cloned(self,node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val,None,None)
                return self.visited[node]
        return None

    def copy_random_list(self,head):
        if not head:
            return head
        
        old_node = head
        #creating a new head node
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        #iterate on the linked list until all nodes are cloned
        while old_node != None:

            #get the clone of the nodes referenceed by random and next pointers
            new_node.random = self.get_cloned(old_node.random)
            new_node.next = self.get_cloned(old_node.next)

            #move one step ahead in the linkedlist
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

class Solution3(object):

    def copy_random(self,head):
        if not head:
            return head

        #create a new weaved list of original and copied nodes
        ptr = head
        while ptr:

            #cloned node
            new_node = Node(ptr.val,None,None)

            #inserting the cloned node just next to the original node
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        
        ptr = head

        #now link the random pointers of the new nodes created
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        #unweave the linkedlist to get back the original linkedlist and cloned list
        ptr_old_list = head
        ptr_new_list = head.next
        head_old = head.next

        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list = ptr_new_list.next.next if ptr_new_list else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old