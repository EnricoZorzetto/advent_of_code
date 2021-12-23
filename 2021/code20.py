import numpy as np
import matplotlib.pyplot as plt


def read_data(inputfile):
    with open(inputfile) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    code = ''
    img = []
    reading_code = True
    for li in lines:
        if li == '':
            reading_code = False
        if reading_code:
            code = code + li
        if li != '' and not reading_code:
            img.append(li)
    print('code::', len(code), code)
    code = np.array( [ 0 if x == '.' else 1 for x in list(code) ])
    img =  np.array( [ [ 0 if x == '.' else 1 for x in list(img[i]) ] for i in range(len(img))] )
    return code, img


def bin_to_dec(bin):
    dec = 0
    # bins = str(bin)
    ndig = len(bin)
    for i in range(ndig):
        exp = ndig - 1 - i
        dec = dec + int(bin[i]) * 2**exp
    return int(dec)


def enhance(mat33, code):
    vec33 = np.ravel(mat33)  # row-wise
    dec = bin_to_dec(vec33)
    newval = code[dec]
    return newval


def update_img(img, code, outerval):
    nyold, nxold = img.shape
    ny = nyold + 4; nx = nxold + 4
    old_img = np.ones((ny, nx)).astype(int)*outerval
    old_img[2:-2, 2:-2] = img

    # update outer value::
    outermat = np.ones((3,3)).astype(int)*outerval
    new_outerval = enhance(outermat, code)

    new_img = np.ones((ny, nx)).astype(int)*new_outerval
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            wind = old_img[i-1:i+2, j-1:j+2]
            # print('wind = {}'.format(wind))
            new_img[i, j] = enhance(wind, code)
    return new_img, new_outerval


# inputfile = 'test_data20.txt'
inputfile = 'data20.txt'
code, img0 = read_data(inputfile)
outerval0 = 0 # value of the pixels outside the boundaries

plt.figure()
plt.imshow(img0)
plt.colorbar()
plt.show()

nenhance = 50
for i in range(nenhance):
    print(i)
    img1, outer1 = update_img(img0, code, outerval0)
    outerval0 = outer1
    img0 = img1

# print( enhance( np.zeros((3,3)), code, outerval))


# img1, outer1 = update_img(img0, code, outerval0)
# plt.figure()
# plt.imshow(img1)
# plt.colorbar()
# plt.show()
# img2, outer2 = update_img(img1, code, outer1)
# plt.figure()
# plt.imshow(img2)
# plt.colorbar()
# plt.show()

print('part 1:: {} lit pixels'.format(np.sum(img1)))




