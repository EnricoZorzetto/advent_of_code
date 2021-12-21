import numpy as np

# inputfile = 'data16.txt'
# inputfile = 'test_data16.txt'



def bin_to_dec(bin):
    dec = 0
    # bins = str(bin)
    ndig = len(bin)
    for i in range(ndig):
        exp = ndig - 1 - i
        dec = dec + int(bin[i]) * 2**exp
    return int(dec)

hexabin = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}


def hexa_to_bin(hexastring):
    binstring = ''
    for i in hexastring:
        binstring += hexabin[i]
    return binstring

# print(hexabin)


# def parse_next(tot_counter, binpacket):
#     binpacket = binpacket[tot_counter:]
#     version = bin_to_dec(binpacket[:3])
#     typeid = bin_to_dec(binpacket[3:6])
#     current_pos = 6
#     if typeid == 4:  # this packet is a litteral
#         frontp = 1
#         litteral = ''
#         while frontp == 1:
#             nextp = binpacket[current_pos:current_pos + 5]
#             print('nextp = {}'.format(nextp))
#             frontp = int(nextp[0])
#             litteral += nextp[1:]
#             current_pos += 5
#             # print(litteral)
#             print('litteral = {}'.format(bin_to_dec(litteral)))
#         tot_counter = tot_counter + current_pos
#         print('tot counter = {}'.format(tot_counter))
#
#     if typeid != 4:  # this packet is an operator
#         length_type_id = int(binpacket[6])
#         print('length type id = {}'.format(length_type_id))
#         if length_type_id == 0:  # next 15 digits are the length
#             tot_len = bin_to_dec(binpacket[7:7 + 15])
#             print('total length = {}'.format(tot_len))
#             tot_counter = tot_counter + 7 + 15
#         elif length_type_id == 1:
#             num_subpackets = bin_to_dec(binpacket[7:7 + 11])
#             tot_counter = tot_counter + 7 + 11
#             print('number of subpackets = {}'.format(num_subpackets))
#         print('tot counter = {}'.format(tot_counter))
#     # next_starting_pos = (tot_counter // 4) * 4 if tot_counter % 4 == 0 else (tot_counter // 4 + 1) * 4
#     next_starting_pos = tot_counter
#     print('tot counter = {}'.format(tot_counter))
#     print('next start pos = {}'.format(next_starting_pos))
#
#     return version, next_starting_pos




def read_packet(binpacket):
    # binpacket = binpacket[tot_counter:]
    totlen = len(binpacket)
    print('totlen = {}'.format(totlen))
    version = bin_to_dec(binpacket[:3])
    VERSION.append(version)
    typeid = bin_to_dec(binpacket[3:6])
    current_pos = 6
    if typeid == 4:  # this packet is a litteral
        frontp = 1
        litteral = ''
        while frontp == 1:
            nextp = binpacket[current_pos:current_pos + 5]
            print('nextp = {}'.format(nextp))
            frontp = int(nextp[0])
            litteral += nextp[1:]
            current_pos += 5
            # print(litteral)
            print('litteral = {}'.format(bin_to_dec(litteral)))
        LITTERALS.append(bin_to_dec(litteral))
        # tot_counter = tot_counter + current_pos
        # print('tot counter = {}'.format(tot_counter))
    elif typeid != 4:  # this packet is an operator
        length_type_id = int(binpacket[6])
        print('operator; length type id = {}'.format(length_type_id))
        if length_type_id == 0:  # next 15 digits are the length
            tot_len = bin_to_dec(binpacket[7:7 + 15])
            print('tot len = {}'.format(tot_len))
            print('operator - total length = {}'.format(tot_len))
            current_pos += (1+15)
            count_len = current_pos
            print('cp = {}'.format(current_pos))
            # while current_pos < count_len + tot_len and current_pos < totlen:
            while current_pos < count_len + tot_len:
                print(binpacket[current_pos:])
                print(binpacket)
                current_pos_new = read_packet(binpacket[current_pos:])
                current_pos += current_pos_new
                print('0 - current pos = {}'.format(current_pos))
                print('totlen = {}'.format(totlen))
        elif length_type_id == 1:
            num_subpackets = bin_to_dec( binpacket[7:7 + 11] )
            print('operator - number subpackets = {}'.format(num_subpackets))
            current_pos += (1+11)
            for nsp in range(num_subpackets):
                print('1 - current pos = {}'.format(current_pos))
                print(binpacket[current_pos:])
                current_pos_new = read_packet(binpacket[current_pos:])
                current_pos += current_pos_new
        # print('tot counter = {}'.format(tot_counter))
    # next_starting_pos = (tot_counter // 4) * 4 if tot_counter % 4 == 0 else (tot_counter // 4 + 1) * 4
    # next_starting_pos = tot_counter
    # print('tot counter = {}'.format(tot_counter))
    # print('next start pos = {}'.format(next_starting_pos))
    # return version, next_starting_pos
    return current_pos



