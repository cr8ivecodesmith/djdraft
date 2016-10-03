#!/bin/bash

echo "--> Starting ssh service"
echo "--> [browser] http://0.0.0.0:8015"
echo "--> [ssh] ssh $PROJECT_SUDO_USER@0.0.0.0 -p 2767 -o IdentitiesOnly=Yes"
/usr/sbin/sshd -D
