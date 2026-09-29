# spider-pixi-template

A minimal template presenting a streamlined workflow for containerizing Conda-based analyses with perfect reproducibility for [Spider](https://spiderdocs.surf.nl/) (and generally for HPC systems where containers are recommended (e.g., due to using a distributed file system)).

This template uses [Pixi](https://pixi.prefix.dev/latest/) (providing a modern Conda experience with lockfile support, and task running), and [Pixitainer](https://github.com/RaphaelRibes/pixitainer) (an extension providing easy image creation).

## Prerequisites

### 0. Work on a Linux machine

[Apptainer cannot run on Mac or Windows](https://apptainer.org/docs/admin/main/installation.html#installation-on-windows-or-mac). Pixitainer depends on Apptainer, hence requires Linux as an operating system.

You need to either use a Linux machine, or run Linux via a virtualmachine.

### 1. Install Pixi

```bash
curl -fsSL https://pixi.sh/install.sh | sh
source ~/.bashrc  # or ~/.zshrc
```

[See docs for more info](https://pixi.prefix.dev/latest/installation/)

### 2. Install Pixitainer globally via Pixi

```bash
pixi global install -c https://prefix.dev/raphaelribes pixitainer
```

[See docs for more info](https://github.com/RaphaelRibes/pixitainer)

> If your system uses Singularity instead of Apptainer, install `pixitainer-singularity` instead.

## Quick start

### Build the container image

```bash
pixi containerize
```

This produces `spider-pixi-template.sif`.

### Run locally (if Apptainer is available)

```bash
apptainer run spider-pixi-template.sif hello
```

The `hello` task runs a Python script that writes `output/hello.txt` in your current working directory.

### Run on Spider

1. Transfer the `.sif` file to Spider.
2. Run:

```bash
apptainer run --mount type=bind,src=./output,dst=/output spider-pixi-template.sif hello
```

Output is written to `output/hello.txt` relative to where you invoked the command, which lives on Spider's persistent storage (outside the read-only container).

## Project structure

```
spider-pixi-template/
  pixi.toml   # Pixi manifest with dependencies, tasks, and Pixitainer config
  hello.py    # Example task — writes results to persistent storage via $INIT_CWD
  README.md
```

## Customising

- Add dependencies: `pixi add numpy pandas` (etc.)
- Add tasks: define new entries under `[tasks]` in `pixi.toml`
- Ensure that the `pixi.toml` `platforms` key is correct
- Modify `pixitainer` config in `[tool.pixitainer]` within `pixi.toml`
- Write output to `$INIT_CWD` (or a subdirectory) so results land on the host filesystem rather than inside the read-only container
