# House Sales Prediction

## Overview
This project aims to predict house prices based on property characteristics using regression models. It supports RealAgents, a real estate company, to optimize listing prices and accelerate sales.

## Project Structure

```
house_sales_prediction/
├── data/
│   ├── house_sales.csv
│   ├── train.csv
│   └── validation.csv
├── missing_city.py
├── clean_data.py
├── price_by_rooms.py
├── baseline_model.py
└── compare_model.py
```

## Data
The dataset includes historical house sales records with the following columns:

- `house_id`: Unique identifier
- `city`: City location
- `sale_price`: Sale price
- `sale_date`: Date of last sale
- `months_listed`: Time listed on the market
- `bedrooms`: Number of bedrooms
- `house_type`: Type of house (Detached, Semi-detached, Terraced)
- `area`: Area in square meters

## Scripts

### `missing_city.py`
Counts and displays the number of missing city entries.
```bash
python missing_city.py
```

### `clean_data.py`
Preprocesses the raw data to handle missing values and correct data types. Outputs `clean_data.csv`.
```bash
python clean_data.py
```

### `price_by_rooms.py`
Generates a summary of average sale price and variance grouped by the number of bedrooms. Outputs `price_by_rooms.csv`.
```bash
python price_by_rooms.py
```

### `baseline_model.py`
Fits a linear regression model and predicts prices on validation data. Outputs `base_result.csv`.
```bash
python baseline_model.py
```

### `compare_model.py`
Fits a Random Forest regression model for improved predictions. Outputs `compare_result.csv`.
```bash
python compare_model.py
```

## Requirements
- Python 3.x
- Pandas
- NumPy
- scikit-learn

Install dependencies using:
```bash
pip install pandas numpy scikit-learn
```

## Usage
Run each script individually as needed from the main project directory.

## Contributing
Contributions, improvements, and suggestions are welcome.

## License
This project is open-sourced under the MIT License.
