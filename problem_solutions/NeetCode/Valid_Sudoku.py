class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = [set(), set(), set(), set(), set(), set(), set(), set(), 
set()]
        three_sub_boxes = [set(), set(), set()]
        for row_ind in range(len(board)):
            row = board[row_ind]
            row_set = set()
            if row_ind % 3 == 0:
                three_sub_boxes = [set(), set(), set()]
            for col_ind in range(len(row)):
                # if the digits repeat in the same row
                # print(col_set)
                grid_ind = col_ind // 3
                col_ele = row[col_ind]
                if col_ele in col_set[col_ind]:
                    return False
                if col_ele in row_set:
                    return False
                if col_ele in three_sub_boxes[grid_ind]:
                    return False
                # if non-empty
                elif col_ele != ".":
                    row_set.add(col_ele)
                    col_set[col_ind].add(col_ele)
                    three_sub_boxes[grid_ind].add(col_ele)
        return True
