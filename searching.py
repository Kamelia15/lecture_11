import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    for a in file_name:
        if field == a:
            return None

    # if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
    #     return None

    file = file_name

    with open("sequential.json") as file_name:
        slovniky = json.load(file_name)

    s = slovniky[field]
    return s


def linear_search(s,hledane_cislo):
    index = []
    count = 0
    for position, a in enumerate(s):
        if a == hledane_cislo:
            index.append(position)
            count += 1

    dict ={
        "position": index,
        "count": count

    }

    return dict


def pattern_search(sekvence, vzor):
    delka = len(vzor)
    position = set()
    start_index = 0
    posledni_index = delka

    while posledni_index < len(sekvence):
        for idx in range(delka):
            if vzor[idx] != sekvence[start_index + idx]:
                break
        else:
            position.add(start_index + delka // 2)
        start_index += 1
        posledni_index += 1

    return position

def binary_search(seq,number):
    konec = len(seq) - 1
    start = 0
    while start <= konec:
        middle = (start + konec) // 2
        if number < seq[middle]:
            konec = middle - 1
        elif number > seq[middle]:
            start = middle + 1
        else:
            return middle


    return None




def main():
    file = "sequential.json"
    s = read_data(file, "unordered_numbers")
    r = linear_search(s, hledane_cislo=0)

    s_2 = read_data(file, "dna_sequence")
    p = pattern_search(s_2,"ATA")

    s_3 = read_data(file, "ordered_numbers")
    b = binary_search(s_3,number=13)
    print(b)


if __name__ == '__main__':
    main()