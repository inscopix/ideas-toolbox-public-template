import logging
import shutil

import matplotlib.pyplot as plt
import pandas as pd
from beartype.typing import List
from ideas import io, plots

logger = logging.getLogger()


def plot_footprints(
    *,
    cell_set_file: List[str],
    title: str = "wow so title",
    choice_param: str = "wow",
) -> None:
    """Save a PNG image showing footprints of cells

    rejected/undecided cells shown in gray

    (unless all cells are undecided, in which case they
    are shown in color)
    """

    logger.info("Tool started")

    output_preview_filename = "cellset.png"

    x, y = io.cell_set_to_contours(cell_set_file[0], threshold=2.0)

    fig, ax = plt.subplots(figsize=(12, 8))

    num_neurons = len(x)

    colors = ["red" for _ in range(num_neurons)]

    plots.plot_footprints(x, y, ax, colors=colors, fill_alpha=0.25)

    ax.set_aspect("equal", "box")
    ax.set_title(
        "Footprints of identified cells.",
        fontsize=12,
        color="gray",
    )
    for spine in ["bottom", "top", "left", "right"]:
        ax.spines[spine].set_color("gray")
    ax.tick_params(axis="y", colors="gray")
    ax.tick_params(axis="x", colors="gray")
    ax.xaxis.label.set_color("gray")
    ax.yaxis.label.set_color("gray")
    plt.tight_layout()
    plt.title(title)
    fig.savefig(
        output_preview_filename,
        dpi=300,
    )

    logger.info("Done making preview file.")

    # also copy over the isxd cellset file to mimic
    # a real output so that we can use the png as its preview
    shutil.copyfile(cell_set_file[0], "output_cellset.isxd")

    # also create a CSV file so that we can have multiple output
    # files

    metrics = io.cell_set_to_footprint_metrics(cell_set_file)
    pd.DataFrame(metrics).to_csv("metrics.csv", index=False)

    logger.info("Tool finished.")


def dummy_function(
    int_param: int,
    str_param: str,
    float_param: float = 1.0,
    bool_param: bool = False,
):
    pass


def dummy_function_2(list_of_strings: list[str]):
    pass
