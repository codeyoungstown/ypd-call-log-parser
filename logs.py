import argparse
import os
import re
import sys

import pytesseract

from PIL import Image


EXCLUDE_KEYWORDS = [
    'amr', 'lift', 'animal', 'alarm', 'structure', 'medical', 'persons',
    'parking', 'dog', 'accident', 'assist', 'paper', 'barking', '911',
    'repossession', 'runaway', 'odor', 'alarm', 'ambulance'
]

ID_RE = re.compile(r'^\d{9}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str, help='Directory containing images to parse')
    parser.add_argument('filter_nature', type=str, help='Comma separated list of natures to filter by', nargs='?', default=None)
    parser.add_argument('--exclude', dest='exclude_lines', action='store_true',
                        default=False, help='Exclude non emergency nature')
    parser.add_argument('--lines', dest='output_lines', action='store_true',
                        default=True, help='Output call lines only')
    parser.add_argument('--ids', dest='output_ids', action='store_true',
                        default=False, help='Output ids only')
    args = parser.parse_args()

    directory = args.directory
    nature_filters = args.filter_nature
    exclude_lines = args.exclude_lines

    if nature_filters:
        nature_filters = [f.strip() for f in nature_filters.split(',')]

    try:
        pages = []
        for filename in os.listdir(directory):
            if filename.endswith('.jpeg') or filename.endswith('.jpg'):

                sys.stdout.write('.')
                sys.stdout.flush()

                filepath = os.path.join(directory, filename)

                # Images to line text
                text = pytesseract.image_to_string(Image.open(filepath), config='--psm 6')
                pages.append(text.split('\n'))
    except FileNotFoundError:
        sys.stderr.write('Directory not found.\n')
        sys.exit(1)

    if not pages:
        sys.stderr.write('No images found.\n')
        sys.exit(1)

    sys.stdout.write('\n')

    # Sanitize lines
    clean_lines = []
    for page in pages:

        for line in page:

            # Skip any lines that don't start with 9 digit call ID
            id_match = ID_RE.match(line)
            if not id_match:
                continue

            # Skip any lines with excluded reasons
            if exclude_lines and any(word.lower() in line.lower() for word in EXCLUDE_KEYWORDS):
                continue

            # If a filter is set, skip any that don't match
            if nature_filters:
                if not any(word.lower() in line.lower() for word in nature_filters):
                    continue

            clean_lines.append(
                # Call ID, line
                (id_match.group(), line)
            )

    if not clean_lines:
        sys.stderr.write('No results\n')
        sys.exit(1)

    # Output comma separated list of IDs only
    if args.output_ids:
        output_ids = ', '.join([l[0] for l in clean_lines])
        sys.stdout.write('{}\n'.format(output_ids))

    # Output full lines
    else:
        for line in clean_lines:
            sys.stdout.write('{}\n'.format(line[1]))


if __name__ == "__main__":
    main()
