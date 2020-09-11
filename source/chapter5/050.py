import random
from collections import defaultdict

def write_file(file_name, list):
    out = open(file_name, 'w')
    for elem in list:
        out.write(elem + '\n')
    return

def check_category(list):
    cate2freq = defaultdict(int)
    for line in list:
        category = line.split('\t')[0]
        cate2freq[category] += 1
    print(cate2freq)


def main():
    in_file = open("NewsAggregatorDataset/newsCorpora.csv")
    # タグをあらかじめリストに
    tags = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']
    news_list = []
    for line in in_file:
        new = {}
        splited_line = line.split('\t')
        for idx, elem in enumerate(splited_line):
            new[tags[idx]] = elem
        # 対象出版元
        pub_list = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
        if new['PUBLISHER'] in pub_list:
            news_list.append(new['CATEGORY'] + '\t' + new['TITLE'])
    print(news_list[:3])
    # シャッフル
    random.shuffle(news_list)
    num_news = len(news_list)
    # データ分割
    train = news_list[:int(num_news*0.8)]
    val = news_list[int(num_news*0.8):int(num_news*0.9)]
    test = news_list[int(num_news*0.9):]
    write_file('train.txt', train)
    write_file('valid.txt', val)
    write_file('test.txt', test)

    check_category(train)
    check_category(test)
    """
    train:
    defaultdict(<class 'int'>, {'m': 729, 'e': 4197, 'b': 4538, 't': 1220})
    test:
    defaultdict(<class 'int'>, {'b': 573, 'e': 533, 't': 142, 'm': 88})

    """
    
    






main()



    

