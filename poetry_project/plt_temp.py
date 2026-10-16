import requests
import matplotlib
matplotlib.use("Agg")          # чтобы сохранять PNG без открытия окна
import matplotlib.pyplot as plt
import pandas as pd


def fetch_hourly_temperature(latitude: float, longitude: float, timeout: int = 10):
    """Запрос к Open-Meteo. Возвращает (hours, temps) — первые 24 значения."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": latitude, "longitude": longitude, "hourly": "temperature_2m"}

    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()          # ошибка HTTP не маскируется под JSON-ошибку
    data = response.json()

    hours = data["hourly"]["time"][:24]
    temps = data["hourly"]["temperature_2m"][:24]
    return hours, temps


def build_dataframe(hours, temps) -> pd.DataFrame:
    """Чистое преобразование: списки -> DataFrame, сортировка по времени.
    Сетевых вызовов не делает — удобно тестировать."""
    df = pd.DataFrame({"time": pd.to_datetime(hours), "temperature_c": temps})
    df = df.sort_values("time").reset_index(drop=True)
    return df


def save_plot(df: pd.DataFrame, path: str = "temperature_24h.png") -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["temperature_c"], marker="o")
    plt.xticks(rotation=45)
    plt.title("Температура в Москве (24 часа)")
    plt.xlabel("Время")
    plt.ylabel("°C")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def main():
    hours, temps = fetch_hourly_temperature(55.75, 37.61, timeout=10)
    df = build_dataframe(hours, temps)
    df.to_csv("temperature_24h.csv", index=False)
    save_plot(df, "temperature_24h.png")
    print("Сохранено в temperature_24h.csv и temperature_24h.png")


if __name__ == "__main__":
    main()