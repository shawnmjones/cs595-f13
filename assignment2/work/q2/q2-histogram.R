#!/usr/bin/Rscript

d = read.csv( "mementoCounts.txt", stringsAsFactors=F, header = FALSE, sep = "\t" )

Mementos = d[,1]

brk <- seq(0, 22157, 1)

png("q2-histogram1.png")
hist(Mementos, col=heat.colors(22157), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<22157)]
Mementos = Mementos[which(Mementos<10543)]

brk <- seq(0, 4000, 1)

png("q2-histogram2.png")
hist(Mementos, col=heat.colors(4000), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()

Mementos = Mementos[which(Mementos<100)]

brk <- seq(0, 100, 1)

png("q2-histogram3.png")
hist(Mementos, col=heat.colors(100), main = "URIs vs. Number of Mementos", breaks=brk, freq = T, xlab="Mementos", ylab="URIs")

dev.off()
