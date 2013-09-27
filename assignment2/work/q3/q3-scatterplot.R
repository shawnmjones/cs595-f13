#!/usr/bin/Rscript

d <- read.csv("mementosVsAge.txt", stringsAsFactors = F, header = FALSE, sep = "\t")

data = d[,c(2,3)]

png("q3-scatterplot.png")

plot(data, col=c("blue"), ylab="Age (in days)", xlab="Number of Mementos", main = "Number of Mementos vs. Age of URI")

dev.off()
