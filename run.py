import folium
import pandas as pd


def main():
    data = {
        "place": [
            "旭川市",
            "札幌市北区",
            "札幌市東区",
            "函館市",
            "札幌市中央区",
            "札幌市豊平区",
        ],
        "population": [333294, 287576, 260414, 261231, 255313, 213790],
        "latitude": [43.7706, 43.1155, 43.0797, 41.7687, 43.0555, 43.0306],
        "longitude": [142.3649, 141.3402, 141.3534, 140.7288, 141.3400, 141.3664],
    }
    df = pd.DataFrame(data)
    # df = pd.read_csv("data.csv")

    base_location = [43.0618, 141.3545]
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
