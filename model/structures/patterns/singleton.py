class Singleton(type):
    """Singleton pattern class that overrides the __call__
    operator: states what should happen before calling its constructor."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
