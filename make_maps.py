import plotly.graph_objects as go


def make_map(US_counties, df, policy_dict, colors, output_file, title):
    df['GeoID'] = df['GeoID'].astype(str).str.zfill(5)
    
    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Week of ",
            "visible": True,
            "xanchor": "right"
        },
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": []
    }

    frames = []
    for column in df.columns[2:]:
        temp_data = []
        for i, policy in enumerate(list(policy_dict.keys())):
            dfp = df[df[column] == policy]
            geoid_list = dfp['GeoID'].tolist()
            geo_filter = {'type': 'FeatureCollection',
                          'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:EPSG::4269'}},
                          'features': []}
            features = []
            j = 0
            while len(geoid_list) > 0 and j < len(US_counties['features']):
                # example feature properties:
                # {'STATEFP': '01', 'COUNTYFP': '061', 'COUNTYNS': '00161556', 'AFFGEOID': '0500000US01061',
                # 'GEOID': '01061', 'NAME': 'Geneva', 'NAMELSAD': 'Geneva County', 'STUSPS': 'AL', 'STATE_NAME':
                # 'Alabama', 'LSAD': '06', 'ALAND': 1487908432, 'AWATER': 11567409}
                current_feature = US_counties["features"][j]
                current_geoid = current_feature['properties']['GEOID']
                if current_geoid in geoid_list:
                    new_feature = {'type': 'Feature',
                                   'properties': {'GEOID': current_geoid},
                                   'geometry': current_feature['geometry']}
                    features.append(new_feature)
                    geoid_list.remove(current_geoid)
                j += 1
            geo_filter['features'] = features

            temp_data.append(go.Choropleth(
                locations=dfp['GeoID'],
                z=[i, ] * len(dfp),
                geojson=geo_filter,
                featureidkey='properties.GEOID',
                colorscale=colors[i],
                locationmode='geojson-id',
                name=policy_dict[policy],
                showscale=False,
                showlegend=True))
        frames.append(go.Frame(data=temp_data, name=column))

        slider_step = {"args": [[column],
                                {"frame": {"duration": 300, "redraw": True},
                                 "mode": "immediate",
                                 "transition": {"duration": 300}}],
                       "label": column,
                       "method": "animate"}
        sliders_dict["steps"].append(slider_step)

    buttons = [{'label': 'Play',
                'method': 'animate',
                'args': [None,
                         {"fromcurrent": True,
                          "redraw": True}]}]

    updatemenus = [{"active": 0,
                    "buttons": buttons,
                    'type': 'buttons',
                    "pad": {"r": 10, "t": 75},
                    "showactive": False,
                    "x": 0.1,
                    "y": 0}]

    fig = go.Figure(data=frames[0]['data'],
                    layout=dict(updatemenus=updatemenus,
                                sliders=[sliders_dict]),
                    frames=frames)

    fig.update_layout(title=title,
                      title_x=0.5,
                      title_font_size=24,
                      geo_scope='usa')

    fig.write_html(output_file, include_plotlyjs='cdn')


# Some definitions
all_colors = {
    0: ((0, '#362e70'), (1, '#362e70')),  # purple
    1: ((0, '#3964a6'), (1, '#3964a6')),  # blue
    2: ((0, '#1caab7'), (1, '#1caab7')),  # teal
    3: ((0, '#65bf76'), (1, '#65bf76')),  # cool green
    4: ((0, '#b5d757'), (1, '#b5d757')),  # warm green
    5: ((0, '#ffea69'), (1, '#ffea69')),  # yellow
    6: ((0, '#ffc253'), (1, '#ffc253')),  # orange
    7: ((0, '#ff9d53'), (1, '#ff9d53'))}  # red

color_keys = {2: [all_colors[7],
                  all_colors[0]],

              3: [all_colors[7],
                  all_colors[3],
                  all_colors[0]],

              4: [all_colors[7],
                  all_colors[5],
                  all_colors[2],
                  all_colors[0]],

              5: [all_colors[7],
                  all_colors[5],
                  all_colors[4],
                  all_colors[2],
                  all_colors[0]],

              6: [all_colors[7],
                  all_colors[6],
                  all_colors[5],
                  all_colors[3],
                  all_colors[2],
                  all_colors[0]],

              7: [all_colors[7],
                  all_colors[6],
                  all_colors[5],
                  all_colors[4],
                  all_colors[3],
                  all_colors[2],
                  all_colors[0]],

              8: [all_colors[7],
                  all_colors[6],
                  all_colors[5],
                  all_colors[4],
                  all_colors[3],
                  all_colors[2],
                  all_colors[1],
                  all_colors[0]]}
