# Pandemic Game ML

This project intends to model and train an AI agent to play the board game, [Pandemic](https://www.zmangames.com/game/pandemic/).

## Installation

The project is managed via the [Poetry](https://python-poetry.org/docs/) cli tool.  

Ensure `poetry` is available and up to date via `pip`:

```bash
python -m pip install --upgrade poetry
cd <project_dir>
poetry install --no-root --with=dev
```

This creates a new virtual environment in the default location with the current Python interpreter.  

It also installs the required dependencies to run the project.  

This will include packages designated for development (ie, testing or static analysis tools)

Currently, the project is not packageable, hence the `--no-root` flag.  


## Usage

If a CLI is available, it will be run via the following command:

```bash
python -m pandemic-game-ml <args>
```

## Running Tests

To run the tests for this project, use the following command:

```bash
poetry run pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.