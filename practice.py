"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    for element in items:
        print element


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """

    long_words = []

    for word in words:
        if len(word) > 4:
            long_words.append(word)
    return long_words


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    words_longer_n = []
    for word in words:
        if len(word) > n:
            words_longer_n.append(word)
    return words_longer_n

# This function, swap_numbers is to be used for the code in smallest_int if we can't use the short function I wrote using sorted()
def swap_numbers(index1, index2, list_to_swap):
    """ Takes in a list and two indicies in a list thats elements must be swapped"""
    element1 = list_to_swap[index1]
    element2 = list_to_swap[index2]
    list_to_swap[index1] = element2
    list_to_swap[index2] = element1
    return list_to_swap

def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    # If we can use sorted:
    # if len(numbers) == 0:
    #     return 
    # ordered = sorted(numbers)
    
    # return ordered[0]

    # If we can't do sorted using function I wrote ABOVE swap_numbers

   
    if len(numbers) == 0:
        return 
   
    index1 = 0
    while index1 < len(numbers):
    
        index2 = 1
        while index2 < len(numbers):
            if numbers[index2] < numbers[index1]:
                swap_numbers(index1, index2, numbers)
            index2 +=1
        index1 +=1

    return numbers[0]

    # OR if it should be shorter code the below is optimized I think
    # if len(numbers) == 0:
    #     return

    # smallest = numbers[0]

    # for number in numbers:
    #     if smallest > number:
    #         smallest = number
    # return smallest




def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    if len(numbers) == 0:
        return

    largest = numbers[0]

    for number in numbers:
        if largest < number:
            largest = number
    return largest



def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    for ind, number in enumerate(numbers):
        numbers[ind] = number/2.0
    return numbers


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    word_len_list = []
    for word in words:
        word_len_list.append(len(word))
    return word_len_list


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    sum_of_list = 0

    for number in numbers:
        sum_of_list = sum_of_list + number
    return sum_of_list

def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    product_of_list = 1

    for number in numbers:
        product_of_list = product_of_list * number
    return product_of_list


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """
    sentence = ""
    
    for word in words:
        sentence = sentence + word
    return sentence

def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
        
    """
    #For some reason adding my test for an empty list messed things up so lets talk about that but this was what I would want
    # >>> average([])
    #     None
    if len(numbers) == 0:
        return 
    sum_numbers = 0
    for number in numbers:
        sum_numbers = float(sum_numbers) + number
    return sum_numbers/len(numbers)


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    list_to_string = words[0]
    index = 1
    while index < len(words):
        list_to_string = list_to_string + ", " + words[index]
        index +=1
    
    return list_to_string


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    new_list = items[::-1]
    
    return new_list

# *********COME BACK TO THIS ONE

def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    # WHEN I RUN THIS WITH OUT LINE 373 and 378 which have >>> orig in it this runs I don't understand why that line is in the test code nor how to accomidate for it. I have checked the id() of my items list before the code is run and after it has executed and they have the same parking spot number so I think that should be proof that this code reverses inplace? Lets talk about how I could have over come this issue! Thank you

    saved_list = items[:]
    negative_ind = 0
    for ind, item in enumerate(items):
    
        if ind == 0:
            negative_ind = -1
        else:
            negative_ind = (-1 * ind) -1
        
        items[ind] = saved_list[negative_ind]
    return items

def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    
    index1 = 0
    duplicates_list = []
    while index1 < (len(items) -1):
        index2 = index1 + 1
        while index2 < len(items):
            if items[index1] == items[index2]:
                if items[index1] not in duplicates_list:
                    duplicates_list.append(items[index1]) 
                    
            index2 +=1
        index1 +=1
        
    return sorted(duplicates_list)

def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    index_list = []
    for word in words:
        index = 0
        while index < len(word):
            if letter not in word:
                index_list.append(None)
                break
            elif word[index] == letter:
                index_list.append(index)
                break 
            index +=1
            
    return index_list


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
