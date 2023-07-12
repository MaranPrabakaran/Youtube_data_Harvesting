#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import pandas as pd

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="youtube_data"
)

# Execute the query to fetch the channel data
query = "SELECT sl_no, Channel_name, Channel_Id, Subscription_Count, Channel_Views, Channel_Description FROM channel"
cursor = mydb.cursor()
cursor.execute(query)

# Convert the fetched data into a dictionary format
channel_data = {}
for row in cursor.fetchall():
    channel_name = row[1]
    channel_data[channel_name] = {
        'sl_no': row[0],
        'Channel_name': row[1],
        'Channel_Id': row[2],
        'Subscription_Count': row[3],
        'Channel_Views': row[4],
        'Channel_Description': row[5]
    }

# Close the database connection
cursor.close()
mydb.close()

# Create a dropdown menu to select the channel
selected_channel = st.sidebar.selectbox("Select a channel", list(channel_data.keys()))

# Retrieve the data for the selected channel
channel_info = channel_data[selected_channel]

# Display the channel data on the left side
st.sidebar.subheader('Channel Data')
st.sidebar.write(f"Channel Name: {channel_info['Channel_name']}")
st.sidebar.write(f"Channel ID: {channel_info['Channel_Id']}")
st.sidebar.write(f"Channel Description: {channel_info['Channel_Description']}")
st.sidebar.write(f"Subscription Count: {channel_info['Subscription_Count']}")
st.sidebar.write(f"Channel Views: {channel_info['Channel_Views']}")

fig_channel, ax_channel = plt.subplots(figsize=(8, 4))

# Line chart for subscription count and channel views over time
subscription_history = np.random.randint(100, 1000, size=10)  # Placeholder data for demonstration
views_history = np.random.randint(1000, 10000, size=10)  # Placeholder data for demonstration
ax_channel.plot(range(1, 11), subscription_history, marker='o', label='Subscription Count')
ax_channel.plot(range(1, 11), views_history, marker='o', label='Channel Views')
ax_channel.set_xlabel('Time')
ax_channel.set_ylabel('Count')
ax_channel.set_title('Subscription Count and Channel Views over Time', fontsize=15)
ax_channel.legend()

st.sidebar.pyplot(fig_channel)

# Connect to the MySQL database again
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="youtube_data"
)

# Execute the query to fetch the video data related to the selected channel
query = f"SELECT sl_no, video_id, video_name, video_description, publishedat, view_count, like_count, favorite_count, comment_count, duration, thumbnail, caption_status FROM video WHERE sl_no = {channel_info['sl_no']}"
cursor = mydb.cursor()
cursor.execute(query)

video_data = {}
for row in cursor.fetchall():
    video_name = row[2]
    video_data[video_name] = {
        'sl_no': row[0],
        'video_id': row[1],
        'video_name': row[2],
        'video_description': row[3],
        'publishedat': row[4],
        'view_count': row[5],
        'like_count': row[6],
        'favorite_count': row[7],
        'comment_count': row[8],
        'duration': row[9],
        'thumbnail': row[10],
        'caption_status': row[11]
    }

# Close the database connection
cursor.close()
mydb.close()

# Create a dropdown menu to select the video
selected_video = st.selectbox("Select a video", list(video_data.keys()))

# Retrieve the data for the selected video
video_info = video_data[selected_video]

# Display the video data on the right side
st.subheader('Video Data')
st.write(f"Video Name: {video_info['video_name']}")
st.write(f"Video ID: {video_info['video_id']}")
st.write(f"Video Description: {video_info['video_description']}")
st.write(f"Published Date: {video_info['publishedat']}")
st.write(f"Views: {video_info['view_count']}")
st.write(f"Likes: {video_info['like_count']}")
st.write(f"Favorite: {video_info['favorite_count']}")
st.write(f"Comments: {video_info['comment_count']}")
st.write(f"Duration: {video_info['duration']}")
st.write(f"Thumbnail: {video_info['thumbnail']}")
st.write(f"Caption Status: {video_info['caption_status']}")

# Create a DataFrame from the video data
df = pd.DataFrame.from_dict(video_data, orient='index')

# Sort the DataFrame by 'view_count' in descending order
df.sort_values('view_count', ascending=False, inplace=True)

# Select the columns for the bar graph
columns = ['view_count', 'like_count', 'comment_count']

fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.1
bar_positions = np.arange(len(df))

for i, column in enumerate(columns):
    ax.bar(bar_positions + (i - 1) * (bar_width + 0.1), df[column], width=bar_width, label=column)

