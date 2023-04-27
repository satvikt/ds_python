from data_structures.Node import Node

def merge_sorted(head1, head2):
    # if both lists are empty then merged list is also empty
    # if one of the lists is empty then other is the merged list
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None

    if head1.data > head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2.data
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        if head1.data > head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp2 = head2
            head2 = head2.next

        mergedHead.next = temp
        mergedHead = mergedHead.next



