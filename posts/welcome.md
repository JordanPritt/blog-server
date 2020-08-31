## Introduction

When writing applications developers often come across scenarios where they need to solve a problem. That could be finding a specific word in a String, a property in an Object, an item/items in a list, and so on. Of the many possibilities you may need to find a number that is missing from a list of numbers.

## Sorted List

First let us take a look at a sorted list. Since it is with integer numbers we'll have them sort from smallest to largest. For example:

```python
number_list = [1, 2, 4, 5, 6, 7, 8, 9, 10]
```

As you can see we have a list ranging from 1 to 10 but missing the number 3. So now we need to figure out how to find it! Seems simple right? Well in a small case it is, but if we had a much larger list or we want to use the solution for different lists, then we will need to make an algorithm to find it.

## Loop Through the List

Since we know that the list is sorted we can use a loop to iterate through every number in the list from 1 to 10. While doing this loop we can then check if the loop's current iteration index/counter is the same as the corresponding index of the list. Let see what this looks like:

```python
def find_missing_number(list):
    for i in range(len(list)):
        if i + 1 != list[i]:
            return i + 1
```

So what do we have going on? Well first off, we are stepping through each number in the list: 1, 2, 3, etc. We are doing this with a for loop where i represents the iteration we are on. We are also checking whether or not that iteration is the same as the corresponding index in the list. You may be wondering why we have that +1, well the iteration is zero-indexed, but our list starts at 1 instead of zero. So without adding that 1 we have an off-by-one error and our first iteration will end the method by returning 0, which isn't what we want. So we add the one, make our check, then when we hit the third iteration we find out mismatch. This returns 3 because 3 is not equal to 4, and thus we have our number!

## Not Using a Loop

This is great! We found the missing number, but we are taking the time to step through each number and make a comparison. That makes our solution slower for larger lists. We could do this quicker! You might be thinking, how? Well with a different algorithm of course! We know we only need one number in the list, and where the list is supposed to end. So we could sum all the numbers in the completed sequence, eg 1 + 2 + 3 ... + 10, to get our total sum of 55. Then we can do the same for our list which gives us 52. Knowing this all we need to do is find the difference of the two and boom, we have our number!

So let's do this with code! First thing, Python makes summing a list easy with the sum() method. For our complete list we could make a new one my hand eg: list = [1,2,3...,10], however, that's not a good solution since we have to manually do that. Alternatively, we can use this formula to find the sum: n * (n + 1) / 2, which would be: 10*(10 + 1) / 2 and that results in the desired result: 55.

```python
def find_missing_number(list):
    sum_of_list = sum(list)
    sum_of_range = list[-1]*(list[-1] + list[0]) // 2
    return sum_of_range - sum_of_list
```

So we are getting the sum of the list in our first variable, then apply the formula to the second variable. Since we know we need the difference we can return sum_of_range - sum_of_list and get our number! We could even make this a one-liner:

```python
def find_missing_number(list):
    return (list[-1]*(list[-1] + list[0]) // 2) - sum(list)
```

Pretty simple right? At least in this case it is. Using formulas and algorithms, like this one, can help make for more concise code. More importantly though, we can get better performance by evaluating the different approaches. Where that doesn't make much of a difference in the small scale, it drastically changes as your data grows exponentially. So it's almost always a good idea to take performance into consideration when writing your application logic.

## Complete Application
Now lets put this altogether into a simple Python application:

```python
def find_missing_number(list):
    return (list[-1]*(list[-1] + list[0]) // 2) - sum(list)
def main():
    number_list = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    missing_num = find_missing_number(number_list)
    print('Missing number is:', missing_num)
if __name__ == "__main__":
    main()

```

And the output is:

`Missing number is: 3`

## Conclusion

So that's one way of finding a missing number with Python. I would encourage you to look for other algorithms and approaches to solve the same problem or similar ones. That way you can compare and contrast them, as this might not be the best solution for your needs. Hopefully you this post will help your coding endeavors. Leave your comments/questions below and happy coding!
