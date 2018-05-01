# 辞書: Key Valueをセットにした配列 (連想配列)

dict_sample = {"red": 100, "green":0, "blue":200}

# key表示
for key in dict_sample.keys():
    print(key)

# valu表示
for val in dict_sample.values():
    print(val)

# key value表示
for key, val in dict_sample.items():
    print(key + ":" + str(val))
