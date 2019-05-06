MLB.Games <- read.csv("MLB-years.csv")

summary(MLB.Games$Win.Score)
summary(MLB.Games$Lose.Score)

summary(MLB.Games$Total.Score)

boxplot(MLB.Games$Total.Score~MLB.Games$Year)
