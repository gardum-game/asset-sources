from krita import Krita
import os
from pathlib import Path


def export_file(filename, output_path):
    document = Krita.instance().openDocument(str(filename))

    # Resize the image if it contains a special suffix.
    fixed_filename, separator, size_suffix = filename.stem.rpartition('-')
    if size_suffix:
        filename = Path(filename.parent, fixed_filename + filename.suffix)
        x, separator, y, = size_suffix.partition('x')
        document.scaleImage(int(x), int(y), document.xRes(), document.yRes(), 'Hermite')

    document.setBatchmode(True)
    document.saveAs(str(output_path / filename.with_suffix('.png')))
    print(output_path / filename.with_suffix('.png'))
    document.close()


output_path = Path(os.getenv('GARDUM_PATH', '../gardum'))
for filename in Path().glob('**/*.kra'):
    export_file(filename, output_path)
