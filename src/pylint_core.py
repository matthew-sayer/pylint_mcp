import shlex


class PylintCommand:
    """Class to build pylint arguments"""
    def __init__(self, path: str, options: str = ""):
        self.path = path
        self.options = shlex.split(options) if options else []

class PylintSubprocess(PylintCommand):
    """Class to enable usage of pylint commands via CLI execution."""

    def run_pylint_subprocess(self):
        """Runs a pylint cmd through a subprocess"""
        import subprocess

        command = ["uv", "run", "pylint"] + self.options + [self.path]

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