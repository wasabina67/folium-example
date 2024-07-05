import folium
import pandas as pd


def main():
    data = {
        "place": [],
        "population": [],
        "latitude": [],
        "longitude": [],
    }
    df = pd.DataFrame(data)

    base_location = [43.06417, 141.34694]
    map = folium.Map(location=base_location, zoom_start=8)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=10,
            color="blue",
            fill=True,
            fill_color="blue",
        ).add_to(map)

    map.save("docs/index.html")


if __name__ == "__main__":
    main()
