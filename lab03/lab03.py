import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')

#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:
    """
    This method should sort input list lst of elements of some type T.

    Elements of the list are compared using function compare that takes two
    elements of type T as input and returns -1 if the left is smaller than the
    right element, 1 if the left is larger than the right, and 0 if the two
    elements are equal.
    """
    num=len(lst)
    i=0
    while(i<num-1):
        min=i
        j=i+1
        while(j<num):
            if(compare(lst[j], lst[min])<0):
                min=j
            j+=1
        if(min!=i):
            var=lst[i]
            lst[i]=lst[min]
            lst[min]=var
        i+=1
    return lst
        
    pass

def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
    """
    This method search for elem in lst using binary search.

    The elements of lst are compared using function compare. Returns the
    position of the first (leftmost) match for elem in lst. If elem does not
    exist in lst, then return -1.
    """
    front=len(lst)-1
    back=0
    mid=0
    while(back<=front):
        mid=(front+back)//2
        if(compare(lst[mid], elem)<0):
            back=mid+1
        elif(compare(lst[mid],elem)==0):
            return mid
        else:
            front=mid-1
    return -1
    pass

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)

#################################################################################
# EXERCISE 2
#################################################################################
class PrefixSearcher():
    saved=[]
    num=0
    def __init__(self, document, k):
        """
        Initializes a prefix searcher using a document and a maximum
        search string length k.
        """
        lst=[]
        comp=lambda i,j:0 if i==j else (-1 if i<j else 1)
        x=0
        while(x<len(document)):
            lst.append(document[x:x+k])
            x+=1
        sortLst=mysort(lst, comp)
        self.saved=sortLst
        self.num=k
        pass

    def search(self, q):
        """
        Return true if the document contains search string q (of

        length up to n). If q is longer than n, then raise an
        Exception.
        """
        comp=lambda x,y:0 if x==y else(-1 if x<y else 1)
        if(len(q)>self.num):
            raise Exception("Length of N less than Length of Q")
        return mybinsearch(self.saved,q,comp)!=-1
        pass

# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertFalse(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

#################################################################################
# EXERCISE 3
#################################################################################
class SuffixArray():

    def __init__(self, document: str):
        """
        Creates a suffix array for document (a string).
        """
        self.doc=document
        lst=list(range(0,len(document)))
        self.arr = mysort(lst, lambda x,y: 0 if document[x:] == document[y:] else (-1 if document[x:] < document[y:] else 1))

        pass


    def positions(self, searchstr: str):
        """
        Returns all the positions of searchstr in the documented indexed by the suffix array.
        """
        n=len(searchstr)
        comp=lambda i,j: 0 if self.doc[i:i+n]==j else (-1 if self.doc[i:] < j else 1)
        var=mybinsearch(self.arr,searchstr,comp)
        i=var
        while(i>1):
            txt = self.doc[self.arr[i-1]:self.arr[i-1]+n]
            if(txt!=searchstr):
                return [i]
            i-=1
        pass

    def contains(self, searchstr: str):
        """
        Returns true of searchstr is coontained in document.
        """
        n=len(searchstr)
        comp=lambda i,j: 0 if self.doc[i:i+n]==j else (-1 if self.doc[i:] < j else 1)
        return mybinsearch(self.arr,searchstr,comp)!=-1
        pass

# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
    tc.assertTrue(s.contains("Moby-Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
    posset = set(s.positions("Moby-Dick"))
    tc.assertEqual(posset, {355, 356})


#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
