6.0.1 (unreleased)
------------------

- Nothing changed yet.


6.0.0 (2020-06-12)
------------------

- Moved to guillotina 6 and python 3.8 [lferran]


5.0.3 (2019-12-02)
------------------

- Fix bug: individual errors are returned separately instead of making
  main request fail. [lferran]

5.0.2 (2019-11-05)
------------------

- Add request body validation
- Add request and responses swagger description
- Black and isort
- Fix travis

[lferran]

5.0.1 (2019-11-01)
------------------

- Be able to import types


5.0.0 (2019-08-30)
------------------

- Upgrade to g5


1.2.1 (2019-06-18)
------------------

- restrict compat version


1.2.0 (2019-05-13)
------------------

- Provide new `max_batch_size` setting and default it to `200`
  [vangheem]


1.1.0 (2019-03-11)
------------------

- Retry requests automatically on ConflictError (with `eager-commit=True`)
  [masipcat]


1.0.5 (2018-11-19)
------------------

- Added GET param `eager-commit` [masipcat]


1.0.4 (2018-07-06)
------------------

- Copy future object from batch request to request


1.0.3 (2018-06-27)
------------------

- Including parent request's security in batched view [lferran]


1.0.2 (2018-06-27)
------------------

- try again


1.0.1 (2018-06-13)

- markdown fix


## 1.0.0 (2018-06-11)

- Initial release
  [vangheem]
