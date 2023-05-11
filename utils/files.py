import csv


def read_csv(filename: str):
    l = []
    with open(filename, encoding='utf-8') as fp:
        reader = csv.reader(fp)
        # 获取标题
        header = next(reader)
        # 遍历数据
        for i in reader:
            m = {}
            for j in range(len(header)):
                m[header[j]] = i[j]
            l.append(m)
    return l
