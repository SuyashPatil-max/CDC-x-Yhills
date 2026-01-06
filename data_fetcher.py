import os
import requests
import pandas as pd
from tqdm import tqdm  

MAPBOX_TOKEN = "pk.eyJ1Ijoic3V5YXNocGF0aWwiLCJhIjoiY21qamdyMXRiMHNndDNkc2NocTNjbnhpZiJ9.DVExH2CXjHdubw9Xf5mfYQ"
EXCEL_PATH = "test2.xlsx"
OUTPUT_FOLDER = "mapbox_images"
STYLE_ID = "mapbox/satellite-v9"
ZOOM = 20
WIDTH = 512
HEIGHT = 512
ROW_LIMIT = None

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

df = pd.read_excel(EXCEL_PATH)
required_cols = {"lat", "long"}
missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing columns in Excel: {missing}")

if ROW_LIMIT is not None:
    df = df.head(ROW_LIMIT)

base_url = (
    "https://api.mapbox.com/styles/v1/{style_id}/static/"
    "{lon},{lat},{zoom}/{width}x{height}?access_token={token}"
)

for idx, row in tqdm(df.iterrows(), total=len(df), desc="Downloading images"):
    lat = float(row["lat"])
    lon = float(row["long"])
    house_id = row["id"] if "id" in df.columns else idx

    url = base_url.format(
        style_id=STYLE_ID,
        lon=lon,
        lat=lat,
        zoom=ZOOM,
        width=WIDTH,
        height=HEIGHT,
        token=MAPBOX_TOKEN,
    )

    filename = f"house_{house_id}_lat{lat:.5f}_lon{lon:.5f}_z{ZOOM}.png"
    filepath = os.path.join(OUTPUT_FOLDER, filename)

    resp = requests.get(url)
    if resp.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(resp.content)

