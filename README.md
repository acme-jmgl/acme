# acme

A tiny todo API. It exists as sample data for testing ShipShow's GitHub sync:
the pull requests in this repo are deliberately left in different states.

## run

    pip install -r requirements.txt
    flask --app app run

## test

    pytest

## deploy

Publishing a GitHub Release deploys it. The `Deploy` workflow checks out the
release's tag and "deploys" it to a mock destination (it only echoes):
a full release goes to `production`, a prerelease to `staging`.

`Deploy` can also be run by hand with a tag or SHA; tick `simulate_failure`
to get a failed run.
