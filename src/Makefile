APPLICATION=fastapi
VERSION=0.1.0

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
		@echo
		@echo "ATENÇÃO!!! Defina as variáveis de ambiente AWS_PROFILE e AWS_DEFAULT_REGION antes de executar este Makefile"
		@echo
		@echo "Uso:"
		@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
