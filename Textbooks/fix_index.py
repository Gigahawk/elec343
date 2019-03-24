import json


def get_offset(cur_page):
    # I have no idea where page 96 went
    if cur_page < 96:
        return 14
    # or page 144
    elif cur_page < 144:
        return 13
    # or page 286...
    elif cur_page < 286:
        return 12
    # yea this is really stupid
    elif cur_page < 344:
        return 11
    elif cur_page < 414:
        return 10
    else:
        return 9


def gen_index(page, title, count=None):
    if count:
        return f'[/Count {count} /Page {page} /Title ({title}) /OUT pdfmark\n'
    else:
        return f'[/Page {page} /Title ({title}) /OUT pdfmark\n'


with open('index_orig.json', 'r') as in_f:
    data = json.load(in_f)
    chapter = 1
    for i, ch in enumerate(data):
        if 'no_number' not in ch:
            ch['title'] = f'{chapter} {ch["title"]}'
        if 'no_offset' not in ch:
            ch['page'] = ch['page'] + get_offset(ch['page'])

        if 'chapters' in ch:
            subchapter = 1
            for i, subch in enumerate(ch['chapters']):
                subch['title'] = f'{chapter}.{subchapter} {subch["title"]}'
                subch['page'] = subch['page'] + get_offset(subch['page'])
                subchapter += 1
        if 'no_offset' not in ch:
            chapter += 1

    with open('index_true.json', 'w') as out_f:
        json.dump(data, out_f, indent=4)

with open('index_true.json', 'r') as in_f:
    data = json.load(in_f)
    with open('index.info', 'w') as out_f:
        for i, ch in enumerate(data):
            if 'chapters' in ch:
                subchs = len(ch['chapters'])
            else:
                subchs = None

            out_f.write(gen_index(ch['page'], ch['title'], subchs))

            if 'chapters' in ch:
                for i, subch in enumerate(ch['chapters']):
                    out_f.write(gen_index(subch['page'], subch['title']))

