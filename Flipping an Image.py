class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        matrix_size = len(image)
        for each_row_index in range(matrix_size):
            left_pointer_position = 0
            right_pointer_position = matrix_size - 1
            
            while left_pointer_position <= right_pointer_position:
                left_value_after_inversion = 1 - image[each_row_index][right_pointer_position]
                right_value_after_inversion = 1 - image[each_row_index][left_pointer_position]
                
                image[each_row_index][left_pointer_position] = left_value_after_inversion
                image[each_row_index][right_pointer_position] = right_value_after_inversion
                
                left_pointer_position += 1
                right_pointer_position -= 1
        
        return image
