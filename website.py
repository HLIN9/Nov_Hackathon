import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import zipfile
from io import BytesIO

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
    st.markdown('''* A visual graphic of social media user statistics from different region.''')

    st.image('https://miro.medium.com/v2/resize:fit:1024/0*rnYWcmRH4KbfCWzt.png', width= 350)

# Import and display raw data
def read_data(platform):
    return pd.read_csv(platform)

# Sample data
fb_data = read_data("cleaned_data_Facebook.csv")
insta_data = read_data("cleaned_data_Instragram.csv")
twitter_data = read_data("cleaned_data_Twitter.csv")
tiktok_data = read_data("cleaned_data_TikTok.csv")
yt_data = read_data("cleaned_data_YouTube.csv")
thrd_data = read_data("cleaned_data_Threads.csv")

zip_buffer = BytesIO()

# Create a ZipFile object
with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
    # Add each CSV file to the zip file
    zip_file.writestr('Facebook_data.csv', fb_data.to_csv(index=False))
    zip_file.writestr('Instagram_data.csv', insta_data.to_csv(index=False))
    zip_file.writestr('Twitter_data.csv', twitter_data.to_csv(index=False))
    zip_file.writestr('TikTok_data.csv', tiktok_data.to_csv(index=False))
    zip_file.writestr('YouTube_data.csv', yt_data.to_csv(index=False))
    zip_file.writestr('Threads_data.csv', thrd_data.to_csv(index=False))

# Download Zip Button for all data
st.download_button(label='Download All Data as CSV Files', data=zip_buffer.getvalue(), file_name='All_data.zip', mime='application/zip')

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
    st.markdown('No precise Data for Instagram for graphical evaluation !!!!')
    st.markdown('Select another social media from the sidebar on your left. Thank You.')

elif input_media == ['Threads']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Threads")
    fig_th_bar = px.bar(thrd_data, x="Name (English)", y="Threads Follower #", title="Total Followers Count for Threads")
    st.plotly_chart(fig_th_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Threads")
    fig_th_donut = px.pie(thrd_data, names="Region of Focus", title="Distribution of Followers for Threads", hole=0.4)
    st.plotly_chart(fig_th_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Threads")
    fig_th_radar = px.line_polar(thrd_data, r="Threads Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Threads")
    st.plotly_chart(fig_th_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Threads")
    fig_th_sunburst = px.sunburst(thrd_data, path=["Region of Focus"], values="Threads Follower #", title="Proportional Representation of Follower Counts for Threads")
    st.plotly_chart(fig_th_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Threads")
    fig_th_treemap_total_followers = px.treemap(thrd_data, path=["Region of Focus", "Name (English)"], values="Threads Follower #",
                                                title="Proportional Representation of Total Followers by Region for Threads")
    st.plotly_chart(fig_th_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatterth_global_distribution = px.scatter_3d(thrd_data, x="Region of Focus", y="Name (English)", z="Threads Follower #",
                                                    color="Threads Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatterth_global_distribution)


elif input_media == ['Tiktok']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Tiktok")
    fig_tt_bar = px.bar(tiktok_data, x="Name (English)", y="TikTok Subscriber #", title="Total Followers Count for Tiktok")
    st.plotly_chart(fig_tt_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Tiktok")
    fig_tt_donut = px.pie(tiktok_data, names="Region of Focus", title="Distribution of Followers for Tiktok", hole=0.4)
    st.plotly_chart(fig_tt_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Tiktok")
    fig_tt_radar = px.line_polar(tiktok_data, r="TikTok Subscriber #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Tiktok")
    st.plotly_chart(fig_tt_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Tiktok")
    fig_tt_sunburst = px.sunburst(tiktok_data, path=["Region of Focus"], values="TikTok Subscriber #", title="Proportional Representation of Follower Counts for Tiktok")
    st.plotly_chart(fig_tt_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Tiktok")
    fig_tt_treemap_total_followers = px.treemap(tiktok_data, path=["Region of Focus", "Name (English)"], values="TikTok Subscriber #",
                                                title="Proportional Representation of Total Followers by Region for Tiktok")
    st.plotly_chart(fig_tt_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scattertt_global_distribution = px.scatter_3d(tiktok_data, x="Region of Focus", y="Name (English)", z="TikTok Subscriber #",
                                                    color="TikTok Subscriber #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scattertt_global_distribution)


elif input_media == ['Twitter']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Twitter")
    fig_tw_bar = px.bar(twitter_data, x="Name (English)", y="X (Twitter) Follower #", title="Total Followers Count for Twitter")
    st.plotly_chart(fig_tw_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Twitter")
    fig_tw_donut = px.pie(twitter_data, names="Region of Focus", title="Distribution of Followers for Twitter", hole=0.4)
    st.plotly_chart(fig_tw_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Twitter")
    fig_tw_radar = px.line_polar(twitter_data, r="X (Twitter) Follower #", theta="Region of Focus", line_close=True, title="Twitter Count Multidimensional Comparison Twitter")
    st.plotly_chart(fig_tw_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Twitter")
    fig_tw_sunburst = px.sunburst(twitter_data, path=["Region of Focus"], values="X (Twitter) Follower #", title="Proportional Representation of Follower Counts for Twitter")
    st.plotly_chart(fig_tw_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Twitter")
    fig_tw_treemap_total_followers = px.treemap(twitter_data, path=["Region of Focus", "Name (English)"], values="X (Twitter) Follower #",
                                                title="Proportional Representation of Total Followers by Region for Twitter")
    st.plotly_chart(fig_tw_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scattertw_global_distribution = px.scatter_3d(twitter_data, x="Region of Focus", y="Name (English)", z="X (Twitter) Follower #",
                                                    color="X (Twitter) Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scattertw_global_distribution)


elif input_media == ['Youtube']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Youtube")
    fig_yt_bar = px.bar(yt_data, x="Name (English)", y="YouTube Subscriber #", title="Total Followers Count for Youtube")
    st.plotly_chart(fig_yt_bar)

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Youtube")
    fig_yt_donut = px.pie(yt_data, names="Region of Focus", title="Distribution of Followers for Youtube", hole=0.4)
    st.plotly_chart(fig_yt_donut)

    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_yt_radar = px.line_polar(yt_data, r="YouTube Subscriber #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Youtube")
    st.plotly_chart(fig_yt_radar)

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Youtube")
    fig_yt_sunburst = px.sunburst(yt_data, path=["Region of Focus"], values="YouTube Subscriber #", title="Proportional Representation of Follower Counts for Youtube")
    st.plotly_chart(fig_yt_sunburst)
    
    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Youtube")
    fig_yt_treemap_total_followers = px.treemap(yt_data, path=["Region of Focus", "Name (English)"], values="YouTube Subscriber #",
                                                title="Proportional Representation of Total Followers by Region for Youtube")
    st.plotly_chart(fig_yt_treemap_total_followers)

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatteryt_global_distribution = px.scatter_3d(yt_data, x="Region of Focus", y="Name (English)", z="YouTube Subscriber #",
                                                    color="YouTube Subscriber #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatteryt_global_distribution)


#