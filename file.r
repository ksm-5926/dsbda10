# Load libraries (install once separately if needed)
library(ggplot2)
library(dplyr)
library(tidyr)
library(stringr)

# Create dataset
data <- data.frame(
  Hashtags = c("#AI,#ML", "#Data,#AI", "#BigData,#ML", "#AI,#Data", "#ML,#AI"),
  Sentiment = c("Positive", "Neutral", "Positive", "Negative", "Positive"),
  Likes = c(120, 80, 200, 60, 140),
  Retweets = c(30, 20, 50, 10, 35)
)

# Split hashtags and count frequency
hashtag_freq <- data %>%
  separate_rows(Hashtags, sep = ",") %>%
  mutate(Hashtags = str_trim(Hashtags)) %>%
  count(Hashtags)

# Bar chart
ggplot(hashtag_freq, aes(reorder(Hashtags, n), n, fill = Hashtags)) +
  geom_bar(stat = "identity") +
  coord_flip()+theme_minimal()

# Pie chart
ggplot(data %>% count(Sentiment), aes("", n, fill = Sentiment)) +
  geom_col() +
  coord_polar("y")+theme_minimal()

# Scatter plot
ggplot(data, aes(Likes, Retweets, color = Sentiment)) +
  geom_point(size = 4)+theme_minimal()