# Set the x-axis labels and title
ax.set_xlabel('categories')
ax.set_ylabel('Count')
ax.set_title('Data of Videos')

# Add value labels on top of each bar
for i, column in enumerate(columns):
    for j, value in enumerate(df[column]):
        ax.text(j + (i - 1) * (bar_width + 0.1), value + 100, str(value), ha='center')

# Move the legend outside the plot
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')

# Adjust the spacing between the bars
ax.set_xticks(bar_positions)
ax.set_xticklabels(df.index, rotation=45)

# Add spacing between the bars
spacing = 0.1
for tick in ax.get_xticks():
    ax.bar(tick - bar_width/2, 0, width=bar_width - spacing, alpha=0)

# Rotate x-axis labels for better readability
plt.xticks(rotation=0)

# Display the bar plot in Streamlit
st.pyplot(fig)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="youtube_data"
)

# Execute the query to fetch the channel data
query = f"SELECT sl_no, comment_id, comment_text, comment_author, comment_publishedat FROM comment WHERE sl_no = {video_info['sl_no']}"
cursor = mydb.cursor()
cursor.execute(query)

comment_data = []
for row in cursor.fetchall():
    comment = {
        'comment_id': row[1],
        'comment_text': row[2],
        'comment_author': row[3],
        'comment_publishedat': row[4]
    }
    comment_data.append(comment)

# Close the database connection
cursor.close()
mydb.close()

# Display the comment data
st.subheader('Comments Data')

for comment in comment_data:
    st.write(f"Comment ID: {comment['comment_id']}")
    st.write(f"Comment Text: {comment['comment_text']}")
    st.write(f"Comment Author: {comment['comment_author']}")
    st.write(f"Comment Published At: {comment['comment_publishedat']}")
    st.write('---')




# In[3]:


import sqlalchemy
import pymysql
import pandas as pd
import streamlit as st
from sqlalchemy import desc
from sqlalchemy import MetaData

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Reflect the tables from the database
metadata = MetaData()
metadata.reflect(bind=engine)

# Define the tables
channels_table = metadata.tables['channel']
videos_table = metadata.tables['video']
comments_table = metadata.tables['comment']

# Rest of your code...


# Set the MySQL dialect to pymysql
pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:12345@localhost:3306/youtube_data')

engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')
connection = engine.connect()

