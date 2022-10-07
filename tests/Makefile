## venv: cria o virtual environment
venv: 
		@echo "Cria virtual environment"
		test -d .venv || python3 -m venv .venv-tests

## deps: instala dependências
deps:
		@echo "Instala dependências"
		bash -c "source .venv-tests/bin/activate && pip install -r requirements.txt"

## run: executados testes
run:
		@echo "Executa os testes"
		./tests_requests.py

## help: exibe esta mensagem de ajuda
help:
		@echo "Uso:"
		@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
