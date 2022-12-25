#! /usr/bin/env bash

function dec82() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "dec82 session start" \
            "start a dec82 session."
        return
    fi

    local function_name=dec82_$task
    if [[ $(type -t $function_name) == "function" ]] ; then
        $function_name ${@:2}
        return
    fi

    abcli_log_error "-dec82: $task: command not found."
}

function dec82_session() {
    abcli_log "dec82: session started."

    blue_sbc_session \
        "$1" \
        $(abcli_option_default "$2" app Dec82) \
        ${@:3} \

    abcli_log "dec82: session ended."
}