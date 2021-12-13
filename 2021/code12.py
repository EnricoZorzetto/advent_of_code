import numpy as np
import matplotlib.pyplot as plt


def get_connect(mypoint, st, en): # both forward and back for now
    # get all the connections from A
    froms = en[st==mypoint]
    # froms = en[np.logical_and(st==mypoint, st != 'start')]
    tooos = st[en==mypoint]
    # tooos = st[np.logical_and(en==mypoint, st != 'start')]
    allc = list(froms) + list(tooos)
    return allc


def remove_visited(AC, history):
    ACV = AC.copy()
    # print('AC', AC)
    for ac in AC:
        # print(ac, history)
        # print(ac.islower())
        if ac == 'start' or (ac in history and ac.islower()):
            # print('removing {}'.format(ac))
            ACV.remove(ac)
    return ACV


def remove_visited_except(AC, history, do_exception = False, exception = None):
    ACV = AC.copy()
    # print('AC', AC)
    for ac in AC:
        # print(ac, history)
        # print(ac.islower())
        if not do_exception:
            cond = (ac == 'start' or (ac in history and ac.islower()))
        else:
            islower_exp = ac.islower() and ac != exception
            cond = (ac == 'start' or (ac in history and islower_exp))
        if cond:
            # print('removing {}'.format(ac))
            ACV.remove(ac)
    return ACV


def get_paths(st, en, do_exception = False, dbllowerc = None):
    saved_paths = []
    paths = [ ['start'] ]
    done_exceptions = [ False]
    number_of_open_paths = 1
    counter_max = 10000
    counter = 0
    while number_of_open_paths > 0 and counter < counter_max:
        counter += 1
        newpaths = []
        new_done_exceptions = []
        for ih, (history, done_exception) in enumerate( zip(paths, done_exceptions)):
            mypoint = history[-1] # last point of current history
            # print('len(paths) = {}'.format(len(paths)))
            # print('count = {}, ih = {}, history = {}'.format(counter, ih, history))
            # print('count = {}, ih = {}, done_exceptions = {}'.format(counter, ih, done_exceptions))
            # print('count = {}, ih = {}, paths = {}'.format(counter, ih, paths))
            # get connections to current point
            AC = get_connect(mypoint, st, en)
            # remove those going to start and to (small letters) points already visited
            if not do_exception or done_exception:
            # if not do_exception:
                ACV = remove_visited(AC, history)
            else:
                ACV = remove_visited_except(AC, history, do_exception=do_exception, exception=dbllowerc)
            # for each point, add a new history:
            for np in ACV:
                newhist = history.copy()
                newhist.append(np)
                if not do_exception:
                    if np == 'end':
                        saved_paths.append(newhist)
                    else:
                        newpaths.append(newhist)
                        new_done_exceptions.append(False)
                if do_exception:
                    if newhist.count(dbllowerc)==2 and np =='end':
                        saved_paths.append(newhist)
                    if not np =='end':
                        newpaths.append(newhist)
                        if newhist.count(dbllowerc) == 2:
                            new_done_exceptions.append(True)
                        else:
                            new_done_exceptions.append(False)
            # print('ih = {}, mypoint = {}'.format(ih, mypoint))
            # print('history = {}'.format(history))
            # print('paths = {}'.format(paths))
            # print('newpaths = {}'.format(newpaths))
            # assert len(paths) == len(done_exceptions)
            paths = newpaths.copy()
            done_exceptions = new_done_exceptions.copy()
    return saved_paths


def main():
    # inputfile = 'test_data12.txt'
    # inputfile = 'test_data12b.txt'
    # inputfile = 'test_data12c.txt'
    inputfile = 'data12.txt'

    # read data
    with open(inputfile) as file:
        map = [line.rstrip('\n') for line in file.readlines()]
    st = np.array([m.split('-')[0] for m in map])
    en = np.array([m.split('-')[1] for m in map]).astype('<U5')
    allpoints = np.unique(np.concatenate((st, en)))
    lowercases = [x for x in allpoints if x.islower() and x != 'start' and x != 'end']

    # compute part 1
    saved_paths = get_paths(st, en, do_exception=False)
    # print('part 1 :: saved_paths = {}'.format(saved_paths))
    print('part 1 :: number of saved_paths = {}'.format(  len(saved_paths)))
    # for i in range(len(saved_paths)):
    #     print(saved_paths[i])

    # compute part 2
    nlowercases = len(lowercases)
    for ilo in range(nlowercases):
        new_paths = get_paths(st, en, do_exception=True, dbllowerc=lowercases[ilo])
        saved_paths += new_paths

    # print('part 2 :: saved_paths = {}'.format(saved_paths))
    print('part 2 :: number of saved_paths = {}'.format(  len(saved_paths)))
    # for i in range(len(saved_paths)):
    #     print(saved_paths[i])

if __name__ == '__main__':
    main()

