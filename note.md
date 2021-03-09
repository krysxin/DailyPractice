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

1. 大数阶乘
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
