#!/bin/bash
# convert plaintext url list from authenticator extension to password store

while read -r otpurl ; do
    name=${otpurl#otpauth://totp/}
    name=${name%%\?*}
    name=${name//%40/@}
    name=${name//%20/_}  # yes it is a space but I don't want to
    printf "%s\n%s\n" "$otpurl" "$otpurl" | pass insert "fu2fa/$name.url"
done
