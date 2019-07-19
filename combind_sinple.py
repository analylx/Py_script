from itertools import combinations, permutations

ne_name = ['1800 2t', '1300', '1200i', '1050i']
version = ['7.5', '7.6']
feature = ["IPv6 interface", "IPv6 ping&TR", "IP BFD"]

if __name__ == "__main__":
    print(ne_name, version, feature)
    result = []
    for i in ne_name:
        for j in version:
            for k in feature:
                if i == "1050i" and j == "8.0":
                    continue
                temp = (i, j, k)
                print(temp)
                result.append(temp)
    print("Total combines: {0} \n".format(len(result)),result)
    #print(list(permutations([1, 2, 3], 2)))
    #print(list(combinations([1, 2, 3], 2)))
