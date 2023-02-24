.PHONY: install lock fmt lint docs create-docs view-docs pcommit commit generate test py-test model

PWD=$$(pwd)

install:
	@pip3 install pipenv

lock:
	@pipenv lock
	@pipenv sync --dev

fmt:
	@pipenv run black ./

lint:
	@pipenv run pylint ./mypydantic

docs: create-docs pcommit

create-docs:
	@pipenv run pdoc -o mypydantic/docs -d google --no-search ./mypydantic

view-docs:
	@open file://${PWD}/mypydantic/docs/index.html

pcommit:
	@pipenv run pre-commit install
	@pipenv run pre-commit run --all-files

commit:
	@pipenv run pre-commit install
	@pipenv run git add --all
	@read -p "Commit Message: " COMMIT_MESSAGE \
	&& pipenv run git commit -m "$${COMMIT_MESSAGE}"
	@read -p "Commit Branch: " COMMIT_BRANCH \
	&& pipenv run git push origin $${COMMIT_BRANCH}

generate:
	@pipenv run python3 generate.py

test:
	@pipenv run python3 example.py

py-test:
	@pipenv run pytest mypydantic

model:
	@pipenv run datamodel-codegen --input templates/web_acl_snake.json \
	--output mypydantic/models/web_acl.py \
	--input-file-type json \
	--class-name WebACL \
	--disable-timestamp
