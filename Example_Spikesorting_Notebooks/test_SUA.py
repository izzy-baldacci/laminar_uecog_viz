#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:35:25 2021

@author: macproizzy
"""


import spikeinterface.extractors as se
import pandas as pd
from SUA_plot import plot_raster, plot_distribution

recording_file_path = '/Users/macproizzy/Desktop/Example_Spikesorting_Notebooks/RVG16_B06.pkl'
sorting_file_path = '/Users/macproizzy/Desktop/Example_Spikesorting_Notebooks/sorting_B06.pkl'

recording = se.load_extractor_from_pickle(recording_file_path)
sorting = se.load_extractor_from_pickle(sorting_file_path)
phy_sorting = se.PhySortingExtractor('/Users/macproizzy/Desktop/Example_Spikesorting_Notebooks/phy_Sept2/', exclude_cluster_groups = ['noise'])
trials_ = pd.read_csv('/Users/macproizzy/Desktop/Example_Spikesorting_Notebooks/trials_tableRVG16.csv')

sampling_frequency = sorting.get_sampling_frequency()

#plot_raster(phy_sorting, 6, trials_)
    
plot_distribution(phy_sorting, 6, trials_, 5, 'smooth')
