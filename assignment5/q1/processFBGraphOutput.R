#!/usr/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)

inputfile <- args[1]
outputfile <- args[2]
mylocation <- args[3]
mytext <- args[4]

data <- read.csv(inputfile)

incdata <- sort(data$Friend.Count)

meanOut <- paste("Mean: ", mean(incdata), collapse = "")

medianOut <- paste("Median: ", median(incdata), collapse = "")

sdOut <- paste("Std Dev: ", sd(incdata), collapse = "")

write(meanOut, stdout())
write(medianOut, stdout())
write(sdOut, stdout())

#png(outputfile)

#ndx = order(data$Friend.Count)
#xlabels <- data[ndx,]$Name

# for the coloring of specific bars in the barplot:
# http://stackoverflow.com/questions/13112974/change-colours-of-particular-bars-in-a-bar-chart
# create a vector containing the items equal to my number of friends
#mylocation = mylocation + 1
pos <- (incdata == mylocation)
cols <- c("white", "red") # colors to use (first is everyone but me)

# draw the barplot
barplot(incdata, main="Friends of Friends on Facebook", xlab="Friends sorted by increasing number of friends", ylab="Number of Friends", col=cols[pos + 1], ylim=c(0, max(incdata) + 100))
#barplot(incdata, main="Friends of Friends on Facebook", xlab="Friends sorted by increasing number of friends", ylab="Number of Friends", col=cols[pos + 1], ylim=c(0, max(incdata) + 100), names.arg=xlabels, las=3, cex.names=0.4)

# annotation and arrow
# http://blog.earlh.com/index.php/2009/07/labeling-plots-annotations-legends-etc-part-6-in-a-series/
text(x=match(c(mylocation + 18), incdata), y=max(incdata), labels=mytext, col='red')
arrows(x0=match(c(mylocation + 18), incdata), y0=(max(incdata) - 50), x1=match(c(mylocation + 18), incdata), y1=175, length=0.1, lwd=3, col='red')

#dev.off()
