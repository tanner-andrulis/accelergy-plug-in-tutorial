import inspect

def write_source(python_object: Any, filename: str) -> None:
    """Write the source code of a Python object to a file. Adds in Accelergy plug-in imports. """
    imports = 'from accelergy.plug_in_interface.estimator import Estimator, action2energy\n'
    open(filename, 'w').write(imports + inspect.getsource(python_object))
