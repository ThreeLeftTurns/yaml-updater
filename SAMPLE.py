
from update import merge

# Example usage
if __name__ == "__main__":
    current_version = {
        "name": "Example",
        "description": "A simple example.",
        "version": 1,
        "OLDER_VERSION" : 123
    }

    new_version = {
        "name": "UPDATED",
        "version": 555,
        "features": ["New feature 1", "New feature 2"]
    }

    merge(current_version, new_version, force_update=False, full_update=False)

    print(current_version)