# depocalypse

## Development
From within the folder `frontend` run `npm` to build the frontend when source files change.
```shell
depocalypse/frontend $ npm run serve
```

From within the folder `backend` run the Django development server.
```shell
depocalypse/backend $ python manage.py runserver
```

## Testing and Code Coverage
Use [coverage.py](https://coverage.readthedocs.io) to execute tests and monitor code coverage of tests. This tool can be installed via `pip` or `conda`.
```shell
$ pip install coverage
```
```shell
$ conda install coverage
```

Run tests (and write coverage results into folder `.coverage`):
```shell
coverage run manage.py test
```
Inspect the results:
```shell
coverage report -m
```
Create an HTML report from the results (into folder `coverage_html`):
```shell
coverage html -d coverage_html
```