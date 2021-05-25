#look at first 2 elements, if first is greater than the second, swap
#move on to the next elements and repeat

class Bubble_sort:

    def bubble_sort(list):
        size = len(list)


        for i in range(size-1):
            for i in range(size-1): #iterate through indices
                if list[i] > list[i+1]:
                    tmp = list[i] #store this variable at this indice
                    list[i] = list[i+1]
                    list[i+1]=tmp  #swap the variables




if __name__ == '__main__':
    list = [5,4,3,6,8,1,2,4,9,10]
    bs = Bubble_sort

    bs.bubble_sort(list)

    print(list) #the list will come back sorted
