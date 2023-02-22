.PHONY: install lock fmt lint generate model

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

generate:
	@pipenv run python3 generate.py

model:
	@pipenv run datamodel-codegen --input templates/web_acl_snake.json \
	--output mypydantic/models/web_acl.py \
	--input-file-type json \
	--class-name WebACL \
	--disable-timestamp