def maximumBobPoints(numArrows, aliceArrows) -> List[int]:
  def test(mask, remainArrows):
      score = 0
      bobArrows = [0] * 12
      for k in range(12):
          if (mask >> k) & 1:
              arrowsNeeded = aliceArrows[k] + 1
              if remainArrows < arrowsNeeded: return 0, []
              score += k
              bobArrows[k] = arrowsNeeded
              remainArrows -= arrowsNeeded


      bobArrows[0] += remainArrows
      return score, bobArrows

  bestScore = 0
  bestBobArrows = None
  for mask in range(1 << 12):
      score, bobArrows = test(mask, numArrows)
      if score > bestScore:
          bestScore = score
          bestBobArrows = bobArrows
  return bestBobArrows

numArrows = 9
aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
res = maximumBobPoints(numArrows, aliceArrows)
print(res)
