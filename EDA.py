import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
import pandas as pd

def eda(df):
    # Global sales over the years
    g_sales_over_years = df.groupby(['Year'])['Global_Sales'].sum()

    box_plot_df = pd.DataFrame(columns=[str(int(i)) for i in g_sales_over_years.index])

    for i in g_sales_over_years.index:
        box_plot_df.at[0, str(int(i))] = g_sales_over_years[i]

    plt.figure(figsize=(13.7, 9))

    sns.barplot(x='variable', y='value', data=pd.melt(box_plot_df), palette='plasma', ec='Black')

    plt.ylabel('Global Sales (in Millions)', fontsize=22)
    plt.xlabel('Year', fontsize=22)
    plt.title('Global Sales (in Millions) throughout the Years', fontsize=24, fontweight='bold')
    plt.xticks(rotation=45, fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig('Charts/Yearly_Global_Sales.png')
    plt.show()


    style.use('seaborn-poster')

    f, ax = plt.subplots()
    platform_releases = df['Platform'].value_counts()

    sns.barplot(x=platform_releases.values, y=platform_releases.index, ec='Black')
    ax.set_title('Platforms with the Most Releases', fontweight='bold', fontsize=23)
    ax.set_xlabel('Releases', fontsize=18)
    ax.set_xlim(0, max(platform_releases.values)+130)
    ax.set_ylabel('Platform', fontsize=18)

    for p in ax.patches:
        width = p.get_width()
        ax.text(width + 62,
                p.get_y() + p.get_height() / 2. + 0.28,
                int(width),
                ha="center", fontsize=14)

    #plt.savefig('Charts/All_Time_Platform_Releases.png')

    plt.show()

