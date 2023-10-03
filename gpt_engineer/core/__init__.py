"""
gpt_engineer.core
-----------------

The core package for the GPT Engineer project, providing essential modules
and functionalities that form the foundation of the application.

Modules:
    - ai: Contains interfaces to the OpenAI GPT models.
    - domain: Houses the domain logic and main business rules.
    - chat_to_files: Provides utilities for converting chat logs to file formats.
    - steps: Includes step definitions and workflows for the application.
    - db: Manages database connections and CRUD operations.

For more specific details, refer to the docstrings within each module.
"""

from gpt_engineer.core import (
    ai,
    domain,
    chat_to_files,
    steps,
    db,
)
