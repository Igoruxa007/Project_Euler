def function(explorers):
    new_list = list()
    new_list.append(explorers[0][1])
    for i in range(len(explorers)):
        for j in range(1, len(explorers[i])):
            for feature in range(len(new_list)):
                if explorers[i][j] == new_list[feature][0]:
                    new_list[feature].append(explorers[i][0])
                    break
                new_list.append(explorers[i][j])
    return new_list


test_list = [
    ["Mallory", "Everest", "Mont Blanc", "Pillar Rock"],
    ["Mawson", "South Pole", "New Hebrides"],
    ["Hillary", "Everest", "South Pole"]
]

print(function(test_list))
