```python
import pandas as pd

# Fetching data from different sources
source1_data = pd.read_csv('source1.csv')
source2_data = pd.read_json('source2.json')

# Combine data
combined_data = pd.concat([source1_data, source2_data], ignore_index=True)

# Clean and preprocess data
# Example: remove duplicates
combined_data.drop_duplicates(inplace=True)

# Store aggregated data
combined_data.to_csv('aggregated_data.csv', index=False)
```