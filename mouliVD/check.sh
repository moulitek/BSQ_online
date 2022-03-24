#!/usr/bin/env bash

BINARY="bsq"

test_expect_success () {
    local str="${2}"
    local expected=$(bash -c "cat ${1}")
    local result=$(bash -c "./${BINARY} ${str}")
    ./${BINARY} ${str} > trash
    ret=`echo $?`
    rm trash
    if [[ ${ret} == 139 ]] || [[ ${ret} == 136 ]] ; then
        printf "%s Crash\n" ${2}
        return;
    fi
    if [[ $ret == 84 ]] || [[ "${result}" != "${expected}" ]]; then
        printf "%s Error\n" ${2}
    else printf "%s Success.\n" ${2}
    fi
}

test_expect_error () {
    local str="${1}"
    ./${BINARY} ${str}
    ret=`echo $?`
    if [[ ${ret} == 139 ]] || [[ ${ret} == 136 ]] ; then
        printf "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" ${1}
        return;
    fi
    if [[ ${ret} != 84 ]] ; then
        printf "%s Error\n" ${1}
    else printf "%s Success\n" ${1}
    fi
}

search_dir="script/mouli_maps/"
search_dir2="script/mouli_maps_solved/"  
for entry in `ls $search_dir`; do
    solved="${search_dir2}${entry}_true"
    mine="${search_dir}${entry}"
    test_expect_success $solved $mine
done

search_dir="script/error/"
echo "~"
for entry in `ls $search_dir`; do
    mine="${search_dir}${entry}"
    test_expect_error $mine
done

test_expect_error fake

./${BINARY} "script/mouli_maps/one_one_full" "issou" > trash
ret=`echo $?`
rm trash
if [[ ${ret} != 84 ]] ; then
        printf "too_many_args Error\n"
    else printf "too_many_args Success\n"
    fi