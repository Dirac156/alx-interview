#!/usr/bin/env python3
"""lockbox interview question"""


def canUnlockAll(boxes):
    """lockbox function"""
    newlist = []
    k = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[k-1]:
            return False
        for j in i:
            newlist.append(j)
    for index, keys in enumerate(boxes):
        if index in newlist or index < k-1:
            pass
        else:
            return False
    return True
