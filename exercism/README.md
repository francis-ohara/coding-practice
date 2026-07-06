# Exercism Workspace

This directory is the [Exercism](https://exercism.org) CLI workspace. The CLI manages the layout below it: one folder per track, one folder per exercise (e.g. `go/hello-world/`).

```
exercism/
└── go/
    ├── hello-world/
    └── ...
```

## Workflow

```bash
exercism download --track=go --exercise=<name>   # fetch starter code + tests
cd go/<name>
go test                                          # iterate until green
exercism submit <solution-file>.go               # upload to exercism.org
```

Don't reorganize folders in here by hand; `exercism submit` expects the CLI's layout. Hand-written experiments from other resources belong in the per-language folders (e.g. [`../go/`](../go/)).
