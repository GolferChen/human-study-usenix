
import pandas as pd

def url_combine(u_1, u_2):
    return "{}@{}".format(u_1, u_2)
ORI_SAME_SPK = 'ori-same-spk'
ORI_DIFFER_SPK_SAME_GENDER = 'ori-differ-spk-same-gender'
ORI_DIFFER_SPK_DIFFER_GENDER = 'ori-differ-spk-differ-gender'
VC = 'VC'
QFA_TARGET = 'QFA_target'
QFA_SOURCE = 'QFA_source'
WHITE_TARGET = 'white-box_target'
WHITE_SOURCE = 'white-box_source'
t3_csv = 't3-unshuffle.csv'
df = pd.read_csv(t3_csv)
ground_url = list(df['ground_url'])
audio_url = list(df['audio_url'])
type_2_url = {ORI_SAME_SPK: [], ORI_DIFFER_SPK_SAME_GENDER: [], ORI_DIFFER_SPK_DIFFER_GENDER: [], VC: [], QFA_TARGET: [], QFA_SOURCE: [], WHITE_TARGET: [], WHITE_SOURCE: []}
for index, (u_1, u_2) in enumerate(zip(ground_url, audio_url)):
    url = url_combine(u_1, u_2)
    if index in range(0, 5):
        type_2_url[ORI_SAME_SPK].append(url)
    elif index in range(5, 11):
        type_2_url[ORI_DIFFER_SPK_DIFFER_GENDER].append(url)
    elif index in range(11, 15):
        type_2_url[ORI_DIFFER_SPK_SAME_GENDER].append(url)
    elif index in range(15, 25):
        type_2_url[VC].append(url)
    elif index in range(25, 44, 2):
        type_2_url[QFA_TARGET].append(url)
    elif index in range(26, 45, 2):
        type_2_url[QFA_SOURCE].append(url)
    elif index in range(45, 64, 2):
        type_2_url[WHITE_TARGET].append(url)
    elif index in range(46, 65, 2):
        type_2_url[WHITE_SOURCE].append(url)


ori_csv = "Batch_4895177_batch_results.csv"
des_csv = "Batch_4895177_batch_results_approve_reject.csv"
des_csv_2 = "Batch_4895177_batch_results_approve.csv"

df = pd.read_csv(ori_csv)
# print(df)

exclude_workers = set()
for i, (u_1, u_2) in enumerate(zip(list(df["Input.ground_url"]), (list(df["Input.audio_url"])))):
    url = url_combine(u_1, u_2)
    if url in type_2_url[ORI_DIFFER_SPK_DIFFER_GENDER]:
        if 'Different' not in list(df["Answer.experiment3-identify-speaker.label"])[i]:
            exclude_workers.add(list(df["WorkerId"])[i])
    
            # print(i, list(df["Answer.experiment3-identify-speaker.label"])[i])

print(exclude_workers, len(exclude_workers))
# print(len(set(list(df["WorkerId"]))))

# df_2 = copy.deepcopy(df)

drop_index = []
for index, row in df.iterrows():
    if row["WorkerId"] not in exclude_workers:
        # row['Approve'] = "x"
        df.loc[index, 'Approve'] = "x"
        # df_2.loc[index, 'Approve'] = "x"
    else:
         # row['Reject'] = 'Failed to pass our concentration test. The answers are randomly choosen.'
        df.loc[index, 'Reject'] = 'Failed to pass our concentration test. The answers are randomly choosen.'
        # df_2.drop(index)
        drop_index.append(index)

df_2 = df.drop(drop_index)

print(df)
print(df_2)

df.to_csv(des_csv, index=False)
df_2.to_csv(des_csv_2, index=False)

print(len(set(df['WorkerId'])), len(set(df_2['WorkerId'])))