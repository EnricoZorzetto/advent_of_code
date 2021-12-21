import numpy as np


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


# def read_packet(binpacket):
#     # binpacket = binpacket[tot_counter:]
#     totlen = len(binpacket)
#     print('totlen = {}'.format(totlen))
#     version = bin_to_dec(binpacket[:3])
#     VERSION.append(version)
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
#         # LITTERALS.append(bin_to_dec(litteral))
#         # tot_counter = tot_counter + current_pos
#         # print('tot counter = {}'.format(tot_counter))
#     elif typeid != 4:  # this packet is an operator
#         length_type_id = int(binpacket[6])
#         print('operator; length type id = {}'.format(length_type_id))
#         if length_type_id == 0:  # next 15 digits are the length
#             tot_len = bin_to_dec(binpacket[7:7 + 15])
#             print('tot len = {}'.format(tot_len))
#             print('operator - total length = {}'.format(tot_len))
#             current_pos += (1+15)
#             count_len = current_pos
#             print('cp = {}'.format(current_pos))
#             while current_pos < count_len + tot_len:
#                 print(binpacket[current_pos:])
#                 print(binpacket)
#                 current_pos_new = read_packet(binpacket[current_pos:])
#                 current_pos += current_pos_new
#                 print('0 - current pos = {}'.format(current_pos))
#                 print('totlen = {}'.format(totlen))
#         elif length_type_id == 1:
#             num_subpackets = bin_to_dec( binpacket[7:7 + 11] )
#             print('operator - number subpackets = {}'.format(num_subpackets))
#             current_pos += (1+11)
#             for nsp in range(num_subpackets):
#                 print('1 - current pos = {}'.format(current_pos))
#                 print(binpacket[current_pos:])
#                 current_pos_new = read_packet(binpacket[current_pos:])
#                 current_pos += current_pos_new
#     return current_pos


def read_packet_2(binpacket, VAL, OPER):
    version = bin_to_dec(binpacket[:3])
    VERSION.append(version)
    typeid = bin_to_dec(binpacket[3:6])
    current_pos = 6
    if typeid == 4:  # this packet is a litteral
        frontp = 1
        litteral = ''
        while frontp == 1:
            nextp = binpacket[current_pos:current_pos + 5]
            frontp = int(nextp[0])
            litteral += nextp[1:]
            current_pos += 5
            dec_litteral = bin_to_dec(litteral)
        VAL.append(dec_litteral)
    elif typeid != 4:  # this packet is an operator
        length_type_id = int(binpacket[6])
        VAL.append([])
        OPER.append([typeid])
        if length_type_id == 0:  # next 15 digits are the length
            tot_len = bin_to_dec(binpacket[7:7 + 15])
            current_pos += (1+15)
            count_len = current_pos
            while current_pos < count_len + tot_len:
                # print(binpacket[current_pos:])
                # print(binpacket)
                current_pos_new = read_packet_2(binpacket[current_pos:], VAL[-1], OPER[-1])
                current_pos += current_pos_new
        elif length_type_id == 1:
            num_subpackets = bin_to_dec( binpacket[7:7 + 11] )
            current_pos += (1+11)
            for nsp in range(num_subpackets):
                current_pos_new = read_packet_2(binpacket[current_pos:], VAL[-1], OPER[-1])
                current_pos += current_pos_new
    return current_pos


def is_simple_list(mylist):
    # return True for a list that does not contains sublists
    # False for a lists with sublists, or an integer
    if not type(mylist) is list:
        return False
    nlists = len([x for x in mylist if type(x) is list])
    if nlists > 0:
        return False
    else:
        return True


def is_deep_list(mylist):
    # return True for a list that does contains sublists
    # False for a lists with sublists, or an integer
    if not type(mylist) is list:
        return False
    nlists = len([x for x in mylist if type(x) is list])
    if nlists > 0:
        return True
    else:
        return False


def step_into(lval, lope):
    # print('step into lval = {} and lope = {}'.format(lval, lope))
    nlval = len(lval); nlope = len(lope)
    pos_intern_lists = [i for i in range(nlval) if is_simple_list(lval[i])]
    pos_intern_opers = [i for i in range(nlope) if is_simple_list(lope[i])]
    n_intern_lists = len( pos_intern_lists )
    n_intern_opers = len( pos_intern_opers )
    assert n_intern_opers == n_intern_lists; nint = n_intern_lists
    for ii in range(nint):
        lv = lval[pos_intern_lists[ii]]; lo = lope[pos_intern_opers[ii]]
        res = resolve(lv, lo[0])
        # print('res = {}'.format(res))
        lval[pos_intern_lists[ii]] = res # substitue results
        lope[pos_intern_opers[ii]] = 'done' # substitue results
    nlval = len(lval); nlope = len(lope)
    pos_deep_lists = [i for i in range(nlval) if is_deep_list(lval[i])]
    pos_deep_opers = [i for i in range(nlope) if is_deep_list(lope[i])]
    n_deep_lists = len( pos_deep_lists )
    n_deep_opers = len( pos_deep_opers )
    assert n_deep_opers == n_deep_lists; ndeep = n_deep_lists
    for ii in range(ndeep):
        lv = lval[pos_deep_lists[ii]]; lo = lope[pos_deep_opers[ii]]
        lv2, lo2 = step_into(lv, lo)
        lval[pos_deep_lists[ii]] = lv2
        lope[pos_deep_opers[ii]] = lo2
    return lval, lope


def multistep(lval, lope):
    isdeep = True
    while isdeep:
        lval, lope = step_into(lval, lope)
        isdeep = is_deep_list(lval)
    # do the last step manually, it's not a deep list anymore:
    lope = [x for x in lope if x != 'done'] # cleanup this mess
    res = resolve(lval, lope[0])
    return res



# PARSE THE PACKET - EZAMPLES PART 1
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


# PARSE THE PACKET - EZAMPLES PART 2
# hexapacket = 'C200B40A82' # 1 + 2 = 3
# hexapacket = '04005AC33890' # 6 * 9 = 54
# hexapacket = '880086C3E88112' # min ( 7, 8, 9 )
# hexapacket = 'CE00C43D881120' # Max ( 7, 8, 9 )
# hexapacket = 'D8005AC2A8F0' # 5 < 15 produces 1
# hexapacket = 'F600BC2D8F' # produces 0
# hexapacket = '9C005AC2F8F0' # produces 0
# hexapacket = '9C0141080250320F1802104A08' # 1 + 3 == 2 * 2


binpacket0 = hexa_to_bin(hexapacket)
VERSION = []
VALUES = []
OPERATORS = []
len(binpacket0)
curr_pos = read_packet_2(binpacket0, VALUES, OPERATORS)
print('part 1 :: sum of packet versions = {}'.format(np.sum(VERSION)))
# print('VALUES = {}'.format(VALUES))
# print('OPERATORS = {}'.format(OPERATORS))
# print(VALUES)
# print(OPERATORS)
vals = VALUES[0].copy()
oper = OPERATORS[0].copy()



res = multistep(vals, oper)
print('part 2 :: the result is = {}'.format(res))
