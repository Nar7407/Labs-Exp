BANNER = "=" * 70


def print_answer(no, question, lines):
    print(BANNER)
    print(f"Q{no}. {question}")
    print("-" * 70)
    for line in lines:
        print(line)
    print()


def main():
    print("EXPERIMENT 10 - SEABORN: POST-LAB ANSWERS\n")

    print_answer(1, "What is the key advantage of Seaborn over raw "
        "Matplotlib when working with Pandas DataFrames?", [
        "Seaborn's API is DataFrame-aware: you pass the DataFrame plus",
        "column names (data=df, x=\"col1\", y=\"col2\") instead of manually",
        "extracting lists/arrays. On top of that it automatically computes",
        "and draws statistics (means with CI bands, quartiles, regression",
        "fits, KDEs, aggregations) and applies polished statistical default",
        "styles - so a plot that takes many lines in Matplotlib takes one",
        "line in Seaborn, directly from the DataFrame.",
    ])

    print_answer(2, "Differentiate between a stripplot and a swarmplot. "
        "Why might one be preferred over the other for a large dataset?", [
        "stripplot: plots individual points with random jitter along the",
        "    category axis, so points may still overlap; it is fast.",
        "swarmplot: uses a deterministic algorithm to place points so that",
        "    NO two points overlap - the width of the swarm locally shows",
        "    the density of the data; it is computationally heavier.",
        "For a LARGE dataset, stripplot is preferred: swarmplot's",
        "non-overlap requirement forces the swarm to become extremely",
        "wide (or the points tiny) as n grows, and the layout algorithm",
        "becomes slow. Stripplot stays fast and readable, especially when",
        "combined with alpha transparency or a box/violin overlay.",
    ])

    print_answer(3, "What is the difference between an axes-level function "
        "(e.g. sns.boxplot) and a figure-level function (e.g. sns.catplot)?", [
        "Axes-level (boxplot, violinplot, scatterplot, histplot, heatmap...):",
        "    draws onto a SINGLE matplotlib Axes you may already have",
        "    (ax=... parameter); it does not create a figure, so it can be",
        "    combined freely with other plots in subplots.",
        "Figure-level (catplot, relplot, displot, pairplot, jointplot,",
        "    FacetGrid): creates and manages its OWN Figure and possibly a",
        "    whole GRID of axes (via row=/col= faceting). It returns a",
        "    FacetGrid object, and figure layout/legend are handled",
        "    automatically. 'kind=' selects the underlying plot type.",
        "Consequence: figure-level functions cannot be placed into an",
        "existing subplot grid, while axes-level functions can.",
    ])

    print_answer(4, "What does the shaded band around a line in "
        "sns.lineplot() or sns.regplot() represent?", [
        "It is a CONFIDENCE INTERVAL (by default 95%) around the estimated",
        "value. In lineplot it is the 95% CI of the MEAN at each x-position",
        "(via bootstrapping when there are repeated observations at the",
        "same x). In regplot it is the 95% CI of the fitted REGRESSION",
        "LINE - the band is narrowest where data is dense, showing where",
        "the true trend is estimated most precisely. Set ci=None to hide it.",
    ])

    print_answer(5, "What is the purpose of the hue parameter, and how does "
        "it extend a 2-D plot to represent a third categorical dimension?", [
        "hue maps a THIRD variable to COLOUR: every distinct value of the",
        "hue column is drawn as a separate coloured group (with an",
        "automatic legend) inside the same axes. The x and y positions are",
        "the first two dimensions, and colour encodes the third, so a",
        "2-D plot gains a categorical third dimension without needing",
        "separate charts - e.g. scatterplot(x=hours, y=marks, hue=branch)",
        "shows how the hours-marks relationship differs per branch. With",
        "style= and size= up to five dimensions can be encoded in one plot.",
    ])

    print_answer(6, "In Task 3, why is a pairplot with hue more informative "
        "than plotting each pair of variables separately without colour?", [
        "With hue='species', every one of the 12 pairwise scatter panels AND",
        "the diagonal distributions are split by colour at once, so you can",
        "see (a) how each species separates on every variable pair, (b)",
        "which measurements discriminate species best (petal length/width",
        "clearly separate setosa), and (c) whether a relationship between",
        "two variables holds within EACH species or is an artefact of",
        "pooling them. Without hue, group structure is invisible - points",
        "from different species overlap into one cloud and clusters that",
        "would be obvious (and useful for classification) stay hidden.",
    ])

    print_answer(7, "In Task 4 (AI case study), why is a diverging colormap "
        "(e.g. 'coolwarm') more appropriate than a single-hue colormap for "
        "visualizing severity levels?", [
        "A diverging colormap has a distinct neutral midpoint with two",
        "contrasting colours pointing in opposite directions, so values",
        "ABOVE and BELOW a reference point (e.g. the moderate-abnormality",
        "midpoint, or a clinical cut-off) pop out immediately in opposite",
        "hues. In the AI case study, one end of the scale (cool) reads as",
        "'low/acceptable abnormality' and the other (warm/red) reads as",
        "'high/severe - needs attention', letting a clinical decision-maker",
        "instantly separate safe wards from risky ones. A single-hue map",
        "only encodes magnitude, so high and low regions do not contrast as",
        "strongly and the 'danger direction' is not visually obvious.",
    ])

    print_answer(8, "When would a jointplot with kind='hex' be preferred "
        "over kind='scatter'?", [
        "When the dataset is LARGE/DENSE, as in Task 2's ~54,000 diamonds:",
        "in a plain scatter, thousands of points stack on the same pixel",
        "(over-plotting), hiding the true shape of the relationship. The",
        "hexbin variant bins the plane into hexagons and colours each by",
        "the NUMBER of observations, revealing density, clusters and gaps",
        "that a scatter would saturate. It also adds marginal histograms/",
        "distributions of each variable. For small datasets (dozens to a",
        "few hundred points) a scatter is better - individual points remain",
        "visible and no information is aggregated away.",
    ])


if __name__ == "__main__":
    main()
