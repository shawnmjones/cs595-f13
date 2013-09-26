#!/usr/bin/Rscript

d = read.csv( "mementoCounts.txt", stringsAsFactors=F, header = FALSE, sep = "\t" )

Mementos = d[,1]

brk <- seq(0, 22157, 1)

png("q2-histogram1.png")
hist(Mementos, main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<22157)]
Mementos = Mementos[which(Mementos<10543)]

brk <- seq(0, 4000, 1)

png("q2-histogram2.png")
hist(Mementos, main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<10)]

brk <- seq(0, 10, 1)

png("q2-histogram3.png")
hist(Mementos, main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()
