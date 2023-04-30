# Flammie’s ubiquitous 2fa tool

Flammie's ubiquituos 2fa tool is a command-line otp generator for `dmenu` and
`pass`.

**⚠️⚠️This is an experiment for my own use only. Please keep in mind that actually
using this you are practically circumventing the 2nd or multith factor in your
multi-factor authentification, this is not good for security.⚠️⚠️**

## Dependencies

* pyotp
* pass
    * gpg
* xclip
* xdotool

## Usage

You can use this from commandline:

```shell
$ fu2fa.py -U otp://totp/issuer:user?secret=SECRET
123456
```

however, the best experience is integrated with `pass` and `dmenu`. You use pass
to store the URL's including the secrets in password-store under
`fu2fa/name.url`.  Then you can use `fu2famenu` to list and select the URL from
dmenu, by default the selected totp code will be clipped into your clipboard
using `xclip` but you can select to use `xdotool` to type it too (this
functionality was basically copied from `passmenu` in dmenu's examples dir).
Because I reused `passmenu` code this should work with wayland stuff but I
haven't tested it.

I use this on `i3` with following `~/.config/i3config`:

```
bindsym $mod+o fu2famenu
```

At the moment you have to type the path of fu2fa.py to fu2famenu manually, maybe
I'll write an installer lol at some point.

## Getting the URLs

The authenicator extension for Firefox and chrome asks you regularly to back up
the authenticator stuffs, this backup is just a plaintext file with the URLs you
need one per line. I made a script `authenticator-extension2password-store.bash`
to convert this automatically to your password store in right path, it just uses
`pass insert` for each line and the URL as a password. These URLs contain a
secret thingie that anyone can use to steal access to your 2FA's so you should
at minimum not show them to anyone and keep them encrypted; even if you are on
your way to circumventing the security provided by the added factors there's no
need to be overly insecure ;-)


