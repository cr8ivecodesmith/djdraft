#!/bin/bash

WORKDIR=$1
DOMAIN=$2

SKEY=$WORKDIR/server.key
SCRT=$WORKDIR/server.crt
SCSR=$WORKDIR/server.csr

PASS=pass:x
PASSKEY=$WORKDIR/pass.key

CC=PH
STATE=Manila
LOC=Manila
ORG=Developers
ORGU=Developers
EXPIRY=1825


echo "--> [dev] Starting non-interactive SSL Generation"
echo "--> Generating private key"
openssl genrsa -des3 -passout $PASS -out $PASSKEY 2048
openssl rsa -passin $PASS -in $PASSKEY -out $SKEY
rm -f $PASSKEY

echo "--> Generating certificate signing request (csr)"
openssl req -new -key $SKEY -out $SCSR \
    -subj "/C=$CC/ST=$STATE/L=$LOC/O=$ORG/OU=$ORGU/CN=$DOMAIN"

echo "--> Generating self-signed certificate"
openssl x509 -req -days $EXPIRY -in $SCSR -signkey $SKEY -out $SCRT

echo "--> Done"
