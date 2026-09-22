# Experiment 9 — Matplotlib: Charts, Pie, Violin, Scatter, Area, Contour & Quiver, Histogram, Bar, Mesh Grid

Solutions for S.Y.B.Tech **Python Programming Laboratory — Experiment No. 9**.

## Folder Structure

```
matplotlib_lab_experiment9/
├── task1_tips_dashboard.py              # Task 1: 2x2 Tips dashboard (bar, pie, hist, violin)
├── task2_trend_correlation_explorer.py  # Task 2: Flights trend+area, MPG scatter (colour=year)
├── task3_flights_contour.py             # Task 3: Flights Year x Month filled contour
├── task4_saddle_contour_quiver.py       # Task 4: Z = X^2 - Y^2 contour + gradient quiver
├── datasets/                            # all CSV datasets used in this lab
│   ├── flights.csv
│   ├── glucose_readings.csv
│   ├── mpg.csv
│   └── tips.csv
├── outputs/                             # all generated PNG output images
├── ai_case_study/
│   ├── case_study_all_tasks.py          # Part A (Tasks 1-3) + Part B (Tasks 4-6)
│   └── final_task_complete_program.py   # Final Task: complete program (9 steps)
├── additional_questions/                # q1 ... q13 (one file per question)
├── practice_tasks/                      # practice1 ... practice6
└── README.md
```

## Requirements

- Python 3.10+
- `matplotlib`, `numpy`, `pandas` (already listed in the project `requirements.txt`)

```bash
pip install -r requirements.txt
```

Each script saves its `.png` chart(s) into `matplotlib_lab_experiment9/outputs/`;
`plt.show()` opens an interactive window when a display is available.

## Running

Each file is a standalone script:

```bash
python matplotlib_lab_experiment9/task1_tips_dashboard.py
python matplotlib_lab_experiment9/task2_trend_correlation_explorer.py
python matplotlib_lab_experiment9/task3_flights_contour.py
python matplotlib_lab_experiment9/task4_saddle_contour_quiver.py
python matplotlib_lab_experiment9/ai_case_study/case_study_all_tasks.py
python matplotlib_lab_experiment9/ai_case_study/final_task_complete_program.py
python matplotlib_lab_experiment9/additional_questions/q6_read_from_csv.py
python matplotlib_lab_experiment9/practice_tasks/practice6_class_dashboard.py
```

Notes:
- Tasks 1-3 load the **Tips**, **Flights** and **Auto MPG** datasets from local files
  in `matplotlib_lab_experiment9/datasets/` (no internet needed).
- q6 also reads `glucose_readings.csv` from `matplotlib_lab_experiment9/datasets/`.
- Scripts use the `Agg` backend and also save `.png` outputs via `plt.savefig()`;
  `plt.show()` opens a window when a display is available.
- Interactive questions (q1, q7) fall back to sample data when run non-interactively.

## Post-Lab Answers (brief)

**Conceptual**

1. **Figure vs Axes** — A `Figure` is the whole canvas/window (everything: title bar,
   all subplots, colorbars). An `Axes` is one individual plot area with its own x/y
   axis, ticks, labels and artists. A figure can hold many axes (`plt.subplots(2, 2)`
   → 1 figure, 4 axes).
2. **Histogram vs bar chart** — Use a *histogram* for continuous numeric data grouped
   into bins (e.g. total-bill distribution); use a *bar chart* for discrete
   categories compared directly (e.g. average tip per day). Histogram bars touch
   (continuous scale); bar-chart bars have gaps (categories).
3. **`np.meshgrid()`** — Turns two 1-D coordinate arrays into 2-D coordinate
   matrices `X`, `Y` covering the whole grid. Contour/quiver functions need `Z`
   evaluated *at every grid point*, which requires these coordinate matrices.
4. **`alpha`** — Sets transparency (0 = invisible, 1 = opaque). Most useful in
   overlapping plots: overlapping histograms, scatter clouds, filled areas.
5. **Violin vs box plot** — A violin adds a rotated kernel-density outline, showing
   the full distribution shape (skewness, multimodality, gaps) that a box plot's
   quartile summary hides.

**Application**

1. **Colour = model year in the MPG scatter** — Points of the same horsepower but
   different eras can be told apart, revealing that newer cars achieve higher mpg at
   equal horsepower — a time trend a plain single-colour scatter hides.
2. **Quiver of the gradient** — A contour shows *where* values are equal/high/low,
   but the quiver arrows show *direction and rate of steepest change* at each point,
   making ascent/descent directions (and the saddle point) immediately visible.
3. **`fill_between` + threshold line** — Shading shows *when* and *how long/how much*
   readings exceeded the threshold directly on the timeline — duration, severity and
   pattern — whereas printing raw values gives no temporal context.
