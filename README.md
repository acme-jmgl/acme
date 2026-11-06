# acme

A tiny todo API. It exists as sample data for testing ShipShow's GitHub sync:
the pull requests in this repo are deliberately left in different states.

## run

    pip install -r requirements.txt
    flask --app app run

## test

    pytest

## deploy and release

- `Deploy` runs on every push to `main` (and by hand). It deploys nothing; it
  only echoes. Run it with `simulate_failure` to get a failed run.
- `Release` runs when a `v*` tag is pushed and publishes a GitHub Release.
  A tag containing `-` (e.g. `v0.2.0-rc.1`) becomes a prerelease.
