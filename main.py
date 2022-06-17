from pathlib import Path

def count_receipt(codes, in_codes):
    with open('target_codes.csv', encoding='cp932') as f:
        rows = f.readlines()

    newtxt = 'コード,名称,実績,入院実績\n'
    for row in rows:
        row = row.replace('\n', '')
        row_list = row.split(',')
        code = row_list[0]
        name = row_list[1]
        newtxt += f'{code},{name},{codes.count(code)},{in_codes.count(code)}\n'

    outfile = Path.cwd()/'count.csv'
    if outfile.exists():
        outfile.unlink()
    with open('count.csv', mode='x') as f:
        f.write(newtxt)

def count(files):
    all_result = ''
    in_result = ''
    in_flag = False
    for file in files:
        print(file)
        with open(file, encoding='cp932') as f:
            rows = f.readlines()
        for row in rows:
            rowlist = row.split(',')
            if rowlist[0] == 'RE':
                if int(rowlist[2]) % 2 == 0:
                    in_flag = False
                else:
                    in_flag = True
            if rowlist[0] == 'SI':
                code = rowlist[3]
                n = int(rowlist[6])
                for i in range(n):
                    all_result += f'{code} '
                if in_flag:
                    for i in range(n):
                        in_result += f'{code} '
    return(all_result, in_result)

if __name__ == '__main__':
    filedir = Path.cwd()/'out'
    files = filedir.glob('**/*.UKE')
    all_result, in_result = count(files)
    count_receipt(all_result, in_result)
