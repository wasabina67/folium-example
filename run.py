import folium
import pandas as pd


def main():
    data = {
        "place": [],
        "population": [],
        "latitude": [],
        "longitude": [],
    }
    _ = pd.DataFrame(data)

    base_location = [43.06417, 141.34694]
    _ = folium.Map(location=base_location, zoom_start=8)


if __name__ == "__main__":
    main()