def read_packet_2(binpacket, VAL, OPER):
    totlen = len(binpacket)
    # print('totlen = {}'.format(totlen))
    version = bin_to_dec(binpacket[:3])
    VERSION.append(version)
    typeid = bin_to_dec(binpacket[3:6])
    current_pos = 6
    if typeid == 4:  # this packet is a litteral
        frontp = 1
        litteral = ''
        while frontp == 1:
            nextp = binpacket[current_pos:current_pos + 5]
            # print('nextp = {}'.format(nextp))
            frontp = int(nextp[0])
            litteral += nextp[1:]
            current_pos += 5
            dec_litteral = bin_to_dec(litteral)
            # print('litteral = {}'.format(dec_litteral))
        LITTERALS.append(dec_litteral)
        VAL.append(dec_litteral)
    elif typeid != 4:  # this packet is an operator
        TID.append(typeid)
        length_type_id = int(binpacket[6])
        # print('operator; length type id = {}'.format(length_type_id))
        VAL.append([])
        OPER.append([typeid])
        if length_type_id == 0:  # next 15 digits are the length
            tot_len = bin_to_dec(binpacket[7:7 + 15])
            # print('tot len = {}'.format(tot_len))
            # print('operator - total length = {}'.format(tot_len))
            current_pos += (1+15)
            count_len = current_pos
            # print('cp = {}'.format(current_pos))
            while current_pos < count_len + tot_len:
                print(binpacket[current_pos:])
                print(binpacket)
                current_pos_new = read_packet_2(binpacket[current_pos:], VAL[-1], OPER[-1])
                current_pos += current_pos_new
                # print('0 - current pos = {}'.format(current_pos))
                # print('totlen = {}'.format(totlen))
        elif length_type_id == 1:
            num_subpackets = bin_to_dec( binpacket[7:7 + 11] )
            # print('operator - number subpackets = {}'.format(num_subpackets))
            current_pos += (1+11)
            for nsp in range(num_subpackets):
                # print('1 - current pos = {}'.format(current_pos))
                # print(binpacket[current_pos:])
                current_pos_new = read_packet_2(binpacket[current_pos:], VAL[-1], OPER[-1])
                current_pos += current_pos_new
    return current_pos


def resolve(vals, oper):
    if oper == 0:
        res = np.sum(np.array(vals))
    elif oper == 1:
        res = np.prod(np.array(vals))
    elif oper == 2:
        res = np.min(np.array(vals))
    elif oper == 3:
        res = np.max(np.array(vals))
    elif oper == 5:
        assert len(vals)==2
        res = int(vals[0] > vals[1])
    elif oper == 6:
        assert len(vals)==2
        res = int(vals[0] < vals[1])
    elif oper == 7:
        assert len(vals)==2
        res = int(vals[0] == vals[1])
    else:
        raise Exception('invalid operator ID!')
    return res


# A = bin_to_dec('011111100101')
# print(A)
# B = hexa_to_bin('D2FE28')
# print(B)

# PARSE THE PACKET

# hexapacket = 'D2FE28'
# A = hexapacket[4:]
# hexapacket = '38006F45291200' # 27 tot len
# hexapacket = 'EE00D40C823060' # 3 sub
# hexapacket = '8A004A801A8002F478' # should be 16
# hexapacket = '620080001611562C8802118E34' # should be 12
# hexapacket = 'C0015000016115A2E0802F182340' # should be 23
# hexapacket = 'A0016C880162017C3686B18A3D4780' # should be 31

