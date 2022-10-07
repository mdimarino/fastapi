APPLICATION=fastapi
VERSION=0.1.0

## venv: cria o virtual environment
venv: 
		@echo "Cria virtual environment"
		test -d .venv || python3 -m venv .venv

## deps: instala dependências
deps: venv
		@echo "Instala dependências"
		bash -c "source .venv/bin/activate && pip install -r requirements.txt"

## image: cria localmente a imagem docker
image:
		@echo "Cria imagem Docker"
		docker build --build-arg arg_version=${VERSION} -t ${APPLICATION}:${VERSION} .
		docker tag ${APPLICATION}:${VERSION} ${APPLICATION}:latest

## clean: remove a imagem docker local
clean:
		@echo "Remove a imagem"
		docker image rm ${APPLICATION}:${VERSION}
		docker image rm ${APPLICATION}:latest

## help: exibe esta mensagem de ajuda
help:
		@echo "Uso:"
		@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
