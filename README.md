# UCB for Online Ad Selection

A simple Python script that uses the Upper Confidence Bound (UCB) algorithm to simulate online ad selection over multiple rounds, track cumulative rewards, and visualize which ads were chosen how often.

## Features

- Implements the UCB1 algorithm to balance exploration vs. exploitation  
- Reports per-ad reward totals and overall reward  
- Plots a histogram of ad selection counts  
- Configurable number of rounds and number of ads  
- PEP8-compliant, command-line interface  

## Requirements

- Python 3.7+  
- `numpy`  
- `pandas`  
- `matplotlib`  

You can install dependencies with:

```
pip install numpy pandas matplotlib
```

## Getting Started
Clone or download this repository.

Make sure your working directory contains:

`ucb_ad_selection.py`

A CSV file (default: `dataset.csv`) where each row is a round and each column is an ad’s binary reward (0 or 1).

## Usage
```
python ucb_ad_selection.py [options]
```

### Arguments

| Flag                     | Description                                         | Default        |
|--------------------------|-----------------------------------------------------|----------------|
| `-f`, `--file <PATH>`    | Path to the CSV dataset (rounds × ads)              | `dataset.csv`  |
| `-o`, `--observations <N>` | Number of rounds to simulate                        | `10000`        |
| `-n`, `--n_ads <N>`      | Total number of distinct ads                        | `10`           |

### Example
```
python ucb_ad_selection.py \
  --file my_click_data.csv \
  --observations 5000 \
  --n_ads 5
```

This will:
1. Load `my_click_data.csv` (shape 5000×5).
2. Run UCB for 5,000 rounds over 5 ads.
3. Print dataset shape, first few rows, per-ad reward sums, total reward, and the full selection sequence.
4. Display a histogram showing how many times each ad was selected.

## Output
- Console
  - Dataset dimensions and preview
  - Rewards by ad: [ … ]
  - Total reward: …
  - Ads selected each round: [ … ]
- Plot
  - Histogram of selection counts for each ad

## Style & License
Script follows PEP8 naming and style guidelines

Feel free to modify and redistribute under the terms of the MIT License.



