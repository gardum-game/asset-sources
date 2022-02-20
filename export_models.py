import bpy
import os
import shutil
from pathlib import Path


def remove_extra_objects():
    # Force object mode
    if bpy.context.object.mode == 'EDIT':
        bpy.ops.object.mode_set(mode='OBJECT')
    # Force clear selection
    bpy.ops.object.select_all(action='DESELECT')

    # Select object to delete them later
    for object in bpy.data.objects:
        if (object.type != 'MESH' and object.type != 'ARMATURE') or \
                object.name.endswith('_hp'):
            if object.hide_get():
                object.hide_set(False)
            print('Deleting: ' + object.name)
            object.select_set(True)

    # Delete all selected objects
    bpy.ops.object.delete()


def export_file(filename, output_path):
    bpy.ops.wm.open_mainfile(filepath=str(filename))
    remove_extra_objects()

    parent_folder = output_path / filename.parent
    parent_folder.mkdir(parents=True, exist_ok=True)

    output_filename = str(output_path / filename.with_suffix('.glb'))
    bpy.ops.export_scene.gltf(filepath=output_filename,
                              export_apply=True)


output_path = Path(os.getenv('GARDUM_PATH', '../gardum'))
# Export models
for filename in Path().glob('**/*.blend'):
    export_file(filename, output_path)

# Copy textures
for filename in Path().glob('**/*.png'):
    shutil.copy(filename, output_path / filename)
