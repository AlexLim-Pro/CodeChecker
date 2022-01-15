def CheckBinarySearchTreeSequence(arr: iter):
  """
  Checks if a binary search sequence can is feasible
  
  :param arr: An array containing the binary search tree sequence
  :type arr: iter
  """
  searchVal = arr[-1]
  minVal = min(arr) - 1
  maxVal = max(arr) + 1
  for i in arr:
    if i < searchVal:
      if i < minVal:
        return i
      if i == minVal:
        return i
      minVal = i
    elif i > searchVal:
      if i > maxVal:
        return i
      if i == maxVal:
        return i
      maxVal = i
  print("no issues")

