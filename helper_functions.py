# geospatial help functions
import geopandas as gpd
import matplotlib.pyplot as plt


def show_overlaps(data_temp, id_col):    
    # checks and plots which areas overlap
    
    overlaps = []
    for index, row in data_temp.iterrows():
        data_temp1 = data_temp.loc[data_temp[id_col] != row[id_col]] # grab all rows, != this row
        temp_list = data_temp1[data_temp1.geometry.overlaps(row.geometry)][id_col].tolist() # grab rows with overlap
        # get index
        if temp_list != []:
            overlaps += temp_list

    data_overlaps = data_temp.copy()
    data_overlaps = data_overlaps.set_index(id_col)
    overlap_areas = data_overlaps.loc[overlaps]
    
    ax = data_temp.plot(figsize=size, linewidth=lw, edgecolor="k", color="whitesmoke")
    if len(overlap_areas) > 0:
        overlap_areas.plot(figsize=size, linewidth=lw, edgecolor="k", color="red", ax=ax)
    print("This many rows still overlap:", overlap_areas.shape[0])


def boundary_cut(df_list, cut_df):
    # cuts a list of dfs out of the input df
    for df in df_list:
        cut_df = gpd.overlay(cut_df, df, how="difference")
        return cut_df

def plot_bounds(gdf):
    # quick plot with standard parameters
    gdf.plot(figsize=(24, 20), color="whitesmoke", edgecolor="k", linewidth=0.5)

