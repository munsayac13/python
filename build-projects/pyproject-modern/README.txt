# Install package
pip install .

# Best Practices
1. Use pyproject.toml for New Projects: For new projects, prefer using pyproject.toml as it aligns with modern packaging standards and improves compatibility with various tools.
2. Keep setup.py for Legacy Support: If you are maintaining an existing project that already uses setup.py, you can continue using it but consider transitioning to pyproject.toml when feasible.
3. Use setup.cfg for Configuration: If you want a more declarative format while still usingsetup.py, consider using setup.cfg. This allows you to specify metadata in a configuration file while keeping the logic in setup.py.
4. Leverage Build Tools: Tools like Poetry or Flit can simplify dependency management and packaging by managing the creation of these files automatically based on your project configuration.


