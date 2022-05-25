# JDP docker

```pwsh
docker build -t jdp-jupyter jdp-jupyter
```

```pwsh
docker run -v "${PWD}:/workspace" -p 8888:8888 jdp-jupyter jupyter notebook
```