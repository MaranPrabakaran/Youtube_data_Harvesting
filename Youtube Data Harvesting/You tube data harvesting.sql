use youtube_data;
create table video (
sl_no int primary key auto_increment not null,
video_id varchar(255),
video_name varchar(255),
video_description text,
publishedat datetime,
view_count int,
like_count int,
favorite_count int,
comment_count int,
duration int,
thumbnail varchar(255),
caption_status varchar(255)
);
use youtube_data;
create table comment (
sl_no int primary key auto_increment not null,
comment_id varchar(255),
comment_text text,
comment_author varchar(255),
comment_publishedat varchar(255)
);