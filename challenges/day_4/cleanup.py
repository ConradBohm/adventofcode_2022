sections_list = open("input.txt", "r")
section_pairs = sections_list.read().split("\n")
sections_list.close()

parsed_section_pairs = []
contains_count = 0
overlap_count = 0

for pair in section_pairs:
    parsed_section_pairs.append(pair.split(','))

for pair in parsed_section_pairs:
    range_1 = pair[0].split('-')
    range_2 = pair[1].split('-')

    first_sections = set([i for i in range(int(range_1[0]),int(range_1[1]) + 1)])
    second_sections = set([i for i in range(int(range_2[0]),int(range_2[1]) + 1)])
    
    if first_sections.issubset(second_sections) or second_sections.issubset(first_sections):
        contains_count += 1
    
    if first_sections.intersection(second_sections) or second_sections.intersection(first_sections):
        overlap_count += 1

print(contains_count) # part 1
print(overlap_count) # part 2