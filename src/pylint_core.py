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

class GitRepoDirectoryReader(DirectoryReaderBaseClass):
    """Read git repo contents""" 
    def __init__(self, path: str):
        super().__init__(path)
        self.runner = CommandRunner()

    def get_git_repo_head(self):
        command = f"git ls-remote --heads {self.path}"
        return self.runner.run_subprocess(command, capture_output=True, text=True, timeout=30)

    def read_git_repo_python_modules(self):
        head = self.get_git_repo_head()
        if "error" in head:
            return {"error": head["error"]}
        command = f"git ls-tree -r --name-only {head} | findstr \".py$\""
        result = self.runner.run_subprocess(command, capture_output=True, text=True, timeout=30)
        
        # Handle errors
        if isinstance(result, dict) and "error" in result:
            return result
        
        if result.returncode != 0:
            return {"error": f"Git command failed: {result.stderr}"}
        
        # Parse the stdout to get Python files
        files = result.stdout.strip().split('\n') if result.stdout else []
        return [f for f in files if f.endswith('.py')]
    
    def show_python_modules(self):
        modules = self.read_git_repo_python_modules()
        module_output = {}
        for module in modules:
            command = f"git show {module}"
            result = self.runner.run_subprocess(command, capture_output=True, text=True, timeout=30)
            module_output[module] = result
        return module_output
    
    def read_entire_git_repo(self):
        """Orchestrate the steps to read an entire git repository"""
        self.get_git_repo_head()
        self.read_git_repo_python_modules()
        module_output = self.show_python_modules()
        return module_output


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
    