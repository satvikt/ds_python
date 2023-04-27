def maximumUnits(boxTypes, truckSize):
    boxTypes= sorted(boxTypes, key= lambda x: x[1],reverse=True)
    ans = 0
    boxes_left = truckSize
    for box, units in boxTypes:
        box = min(boxes_left, box)
        ans += box * units
        boxes_left -= box
        if boxes_left == 0:
            break
    return ans

# def maximumUnits(boxTypes, truckSize):
#     boxTypes.sort(key=lambda x: -x[1])
#     ans = 0
#     for box, units in boxTypes:
#         if truckSize > box:
#             truckSize -= box
#             ans += box * units
#         else:
#             ans += truckSize * units
#             return ans
#     return ans

if __name__ == "__main__":
    boxTypes = [[2,2],[1,3],[3,1]]
    truckSize = 4
    print(maximumUnits(boxTypes, truckSize))