import pandas as pd
import json
from make_maps import make_map, color_keys


def main():
    with open('US county base map files/cb_2020_us_county_20m.json') as f:
        US_counties = json.load(f)
    exec(open('pythonProject2/0Main.py').read())

    df_dict = {
        'Bars': pd.read_csv("pythonProject2/Bars_sumform.csv"),
        'State of Emergency': pd.read_csv("pythonProject2/emergency_sumform.csv"),
        'Gatherings': pd.read_csv("pythonProject2/Gathering_sumform.csv"),
        'Gyms': pd.read_csv("pythonProject2/Gyms_sumform.csv"),
        'Masks - Employees': pd.read_csv("pythonProject2/mask_employees_sumform.csv"),
        'Masks - Residents': pd.read_csv("pythonProject2/mask_residents_sumform.csv"),
        'Movies': pd.read_csv("pythonProject2/movie_sumform.csv"),
        'Nursing Homes - Accept COVID Positive':
            pd.read_csv("pythonProject2/medical_nursing home_covidpositive_sumform.csv"),
        'Nursing Homes - Visitors':
            pd.read_csv("pythonProject2/medical_nursing home_visitors_sumform.csv"),
        'Elective Medical Procedures':
            pd.read_csv("pythonProject2/no elective_sumform.csv"),
        'Recreation - Beaches': pd.read_csv("pythonProject2/recreation_Beach_sumform.csv"),
        'Recreation - Parks': pd.read_csv("pythonProject2/recreation_Park_sumform.csv"),
        'Restaurants': pd.read_csv("pythonProject2/Restaurants_sumform.csv"),
        'Retail': pd.read_csv("pythonProject2/Retail_sumform.csv"),
        'Spas': pd.read_csv("pythonProject2/Spas_sumform.csv"),
        'Stay at Home': pd.read_csv("pythonProject2/sthm_sumform.csv")}

    all_policy_dicts = {
        'Bars': {5: "Closed", 4: "Capacity 25", 3: "Capacity 50", 2: "Capacity 50plus",
                 1: "Outdoor", 0: "No Restriction"},
        'State of Emergency': {1: "State of Emergency", 0: "No State of Emergency"},
        'Gatherings': {4: 'Closed', 3: "Max 10 or Less", 2: "Max 11 to 100",
                       1: "Max Over 100", 0: "No Restriction"},
        'Gyms': {5: "Closed", 4: "Capacity 25", 3: "Capacity 50", 2: "Capacity 50plus",
                 1: "Outdoor", 0: "No Restriction"},
        'Masks - Employees': {2: 'Mask Mandatory', 1: 'Mask Recommended', 0: 'No Restriction'},
        'Masks - Residents': {3: 'Mask Mandatory Indoor and Out', 2: 'Mask Mandatory Indoors',
                              1: 'Mask Recommended', 0: 'No Restriction'},
        'Movies': {4: 'Closed', 3: 'Capacity 25', 2: 'Capacity 50', 1: 'Capacity 50plus',
                   0: 'No Restriction'},
        'Nursing Homes - Accept COVID Positive': {1: 'Not Accepting COVID Positive',
                                                  0: 'Accepting COVID Positive'},
        'Nursing Homes - Visitors': {1: 'Not Accepting Visitors', 0: 'Accepting visitors'},
        'Elective Medical Procedures': {1: 'No Elective Procedures', 0: 'No Restriction'},
        'Recreation - Beaches': {1: 'Beaches Closed', 0: 'Beaches Open'},
        'Recreation - Parks': {1: 'Parks Closed', 0: 'Parks Open'},
        'Restaurants': {5: "Closed", 4: "Capacity 25", 3: "Capacity 50", 2: "Capacity 50plus",
                        1: "Outdoor", 0: "No Restriction"},
        'Retail': {4: "Closed", 3: "Capacity 25", 2: "Capacity 50", 1: "Capacity 50plus",
                   0: "No Restriction"},
        'Spas': {5: "Closed", 4: "Capacity 25", 3: "Capacity 50", 2: "Capacity 50plus",
                 1: "Outdoor", 0: "No Restriction"},
        'Stay at Home': {1: 'Stay at Home', 0: 'No Restriction'}}

    for key in df_dict:
        policy_dict = all_policy_dicts[key]
        make_map(US_counties=US_counties,
                 df=df_dict[key],
                 policy_dict=policy_dict,
                 colors=color_keys[len(policy_dict)],
                 output_file='policy maps/' + key + ' Map.html',
                 title=key)


if __name__ == '__main__':
    main()
