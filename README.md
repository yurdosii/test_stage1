# test_stage1

## Demo
https://user-images.githubusercontent.com/41447717/236241068-304908bd-5071-4ee9-8b6b-337ba7e8396f.mp4

## Stack
FastAPI, MongoDB, Docker, PyTest, black, flake8, isort, mypy, Makefile

## Development
### To run locally
```
uvicorn src.main:app --reload
```

### To run via Docker
```
docker-compose build
docker-compose up
```

### Linters
```
make lint
```
