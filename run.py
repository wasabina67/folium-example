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

    _ = folium.Map(location=[43.06417, 141.34694], zoom_start=8)


if __name__ == "__main__":
    main()
