import pandas as pd
import pickle
URL_JAPANESE_ADDRESSES = 'https://raw.githubusercontent.com/geolonia/' \
                         'japanese-addresses/master/data/latest.csv'


def main():
    prefecture_col = '都道府県名'
    city_col = '市区町村名'
    japanese_addresses = pd.read_csv(URL_JAPANESE_ADDRESSES)
    groups = japanese_addresses.groupby(prefecture_col)[city_col].unique()
    prefecture2city = groups.to_dict()
    # numpy.array to set
    for k, v in prefecture2city.items():
        prefecture2city[k] = set(v)
    save_path = 'prefecture2city.pkl'
    with open(save_path, mode='wb') as f:
        pickle.dump(prefecture2city, f)


if __name__ == '__main__':
    main()
