from matplotlib import pyplot as plt
from PIL import Image
import pandas as pd
import matplotlib
import numpy as np
import networkx as nx

from typing import Optional, Union, Mapping  # Special
from typing import Sequence, Iterable  # ABCs
from typing import Tuple  # Classes

from anndata import AnnData
import warnings

from .classes import ClusterPlot
from ..utils import _AxesSubplot, Axes

def cluster_plot(
    adata: AnnData,
    # plotting param
    title: Optional['str'] = None,
    figsize: Optional[Tuple[float, float]] = None,
    cmap: Optional[str] = "default",
    use_label: Optional[str] = None,
    list_clusters: Optional[list] = None,
    ax: Optional[_AxesSubplot] = None,
    show_plot: Optional[bool] = True,
    show_axis: Optional[bool] = False,
    show_image: Optional[bool] = True,
    show_color_bar: Optional[bool] = True,
    crop: Optional[bool] = True,
    margin: Optional[bool] = 100,
    size: Optional[float] = 5,
    image_alpha: Optional[float] = 1.0,
    cell_alpha: Optional[float] = 1.0,
    # cluster plot param
    show_subcluster: Optional[bool] = False,
    show_cluster_labels: Optional[bool] = False,
    show_trajectories: Optional[bool] = False,
    reverse: Optional[bool] = False,
    show_node: Optional[bool] = False,
    threshold_spots: Optional[int] = 5,
    text_box_size: Optional[float] = 5,
    color_bar_size: Optional[float] = 10,
    bbox_to_anchor: Optional[Tuple[float, float]] = (1,1),
) -> Optional[AnnData]:

    ClusterPlot(adata,
        title=title,
        figsize=figsize,
        cmap=cmap,
        use_label=use_label,
        list_clusters=list_clusters,
        ax=ax,
        show_plot=show_plot,
        show_axis=show_axis,
        show_image=show_image,
        show_color_bar=show_color_bar,
        crop=crop,
        margin=margin,
        size=size,
        image_alpha=image_alpha,
        cell_alpha=cell_alpha,
        show_subcluster=show_subcluster,
        show_cluster_labels=show_cluster_labels,
        show_trajectories=show_trajectories,
        reverse=reverse,
        show_node=show_node,
        threshold_spots=threshold_spots,
        text_box_size=text_box_size,
        color_bar_size=color_bar_size,
        bbox_to_anchor=bbox_to_anchor
        )