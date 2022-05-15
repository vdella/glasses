from dataclasses import dataclass


@dataclass
class Structure:
    points = set()
    label: str = ''
