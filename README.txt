Reddit Scraper Project

Goal:
view most popular posts from each day for selected subset of subreddits

Technologies:
Kafka
    hit reddit's api and send data to apache cassandra DB
    verify post isn't already in DB

Cassandra
    store date, post_id, post_title, post_description, dictionary of images, upvotes