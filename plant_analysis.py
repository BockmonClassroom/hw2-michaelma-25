import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('plant_data.csv')

# 1. Combined Histograms
plt.figure(figsize=(10, 8))

plant_types = data['Plant Name'].unique()
for i, plant in enumerate(plant_types):
    plt.subplot(2, 2, i + 1)  # 2x2 grid
    subset = data[data['Plant Name'] == plant]
    plt.hist(subset['Leaf Length (cm)'], bins=10, alpha=0.7, label=f"{plant} Length", color=f'C{i}')
    plt.xlabel('Leaf Length (cm)')
    plt.ylabel('Count')
    plt.title(f'Histogram - {plant}')
    plt.legend()

plt.tight_layout()
plt.suptitle("Histograms of Leaf Length for Each Plant", y=1.02, fontsize=16)
plt.show()

# 2. Combined Boxplots
plt.figure(figsize=(10, 5))

# Leaf Length Boxplot
plt.subplot(1, 2, 1)
sns.boxplot(x='Plant Name', y='Leaf Length (cm)', data=data)
plt.title('Boxplot of Leaf Length by Plant Type')
plt.ylabel('Leaf Length (cm)')

# Leaf Width Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(x='Plant Name', y='Leaf Width (cm)', data=data)
plt.title('Boxplot of Leaf Width by Plant Type')
plt.ylabel('Leaf Width (cm)')

plt.tight_layout()
plt.suptitle("Boxplots of Leaf Measurements", y=1.05, fontsize=16)
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Leaf Width (cm)', y='Leaf Length (cm)', hue='Plant Name', data=data, palette='deep')
plt.title('Scatter Plot of Leaf Dimensions')
plt.xlabel('Leaf Width (cm)')
plt.ylabel('Leaf Length (cm)')
plt.legend(title='Plant Name')
plt.show()

# 4. Summary Statistics
stats = data.groupby('Plant Name')[['Leaf Width (cm)', 'Leaf Length (cm)']].agg(['mean', 'median', 'std', 'var'])
print("Summary Statistics:")
print(stats)

# 5. Insights
print("\nInsights from Data and Graphs:")
print("""
1. Histograms show the distribution of leaf lengths, revealing how sizes vary across plant types.
2. Boxplots indicate the spread and outliers for leaf lengths and widths. Differences between plant types are visible.
3. The scatter plot demonstrates the relationship between leaf width and length. Plant types form clusters.
4. Statistics provide quantitative insights: mean and median show central tendency, while std and var indicate variability.
""")