# actual data
hexapacket = '4057231006FF2D2E1AD8025275E4EB45A9ED518E5F1AB4363C60084953FB09E008725772E8ECAC312F0C18025400D34F732333DCC8FCEDF7CFE504802B4B00426E1A129B86846441840193007E3041483E4008541F8490D4C01A89B0DE17280472FE937C8E6ECD2F0D63B0379AC72FF8CBC9CC01F4CCBE49777098D4169DE4BF2869DE6DACC015F005C401989D0423F0002111723AC289DED3E64401004B084F074BBECE829803D3A0D3AD51BD001D586B2BEAFFE0F1CC80267F005E54D254C272950F00119264DA7E9A3E9FE6BB2C564F5376A49625534C01B0004222B41D8A80008446A8990880010A83518A12B01A48C0639A0178060059801C404F990128AE007801002803AB1801A0030A280184026AA8014C01C9B005CE0011AB00304800694BE2612E00A45C97CC3C7C4020A600433253F696A7E74B54DE46F395EC5E2009C9FF91689D6F3005AC0119AF4698E4E2713B2609C7E92F57D2CB1CE0600063925CFE736DE04625CC6A2B71050055793B4679F08CA725CDCA1F4792CCB566494D8F4C69808010494499E469C289BA7B9E2720152EC0130004320FC1D8420008647E8230726FDFED6E6A401564EBA6002FD3417350D7C28400C8C8600A5003EB22413BED673AB8EC95ED0CE5D480285C00372755E11CCFB164920070B40118DB1AE5901C0199DCD8D616CFA89009BF600880021304E0EC52100623A4648AB33EB51BCC017C0040E490A490A532F86016CA064E2B4939CEABC99F9009632FDE3AE00660200D4398CD120401F8C70DE2DB004A9296C662750663EC89C1006AF34B9A00BCFDBB4BBFCB5FBFF98980273B5BD37FCC4DF00354100762EC258C6000854158750A2072001F9338AC05A1E800535230DDE318597E61567D88C013A00C2A63D5843D80A958FBBBF5F46F2947F952D7003E5E1AC4A854400404A069802B25618E008667B7BAFEF24A9DD024F72DBAAFCB312002A9336C20CE84'


# hexapacket = 'C200B40A82' # 1 + 2 = 3
# hexapacket = '04005AC33890' # 6 * 9 = 54
# hexapacket = '880086C3E88112' # min ( 7, 8, 9 )
# hexapacket = 'CE00C43D881120' # Max ( 7, 8, 9 )
# hexapacket = 'D8005AC2A8F0' # 5 < 15
# hexapacket = '9C0141080250320F1802104A08' # 1 + 3 == 2 * 2

binpacket0 = hexa_to_bin(hexapacket)

VERSION = []
LITTERALS = []
TID = []
VALUES = []
OPERATORS = []
len(binpacket0)
#
# curr_pos = read_packet(binpacket0)
curr_pos = read_packet_2(binpacket0, VALUES, OPERATORS)
print('VERSION = {}'.format(VERSION))
print('part 1 :: sum of packet versions = {}'.format(np.sum(VERSION)))
print('LITTERALS = {}'.format(LITTERALS))
print('VALUES = {}'.format(VALUES))
print('OPERATORS = {}'.format(OPERATORS))


# curr_pos = read_packet("0101001010010001001000000000")



# res = resolve(vals, oper)
# print(res)

# for el1, el2 in zip(VALUES[0], OPERATORS[0]):
#     assert type(el1) == type(el2)
#     if type(el1) is list:
#         print(len(el1))
#     else:
#         pass

