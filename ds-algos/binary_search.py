#binary search:
#take middle element and check if number on left or right hand side since list is sorted
#if number not on left side, discard left side
#after this, go to middle of the remaining list and check both sides and discard again


class BinarySearch:

    def binary_search(list,x):

        left_index = 0 #left hand side of list
        right_index = len(list) - 1 #right hand side of list


        while left_index <= right_index:
            mid_index = (left_index+right_index)//2
            mid_number = list[mid_index]

            if mid_number == x:
                return mid_index

            #in this example if mid index is 5, which is less than 8
            #we then rearrange the lsit so that the left side of the list
            #is discarded
            if mid_number < x:
                left_index = mid_index+1

            else:
                right_index = mid_index-1 #rearragne right index

        return -1


if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10]
    x = 2

    bs = BinarySearch
    result = bs.binary_search(list,x)
    print(result)

