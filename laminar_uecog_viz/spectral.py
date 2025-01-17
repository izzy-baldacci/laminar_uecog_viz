import numpy as np
import matplotlib.pyplot as plt
from laminar_uecog_viz import utils


def plot_spectrogram(W, f, t, colorbar=False, fig=None, ax=None):
    """Plot spectrogram given wavelet magnitude coefficents

    Parameters
    ----------
    W : 2-D array
        Wavelet coefficients, time x frequency
    f : 1-D array
        Center frequencies in hertz
    t : 1-D array
        Time points in seconds
    colorbar : bool, optional
        Whether to plot colorbar, by default False
    fig : matplotlib.Figure, optional
        Figure handle, by default None
    ax : matplotlib.axes.Axes, optional
        Axes handle, by default None

    Returns
    -------
    Tuple
        Matplotlib figure and axes handle
    """
    fig, ax = utils.check_fig_ax(fig, ax)

    pos = ax.imshow(W.T, interpolation='none', aspect=1/150, vmin=0, vmax=None, cmap='binary',
                    origin='lower', extent=[t[0], t[-1], 0, len(f)])

    yticks = [10, 30, 75, 150, 300, 600, 1200]
    positions = [np.argmin(np.abs(v - f)) for v in yticks]
    plt.yticks(positions, yticks)

    if colorbar:
        cbar = fig.colorbar(pos, ax=ax)

    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(8)

    return fig, ax