# def step_into(lval, lope):
#     # if I am in the deepest level, resolve all operations
#     # otherwise step into the next level
#     print('step into lval = {} and lope = {}'.format(lval, lope))
#     # has_lists_1 = 0; has_lists_2 = 0
#     # for el1, el2 in zip(lval, lope):
#     #     if type(el1) is list:
#     #         has_lists_1 += 1
#     #     if type(el2) is list:
#     #         has_lists_2 += 1
#     # assert has_lists_1 == has_lists_2
#     myvals = [x for x in lval if type(x) is list]
#     myopers = [x for x in lope if type(x) is list]
#     # nextopers = [x for x in lope if type(x) is not list]
#     # nextvals = []
#     nl1 = len(myvals); nl2 = len(myopers)
#     assert nl1 == nl2
#     nlists = nl1
#     print('number of common internal lists is = {}'.format(nlists))
#     if nlists > 0:
#         resolving = False
#         res = None
#         # myopers = [x for x in lope if type(x) is list]
#         # myvals = [x for x in lval if type(x) is list]
#         print('myopers = {}'.format(myopers))
#         print('myvals = {}'.format(myvals))
#         countnl = 0
#         nopers = len(lope)
#         for nl in range(nopers):
#             if type(lope[nl]) is list:
#                 print('stepping into list element # {}'.format(nl))
#                 # res1 = step_into(lval[nl], lope[countnl])
#                 # lval[countnl], lope[nl] = step_into(lval[countnl], lope[nl])
#                 lval_upd, lope_upd, myersolving = step_into(lval[countnl], lope[nl])
#                 print('res1: {}, {}'.format(lval[countnl], lope[nl]))
#                 print('restot {}, {}'.format(lval, lope))
#                 countnl += 1
#                 # print('nl = {}; res1 = {}'.format(nl, res1))
#     else:
#         # resolving = True
#         # print(lval)
#         print('no lists reamining at this level; resolve operations!')
#         print('between:: vals = {}, operator = {}'.format(lval, lope))
#         res = resolve(lval, lope[0])
#         print('operation result is {}'.format(res))
#         lval = res
#         _ = lope.pop(lope[0])
#         # _ = LVAL.pop(lval)
#         # LVAL.append(res)
#     return lval, lope, resolving

def is_simple_list(mylist):
    nlists = len([x for x in mylist if type(x) is list])
    if nlists > 0:
        return False
    else:
        return True


def step_into(lval, lope):
    print('step into lval = {} and lope = {}'.format(lval, lope))
    # for iv, lv in enumerate(lval):
    #     print(iv, lv)
    intern_lists = [x for x in lval if type(x) is list]
    intern_opers = [x for x in lope if type(x) is list]
    # new_intern_lists = intern_lists.copy()
    # new_intern_opers = intern_opers.copy()
    next_opers = [x for x in lope if type(x) is not list]
    n_intern_lists = len( intern_lists )
    n_intern_opers = len( intern_opers )
    print('n internal lists = {}'.format(n_intern_lists))
    print('n internal opers = {}'.format(n_intern_opers))
    for ii, (il, io) in enumerate(zip(intern_lists, intern_opers)):
        # print(ii, il, io)
        if is_simple_list(il):
            print('is a simple list: resolving list {}'.format(il))
            res = resolve(il, io[0])
            print('res = {}'.format(res))
            intern_lists[ii] = res # substitue results
            intern_opers[ii] = 'done' # substitue results
    # print('after: intern list = {}'.format(intern_lists))
    # print('after: intern opers = {}'.format(intern_opers))

    # if is_simple_list(intern_lists): intern_lists = [intern_lists]
    # if is_simple_list(next_opers): next_opers = [next_opers]

        # else:
        # # for ii, (il, io) in enumerate(zip(intern_lists, intern_opers)):
        #     print('{} is not a simple list'.format(il))
        #     print('input = {} {}'.format(intern_lists[ii], intern_opers[ii]))
        #     intern_lists[ii], intern_opers[ii] = step_into(intern_lists[ii], intern_opers[ii])
        #     print('output = {} {}'.format(intern_lists[ii], intern_opers[ii]))

            # step into the next level

    if is_simple_list(intern_lists): intern_lists = [intern_lists]
    if is_simple_list(next_opers): next_opers = [next_opers]
    lval = intern_lists
    lope = next_opers + [x for x in intern_opers if x != 'done']
    print('final lval = {}'.format(lval))
    print('final lope = {}'.format(lope))
    return lval, lope
    # lope = [x for x in intern_opers]



vals = VALUES[0]
oper = OPERATORS[0]
# res1 = step_into([4,4], [7])


    # if type(lv) == list:
    #     print("found a basic element to process!")
    # elif type(lv) == list and len(lv)==2:

res = step_into(VALUES[0], OPERATORS[0])
# res = multistep(VALUES[0], OPERATORS[0])
# res = step_into(vals, opers)
#
LVAL = [[1,3], [2,2] ]
OPER = [7, [0], [1] ]
res1, res2 = step_into(LVAL, OPER)
# res3, res4 = step_into(res1, res2)
print(res1, res2)
# print(LVAL)
# print(OPER)

def multistep(lval, lope):
    while lope[0] != []:
        lval, lope = step_into(lval, lope)
    return lval, lope

res = multistep(LVAL, OPER)
print(res)


for v in VALUES[0][:5]:
    print(v)


for v in OPERATORS[0][:5]:
    print(v)

