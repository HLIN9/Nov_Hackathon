import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px

# Set titles 
st.markdown('# <font color="#ffc72c">Visual Explorer </font>', unsafe_allow_html=True)
st.markdown('*Hackathon 2023*')
st.markdown('## <font color="#006BB6">Introduction</font>', unsafe_allow_html=True)

# Set Introduction 
# set two columns to seperate the text and image while they are side by side
col1,col2, =st.columns(2)
with col2:
    st.image('https://www.ncsc.gov.uk/images/social-icons.jpg', width= 300)

with col1:
    st.markdown('''* A visual graphic of social media user statistics from different region.
    * **Data source:** Do we need this.''')

    st.image('https://miro.medium.com/v2/resize:fit:1024/0*rnYWcmRH4KbfCWzt.png', width= 350)

# Import and display raw data
def read_data(platform):
    return pd.read_csv(platform)

# Sample data
fb_data = read_data("cleaned_data_Facebook.csv")
insta_data = read_data("cleaned_data_Instragram.csv")
twitter_data = read_data("cleaned_data_Twitter.csv")
tiktok_data = read_data("cleaned_data_Twitter.csv")
yt_data = read_data("cleaned_data_YouTube.csv")
thrd_data = read_data("cleaned_data_Threads.csv")
# Download Data Button
st.download_button(label= 'Download Raw Data', data=twitter_data.to_csv().encode('utf-8'), file_name='Twitter_data.csv', mime='text/csv')

#Sidebar
# Set region user input
st.sidebar.markdown('**<font color="#ffc72c">User Input Features</font>**',unsafe_allow_html=True)
st.sidebar.markdown("*Select the social media platform you want to analyze:*")

input_media = st.sidebar.multiselect('Social Media', ["Facebook", "Instagram", "Threads", "Tiktok", "Twitter", "Youtube"])

if input_media == ['Facebook']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(fb_data, x="Name (English)", y="Facebook Follower #", title="Total Followers Count for Facebook")
    st.plotly_chart(fig_fb_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(fb_data, names="Region of Focus", title="Distribution of Followers for Facebook", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(fb_data, r="Facebook Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Facebook")
    st.plotly_chart(fig_fb_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(fb_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(fb_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(fb_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)


elif input_media == ['Instagram']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(insta_data, x="Name (English)", y="Instagram Follower #", title="Total Followers Count for Instagram")
    st.plotly_chart(fig_fb_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(insta_data, names="Region of Focus", title="Distribution of Followers for Instagram", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(insta_data, r="Instagram Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Instagram")
    st.plotly_chart(fig_fb_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(insta_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(insta_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(insta_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)


elif input_media == ['Threads']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(thrd_data, x="Name (English)", y="Facebook Follower #", title="Total Followers Count for Facebook")
    st.plotly_chart(fig_fb_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(thrd_data, names="Region of Focus", title="Distribution of Followers for Facebook", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(thrd_data, r="Facebook Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Facebook")
    st.plotly_chart(fig_fb_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(thrd_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(thrd_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(thrd_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)


elif input_media == ['Tiktok']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(tiktok_data, x="Name (English)", y="Facebook Follower #", title="Total Followers Count for Facebook")
    st.plotly_chart(fig_fb_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(tiktok_data, names="Region of Focus", title="Distribution of Followers for Facebook", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(tiktok_data, r="Facebook Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Facebook")
    st.plotly_chart(fig_fb_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(tiktok_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(tiktok_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(tiktok_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)


elif input_media == ['Twitter']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(twitter_data, x="Name (English)", y="Facebook Follower #", title="Total Followers Count for Facebook")
    st.plotly_chart(fig_fb_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(twitter_data, names="Region of Focus", title="Distribution of Followers for Facebook", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(twitter_data, r="Facebook Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Facebook")
    st.plotly_chart(fig_fb_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(twitter_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(twitter_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(twitter_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)


elif input_media == ['Youtube']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(yt_data, x="Name (English)", y="Facebook Follower #", title="Total Followers Count for Facebook")
    st.plotly_chart(fig_fb_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(yt_data, names="Region of Focus", title="Distribution of Followers for Facebook", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(yt_data, r="Facebook Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Facebook")
    st.plotly_chart(fig_fb_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(yt_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(yt_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(yt_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)


#