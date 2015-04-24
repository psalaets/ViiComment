# Install

Clone repo into your Sublime packages directory.

1. `cd` into the [Packages directory](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-packages-directory) of your Sublime Text
2. `git clone https://github.com/psalaets/ViiComment.git`

# Set your initials

Go to `Preferences | Package Settings | ViiComment | Settings - Default`

# Set up keyboard shortcut

Go to  `Preferences | Key Bindings - User` and to that array, add

OSX:

```json
{ "keys": ["super+forward_slash"], "command": "vii_comment" }
```

Others:

```json
{ "keys": ["ctrl+forward_slash"], "command": "vii_comment" }
```

Note: This takes over the shortcut for `toggle_comment` but `vii_comment` acts as `toggle_comment` so it should be okay.
