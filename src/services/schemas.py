import importlib.util
import json
import os


def load_json(file_path: str) -> dict:
    """Generic function to load any JSON file and return its contents."""
    with open(file_path, "r") as f:
        return json.load(f)


def load_inputs(script_name: str):
    """Dynamically load and validate JSON input for a given script."""

    # Get script's input path
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Base dir of services
    input_path = os.path.join(script_dir, f"../scripts/{script_name}/input.json")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input JSON file not found: {input_path}")

    # Load schema dynamically from the script folder
    schema_path = os.path.join(script_dir, f"../scripts/{script_name}/schemas.py")

    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    # Import schema dynamically
    spec = importlib.util.spec_from_file_location("schemas", schema_path)
    schemas = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schemas)

    if not hasattr(schemas, "ScriptInputs"):
        raise ImportError(
            f"Schema file {schema_path} does not contain `ScriptInputs` class."
        )

    # Load JSON and validate with ScriptInputs
    data = load_json(input_path)
    return schemas.ScriptInputs(**data)  # Validate using dynamically loaded schema
