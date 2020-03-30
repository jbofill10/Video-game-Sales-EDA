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

    plt.savefig('Charts/All_Time_Platform_Releases.png')
    plt.show()
    
    # Most successful genres
    style.use('seaborn-poster')
    genre_global_sales = df.groupby(['Genre'])['Global_Sales'].sum().sort_values(ascending=False)
    print(genre_global_sales)
    sns.barplot(x=genre_global_sales.index, y=genre_global_sales.values, ec='Black', palette='twilight')
    plt.xticks(rotation=20, fontsize=10)
    plt.xlabel('Genre', fontsize=18)
    plt.ylabel('Global Sales (in Millions)', fontsize=18)
    plt.title('Global Sales of Genres from 1980-2016', fontweight='bold', fontsize=22)
    plt.savefig('Charts/GlobalSales_ofGenres')
    plt.tight_layout()
    plt.show()

    top5_genres_list = df.groupby(['Genre'])['Global_Sales'].sum().sort_values(ascending=False).head(5).index
    print([i for i in top5_genres_list])
    top5_genre_df = df[df.Genre.isin(top5_genres_list)]
    fig, (ax0,ax1) = plt.subplots(2,2, figsize=(17,10))

    fig.suptitle('Top 5 Genres and their Sales (in Millions) Respective to their Country', fontsize=20, fontweight = 'bold')

    sns.lineplot(x='Year', y='NA_Sales', hue='Genre', data=top5_genre_df, ci=None, ax=ax0[0], palette='Set1')

    sns.lineplot(x='Year', y='EU_Sales', hue='Genre', data=top5_genre_df, ci=None, ax=ax0[1], palette='Set1')

    sns.lineplot(x='Year', y='JP_Sales', hue='Genre', data=top5_genre_df, ci=None, ax=ax1[0], palette='Set1')

    sns.lineplot(x='Year', y='Other_Sales', hue='Genre', data=top5_genre_df, ci=None, ax=ax1[1], palette='Set1')

    ax0[0].legend(loc='upper right')
    ax0[1].legend(loc='upper right')
    ax1[0].legend(loc='upper right')
    ax1[1].legend(loc='upper right')

    ax1[1].set_ylim(-0.1,1.6)

    ax0[0].set_ylabel('NA Sales (in Millions)', fontsize=16)
    ax0[1].set_ylabel('EU Sales (in Millions)', fontsize=16)
    ax1[0].set_ylabel('Japan Sales (in Millions)', fontsize=16)
    ax1[1].set_ylabel('Other Sales (in Millions)', fontsize=16)

    ax0[0].set_xlabel('Year', fontsize=16)
    ax0[1].set_xlabel('Year', fontsize=16)
    ax1[0].set_xlabel('Year', fontsize=16)
    ax1[1].set_xlabel('Year', fontsize=16)

    plt.savefig('Charts/CountryRespectiveSales')
    plt.show()

    style.use('seaborn-poster')
    
    top10_publishers_list = df.groupby(['Publisher'])['Global_Sales']\
        .sum()\
        .sort_values(ascending=False).head(10).index

    zero_to_five_publishers_list = top10_publishers_list[0:5]
    five_to_ten_publishers_list = top10_publishers_list[5:]
    zero_to_five_publishers_df = df[df.Publisher.isin(zero_to_five_publishers_list)]
    five_to_ten_publishers_df = df[df.Publisher.isin(five_to_ten_publishers_list)]
    

    fig, (ax0, ax1) = plt.subplots(2,1)
    plt.subplots_adjust(hspace=0.33, top=.95)

    # 1 - 5 in Global Sales
    sns.lineplot(x='Year', y='Global_Sales',
                 data=zero_to_five_publishers_df, hue='Publisher',
                 ci=None, ax=ax0, palette='Set1')

    ax0.legend(prop={'size':11.5})

    # 5-10 in Global Sales
    sns.lineplot(x='Year', y='Global_Sales',
                 data=five_to_ten_publishers_df, hue='Publisher',
                 ci=None, ax=ax1, palette='Set1')

    ax0.set_title('Top 1-5 Publishers by Global Sales')
    ax0.set_ylabel('Global Sales (in Millions)')

    ax0.spines['right'].set_visible(False)
    ax0.spines['top'].set_visible(False)

    ax1.set_title('Top 5-10 Publishers by Global Sales')
    ax1.set_ylabel('Global Sales (in Millions)')
    ax1.legend(loc='upper center', prop={'size': 11.5})
    ax1.set_ylim(-0.5, 5)

    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

    plt.savefig('Charts/GlobalSalesPublishers.png')

    plt.show()

