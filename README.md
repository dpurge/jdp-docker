# JDP docker

```pwsh
docker build -t jdp-jupyter jdp-jupyter
```

```pwsh
docker run -v "${PWD}:/workspace" -p 8888:8888 jdp-jupyter jupyter notebook
```

```pwsh
pipenv shell
pipenv install flask
pipenv install requests
pipenv requirements --exclude-markers
pipenv shell
pipenv run python src/app.py
```