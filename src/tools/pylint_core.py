from dataclasses import dataclass
import pylint as pl


@dataclass
class PylintOutput:
    """Class to provide a template for pylint output messages."""
    score: float
    total_messages: int
    errors: int
    warnings: int
    file_path: str
    timestamp: str


class PylintInput:
    """Class to enable usage of pylint commands via CLI execution."""

    def run_pylint_command(self, path: str, options: str = ""):
        """Runs a pylint cmd through a subprocess"""
        import subprocess

        command = ["uv", "run", "pylint"] + [options] + [path]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=60
                )
            return result
        except Exception as e:
            print(f"Error occurred while running pylint: {e}")
            return None