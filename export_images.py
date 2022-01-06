from krita import Krita
import os
from pathlib import Path


def export_file(filename, output_path):
    document = Krita.instance().openDocument(str(filename))
    output_path.mkdir(parents=True, exist_ok=True)

    # Resize the image if it contains a special suffix.
    fixed_filename, separator, size_suffix = filename.stem.rpartition('-')
    if size_suffix:
        filename = Path(filename.parent, fixed_filename + filename.suffix)
        x, separator, y, = size_suffix.partition('x')
        document.scaleImage(int(x),
                            int(y),
                            int(document.xRes()),
                            int(document.yRes()),
                            'Hermite')

    output_filename = str(output_path / filename.with_suffix('.png'))
    document.setBatchmode(True)
    document.saveAs(output_filename)
    print(f'Saved to {output_filename}')
    document.close()


output_path = Path(os.getenv('GARDUM_PATH', '../gardum'))
for filename in Path().glob('**/*.kra'):
    export_file(filename, output_path)
