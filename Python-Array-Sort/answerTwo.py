#Python code
#author: Enda Sexton
#date: 29th March 2016
#purpose: to demonstrate ability to write function to flatten an arbitrary multidimensional array
#         to a single flat dimensional array, this function accepts chars, ints, floats, etc and copes
#         with them.


def flatten( array,builderArray):
        for i in array:
                try:
                        if i.__len__() >= 1:
                                flatten(i,builderArray)
                except:
                        builderArray.append(i)

        return builderArray


def main():
        age = [[1,2,[3]],4]
        #age = [[1,2],[4],[[[7,4,3]],[5,[2],[34,[4,[[[[[[[[[3],4]]]]]]]]]]]]]
        flatArray= []
        flatArray = flatten(age,flatArray)
        print (flatArray)

if __name__ == "__main__":
        main()




