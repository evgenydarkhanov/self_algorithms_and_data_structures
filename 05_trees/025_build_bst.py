# построить из отсортированного массива сбалансированное бинарное дерево поиска
# [1, 2, 3, 4, 5, 6, 7] то есть, словно опустить массив
#
#           |
#           |
#           V
#
#           4
#     2           6
#  1     3     5     7

from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_balanced_bst(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    idx = len(nums) // 2
    curr_val = nums[idx]
    node = TreeNode(curr_val)
    
    node.left = build_balanced_bst(nums[:idx])
    node.right = build_balanced_bst(nums[idx + 1:])

    return node


if __name__ == "__main__":
    pass
