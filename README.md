# dcbot

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deeplook/dcbot/main?urlpath=lab)

This is a first attempt at writing a [bot](https://bots.delta.chat/) for [DeltaChat](https://delta.chat/en/) using its [Python bindings](https://py.delta.chat/).

**Warning:** Because the standard mybinder servers will not allow network access to IMAP/SMTP ports this will actually *not* work using the "launch binder" button above! Running this repo with `repo2docker` locally should work, though.

To get started with a local [repo2docker](https://github.com/jupyterhub/repo2docker), make sure you have it installed and run it similar to this, with your own values:

```bash
pip install jupyter-repo2docker
repo2docker --debug -e HEREMAPS_API_KEY=$HEREMAPS_API_KEY -e ADDR=email@example.com -e PASSWORD=supersecret .
```

Then, in the running docker container, start `binder/start_bot.sh`.

On Linux this bot should work without binder/repo2docker after installing the dependencies in binder/environment.yml, setting the environment variable,  and starting the bot like this:

```bash
export HEREMAPS_API_KEY=MY_API_KEY
export ADDR=email@example.com
export PASSWORD=supersecret
binder/start_bot.sh`
```
