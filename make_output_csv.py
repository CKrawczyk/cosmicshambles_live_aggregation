import pandas
import os.path
import sys
from collections import OrderedDict
from panoptes_client import Panoptes, Subject, User
from tqdm import tqdm

client = Panoptes.connect()  # login info is in sys env

reduction_file = sys.argv[1]
folder = os.path.dirname(reduction_file)
threshold = float(sys.argv[2])
reductions = pandas.read_csv(reduction_file)

user_cache = {}  # cache user look ups to save time

output_data = []

nan = None  # for correct string conversion of non-logged in users

talk_url_base = 'https://www.zooniverse.org/projects/dwright04/supernova-hunters/talk/subjects/{0}'
qub_url = 'https://star.pst.qub.ac.uk/sne/ps13pi/psdb/candidate/{0}'

for _, reduction in tqdm(reductions.iterrows(), total=reductions.shape[0]):
    votes_yes = reduction['data.yes']
    if pandas.isnull(votes_yes):
        votes_yes = 0
    votes_no = reduction['data.no']
    if pandas.isnull(votes_no):
        votes_no = 0
    votes_total = votes_yes + votes_no
    votes_fraction = votes_yes / votes_total
    if votes_fraction > threshold:
        subject = Subject.find(reduction.subject_id)
        object_id = subject.metadata['#object_id'][1:]  # strip leading "#" from id number
        users = []
        for user_id in eval(reduction['data.user_ids_yes']):
            if user_id is not None:
                user_id = int(user_id)
                if user_id in user_cache:
                    user = user_cache[user_id]
                else:
                    user = User.find(user_id)
                    user_cache[user_id] = user
                if (user.credited_name is not None) and (len(user.credited_name) > 0):
                    name = user.credited_name
                elif (user.display_name is not None) and (len(user.display_name) > 0):
                    name = user.display_name
                else:
                    name = user.login
                # filter out full email addresses
                name = name.split('@')[0]
                if len(name) > 0:
                    users.append(name)
        row = OrderedDict([
            ('subject_id', reduction.subject_id),
            ('object_id', object_id),
            ('votes_yes', votes_yes),
            ('votes_no', votes_no),
            ('votes_fraction_yes', votes_fraction),
            ('votes_total', votes_total),
            ('volunteers_yes', users),
            ('talk_link', talk_url_base.format(reduction.subject_id)),
            ('qub_url', qub_url.format(object_id))
        ])
        output_data.append(row)

df = pandas.DataFrame(output_data)
df = df.sort_values(by=['votes_fraction_yes', 'votes_total'], ascending=False)
df.to_csv(os.path.join(folder, 'candidates.csv'), index=False)
