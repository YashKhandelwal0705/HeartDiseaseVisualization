import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("heart.csv")

st.title("Heart Disease Data Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")

# Filter: Gender
gender_options = st.sidebar.multiselect("Select Gender", options=df['Sex'].unique())
if gender_options:
    df = df[df['Sex'].isin(gender_options)]

# Filter: Age
age_range = st.sidebar.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (40, 60))
df = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]

# Main metrics
st.subheader("Dataset Summary")
st.write(df.describe())

# Visualization 1: Age vs Cholesterol
st.subheader("Age vs Cholesterol")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x='Age', y='Cholesterol', hue='Sex', ax=ax1)
st.pyplot(fig1)

# Visualization 2: Chest Pain Type count
st.subheader("Chest Pain Type Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='ChestPainType', hue='Sex', ax=ax2)
st.pyplot(fig2)

# Visualization 3: Heart Disease by FastingBS
st.subheader("Heart Disease by Fasting Blood Sugar")
fig3, ax3 = plt.subplots()
sns.countplot(data=df, x='FastingBS', hue='HeartDisease', ax=ax3)
st.pyplot(fig3)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

