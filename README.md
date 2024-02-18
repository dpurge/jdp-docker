# JDP docker

Build:

```pwsh
task jdp-buildenv
task jdp-dictionary
docker build -t jdp-jupyter jdp-jupyter
```

Run locally:

```pwsh
docker run --interactive --tty --rm -v "${PWD}:/workspace" gcr.io/kaniko-project/executor:debug --context dir:///workspace --context-sub-path jdp-buildenv --no-push
docker run --interactive --tty --rm -v "${PWD}:/workspace" jdp-buildenv bash
docker run -v "${PWD}:/workspace" -p 8888:8888 jdp-jupyter jupyter notebook
```

Release:

```pwsh
docker login
task jdp-buildenv-release
```

```pwsh
pipenv shell
pipenv install flask
pipenv install requests
pipenv requirements --exclude-markers
pipenv shell
pipenv run python src/app.py
```