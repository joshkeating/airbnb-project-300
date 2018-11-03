setwd("~/School/info300/airbnb-project/")
library(dplyr)

cal <- read.csv("./calendar.csv", stringsAsFactors = FALSE)

num.unique.prices <- cal %>% select(price) %>% unique() %>% count()

