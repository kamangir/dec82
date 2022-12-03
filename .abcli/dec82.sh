#! /usr/bin/env bash

function dec82() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "dec82 session start [<options>]" \
            "start a dec82 session."

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

    abcli_log_error "-dec82: $task: command not found."
}

function dec82_session() {
    abcli_log "dec82: session started."

    abcli_tag set \
        $abcli_object_name \
        open,$abcli_hostname,dec82

    local options=$1

    python3 -m dec82 \
        start_session \
        ${@:2}

    abcli_upload open

    abcli_log "dec82: session ended."
}