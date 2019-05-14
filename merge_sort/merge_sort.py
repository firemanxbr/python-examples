"""
    Merge Sort with Unittests
"""
import unittest


def split(input_list):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]


def merge_sorted_lists(list_left, list_right):
    """
    Merge two sorted lists
    This is a linear operation
    O(len(list_right) + len(list_right))
    :param left_list: list
    :param right_list: list
    :return merged list
    """
    # Special case: one or both of lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left
    
    # General case
    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Right value bigger
            list_merged.append(list_right[index_right])
            index_right += 1
            
        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len(list_right):
            # Reached the end of right
            # Append the remainder of left and break
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Reached the end of left
            # Append the remainder of right and break
            list_merged += list_right[index_right:]
            break
        
    return list_merged


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        # The following line is the most important piece in this whole thing
        return merge_sorted_lists(merge_sort(left), merge_sort(right))


class Testing(unittest.TestCase):
    def test_split_odd(self):
        self.assertEqual(split(input_list=[1, 2, 3]), ([1], [2, 3]))

    def test_split_pair(self):
        self.assertEqual(split(input_list=[1, 2, 3, 4]), ([1, 2], [3, 4]))

    def test_split_five(self):
        self.assertEqual(split(input_list=[1, 2, 3, 4, 5]), ([1, 2], [3, 4, 5]))

    def test_split_one(self):
        self.assertEqual(split(input_list=[1]), ([], [1]))
    
    def test_split_none(self):
        self.assertEqual(split(input_list=[]), ([], []))

    def test_merge_sorted_lists_pair(self):
        self.assertEqual(merge_sorted_lists(list_left=[1, 5], list_right=[3, 4]), ([1, 3, 4, 5]))

    def test_merge_sorted_lists_one(self):
        self.assertEqual(merge_sorted_lists(list_left=[5], list_right=[1]), ([1, 5]))

    def test_merge_sorted_lists_none(self):
        self.assertEqual(merge_sorted_lists(list_left=[], list_right=[]), ([]))

    def test_merge_sorted_lists_four(self):
        self.assertEqual(merge_sorted_lists(list_left=[1, 2, 3, 5], list_right=[4]), ([1, 2, 3, 4, 5]))

    def test_merge_sorted_lists_three(self):
        self.assertEqual(merge_sorted_lists(list_left=[1, 2, 3], list_right=[]), ([1, 2, 3]))

    def test_merge_sorted_lists_one2three(self):
        self.assertEqual(merge_sorted_lists(list_left=[1], list_right=[1, 2, 3]), ([1, 1, 2, 3]))

    def test_merge_sorted_lists_someones(self):
        self.assertEqual(merge_sorted_lists(list_left=[1, 1], list_right=[1, 1]), ([1, 1, 1, 1]))

    def test_merge_sorted_lists_someones2two(self):
        self.assertEqual(merge_sorted_lists(list_left=[1, 1], list_right=[1, 2]), ([1, 1, 1, 2]))

    def test_merge_sorted_lists_three2onefour(self):
        self.assertEqual(merge_sorted_lists(list_left=[3, 3], list_right=[1, 4]), ([1, 3, 3, 4]))

    def test_merge_sort_two(self):
        self.assertEqual(merge_sort(input_list=[1, 2]), ([1, 2]))

    def test_merge_sort_pair(self):
        self.assertEqual(merge_sort(input_list=[2, 1]), ([1, 2]))

    def test_merge_sort_none(self):
        self.assertEqual(merge_sort(input_list=[]), ([]))

    def test_merge_sort_one(self):
        self.assertEqual(merge_sort(input_list=[1]), ([1]))

    def test_merge_sort_three(self):
        self.assertEqual(merge_sort(input_list=[5, 1, 1]), ([1, 1, 5]))

    def test_merge_sort_four(self):
        self.assertEqual(merge_sort(input_list=[9, 1, 10, 2]), ([1, 2, 9, 10]))


if __name__ == '__main__':
    unittest.main()
