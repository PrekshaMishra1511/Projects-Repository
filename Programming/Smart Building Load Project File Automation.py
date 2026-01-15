import os
import pandas as pd

seconds_per_day = 86400
params = list(param_map.keys())

for file in os.listdir(csv_folder):

    if file.endswith(".csv") and len(file.split("_")[0]) == 4:

        code = file.split("_")[0]
        A, B, C, D = code[0], code[1], code[2], code[3]

        material = materials.get(A, "unknown")
        layer    = layers.get(B, "w")
        month    = months.get(C + D, "")

        file_base = f"{material}_{layer}_{month}".replace(" ", "_")

        print(f"Processing: {file_base}")

        file_path = os.path.join(csv_folder, file)
        df = pd.read_csv(file_path)

        if "time" in df.columns:
            df["Time (seconds)"] = df["time"]
        else:
            df["Time (seconds)"] = df.iloc[:, 0]

        save_folder = os.path.join(plot_root, file_base)
        os.makedirs(save_folder, exist_ok=True)

        plot_graph(
            df,
            ["Tasb.y", "Tsol.y", "Multilayer roof.port a.T", "Multilayer roof.port b.T"],
            ["Ambient Temp", "Sol-air Temp", "Outer Roof Surface", "Inner Roof Surface"],
            "Temperature (°C)",
            "Temperature Variations",
            os.path.join(save_folder, f"temperature_{file_base}.png")
        )

        plot_graph(
            df,
            ["Radiation.y[1]"],
            ["Radiation"],
            "Radiation (W/m²)",
            "Radiation Over Time",
            os.path.join(save_folder, f"radiation_{file_base}.png")
        )

        plot_graph(
            df,
            ["heatfloksensor.Qflow"],
            ["Heat Flow"],
            "Heat Flow (W)",
            "Heat Flow Over Time",
            os.path.join(save_folder, f"heatflow_{file_base}.png")
        )

        peak_data = []

        for day in range(7):

            day_start = day * seconds_per_day
            day_end   = (day + 1) * seconds_per_day

            day_df = df[
                (df["Time (seconds)"] >= day_start) &
                (df["Time (seconds)"] <  day_end)
            ].copy()

            day_df["Time (hours)"] = ((day_df["Time (seconds)"] - day_start) / 3600) + 6

            row = {"Day": f"Day {day + 1}"}

            for param in params:
                if param in day_df.columns:
                    peak_idx  = day_df[param].idxmax()
                    peak_val  = round(day_df.loc[peak_idx, param], 2)
                    peak_time = round(day_df.loc[peak_idx, "Time (hours)"], 2)

                    label = param_map[param]
                    row[label] = f"{peak_val} at {peak_time}"

            peak_data.append(row)

        peak_df = pd.DataFrame(peak_data)

        ordered_cols = ["Day"] + list(param_map.values())
        peak_df = peak_df[ordered_cols]

        peak_save_path = os.path.join(peak_root, f"Peaks_{file_base}.csv")
        peak_df.to_csv(peak_save_path, index=False)
