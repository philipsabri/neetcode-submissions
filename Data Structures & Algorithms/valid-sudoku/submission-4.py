class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal_set = [set() for _ in range(9)]
        vertical_set = [set() for _ in range(9)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]

        for h in range(9):
            for v in range(9):
                number = board[h][v]
                box = (h // 3, v // 3)
                if number == ".":
                    continue

                # check horizontal
                if number in horizontal_set[h]:
                    return False
                horizontal_set[h].add(number)

                # check vertical
                if number in vertical_set[v]:
                    return False
                vertical_set[v].add(number)

                # check box
                if number in box_set[box[0]][box[1]]:
                    return False
                box_set[box[0]][box[1]].add(number)
        return True
