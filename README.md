# dcbot

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deeplook/dcbot/jlab?urlpath=lab)

Warning: Because the standard mybinder servers will not allow network access to IMAP/SMTP ports this will actually *not* work using the "launch binder" button above! Running this repo with `repo2docker` locally should work, though.

To get started with a local repo2docker, make sure you have it installed and run it similar to this, with your own values:

```bash
pip install jupyter-repo2docker
repo2docker --debug -e HEREMAPS_API_KEY=$HEREMAPS_API_KEY -e ADDR=email@example.com -e PASSWORD=supersecret .
```

Then, in the running docker container, start `binder/start_bot.sh`.

