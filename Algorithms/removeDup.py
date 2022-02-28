# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP:
# How would you solve this problem if a temporary buffer is not allowed?


# O(N) Time
# O(N) Space
# Remove dups with a temp buffer
def removeDup(node):
        endHead = node
        dataSet = set()
        prev = None
        while node != None:
            if node.val in dataSet:
                prev.next = node.next
            else:
                dataSet.add(node.val)
                prev = node
            node = node.next
        return end

# O(n^2) Time
# O(1) Space
# Remove without buffer
def removeDup2(node):
    current = node
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.data == current.data:
                runner.next = runner.next.nex
            else:
                runner = runner.next
        current = current.next