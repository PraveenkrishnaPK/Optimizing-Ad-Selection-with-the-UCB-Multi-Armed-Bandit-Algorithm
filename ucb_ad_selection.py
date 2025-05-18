#!/usr/bin/env python3
"""
ucb_ad_selection.py

Apply the Upper Confidence Bound (UCB) algorithm to select ads
over multiple rounds, track rewards, and plot a histogram of 
ad selections.
"""

import argparse
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(csv_path):
    """Load the ad-click dataset from a CSV file."""
    return pd.read_csv(csv_path)


def select_ads(dataset, observations, n_ads):
    """
    Run the UCB algorithm to decide which ad to show each round.

    Args:
        dataset (pd.DataFrame): Click data of shape (observations, n_ads).
        observations (int): Number of selection rounds.
        n_ads (int): Total number of ads.

    Returns:
        ads_selected (list of int): Chosen ad index each round.
        selection_counts (list of int): How often each ad was selected.
        reward_sums (list of int): Total rewards per ad.
        total_reward (int): Sum of all rewards.
    """
    ads_selected = []
    selection_counts = [0] * n_ads
    reward_sums = [0] * n_ads
    total_reward = 0

    for n in range(observations):
        ad = 0
        max_upper_bound = 0
        for i in range(n_ads):
            if selection_counts[i] > 0:
                avg_reward = reward_sums[i] / selection_counts[i]
                delta = math.sqrt((3 / 2) * math.log(n + 1) /
                                  selection_counts[i])
                upper_bound = avg_reward + delta
            else:
                upper_bound = float('inf')

            if upper_bound > max_upper_bound:
                max_upper_bound = upper_bound
                ad = i

        ads_selected.append(ad)
        selection_counts[ad] += 1
        reward = dataset.iloc[n, ad]
        reward_sums[ad] += reward
        total_reward += reward

    return ads_selected, selection_counts, reward_sums, total_reward


def plot_histogram(ads_selected, n_ads):
    """Plot a histogram showing how many times each ad was selected."""
    plt.hist(ads_selected, bins=range(n_ads + 1), edgecolor='black')
    plt.title('Histogram of Ad Selections')
    plt.xlabel('Ad Index')
    plt.ylabel('Number of Selections')
    plt.xticks(range(n_ads))
    plt.tight_layout()
    plt.show()


def main():
    """Parse arguments, run UCB, and display results."""
    parser = argparse.ArgumentParser(
        description='UCB for Online Ad Selection'
    )
    parser.add_argument(
        '-f', '--file',
        default='dataset.csv',
        help='Path to CSV dataset (rounds × ads)'
    )
    parser.add_argument(
        '-o', '--observations',
        type=int,
        default=10000,
        help='Number of rounds to simulate'
    )
    parser.add_argument(
        '-n', '--n_ads',
        type=int,
        default=10,
        help='Total number of ads'
    )
    args = parser.parse_args()

    data = load_data(args.file)
    print(f'Dataset shape: {data.shape}')
    print(data.head())

    (ads_selected,
     counts,
     rewards,
     total) = select_ads(data, args.observations, args.n_ads)

    print('Rewards by ad:', rewards)
    print('Total reward:', total)
    print('Ads selected each round:', ads_selected)

    plot_histogram(ads_selected, args.n_ads)


if __name__ == '__main__':
    main()
