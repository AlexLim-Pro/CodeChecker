def CheckBinarySearchTreeSequence(arr: iter):
  """
  Checks if a binary search sequence can is feasible
  
  :param arr: An array containing the binary search tree sequence
  :type arr: iter
  """
  invalidSequenceString = "sequence is invalid: %s %s %s."
  searchVal = arr[-1]
  minVal = min(arr) - 1
  maxVal = max(arr) + 1
  for i in arr:
    if i < searchVal:
      if i < minVal:
        return invalidSequenceString % (i, "<", minVal)
      if i == minVal:
        return invalidSequenceString % (i, "appears", "multiple times")
      minVal = i
    elif i > searchVal:
      if i > maxVal:
        return invalidSequenceString % (i, ">", maxVal)
      if i == maxVal:
        return invalidSequenceString % (i, "appears", "multiple times")
      maxVal = i
  return "the sequence is valid."

