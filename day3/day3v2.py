import math

def GetXY(index):
    # print('index = ' + str(index))
    sqrtInput = math.sqrt(index)

    sqrtCeil = math.ceil(sqrtInput)

    # print('sqrtCeil = ' + str(sqrtCeil))

    sqrtMaxIndexInEdge = -1
    if sqrtCeil % 2 == 0:
        sqrtMaxIndexInEdge = sqrtCeil + 1
    else:
        sqrtMaxIndexInEdge = sqrtCeil

    # print('sqrtMaxIndexInEdge = ' + str(sqrtMaxIndexInEdge))

    maxIndexInEdge = math.pow(sqrtMaxIndexInEdge, 2)
    # print('maxIndexInEdge = ' + str(maxIndexInEdge))

    maxIndexInPrevEdge = math.pow(sqrtMaxIndexInEdge - 2, 2)
    # print('maxIndexInPrevEdge = ' + str(maxIndexInPrevEdge))

    indexRelativeToEdgeStart = index - maxIndexInPrevEdge
    # print('indexRelativeToEdgeStart = ' + str(indexRelativeToEdgeStart))

    edgeRadius = (sqrtMaxIndexInEdge - 1)/2
    # print('edgeRadius = ' + str(edgeRadius))


    xStart = edgeRadius
    yStart = -edgeRadius

    # print('xstart = ' + str(xStart) + ', ystart = ' + str(yStart))

    numTilesInRing = maxIndexInEdge - maxIndexInPrevEdge
    # print('numTilesInRing = ' + str(numTilesInRing))

    xTile = -1
    yTile = -1

    numTilesInEdge = numTilesInRing/4
    # print('numTilesInEdge = ' + str(numTilesInEdge))

    # Walk around edge
    if indexRelativeToEdgeStart < numTilesInRing*(1/4):
        # print('Tile is on right side of ring')
        xTile = xStart
        yTile = yStart + (indexRelativeToEdgeStart % numTilesInEdge)
        return xTile, yTile

    xStart = xStart
    yStart = yStart + numTilesInEdge

    if indexRelativeToEdgeStart < numTilesInRing*(2/4):
        # print('Tile is on top side of ring')
        xTile = xStart - (indexRelativeToEdgeStart % numTilesInEdge)
        yTile = yStart
        return xTile, yTile

    xStart = xStart - numTilesInEdge
    yStart = yStart

    if indexRelativeToEdgeStart < numTilesInRing*(3/4):
        # print('Tile is on left side of ring')
        xTile = xStart
        yTile = yStart - (indexRelativeToEdgeStart % numTilesInEdge)
        return xTile, yTile

    xStart = xStart
    yStart = yStart - numTilesInEdge

    if indexRelativeToEdgeStart < numTilesInRing*(4/4):
        # print('Tile is on bottom side of ring')
        xTile = xStart + (indexRelativeToEdgeStart % numTilesInEdge)
        yTile = yStart
        return xTile, yTile

    # print('Tile is last tile in ring!')
    # Must be last tile in ring!
    xStart = xStart + numTilesInEdge
    yStart = yStart

    return xStart, yStart


def FindSumGreaterThan(sum):
    part2AnswerFound = False
    index = 1
    sumDict = {}
    while not part2AnswerFound:

        # print('Index = ' + str(index))

        xVal, yVal = GetXY(index)

        # print('xVal = ' + str(xVal) + ', yVal = ' + str(yVal))

        if index == 1:
            sumDict[(xVal, yVal)] = 1
        else:
            sumNeighbourTiles = 0

            # Start in lower right corner, walk anti-clockwise
            sumNeighbourTiles += sumDict.get((xVal + 1, yVal - 1), 0)
            sumNeighbourTiles += sumDict.get((xVal + 1, yVal + 0), 0)
            sumNeighbourTiles += sumDict.get((xVal + 1, yVal + 1), 0)
            sumNeighbourTiles += sumDict.get((xVal + 0, yVal + 1), 0)
            sumNeighbourTiles += sumDict.get((xVal - 1, yVal + 1), 0)
            sumNeighbourTiles += sumDict.get((xVal - 1, yVal + 0), 0)
            sumNeighbourTiles += sumDict.get((xVal - 1, yVal - 1), 0)
            sumNeighbourTiles += sumDict.get((xVal + 0, yVal - 1), 0)
            
            # print('sumNeighbourTiles = ' + str(sumNeighbourTiles))

            # Check if sum meets finish condition
            if sumNeighbourTiles > input:
                return sumNeighbourTiles

            sumDict[(xVal, yVal)] = sumNeighbourTiles

        index += 1

# input = 5
input = 277678
result = GetXY(input)
part1Answer = math.fabs(result[0]) + math.fabs(result[1])
print('part1Answer = ' + str(part1Answer))


sum = FindSumGreaterThan(input)
print('part2Answer = ' + str(sum))
