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
loc_data = pd.read_csv('country_loc.csv')
st.markdown('#### <font color = "#006BB6">Raw Data', unsafe_allow_html=True)
check_data = st.expander('Click to see raw data')
with check_data:
    st.dataframe(twitter_data)

# Download Data Button
st.download_button(label= 'Download Raw Data', data=twitter_data.to_csv().encode('utf-8'), file_name='Twitter_data.csv', mime='text/csv')

#Sidebar
# Set region user input
st.sidebar.markdown('**<font color="#ffc72c">User Input Features</font>**',unsafe_allow_html=True)
st.sidebar.markdown("*Select the social media platform you want to analyze:*")
input_region = st.sidebar.multiselect('Region', twitter_data['Region of Focus'].unique())
filtered_data = loc_data[loc_data['name'].isin(input_region)]

if not filtered_data.empty:
    # Calculate the center of the map based on the selected countries
    center_lat = filtered_data['latitude'].mean()
    center_lon = filtered_data['longitude'].mean()

# Plot the map bar chart displaying number of social media users
st.markdown('## <font color = "#006BB6">Number Social Media Users Per Region', unsafe_allow_html=True)

for i in input_region:
    if i == None:
        st.error("Please select at least one region in the sidebar.")

    else:
        num_user = twitter_data[twitter_data['Region of Focus'] == i]["X (Twitter) Follower #"]
        st.markdown(num_user)

        world_map_chart = pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=center_lat,
                longitude=center_lon,
                zoom=2,
                pitch=50,
            ),
        )

        scatter_layer = pdk.Layer(
            'ScatterplotLayer',
            data=filtered_data,
            get_position='[longitude, latitude]',
            get_radius=10000,  # Adjust the radius as needed
            get_fill_color=[255, 0, 0],  # Red color for markers
            pickable=True,
        )


    st.pydeck_chart(world_map_chart)

