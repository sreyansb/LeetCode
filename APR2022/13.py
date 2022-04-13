#attempt1:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        is_row_being_filled = 1
        row_to_fill = 0
        col_to_fill = n-1
        col_direction = 1
        row_direction = 1
        row_subtrahend = 0
        col_subtrahend = 0
        sentinel_value = float('inf')
        final_matrix = [[sentinel_value for i in range(n)] for j in range(n)]
        value_being_filled = 1
        while(value_being_filled<=n*n):
            #print(row_direction,row_to_fill,row_subtrahend,col_direction,col_to_fill,col_subtrahend)
            if is_row_being_filled:
                range_obj = range(n) if row_direction == 1 else range(n-1,-1,-1)
                for col in range_obj:
                        if final_matrix[row_to_fill][col] == sentinel_value:
                            final_matrix[row_to_fill][col] = value_being_filled
                            value_being_filled += 1
                if row_direction == -1:
                    row_subtrahend += 1
                    row_to_fill = row_subtrahend
                else:
                    row_to_fill = n-1-row_direction*row_subtrahend
                row_direction *= -1
            else:
                range_obj = range(n) if col_direction == 1 else range(n-1,-1,-1)
                for row in range_obj:
                    if final_matrix[row][col_to_fill] == sentinel_value:
                        final_matrix[row][col_to_fill] = value_being_filled
                        value_being_filled += 1
                if col_direction == -1:
                    col_subtrahend += 1
                    col_to_fill = n-1+col_direction*col_subtrahend
                else:
                    col_to_fill = col_direction*col_subtrahend                   
                col_direction *= -1
            is_row_being_filled ^= 1
        return final_matrix
                
                
                        
                    
            
        
