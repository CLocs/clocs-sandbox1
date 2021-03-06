import os
import pandas as pd


def csv_daily_to_events(daily_local_filepath,
                        out_filename,
                        event_cats):
    # Load CSV
    curr_path = os.path.dirname(__file__)
    abs_filepath = os.path.join(curr_path, daily_local_filepath)
    df_daily = pd.read_csv(abs_filepath, header=[0, 1], index_col=0)  # index_col=[0, 1]
    # Convert daily to event
    event_cols = ['Participant', 'Date', 'Activity', 'Count', 'Units', 'Category', 'Normalized Amount']
    df_event = pd.DataFrame(columns=event_cols)
    participant = 'Coco'
    for ind, d_row in df_daily.iterrows():
        for cat in event_cats:
            cat_val = d_row[participant][cat]
            # New row for each category (if work was done)
            if cat_val:
                e_row = pd.DataFrame([{
                    'Participant': 'Colin',
                    'Date': ind,
                    'Category': cat,
                    'Normalized Amount': cat_val
                }])
                df_event = df_event.append(e_row, ignore_index='True')
    # Clean dataframe
    df_event = df_event.fillna(0)
    df_event = df_event[event_cols]  # order like I want
    # Dump file
    out_filedir = os.path.dirname(abs_filepath)
    out_filepath = os.path.join(out_filedir, out_filename)
    df_event.to_csv(out_filepath, index=False)
    logstr = 'Conversion finished! Writing file {}'.format(out_filepath)
    print(logstr)


if __name__ == '__main__':
    csv_daily_to_events('data/2019 Workout Log - Logs Daily.csv',
                        '2019_workout_logs_events.csv',
                        ['Break', 'Climb', 'Abs', 'Run', 'Bike', 'Lift'])
    csv_daily_to_events('data/2018 Workout Log for Coco and Nico - Logs Daily.csv',
                        '2018_workout_logs_events.csv',
                        ['Abs', 'Run', 'Bike', 'Lift'])
    csv_daily_to_events('data/2017 Workout Log for Coco and Nico - Logs Daily.csv',
                        '2017_workout_logs_events.csv',
                        ['Abs', 'Run', 'Bike', 'Lift'])

