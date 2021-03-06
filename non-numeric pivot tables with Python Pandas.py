import pandas as pd

feedbck = pd.read_csv('feedback.csv')

pivot_table = feedbck.pivot_table(index='Id',
                                     columns='Que', 
                                     values='answer_text',
                                     aggfunc=lambda x: ','.join(str(v) for v in x))

pivot_table


pivot_table.to_csv('output.csv')