# Define the tables you want to join
channels_table = sqlalchemy.Table('channel', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
comments_table = sqlalchemy.Table('comment', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)

# Connect to the database
#engine = sqlalchemy.create_engine('your_database_connection_string')

# Query 1: Names of all videos and their corresponding channels
query1 = sqlalchemy.select([videos_table.c.video_name, channels_table.c.channel_name]).\
    select_from(videos_table.join(channels_table, videos_table.c.sl_no == channels_table.c.sl_no))
result1 = engine.execute(query1)
data1 = []
for row in result1:
    data1.append(row)
df1 = pd.DataFrame(data1, columns=['Video Name', 'Channel Name'])

# Query 2: Channels with the most number of videos and the count
query2 = sqlalchemy.select([channels_table.c.channel_name, channels_table.c.video_count]).\
    order_by(channels_table.c.video_count.desc()).\
    limit(1)
result2 = engine.execute(query2)
data2 = []
for row in result2:
    data2.append(row)
df2 = pd.DataFrame(data2, columns=['Channel Name', 'Video Count'])

# Query 3: Top 10 most viewed videos and their respective channels
query3 = sqlalchemy.select([videos_table.c.video_name, channels_table.c.channel_name]).\
    select_from(videos_table.join(channels_table, videos_table.c.sl_no == channels_table.c.sl_no)).\
    order_by(desc(videos_table.c.view_count)).\
    limit(10)
result3 = engine.execute(query3)
data3 = []
for row in result3:
    data3.append(row)
df3 = pd.DataFrame(data3, columns=['Video Name', 'Channel Name'])

# Query 4: Number of comments on each video and their corresponding video names
query4 = sqlalchemy.select([videos_table.c.video_name, videos_table.c.comment_count])
result4 = engine.execute(query4)
data4 = []
for row in result4:
    data4.append(row)
df4 = pd.DataFrame(data4, columns=['Video Name', 'Comment Count'])

# Query 5: Videos with the highest number of likes and their corresponding channel names
query5 = sqlalchemy.select([videos_table.c.video_name, channels_table.c.channel_name, videos_table.c.like_count]).\
        select_from(videos_table.join(channels_table, videos_table.c.sl_no == channels_table.c.sl_no)).\
        order_by(videos_table.c.like_count.desc()).\
        limit(10)
result5 = engine.execute(query5)
data5 = []
for row in result5:
    data5.append(row)
df5 = pd.DataFrame(data5, columns=['Video Name', 'Channel Name','Likes'])

# Query 6: Total number of likes and dislikes for each video and their corresponding video names
query6 = sqlalchemy.select([videos_table.c.video_name, sqlalchemy.func.sum(videos_table.c.like_count).label('total_likes')]).\
        group_by(videos_table.c.video_name)
result6 = engine.execute(query6)
data6 = []
for row in result6:
    data6.append(row)
df6 = pd.DataFrame(data6, columns=['Video Name', 'Total Likes'])

# Query 7: Total number of views for each channel and their corresponding channel names
query7 = sqlalchemy.select([channels_table.c.channel_name, sqlalchemy.func.sum(videos_table.c.view_count).label('total_views')]).\
        select_from(channels_table.join(videos_table, channels_table.c.sl_no == videos_table.c.sl_no)).\
        group_by(channels_table.c.channel_name)
result7 = engine.execute(query7)
data7 = []
for row in result7:
    data7.append(row)
df7 = pd.DataFrame(data7, columns=['Channel Name', 'Total Views'])

# Query 8: Channels that published videos in the year 2022
subquery = sqlalchemy.select([videos_table.c.sl_no]).\
            where(sqlalchemy.extract('year', videos_table.c.publishedat) == 2022).\
            distinct().\
            subquery()

query8 = sqlalchemy.select([
        channels_table.c.channel_name,
        sqlalchemy.func.coalesce(sqlalchemy.func.count(subquery.c.sl_no), 0).label('video_count')
    ]).\
    select_from(channels_table).\
    outerjoin(subquery, channels_table.c.sl_no == subquery.c.sl_no).\
    group_by(channels_table.c.channel_name)
result8 = engine.execute(query8)
data8 = []
for row in result8:
    data8.append(row)
df8 = pd.DataFrame(data8, columns=['Channel Name','Videos'])

# Query 9: Average duration of all videos in each channel and their corresponding channel names
query9 = sqlalchemy.select([
        channels_table.c.channel_name,
        sqlalchemy.func.avg(videos_table.c.duration).label('average_duration')
    ]).\
    select_from(channels_table).\
    join(videos_table, channels_table.c.sl_no == videos_table.c.sl_no).\
    group_by(channels_table.c.channel_name)
result9 = engine.execute(query9)
data9 = []
for row in result9:
    data9.append(row)
df9 = pd.DataFrame(data9, columns=['Channel Name', 'Average Duration'])

# Query 10: Videos with the highest number of comments and their corresponding channel names
query10 = sqlalchemy.select([
        channels_table.c.channel_name,
        videos_table.c.video_name,
        videos_table.c.comment_count
    ]).\
    select_from(videos_table).\
    join(channels_table, channels_table.c.sl_no == videos_table.c.sl_no).\
    order_by(sqlalchemy.desc(videos_table.c.comment_count)).limit(10)
result10 = connection.execute(query10)
df10 = pd.DataFrame(result10.fetchall(), columns=['Channel Name', 'Video Name', 'Comment Count'])

# Close the connection
connection.close()

# Display the results in the Streamlit application
st.title("SQL Query Results")

st.header("Query 1: Names of all videos and their corresponding channels")
st.dataframe(df1)

st.header("Query 2: Channels with the most number of videos and the count")
st.dataframe(df2)

st.header("Query 3: Top 10 most viewed videos and their respective channels")
st.dataframe(df3)

st.header("Query 4: Number of comments on each video and their corresponding video names")
st.dataframe(df4)

st.header("Query 5: Videos with the highest number of likes and their corresponding channel names")
st.dataframe(df5)

st.header("Query 6: Total number of likes and dislikes for each video and their corresponding video names")
st.dataframe(df6)

st.header("Query 7: Total number of views for each channel and their corresponding channel names")
st.dataframe(df7)

st.header("Query 8: Channels that published videos in the year 2022")
st.dataframe(df8)

st.header("Query 9: Average duration of all videos in each channel and their corresponding channel names")
st.dataframe(df9)

st.header("Query 10: Videos with the highest number of comments and their corresponding channel names")
st.dataframe(df10)


# In[ ]:




