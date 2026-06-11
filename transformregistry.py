from typing import Callable
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Transform:
    name: str
    func: Callable[[list[str]], list[str]]
    disableFlag: str

global transforms
transforms: list[Transform] = []

def transform(name: str, *, disableFlag: str):
    '''
    Register a gcode transform.
    `name` is the name that will be printed before it runs.
    `disableFlag` is a command-line flag that can be added to disable this transform.
    '''
    def decorator(func: Callable[[list[str]], list[str]]):
        def wrapper(file: list[str]) -> list[str]:
            print(f'Running "{name}"...')
            return func(file)
        
        transforms.append(Transform(name, func, disableFlag))
        
        return wrapper
    
    return decorator