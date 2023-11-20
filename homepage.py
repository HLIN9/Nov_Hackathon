import streamlit as st
import pandas as pd
import pydeck as pdk

# Set titles 
st.markdown('# <font color="#ffc72c">Bing Bong</font>', unsafe_allow_html=True)
st.markdown('*Gia Khang Ngo - Who - Who - Who*')
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
twitter_data = pd.read_csv('cleaned_data_Twitter.csv')
loc_data = pd.read_csv('country_loc.csv', encoding='ISO-8859-1')
st.markdown('#### <font color = "#006BB6">Raw Data', unsafe_allow_html=True)
check_data = st.expander('Click to see raw data')
with check_data:
    st.dataframe(twitter_data)

# Download Data Button
st.download_button(label= 'Download Raw Data', data=twitter_data.to_csv().encode('utf-8'), file_name='Twitter_data.csv', mime='text/csv')

#Sidebar
# Set region user input
st.sidebar.markdown('**<font color="#ffc72c">User Input Features</font>**',unsafe_allow_html=True)
st.sidebar.markdown("*Select the region you want to analyze:*")
input_region = st.sidebar.multiselect('Region', twitter_data['Region of Focus'].unique())
st.sidebar.markdown("*Select the social media platform you want to analyze:*")
input_media = st.sidebar.multiselect('Social Media', ["Facebook", "Instagram", "Threads", "Tiktok", "Twitter", "Youtube"])

st.sidebar.markdown("*Select the social media platform you want to analyze:*")

filtered_data = loc_data[loc_data['name'].isin(input_region)]

if not filtered_data.empty:
    # Calculate the center of the map based on the selected countries
    center_lat = filtered_data['latitude'].mean()
    center_lon = filtered_data['longitude'].mean()

# Plot the map bar chart displaying number of social media users
st.markdown('## <font color = "#006BB6">Number Social Media Users Per Region', unsafe_allow_html=True)

for selected_region in input_region:
    if selected_region == None:
        st.error("Please select at least one region in the sidebar.") # D
    else:
        # Filter data for the selected region
        region_data = filtered_data[filtered_data['name'] == selected_region]

        # Check if the region data is not empty
        if not region_data.empty:
            # Display the number of social media users
            num_users = twitter_data[twitter_data['Region of Focus'] == selected_region]["X (Twitter) Follower #"]
            st.markdown(f"Number of Twitter users in {selected_region}: {num_users.iloc[0]}")

            # Display the map for the selected region
            st.pydeck_chart(pdk.Deck(
                map_style=None,
                initial_view_state=pdk.ViewState(
                    latitude=region_data['latitude'].iloc[0],
                    longitude=region_data['longitude'].iloc[0],
                    zoom=6,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        'HexagonLayer',
                        data=region_data,
                        get_position='[longitude, latitude]',
                        radius= 20000,
                        color = '[0, 0, 0, 255]',
                        elevation_scale= (num_users.iloc[0])*100,
                        elevation_range = [0,100000],
                        pickable=True,
                        extruded = True,       
                    ),
                ],
            ))
        else:
            st.warning(f"No data available for {selected_region}")




