#!/usr/bin/Rscript

d <- read.csv("mementosVsAge.txt", stringsAsFactors = F, header = FALSE, sep = "\t")

data = d[,c(2,3)]

png("q3-scatterplot.png")

plot(data, ylab="Age (in days)", xlab="Number of Mementos", main = "Number of Mementos vs. Age of URI")

# abline(lm(data[1]~data[2]), col="red")

dev.off()
