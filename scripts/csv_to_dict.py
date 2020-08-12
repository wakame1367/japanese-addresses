import pandas as pd
import pickle
URL_JAPANESE_ADDRESSES = 'https://raw.githubusercontent.com/geolonia/' \
                         'japanese-addresses/master/data/latest.csv'


def main():
    prefecture_col = '都道府県名'
    city_col = '市区町村名'
    street_col = '大字町丁目名'
    japanese_addresses = pd.read_csv(URL_JAPANESE_ADDRESSES)
    prefecture2city = dict()
    for prefecture, groups1 in japanese_addresses.groupby(prefecture_col):
        city2street = dict()
        for city, groups2 in groups1.groupby(city_col):
            # numpy.array to set
            city2street[city] = set(groups2[street_col].unique())
        prefecture2city[prefecture] = city2street
    save_path = 'prefecture2city2street.pkl'
    with open(save_path, mode='wb') as f:
        pickle.dump(prefecture2city, f)


if __name__ == '__main__':
    main()
