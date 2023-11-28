#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""Used to create one or more applications.
 A website may consist of one or more sections. For example, main site, blog, wiki, downloads area, etc. 
 Django encourages you to develop these components as separate applications, which could then be re-used in different projects if desired."""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team8.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
