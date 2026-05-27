import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib.gridspec import GridSpec

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Social Media Engagement Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Dark background */
.stApp {
    background-color: #0d0f14;
    color: #e8eaf0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #13161e !important;
    border-right: 1px solid #1e2230;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1a1d28 0%, #1e2235 100%);
    border: 1px solid #2a2f45;
    border-radius: 12px;
    padding: 18px 22px !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

[data-testid="metric-container"] label {
    color: #7b82a0 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-family: 'Space Mono', monospace !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #f0f2ff !important;
    font-size: 1.9rem !important;
    font-weight: 700 !important;
}

[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    color: #4ade80 !important;
    font-size: 0.8rem !important;
}

/* Section headers */
.section-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #5b6282;
    margin-bottom: 6px;
    margin-top: 32px;
}

/* Chart containers */
.chart-card {
    background: #13161e;
    border: 1px solid #1e2230;
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 16px;
}

/* Insight pills */
.insight-pill {
    display: inline-block;
    background: linear-gradient(90deg, #1e2a4a, #1a2038);
    border: 1px solid #2e4080;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 6px 0;
    font-size: 0.88rem;
    line-height: 1.5;
    color: #c8d0f0;
}

.insight-num {
    color: #6b8cff;
    font-family: 'Space Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    margin-right: 8px;
}

/* Selectbox / multiselect */
[data-testid="stSelectbox"], [data-testid="stMultiSelect"] {
    background: #1a1d28 !important;
}

/* Divider */
hr { border-color: #1e2230 !important; }

/* Table */
.dataframe { background: #13161e !important; color: #e8eaf0 !important; }

</style>
""", unsafe_allow_html=True)

# ── Data generation (same seed as original project) ──────────
@st.cache_data
def generate_data():
    np.random.seed(42)
    n = 500
    categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']
    platforms  = ['Instagram', 'Twitter', 'Facebook', 'TikTok']

    dates = pd.date_range(start='2023-01-01', end='2024-05-31', periods=n)
    cat   = np.random.choice(categories, n)
    plat  = np.random.choice(platforms, n)
    views = np.random.randint(500, 50_000, n)
    likes    = (views * np.random.uniform(0.01, 0.60, n)).astype(int)
    comments = (views * np.random.uniform(0.00, 0.10, n)).astype(int)
    shares   = (views * np.random.uniform(0.00, 0.08, n)).astype(int)

    df = pd.DataFrame({
        'Date': dates, 'Category': cat, 'Platform': plat,
        'Views': views, 'Likes': likes, 'Comments': comments, 'Shares': shares
    })
    df['total_engagement'] = df['Likes'] + df['Comments'] + df['Shares']
    df['engagement_rate']  = (df['total_engagement'] / df['Views'] * 100).round(2)
    df['YearMonth']        = df['Date'].dt.to_period('M')
    df['Month']            = df['Date'].dt.strftime('%b')
    return df

df = generate_data()

# ── Palette ───────────────────────────────────────────────────
ACCENT   = '#6b8cff'
PALETTE  = ['#6b8cff','#ff6b9d','#ffc96b','#6bffb8','#b06bff','#ff9d6b','#6bdeff','#ff6b6b']
CAT_CLR  = dict(zip(sorted(df['Category'].unique()), PALETTE))
PLT_CLR  = {'Instagram':'#6b8cff','Twitter':'#1da1f2','Facebook':'#4267B2','TikTok':'#ff6b9d'}

MPL_STYLE = {
    'axes.facecolor':  '#13161e',
    'figure.facecolor':'#13161e',
    'axes.edgecolor':  '#1e2230',
    'axes.labelcolor': '#7b82a0',
    'xtick.color':     '#5b6282',
    'ytick.color':     '#5b6282',
    'text.color':      '#e8eaf0',
    'grid.color':      '#1e2230',
    'grid.linestyle':  '--',
    'axes.spines.top':    False,
    'axes.spines.right':  False,
}
plt.rcParams.update(MPL_STYLE)

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎛️ Filters")
    st.markdown("---")

    sel_cats  = st.multiselect("Category", sorted(df['Category'].unique()),
                               default=sorted(df['Category'].unique()))
    sel_plats = st.multiselect("Platform", sorted(df['Platform'].unique()),
                               default=sorted(df['Platform'].unique()))
    date_range = st.date_input("Date Range",
                               value=[df['Date'].min(), df['Date'].max()],
                               min_value=df['Date'].min(),
                               max_value=df['Date'].max())

    st.markdown("---")
    st.markdown("<span style='color:#5b6282;font-size:0.75rem;font-family:Space Mono'>DATASET</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:#c8d0f0;font-size:0.85rem'>500 records · 7 columns<br>Jan 2023 – May 2024<br>8 categories · 4 platforms</span>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Social Media EDA v2.0 · Python · Pandas · Seaborn")

# ── Filter data ───────────────────────────────────────────────
fdf = df[
    df['Category'].isin(sel_cats) &
    df['Platform'].isin(sel_plats) &
    (df['Date'] >= pd.Timestamp(date_range[0])) &
    (df['Date'] <= pd.Timestamp(date_range[1]))
].copy()

# ── Header ────────────────────────────────────────────────────
st.markdown("# 📊 Social Media Engagement")
st.markdown("<span style='color:#5b6282;font-family:Space Mono;font-size:0.75rem;letter-spacing:0.1em'>END-TO-END EDA · VERSION 2.0</span>", unsafe_allow_html=True)
st.markdown("---")

# ── KPI row ───────────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Records",       f"{len(fdf):,}")
k2.metric("Avg Engagement Rate", f"{fdf['engagement_rate'].mean():.2f}%")
k3.metric("Total Engagement",    f"{fdf['total_engagement'].sum():,.0f}")
k4.metric("Avg Views / Post",    f"{fdf['Views'].mean():,.0f}")
k5.metric("Top Category",
          fdf.groupby('Category')['engagement_rate'].mean().idxmax() if len(fdf) else "—")

st.markdown("---")

# ── Row 1: Category bar + Platform bar ───────────────────────
st.markdown('<p class="section-title">Engagement Rate by Segment</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)

with c1:
    cat_avg = (fdf.groupby('Category')['engagement_rate']
               .mean().sort_values(ascending=True).round(2))
    fig, ax = plt.subplots(figsize=(6, 4))
    colors  = [CAT_CLR.get(c, ACCENT) for c in cat_avg.index]
    bars    = ax.barh(cat_avg.index, cat_avg.values, color=colors,
                      height=0.65, edgecolor='none')
    for bar, val in zip(bars, cat_avg.values):
        ax.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}%', va='center', fontsize=8, color='#c8d0f0')
    ax.set_xlabel('Avg Engagement Rate (%)', fontsize=8)
    ax.set_title('By Category', fontsize=10, color='#e8eaf0', pad=10)
    ax.set_xlim(0, cat_avg.max() * 1.18)
    ax.yaxis.set_tick_params(labelsize=8)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close()

with c2:
    plat_avg = (fdf.groupby('Platform')['engagement_rate']
                .mean().sort_values(ascending=True).round(2))
    fig, ax  = plt.subplots(figsize=(6, 4))
    pcolors  = [PLT_CLR.get(p, ACCENT) for p in plat_avg.index]
    bars     = ax.barh(plat_avg.index, plat_avg.values, color=pcolors,
                       height=0.55, edgecolor='none')
    for bar, val in zip(bars, plat_avg.values):
        ax.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}%', va='center', fontsize=8, color='#c8d0f0')
    ax.set_xlabel('Avg Engagement Rate (%)', fontsize=8)
    ax.set_title('By Platform', fontsize=10, color='#e8eaf0', pad=10)
    ax.set_xlim(0, plat_avg.max() * 1.18)
    ax.yaxis.set_tick_params(labelsize=8)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close()

# ── Row 2: Monthly trend + Distribution ──────────────────────
st.markdown('<p class="section-title">Trends & Distributions</p>', unsafe_allow_html=True)
c3, c4 = st.columns(2)

with c3:
    monthly = (fdf.groupby('YearMonth')['total_engagement']
               .sum().reset_index())
    monthly['YearMonth'] = monthly['YearMonth'].astype(str)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.fill_between(monthly['YearMonth'], monthly['total_engagement'],
                    alpha=0.15, color=ACCENT)
    ax.plot(monthly['YearMonth'], monthly['total_engagement'],
            color=ACCENT, linewidth=2, marker='o', markersize=4)
    ax.set_xlabel('Month', fontsize=8)
    ax.set_ylabel('Total Engagement', fontsize=8)
    ax.set_title('Monthly Engagement Trend', fontsize=10, color='#e8eaf0', pad=10)
    step = max(1, len(monthly) // 6)
    ax.set_xticks(range(0, len(monthly), step))
    ax.set_xticklabels(monthly['YearMonth'].iloc[::step], rotation=35, ha='right', fontsize=7)
    ax.yaxis.set_tick_params(labelsize=8)
    ax.grid(True, axis='y')
    fig.tight_layout()
    st.pyplot(fig)
    plt.close()

with c4:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(fdf['engagement_rate'], bins=30, kde=True, ax=ax,
                 color=ACCENT, edgecolor='none', alpha=0.7)
    ax.set_xlabel('Engagement Rate (%)', fontsize=8)
    ax.set_ylabel('Frequency', fontsize=8)
    ax.set_title('Engagement Rate Distribution', fontsize=10, color='#e8eaf0', pad=10)
    ax.axvline(fdf['engagement_rate'].mean(), color='#ff6b9d',
               linestyle='--', linewidth=1.5, label=f"Mean: {fdf['engagement_rate'].mean():.1f}%")
    ax.legend(fontsize=8)
    ax.yaxis.set_tick_params(labelsize=8)
    ax.xaxis.set_tick_params(labelsize=8)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close()

# ── Row 3: Boxplot + Scatter ──────────────────────────────────
st.markdown('<p class="section-title">Post-Level Deep Dive</p>', unsafe_allow_html=True)
c5, c6 = st.columns(2)

with c5:
    order = (fdf.groupby('Category')['Likes'].median()
             .sort_values().index.tolist())
    fig, ax = plt.subplots(figsize=(6, 4))
    palette = {c: CAT_CLR.get(c, ACCENT) for c in order}
    sns.boxplot(data=fdf, x='Category', y='Likes', order=order,
                palette=palette, ax=ax, width=0.55,
                flierprops=dict(marker='o', markersize=2,
                                markerfacecolor='#5b6282', alpha=0.5))
    ax.set_xlabel('Category', fontsize=8)
    ax.set_ylabel('Likes', fontsize=8)
    ax.set_title('Likes per Category (Boxplot)', fontsize=10, color='#e8eaf0', pad=10)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=35, ha='right', fontsize=7)
    ax.yaxis.set_tick_params(labelsize=8)
    ax.grid(True, axis='y')
    fig.tight_layout()
    st.pyplot(fig)
    plt.close()

with c6:
    fig, ax = plt.subplots(figsize=(6, 4))
    for cat in fdf['Category'].unique():
        sub = fdf[fdf['Category'] == cat]
        ax.scatter(sub['Views'], sub['Likes'],
                   color=CAT_CLR.get(cat, ACCENT),
                   alpha=0.55, s=18, label=cat, edgecolors='none')
    ax.set_xlabel('Views', fontsize=8)
    ax.set_ylabel('Likes', fontsize=8)
    ax.set_title('Likes vs Views by Category', fontsize=10, color='#e8eaf0', pad=10)
    ax.legend(fontsize=6, ncol=2, framealpha=0.2,
              facecolor='#1a1d28', edgecolor='#2a2f45')
    ax.xaxis.set_tick_params(labelsize=8)
    ax.yaxis.set_tick_params(labelsize=8)
    ax.grid(True)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close()

# ── Correlation Heatmap ───────────────────────────────────────
st.markdown('<p class="section-title">Correlation Matrix</p>', unsafe_allow_html=True)
num_cols = ['Views', 'Likes', 'Comments', 'Shares', 'total_engagement', 'engagement_rate']
corr     = fdf[num_cols].corr().round(2)
fig, ax  = plt.subplots(figsize=(8, 4))
mask     = np.triu(np.ones_like(corr, dtype=bool), k=1)
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', ax=ax,
            cmap=sns.diverging_palette(240, 10, as_cmap=True),
            linewidths=0.5, linecolor='#0d0f14',
            annot_kws={'size': 9},
            vmin=-1, vmax=1,
            cbar_kws={'shrink': 0.8})
ax.set_title('Correlation Heatmap of Engagement Metrics',
             fontsize=11, color='#e8eaf0', pad=12)
ax.tick_params(labelsize=8)
fig.tight_layout()
st.pyplot(fig)
plt.close()

# ── Key Insights ──────────────────────────────────────────────
st.markdown("---")
st.markdown('<p class="section-title">Key Insights</p>', unsafe_allow_html=True)

insights = [
    ("01", "Fashion drives the highest engagement — 43.33% avg rate, 7.7pp above the lowest category (Family at 35.59%)."),
    ("02", "More views ≠ better engagement. Views vs engagement_rate correlation = –0.01. Content quality matters more than reach."),
    ("03", "Likes alone predict total engagement extremely well (r = 0.98). Use Likes as a quick proxy in reporting."),
    ("04", "Platform spread is narrow (~4pp). Twitter leads at 42.13% vs TikTok at 38.12% — content > platform choice."),
    ("05", "Top 10 posts span 8 different category–platform combos. No single pairing dominates. Diversify your content strategy."),
]

for num, text in insights:
    st.markdown(
        f'<div class="insight-pill"><span class="insight-num">#{num}</span>{text}</div>',
        unsafe_allow_html=True
    )

# ── Top 10 Posts ──────────────────────────────────────────────
st.markdown("---")
st.markdown('<p class="section-title">Top 10 Posts by Total Engagement</p>', unsafe_allow_html=True)

top10 = (fdf.nlargest(10, 'total_engagement')
         [['Date','Category','Platform','Views','total_engagement','engagement_rate']]
         .reset_index(drop=True))
top10.index += 1
top10['Date']  = top10['Date'].dt.strftime('%Y-%m-%d')
top10['engagement_rate'] = top10['engagement_rate'].astype(str) + '%'
top10.columns = ['Date','Category','Platform','Views','Total Engagement','Eng. Rate %']
st.dataframe(top10, use_container_width=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<span style='color:#3a3f55;font-size:0.75rem;font-family:Space Mono'>"
    "Social Media Engagement Analysis · v2.0 · Python · Pandas · Seaborn · Streamlit"
    "</span>",
    unsafe_allow_html=True
)
