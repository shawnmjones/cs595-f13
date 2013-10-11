#!/usr/bin/Rscript

data <- read.csv('fb-frienddata.csv')

incdata <- sort(data$Friend.Count)

meanOut <- paste("Mean: ", mean(incdata), collapse = "")

medianOut <- paste("Median: ", median(incdata), collapse = "")

sdOut <- paste("Std Dev: ", sd(incdata), collapse = "")

write(meanOut, stdout())
write(medianOut, stdout())
write(sdOut, stdout())

png("q1-barplot.png")

# for the coloring of specific bars in the barplot:
# http://stackoverflow.com/questions/13112974/change-colours-of-particular-bars-in-a-bar-chart
# create a vector containing the items equal to my number of friends
pos <- (incdata == 153)
cols <- c("white", "red") # colors to use (first is everyone but me)

# draw the barplot
barplot(incdata, main="Friends of Friends on Facebook", xlab="Friends sorted by increasing number of friends", ylab="Number of Friends", col=cols[pos + 1])

# annotation and arrow
# http://blog.earlh.com/index.php/2009/07/labeling-plots-annotations-legends-etc-part-6-in-a-series/
text(x=match(c(153), incdata), y=330, labels="ME!", col='red')
arrows(x0=match(c(153), incdata), y0=300, x1=50, y1=175, length=0.1, lwd=3, col='red')

dev.off()
