# Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version when you make incompatible API changes  
- **MINOR** version when you add functionality in a backwards-compatible manner  
- **PATCH** version when you make backwards-compatible bug fixes

**Bumping the version**  
Use Poetry’s built-in command:

```bash
# patch release (0.1.0 → 0.1.1)
poetry version patch

# minor release (0.1.0 → 0.2.0)
poetry version minor

# major release (0.1.0 → 1.0.0)
poetry version major
