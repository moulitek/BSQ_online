from moulitek.moulitek import *
import sys
import os

init_moulitek()

basic_failed = []
lst_97 = []
lst_34 = []
lst_187 = []
lst_crown = []
lst_line = []
lst_col = []
lst_other = []
err_failed = []
crash = 0


def seperate():
    for elem in basic:
        if "34" in elem:
            lst_34.append(elem)
        elif "187" in elem:
            lst_187.append(elem)
        elif "97" in elem:
            lst_97.append(elem)
        elif "line" in elem:
            lst_line.append(elem)
        elif "column" in elem:
            lst_col.append(elem)
        elif "one" in elem:
            lst_crown.append(elem)
        else:
            lst_other.append(elem)


def get_trace():
    os.system("script/check.sh > trace")
    try:
        text_file = open("trace", "r")
        data = text_file.read()
        data = data.split('~')
        basic = data[0]
        errore = data[1]
        text_file.close()
    except:
        exit(84)
    os.system("rm trace")
    return basic, errore


def get_name(name):
    i = len(name)
    i -= 1
    while i > 0 and name[i] != '/':
        i -= 1
    if name[i] == '/':
        i += 1
    return name[i:]


def testor(lst, trace):
    tmp = 0
    seg = 0
    for elem in trace:
        if "Error" in elem or "Crash" in elem:
            tmp = elem.split(' ')
            lst.append(get_name(tmp[0]))
        if "Crash" in elem:
            seg += 1
    return seg


def lst_to_str(lst):
    res = ""
    for elem in lst:
        res += elem + "\n"
    return res[:-1]


basic, err = get_trace()
print(basic)
basic = [e for e in basic.split('\n') if len(e) > 0]
err = [e for e in err.split('\n') if len(e) > 0]

seperate()

os.system("make")
Given_maps = Category(
    "Given maps", "Basics tests made by moulinette : given maps on subject")
error_hand = Category("Error handling", "Error handling tests")
looper = Category("Loop", "Loop on 1500 random maps to check segfault")

basic_failed = []
Given_maps_97 = Given_maps.add_sequence("97*21")
Given_maps_97.add_test("97*21")
crash = testor(basic_failed, lst_97)
if len(basic_failed) == 0:
    Given_maps_97.set_status("97*21", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_97.set_status(
        "97*21", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))

crash = 0
basic_failed = []
Given_maps_34 = Given_maps.add_sequence("34*137")
Given_maps_34.add_test("34*137")
crash = testor(basic_failed, lst_34)
if len(basic_failed) == 0:
    Given_maps_34.set_status("34*137", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_34.set_status(
        "34*137", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))

crash = 0
basic_failed = []
Given_maps_187 = Given_maps.add_sequence("187*187")
Given_maps_187.add_test("187*187")
crash = testor(basic_failed, lst_187)
if len(basic_failed) == 0:
    Given_maps_187.set_status("187*187", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_187.set_status(
        "187*187", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))


crash = 0
basic_failed = []
Given_maps_one = Given_maps.add_sequence("one*one")
Given_maps_one.add_test("one*one")
crash = testor(basic_failed, lst_crown)
if len(basic_failed) == 0:
    Given_maps_one.set_status("one*one", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_one.set_status(
        "one*one", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))


crash = 0
basic_failed = []
Given_maps_line = Given_maps.add_sequence("line")
Given_maps_line.add_test("line")
crash = testor(basic_failed, lst_line)
if len(basic_failed) == 0:
    Given_maps_line.set_status("line", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_line.set_status(
        "line", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))


crash = 0
basic_failed = []
Given_maps_col = Given_maps.add_sequence("col")
Given_maps_col.add_test("col")
crash = testor(basic_failed, lst_col)
if len(basic_failed) == 0:
    Given_maps_col.set_status("col", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_col.set_status(
        "col", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))


crash = 0
basic_failed = []
Given_maps_other = Given_maps.add_sequence("other")
Given_maps_other.add_test("other")
crash = testor(basic_failed, lst_other)
if len(basic_failed) == 0:
    Given_maps_other.set_status("other", True)
else:
    res = BADOUTPUT
    if crash > 0:
        res = SEGFAULT
    Given_maps_other.set_status(
        "other", False, res, expected="OK", got="KO on\n" + lst_to_str(basic_failed))

for elem in err:
    Given_maps_error = 0
    tmp = elem.split(' ')
    name = get_name(tmp[0])
    Given_maps_error = error_hand.add_sequence(name)
    Given_maps_error.add_test(name)
    if "Error" in elem:
        Given_maps_error.set_status(name, False, BADOUTPUT, expected="OK", got="KO")
    elif "Crash" in elem:
        Given_maps_error.set_status(name, False, SEGFAULT, expected="OK", got="CRASH")
    else:
        Given_maps_error.set_status(name, True)

loop = looper.add_sequence("Loop 1500")
loop.add_test("Loop 1500")
crash = testor(basic_failed, err)
ret = os.system("script/loop.sh 1500")
if ret == 0:
    loop.set_status("Loop 1500", True)
else:
    if ret == 139 or ret == 136:
        loop.set_status("Loop 1500", False, SEGFAULT, expected="OK", got="KO")
    else:
        loop.set_status("Loop 1500", False, BADOUTPUT, expected="OK", got="KO")
gen_trace()
