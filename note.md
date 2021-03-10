# Practice Diary

## Top Interview Questions

#### 2021/3/1

**Array**

1. Rotate Array  
   根据所给数字 k，向右选择数组。
   注意点：do it in-place with O(1) place
   方法： 先反转整个数组，然后以 k 为分界点，再次反转下标[0,k]
   复盘：1.注意对 corner case: [1]的处理。</br> 2.先对 k 进行处理，k = k % len(nums)

**String**

2. Reverse String
3. First Unique Character in a String
4. String to Integer (Don't forget the corner case
   like "","+","0000-")

#### 2021/3/8

1. Extra Long Factorials 大数阶乘(HackerRank)
   URL: https://www.hackerrank.com/challenges/extra-long-factorials/problem
   Note: 改行なし出力: print(str, end="")
   backwark for loop: for i in range(num, -1, -1)

   ```python
   def extraLongFactorials(n):
      a = [0]*40000
      a[0] = 1
      digit, carry = 0, 0
      res =""
      for i in range(2,n+1):
         for j in range(0,digit+1):
               temp = a[j] * i + carry
               a[j] = temp % 10
               carry = temp // 10

         while carry > 0:
               digit += 1
               a[digit] = carry % 10
               carry //= 10

      for i in range(digit, -1, -1):
         res += str(a[i])

      print(res)
   ```

2. AM/PM -> 24h

   ```python
   time = input().strip()
   h, m, s = map(int, time[:-2].split(':'))
   p = time[-2:]
   h = h % 12 + (p.upper() == 'PM') * 12
   print(('%02d:%02d:%02d') % (h, m, s))
   # {:02d}.format(数字)： 数字至少2位
   # （e.g: 1 -> 01)

   ```

#### 2020/3/9

1. Forming a magic square (HackerRank, Medium)
   URL: https://www.hackerrank.com/challenges/magic-square-forming/problem
   Note: the center of a 3\*3 magic square is 5.  
    There are only 8 patterns of a 3\*3 magic square.
   Match the given s s with all the possible patterns and calculate the minimum cost.
   Turn a 2D array to 1D array: s = sum(s, [])
   Methond: Search(全探索) , DFS: generate all possible magic squares (TODO)
   Similar problem: leetcode Find magic square

   ```python
   def formingMagicSquare(s):
     minCost = sys.maxsize
     s = [ j for i in s for j in i] #2D -> 1D
     magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
              [6, 1, 8, 7, 5, 3, 2, 9, 4],
              [4, 9, 2, 3, 5, 7, 8, 1, 6],
              [2, 9, 4, 7, 5, 3, 6, 1, 8],
              [8, 3, 4, 1, 5, 9, 6, 7, 2],
              [4, 3, 8, 9, 5, 1, 2, 7, 6],
              [6, 7, 2, 1, 5, 9, 8, 3, 4],
              [2, 7, 6, 9, 5, 1, 4, 3, 8]]

     for m in magic:
        cost = 0
        for i in range(len(s)):
              cost += abs(s[i]-m[i])
        minCost = min(minCost,cost)

     return minCost
   ```

#### 2020/3/10

1. Strings: Making Anagrams (HackerRank, Easy)
   URL: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

   **Solution:**

   1. use Counter to calculate the numbers of every character in each string.
   2. if there's element in a that is not in b, we need to delet all these elements, so cnt += v
      if an element is contained in both strings, we need to delet part of them until they have the same numbers. so cnt += abs(difference of the numbers of the element between two strings)
   3. **miss the following situation at first!!**  
      Also need to think of the situation, which an element is in b but not in a. Need to delete these elements too.

   ```python
   def makeAnagram(a, b):
      a = Counter(a)
      b = Counter(b)
      cnt = 0

      #----------------#
      for k, v in a.items():
         if not b.get(k):
               cnt += v
         else:
               cnt += abs(v-b.get(k))

      for k, v in b.items():
         if not a.get(k):
               cnt += v
      #----------------#
      could be replaced by below
      #----------------#
      # New method
      a.subtract(b) #conbine all elements in both a and b,
                    #the value of each element is the value difference of two (a-b)
      cnt = sum(abs(i) for i in a.values())
      #-----------------#

      return cnt
   ```
