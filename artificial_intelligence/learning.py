import numpy as np

def create_child(dad, mom):
    if islist(dad) and islist(mom):
        assert_length(dad, mom)
        child = []
        for index in range(0, len(dad)):
            child.append(create_child(dad[index], mom[index]))
        assert_length(dad, child)
        return child
    else:
        child = pick_random(dad, mom)
        return child

def introduce_mutation(weights):
    for index, elem in enumerate(weights):
        if islist(elem):
            introduce_mutation(elem)
        else:
            max_mutation_amount = 1
            mutation = np.random.rand() * 2 - 1
            mutation *= max_mutation_amount
            weights[index] += mutation

def assert_length(one, two):
    assert len(one) == len(two)

def pick_random(one, two):
    pick = np.random.randint(2)
    result = one if pick == 0 else two
    return result

def islist(obj):
    return isinstance(obj, list)


if __name__ == "__main__":
    weights = [[[3, 2, 1],[1,2,3]],[[0,1,2], [-1, -2, -3]]]
    introduce_mutation(weights)
    print(weights)
    weights_dad = [[[3, 2, 1],[1,2,3]],[[0,1,2], [-1, -2, -3]]]
    weights_mom = [[[8,9,10],[4,5,6]],[[-10,-1,-2], [9,9,9]]]
    child = create_child(weights_dad, weights_mom)
    print(child)