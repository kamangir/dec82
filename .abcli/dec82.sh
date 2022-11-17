#! /usr/bin/env bash

function dec82() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "dec82 validate_hardware" \
            "validate dec82 hardware."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m dec82 --help
        fi

        return
    fi

    local function_name=dec82_$task
    if [[ $(type -t $function_name) == "function" ]] ; then
        $function_name ${@:2}
        return
    fi

    if [ "$task" == "validate_hardware" ] ; then
        python3 -m dec82 \
            validate_hardware \
            ${@:2}
        return
    fi

    abcli_log_error "-dec82: $task: command not found."
}