
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

results = dict()
SAME = 'same'
DIFFER = 'diff'
NOT_SURE = 'not sure'
results[ORI_SAME_SPK] = {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[ORI_DIFFER_SPK_DIFFER_GENDER] = {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[ORI_DIFFER_SPK_SAME_GENDER] = {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[VC]= {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[QFA_TARGET]= {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[QFA_SOURCE]= {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[WHITE_TARGET]= {SAME: 0, DIFFER: 0, NOT_SURE: 0}
results[WHITE_SOURCE]= {SAME: 0, DIFFER: 0, NOT_SURE: 0}

ori_csv = "Batch_4895177_batch_results_approve.csv"
df = pd.read_csv(ori_csv)
ground_urls = list(df['Input.ground_url'])
audio_urls = list(df['Input.audio_url'])
answers = audio_url = list(df['Answer.experiment3-identify-speaker.label'])
for index, (u_1, u_2, answer) in enumerate(zip(ground_urls, audio_urls, answers)):

    url = url_combine(u_1, u_2)
    if url in type_2_url[ORI_SAME_SPK]:
        des_1 = ORI_SAME_SPK
    elif url in type_2_url[ORI_DIFFER_SPK_DIFFER_GENDER]:
        des_1 = ORI_DIFFER_SPK_DIFFER_GENDER
    elif url in type_2_url[ORI_DIFFER_SPK_SAME_GENDER]:
        des_1 = ORI_DIFFER_SPK_SAME_GENDER
    elif url in type_2_url[VC]:
        des_1 = VC
    elif url in type_2_url[QFA_TARGET]:
        des_1 = QFA_TARGET
    elif url in type_2_url[QFA_SOURCE]:
        des_1 = QFA_SOURCE
    elif url in type_2_url[WHITE_TARGET]:
        des_1 = WHITE_TARGET
    elif url in type_2_url[WHITE_SOURCE]:
        des_1 = WHITE_SOURCE
    else:
        raise NotImplementedError
    
    if 'Same' in answer:
        des_2 = SAME
    elif 'Different' in answer:
        des_2 = DIFFER
    elif 'Not Sure' in answer:
        des_2 = NOT_SURE
    else:
        raise NotImplementedError
    
    results[des_1][des_2] = results[des_1][des_2] + 1

for k, v in results.items():
    tol  = v["same"] + v["diff"] + v["not sure"]
    # print(k, tol,  v['same'], v['diff'], v['not sure'], v['same'] * 100 / tol, v['diff'] * 100 / tol, v['not sure'] * 100 / tol)
    print(k, round(v['same'] * 100 / tol, 2), round(v['diff'] * 100 / tol, 2), round(v['not sure'] * 100 / tol, 2))