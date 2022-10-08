

import numpy as np
import pandas as pd
import os

url_predix = "https://golferchen.github.io/human-study-usenix"
info = dict()
info["ground_url"] = []
info["audio_url"] = []

spk_ids = ['chengk', 'zhezhao', 'zhangyedi', 'tanhuiyu', 'cenwc']

# ori same spk (5)
for text, spk_id in zip(range(5), spk_ids):
    text = str(text)
    text = 'text=' + text
    root = os.path.join('clean', text, spk_id)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    names = names[:2]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_id, names[0])
    info["ground_url"].append(url)
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_id, names[1])
    info["audio_url"].append(url)

# ori differ spk differ gender (3)
pairs = [['zhangyedi', 'cenwc'], ['zhezhao', 'tanhuiyu'], ['tanhuiyu', 'chengk']]
for text, pair in zip(range(7, 10), pairs):
    text = str(text)
    text = 'text=' + text
    spk_1, spk_2 = pair

    root = os.path.join('clean', text, spk_1)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_1, name)
    info["ground_url"].append(url)

    root = os.path.join('clean', text, spk_2)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_2, name)
    info["audio_url"].append(url)

# ori differ spk differ gender (3)--> 6
pairs = [['zhangyedi', 'chengk'], ['zhezhao', 'zhangyedi'], ['tanhuiyu', 'cenwc']]
for text, pair in zip(range(7, 10), pairs):
    text = str(text)
    text = 'text=' + text
    spk_1, spk_2 = pair

    root = os.path.join('clean', text, spk_1)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_1, name)
    info["ground_url"].append(url)

    root = os.path.join('clean', text, spk_2)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_2, name)
    info["audio_url"].append(url)

# ori differ spk same gender (4)
pairs = [['zhangyedi', 'tanhuiyu'], ['zhezhao', 'chengk'], ['zhezhao', 'cenwc'], ['cenwc', 'chengk']]
for text, pair in zip(range(3, 7), pairs):
    text = str(text)
    text = 'text=' + text
    spk_1, spk_2 = pair

    root = os.path.join('clean', text, spk_1)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_1, name)
    info["ground_url"].append(url)

    root = os.path.join('clean', text, spk_2)
    names = sorted(os.listdir(root))
    np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_2, name)
    info["audio_url"].append(url)

# VC (10)
texts = range(10)
text_2_spk_id = dict(zip(texts, ['cenwc', 'chengk', 'tanhuiyu', 'tanhuiyu', 'chengk', 'chengk', 'tanhuiyu', 'zhezhao', 'zhezhao', 'zhezhao']))
for text in texts:
    spk_id = text_2_spk_id[text]
    text = str(text)
    text = 'text=' + text
    spk_dir = os.path.join('VC', text, spk_id)
    name = os.listdir(spk_dir)[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'VC', text, spk_id, name)
    info["audio_url"].append(url)

    spk_dir = os.path.join('clean', text, spk_id)
    names = sorted(os.listdir(spk_dir))
    # np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_id, name)
    info["ground_url"].append(url)

# QFA2SR (10)
texts = range(10)
text_2_spk_id = dict(zip(texts, ['cenwc', 'chengk', 'tanhuiyu', 'tanhuiyu', 'chengk', 'chengk', 'tanhuiyu', 'zhezhao', 'zhezhao', 'zhezhao']))
for text in texts:
    spk_id = text_2_spk_id[text]
    text = str(text)
    text = 'text=' + text
    spk_dir = os.path.join('QFA2SR', text, spk_id)
    name = os.listdir(spk_dir)[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'QFA2SR', text, spk_id, name)
    info["audio_url"].append(url)
    info["audio_url"].append(url)
    src_spk = name.split('-')[0]
    src_name = name

    spk_dir = os.path.join('clean', text, spk_id)
    names = sorted(os.listdir(spk_dir))
    # np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_id, name)
    info["ground_url"].append(url)

    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, src_spk, src_name)
    info["ground_url"].append(url)

# White-box (10)
texts = range(10)
text_2_spk_id = dict(zip(texts, ['cenwc', 'chengk', 'tanhuiyu', 'tanhuiyu', 'chengk', 'chengk', 'tanhuiyu', 'zhezhao', 'zhezhao', 'zhezhao']))
for text in texts:
    spk_id = text_2_spk_id[text]
    text = str(text)
    text = 'text=' + text
    spk_dir = os.path.join('white-box', text, spk_id)
    name = os.listdir(spk_dir)[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'white-box', text, spk_id, name)
    info["audio_url"].append(url)
    info["audio_url"].append(url)
    src_spk = name.split('-')[0]
    src_name = name

    spk_dir = os.path.join('clean', text, spk_id)
    names = sorted(os.listdir(spk_dir))
    # np.random.shuffle(names)
    name = names[0]
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, spk_id, name)
    info["ground_url"].append(url)
    
    url = "{}/{}/{}/{}/{}".format(url_predix, 'clean', text, src_spk, src_name)
    info["ground_url"].append(url)


df = pd.DataFrame(info)
df.to_csv("t3-unshuffle.csv", index=False)
print(df)
df = df.sample(frac=1)
print(df)
df.to_csv("t3.csv", index=False)