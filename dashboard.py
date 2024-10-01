import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def create_monthly_df(df):
    grouped_df = df.groupby(by=['yr', 'mnth']).agg({
        'cnt': 'sum'
    }).reset_index()
    return grouped_df

def create_status_df(df):
    grouped_df = day_df.groupby(by=['workingday','mnth']).agg({
    'cnt': 'sum'
    }).reset_index()
    return grouped_df

day_df = pd.read_csv('day.csv')

st.header('Bike Sharing Dashborad:sparkles:')

monthly_df=create_monthly_df(day_df)
status_df=create_status_df(day_df)

grouped_2011 = monthly_df[monthly_df['yr'] == 0]
grouped_2012 = monthly_df[monthly_df['yr'] == 1]

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(grouped_2011['mnth'], grouped_2011['cnt'], marker='o', color='blue', label='2011')
ax.plot(grouped_2012['mnth'], grouped_2012['cnt'], marker='o', color='orange', label='2012')

st.subheader("Total Count by Month for 2011 and 2012")

ax.set_title("Total Count by Month for 2011 and 2012")
ax.set_xlabel('Month')
ax.set_ylabel('Total Count')
ax.set_xticks(grouped_2011['mnth'].unique())  
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

ax.legend(title='Year')
ax.grid()

st.pyplot(fig)

st.subheader("Total Count by Month for Working Days and Holidays")

pivot_df = status_df.pivot(index='mnth', columns='workingday', values='cnt').fillna(0)

fig, ax = plt.subplots(figsize=(16, 10))
pivot_df.plot(kind='bar', width=0.8, ax=ax)

ax.set_title('Total Count by Month for Working Days and Holidays')
ax.set_xlabel('Month')
ax.set_ylabel('Total Count')
ax.set_xticks(ticks=range(len(pivot_df.index)))
ax.set_xticklabels(labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)
ax.legend(title='Working Day', labels=['Holiday', 'Working Day'])
ax.grid(axis='y')

plt.tight_layout()

st.pyplot(fig)

st.caption('M.Faqih Ajiputra')

