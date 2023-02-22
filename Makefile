.PHONY: install lock fmt lint

PWD=$${pwd}

install:
	@pip3 install pipenv

lock:
	@pipenv lock
	@pipenv sync

fmt:
	@pipenv run black ./

lint:
	@pipenv run pylint ./mypydantic