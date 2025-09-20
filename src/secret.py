"""secret.py

This is an example for a class that hides values automatically, when used in logging or printing"
"""

class Secret:

    def __init__(self, value, placeholder = "[REDACTED]"):
        self.placeholder = placeholder
        object.__setattr__(self, 'value', value)

    def __str__(self):
        return self.placeholder

    def __repr__(self):
        return self.placeholder

    def __getattribute__(self, name):
        if name == 'value':
            return object.__getattribute__(self, name)
        return object.__getattribute__(self, name)

    def __eq__(self, other):
        if isinstance(other, Secret):
            return self.value == other.value
        return self.value == other

    def __hash__(self):
        return hash(self.value)

    def __getattr__(self, name):
        # Delegate attribute access to the wrapped value
        return getattr(self.value, name)

    def __call__(self, *args, **kwargs):
        # Allow the secret to be called if the wrapped value is callable
        return self.value(*args, **kwargs)
    
    def __iter__(self):
        # Prevent iteration to avoid exposing secret value character by character
        raise TypeError(f"'{self.__class__.__name__}' object is not iterable")


if __name__ == "__main__":
    secret_value = "my_secret_value"
    print("before", secret_value)
    print("after ", Secret(secret_value))

