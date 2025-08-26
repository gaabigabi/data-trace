import streamlit as st
import pandas as pd
import altair as alt
import os


def get_df(file: str) -> pd.DataFrame:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, file)

    df = pd.read_csv(data_path)

    return df

def get_years():
    return get_df('data/years.csv')['year'].unique()

def get_regions():
    return get_df('data/regions.csv').set_index('region_name')['region_years_title'].to_dict()

def get_region_df():
    df = get_df('data/region.csv')
    return df

def get_region_year_df():
    df = get_df('data/region_year.csv')
    return df


def get_bar_chart_horizontal(df, x, y, x_desc, y_desc, title, sort):
    bar_chart = alt.Chart(df).mark_bar(color='darkorange').encode(
        x=alt.X(f'{x}:Q', title=x_desc, axis=alt.Axis(
            labelExpr='datum.value'
        )),
        y=alt.Y(f'{y}:O', title=y_desc, sort=sort)
    ).properties(
        title=title
    )

    return bar_chart

def get_bar_chart_vertical(df, x, y, x_desc, y_desc, title, sort):
    bar_chart = alt.Chart(df).mark_bar(color='darkorange').encode(
        y=alt.Y(f'{x}:Q', title=x_desc, axis=alt.Axis(
            labelExpr='datum.value'
        )),
        x=alt.X(f'{y}:O', title=y_desc, sort=sort)
    ).properties(
        title=title
    )

    return bar_chart

def get_line_chart(df, x, y, color, x_desc, y_desc, color_desc, title):
    line_chart = alt.Chart(df).mark_line().encode(
        y=alt.Y(f'{y}:Q', title=x_desc, axis=alt.Axis(
            labelExpr='datum.value'
        )),
        x=alt.X(f'{x}:O', title=y_desc),
        color=alt.Color(
            f'{color}:O',
            title=color_desc,
            scale=alt.Scale(scheme='oranges')
        ),
    ).properties(
        title=title
    )

    return line_chart