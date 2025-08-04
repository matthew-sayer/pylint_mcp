#Core class to build pylint universe commands, incl. pylint, pyreverse and symilar

class PylintUniverseCommandBuilder:
    """Class to build pylint or pyreverse arguments"""
    def __init__(self, path: str, options: str):
        import shlex
        self.path = path
        self.options = shlex.split(options) if options else []

#Cmd runner

class CommandRunner:
    """Runs commands in a subprocess"""
    def run_subprocess(self, command: list, capture_output = True, text = True, timeout = 60):
        import subprocess
        try:
            result = subprocess.run(command,
                                    capture_output = capture_output,
                                    text = text,
                                    timeout = timeout
                                    )
            return result
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running command: {e}")
            return {"error": str(e)}
        
#Dir readers

class DirectoryReaderBaseClass:
    """Base class for reading directories"""
    def __init__(self, path: str):
        self.path = path

class LocalDirectoryReader(DirectoryReaderBaseClass):
    """Read local directory of choice"""
    def read_python_modules(self):
        import os
        python_modules = []

        if os.path.isfile(self.path):
            return [self.path]
        
        if os.path.isdir(self.path):
            for root, dir, files in os.walk(self.path):
                for file in files:
                    if file.endswith(".py"):
                        python_modules.append(os.path.join(root, file))

        return python_modules

class GitRepoDirectoryReader(DirectoryReaderBaseClass): # Planning to enable remote repo linting
    pass

#Pylint command factory
        
class PylintUniverseCommandFactory(PylintUniverseCommandBuilder):
    """Runs pylint, Pyreverse or Symilar commands"""

    def __init__(self, tool_name: str, path: str, options: str = ""):
        super().__init__(path, options)
        self.tool_name = tool_name
        self.runner = CommandRunner()

    def run_code_quality_tool(self):
        command = ["uv", "run", self.tool_name] + self.options + [self.path]
        return self.runner.run_subprocess(command, capture_output=True, text=True, timeout=60)
    
    def run_similarity_checker(self):
        python_files = LocalDirectoryReader(self.path).read_python_modules()
        command = ["uv", "run", "symilar"] + self.options + python_files
        return self.runner.run_subprocess(command, capture_output=True, text=True, timeout=60)