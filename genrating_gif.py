import os
import glob
import xarray as xr 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

nc_files = glob.glob("*.nc")
if not nc_files: 
    raise FileNotFoundError("No NetCDF file found in the repository! Did you upload a wrong file?")

target_file = nc_files[0]
print(f"Successfully fetched and processing: {target_file}")
ds = xr.open_dataset(target_file)
fig, ax = plt.subplots(figsize=(8,6))

def update_map(frame_idx):
    ax.clear()
    daily_slice = ds['RAINFALL'].isel(TIME=frame_idx)
    raw_date = ds['TIME'].isel(TIME=frame_idx).values
    
  
    clean_date = pd.to_datetime(raw_date).strftime('%B %d')
    
    im = daily_slice.plot(ax=ax, cmap="Reds", add_colorbar=False, vmin=0, vmax=50)
    ax.set_title(f"Rainfall Timeline: {clean_date}")
    ax.axis('off')
    return [im]


spatial_animation = animation.FuncAnimation(fig, update_map, frames=365, interval=100)

spatial_animation.save("WOOOOO_animation.gif", writer='pillow')
print("GIF Generated Successfully !!!!!")
