
import os
file = 'data4.txt'

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
nfields = len(fields)
# cid is optional for a passport
# the other fields are all required
# invalid if any field except cid is missing

# read file
# space OR newline -> new field
# blank line -> new passport
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

PASSPORTS = []
mypass = {}
for i in range(len(x)):
    if x[i] == '' and i > 0:
        PASSPORTS.append(mypass)
        mypass = {}
    else:
        separ = x[i].split(' ')
        print(len(separ))
        for j in range(len(separ)):
            key, field = separ[j].split(':')
            mypass[key] = field
# last value
PASSPORTS.append(mypass)

# count valid passports
ISVALID = [0 for x in range(len(PASSPORTS))]
for ip, pp in enumerate(PASSPORTS):
    keys = list(pp.keys())
    print(keys)

    if len(keys) == nfields or (len(keys) == nfields - 1 and 'cid' not in keys ):
        ISVALID[ip] = 1

print('The number of valid passports is = {}'.format(sum(ISVALID)))

# NOW CHECK CONSISTENCY OF EACH FIELD:
# count consistent passports

# reqfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# nreq = len(reqfields)
admissible_hcl = list('0123456789abcdef')
admissible_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
admissible_pid = list('0123456789')

COND_BYR = [0 for x in range(len(PASSPORTS))]
COND_IYR = [0 for x in range(len(PASSPORTS))]
COND_EYR = [0 for x in range(len(PASSPORTS))]
COND_HGT = [0 for x in range(len(PASSPORTS))]
COND_HCL = [0 for x in range(len(PASSPORTS))]
COND_ECL = [0 for x in range(len(PASSPORTS))]
COND_PID = [0 for x in range(len(PASSPORTS))]

ISCONS = [0 for x in range(len(PASSPORTS))]
for ip, pp in enumerate(PASSPORTS):

    cond_byr = 0
    cond_iyr = 0
    cond_eyr = 0
    cond_hgt = 0
    cond_hcl = 0
    cond_ecl = 0
    cond_pid = 0
    if ISVALID[ip]:

        def allnumeric(x):
            # check if a string is only composed by numbers:
            if x == '':
                return False
            for el in list(x):
                if el not in admissible_pid:
                    return False
            return True

        if allnumeric(pp['byr']):
            if len(pp['byr']) == 4 and int(pp['byr'])>=1920 and int(pp['byr'])<=2020:
                cond_byr = 1

        if allnumeric(pp['iyr']):
            if len(pp['iyr']) == 4 and int(pp['iyr'])>=2010 and int(pp['iyr']) <=2020:
                cond_iyr = 1

        if allnumeric(pp['eyr']):
            if len(pp['eyr']) == 4 and int(pp['eyr'])>=2020 and int(pp['eyr']) <=2030:
                cond_eyr = 1

        hgt = pp['hgt']
        if allnumeric(hgt[:-2]) and hgt[-2:] in ['cm', 'in']:
            hgt_num = int(hgt[:-2])
            hgt_unit = hgt[-2:]
            if hgt_unit == 'cm' and hgt_num >= 150 and hgt_num <= 193:
                cond_hgt = 1
            if hgt_unit == 'in' and hgt_num >= 59 and hgt_num <= 76:
                cond_hgt = 1

        hcl = pp['hcl']
        if hcl[0] == '#' and len(hcl) == 7:
            cond_hcl = 1
            for el in list(hcl[1:]):
                if el not in admissible_hcl:
                    cond_hcl = 0

        if pp['ecl'] in admissible_ecl:
            cond_ecl = 1

        pid = pp['pid']
        if len(pid) == 9:
            cond_pid = 1
            for ep in list(pid):
                if ep not in admissible_pid:
                    cond_pid = 0

    COND_BYR[ip] = cond_byr
    COND_IYR[ip] = cond_iyr
    COND_EYR[ip] = cond_eyr
    COND_HGT[ip] = cond_hgt
    COND_HCL[ip] = cond_hcl
    COND_ECL[ip] = cond_ecl
    COND_PID[ip] = cond_pid

    ISCONS[ip] = (cond_pid + cond_ecl + cond_hgt + cond_byr
               + cond_eyr + cond_iyr + cond_hcl) == 7


print('Number of consistent passports is {}'.format(sum(ISCONS)))
