# Asset sources

Files for generating assets for [Gardum](https://github.com/gardum-game/gardum)

## Assets generation

Scripts `export_models.py` (should run from Blender) and `export_images.py` (should run from Krita) automatically exports all asset sources to corresponding folders. The scripts assume by default that the game folder is in the directory above (`../gardum`). But this can be overwriten by using the `GARDUM_PATH` environment variable.

**Example:**

```bash
blender --background --python export_models.py

# kritarunner takes a module name, so we have to add the current folder to the module path
env PYTHONPATH=. kritarunner -s export_images
```
