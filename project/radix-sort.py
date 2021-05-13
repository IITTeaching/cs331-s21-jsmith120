import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    lst = book_to_words()
    max=0
    i=0
    while(i<len(lst)):
      c=len(lst[i])
      if(c>max):
        max=c 
      i+=1
    fin = radixSort(lst, max + 1)
    i=max
    while(i>-1):
      fin=radixSort(fin,i)
      i-=1
    return fin

def radixSort(lst, num):
    vars = [None] * len(lst)
    rad = [0] * 128
    for i in lst:
        if(len(i)<num+1):
          k = 0
        else:
          k = ord(i.decode('ascii')[num])
        rad[k] += 1
    j=0
    while(j<len(rad)-1):
      rad[j+1]+=rad[j]
      j+=1
    j=len(lst)-1
    while(j>-1):
      if(len(lst[j])<num+1):
        k = 0
      else:
        k = ord(lst[j].decode('ascii')[num])
      vars[rad[k]-1]=lst[j]
      rad[k] += -1
      j-=1
    return vars


def main():
  print(radix_a_book())

if(__name__ == '__main__'):
  main()
