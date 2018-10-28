# ~/.bashrc: executed by bash(1) for non-login shells.

source ~/git-completion.bash

function parse_git_dirty {
  [[ $(git status --porcelain 2> /dev/null | tail -n 1) != "" ]] && echo "*"
}

function parse_git_branch {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/ [\1$(parse_git_dirty)]/"
}

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
PS1="$(host_name)\n\u@\h:\w\$ \[\033[32m\]\w\[\033[33m\]$(parse_git_branch)\[\033[00m\] $ "
# umask 022

# Some alias
alias ll="ls -la"
