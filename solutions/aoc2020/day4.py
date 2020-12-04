from aocd import data
from aocd import submit
import re

def part_a(data):
    lines = data.split("\n\n")
    valid = 0
    for line in lines:
        parts = line.replace('\n', ' ').strip().split(' ')
        fields = set()
        for part in parts:
            fields.add(part.split(':')[0])
        isValid = 'byr' in fields and\
                    'iyr' in fields and\
                    'eyr' in fields and\
                    'hgt' in fields and\
                    'hcl' in fields and\
                    'ecl' in fields and\
                    'pid' in fields
                    #'cid' in fields;
        if isValid:
            valid += 1
    return str(valid)


def part_b(data):
    lines = data.split("\n\n")
    valid = 0
    for line in lines:
        parts = line.replace('\n', ' ').strip().split(' ')
        fields = dict()
        for part in parts:
            key, val = part.split(':')
            fields[key] = val

        byr = 'byr' in fields and byrValid(fields['byr'])
        iyr = 'iyr' in fields and iyrValid(fields['iyr'])
        eyr = 'eyr' in fields and eyrValid(fields['eyr'])
        hgt = 'hgt' in fields and hgtValid(fields['hgt'])
        hcl = 'hcl' in fields and hclValid(fields['hcl'])
        ecl = 'ecl' in fields and eclValid(fields['ecl'])
        pid = 'pid' in fields and pidValid(fields['pid'])

        isValid = byr and iyr and eyr and hgt and hcl and ecl and pid
        if isValid:
            valid += 1
    return str(valid)

def byrValid(byr):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002

def iyrValid(iyr):
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020

def eyrValid(eyr):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030

def hgtValid(height):
    if 'cm' in height:
        return 150 <= int(height[:-2]) <= 193
    if 'in' in height:
        return 59 <= int(height[:-2]) <= 76
    return False

def hclValid(hcl):
    return bool(re.match(r"#[0-9a-f]{6}", hcl))

def eclValid(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pidValid(pid):
    return bool(re.match(r"^\d{9}$", pid))

test_data = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_data_incorrect = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

test_data_correct = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

if __name__ == "__main__":
    assert byrValid('2002')
    assert not byrValid('2003')

    assert hgtValid('60in')
    assert hgtValid('190cm')
    assert not hgtValid('190in')
    assert not hgtValid('190')

    assert hclValid('#123abc')
    assert not hclValid('#123abz')
    assert not hclValid('123abc')

    assert eclValid('brn')
    assert not eclValid('wat')

    assert pidValid('000000001')
    assert not pidValid('0123456789')

    assert part_a(test_data) == "2"
    solution_a = part_a(data)
    print(solution_a)
    #submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data_incorrect) == "0"
    assert part_b(test_data_correct) == "4"
    solution_b = part_b(data)
    print(solution_b)
    #submit(solution_b, part="b", day=2, year=2020)

