import streamlit as st

from analysis.acute_care_in_psychiatry import analysis


st.title('Akutní psychiatrická péče')

selected = st.selectbox('Výběr kategorie', ['Počet hospitalizací v letech a v krajích'])


if selected == 'Počet hospitalizací v letech a v krajích':
    st.header('Počet hospitalizací v letech a v krajích')
    st.divider()
    df_region= analysis.get_region_df()
    bar_region = analysis.get_bar_chart_horizontal(df_region, x='count', y='region_name', x_desc='Celkový počet', y_desc='Kraj', title='Celkový počet hospitalizací podle krajů v letech 2010 až 2023', sort='-x')

    st.altair_chart(bar_region, use_container_width=True)


    df_region_year = analysis.get_region_year_df()

    # Select years
    years = analysis.get_years()
    year = st.selectbox('Rok', years)

    df_region_by_year = df_region_year[df_region_year['year'] == year]
    bar_region_by_year = analysis.get_bar_chart_horizontal(df_region_by_year, x='count', y='region_name', x_desc='Celkový počet', y_desc='Kraj', title=f'Celkový počet hospitalizací podle krajů v roce {year}', sort='-x')
    st.altair_chart(bar_region_by_year, use_container_width=True)

    # Select regions
    regions = analysis.get_regions()
    region = st.selectbox('Kraj', regions)

    df_year_by_region = df_region_year[df_region_year['region_name'] == region]
    bar_year_by_region = analysis.get_bar_chart_vertical(df_year_by_region, x='count', y='year', x_desc='Celkový počet', y_desc='Kraj', title=f'Celkový počet hospitalizací v letech {regions[region]}', sort='x')
    st.altair_chart(bar_year_by_region, use_container_width=True)

    compare_left, compare_right = st.columns(2)
    with compare_left:
        selected_left = st.selectbox('Kraj č. 1', regions)

    with compare_right:
        selected_right = st.selectbox('Kraj č. 2', [r for r in regions if r != selected_left])

    line_region_year = analysis.get_line_chart(
        df_region_year[df_region_year['region_name'].isin([selected_left, selected_right])],
        x='year',
        y='count',
        color='region_name',
        x_desc='Počet hospitalizací',
        y_desc='Rok',
        color_desc='Kraj',
        title=f'Porovnání krajů ({selected_left} a {selected_right})'
    )

    st.altair_chart(line_region_year, use_container_width=True)
    # st.dataframe(df_region_year, hide_index=True)
