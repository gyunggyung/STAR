library(dplyr)
library(ggplot2)

# read csv
scores <- read.csv("../data/Statistical_Value.csv")

#show kinds
AVscore <- scores %>% filter(Kinds == "AVscore")
group=1
ggplot(AVscore, aes(x= line, y= score,group=1)) + geom_line() + ggtitle("AVscores")

Lienlen <- scores %>% filter(Kinds == "Linelen")
ggplot(Lienlen, aes(x= line, y= score,group=1)) + geom_line() + ggtitle("Lienlen")


# show all
Status <- scores %>% filter (Kinds %in% c("AVscore", "Linelen", "KEP", "Spacelen", "complexity"))
Status %>% ggplot(aes(x= line, y= score,group=1)) + geom_line()+ facet_wrap(~Kinds) + ggtitle("status")

library(tidyr)

# find associative relation
all <- scores %>% spread(Kinds,score)
head (all)
all [, -1] %>% cor
all [, -1] %>% pairs
