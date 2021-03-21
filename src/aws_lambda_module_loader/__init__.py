import importlib
import pkgutil


class SubModuleImporterExpection(Exception):
    pass

def import_submodules(package:str, recursive=True):
    """[summary]

    Args:
        package (str): [description]
        recursive (bool, optional): [description]. Defaults to True.

    Returns:
        [dict]: [list of imported modules]
    """

    try:
        package = importlib.import_module(package)
    except ModuleNotFoundError:
        raise SubModuleImporterExpection(f'No such module: {package}')

    if not hasattr(package, '__path__'):
        # this ain't a package
        raise SubModuleImporterExpection(f'No such package: {package}')

    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results
