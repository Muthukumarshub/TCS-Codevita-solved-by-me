def calculate_valency(element):
    return sum(map(int, str(sum(map(int, map(str, map(ord, element))))))) % 9 or 9

def balance_compound(compound, equivalent_point):
    element1, element2 = compound[0], compound[1]

    valency1, valency2 = calculate_valency(element1), calculate_valency(element2)
    result_list = []

    for multiple1 in range(1, equivalent_point // valency1 + 1):
        remaining_point = equivalent_point - multiple1 * valency1
        if remaining_point % valency2 == 0:
            multiple2 = remaining_point // valency2
            result_list.append(f"{element1}{multiple1} {element2}{multiple2}")

    for i in range(len(result_list) - 2, -1, -1):
        print(result_list[i])

    if not result_list:
        print("Not Possible")

# Example usage:
compound_input = input().strip()
equivalent_point_input = int(input().strip())

balance_compound(compound_input, equivalent_point_input)