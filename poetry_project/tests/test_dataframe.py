import pandas as pd
from plt_temp import build_dataframe


def test_build_dataframe_columns_rows_sorted():
    # Списки заведомо в неправильном порядке — проверим сортировку
    hours = [
        "2024-01-01T03:00",
        "2024-01-01T01:00",
        "2024-01-01T02:00",
    ]
    temps = [3.0, 1.0, 2.0]

    df = build_dataframe(hours, temps)

    # 1) названия столбцов
    assert list(df.columns) == ["time", "temperature_c"]

    # 2) количество строк
    assert len(df) == 3

    # 3) сортировка по времени
    assert df["time"].is_monotonic_increasing

    # 4) температура соответствует времени после сортировки
    assert df.loc[0, "temperature_c"] == 1.0   # 01:00
    assert df.loc[1, "temperature_c"] == 2.0   # 02:00
    assert df.loc[2, "temperature_c"] == 3.0   # 03:00