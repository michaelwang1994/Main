#import packages

library(ggplot2)
library(GGally)
library(dplyr)

#intro

setwd("~/GitHub/Kaggle/HousePrices")
train = read.csv('train.csv')
test = read.csv('test.csv')
summary(train)

head(train[, c("Condition1", "Condition2")], 10)
#it seems like condition 1 and 2 can be the same

#analysis

train_subset1 <- train %>%
  select(MSSubClass, MSZoning, BldgType, HouseStyle, OverallCond, YrSold, SalePrice) %>%
  mutate(highlow = ifelse(SalePrice > mean(SalePrice), 'high', 'low'))

pairplot1 = ggpairs(train_subset1, mapping = aes(color = highlow))
