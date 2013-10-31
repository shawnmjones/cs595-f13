library(igraph)
library(igraphdata)
library(Matrix)
library(lattice)

data(karate)

club <- karate
threshold <- 2

while( clusters(k) $no < threshold ) {
  keb <- edge.betweenness(club)
  
  decreasing.betweenness <- order(keb, decreasing = TRUE)
  
  # for fun, pick off the ones with the lowest betweenness,
  # and watch the graph kick out one memeber at a time
  #decreasing.betweenness <- order(decreasing.betweenness)
  
  highest.betweenness <- decreasing.betweenness[-1]
  
  edge.to.delete <- get.edge(club, highest.betweenness)
  
  club <- delete.edges(club, E(club, P = edge.to.delete))
}

plot.igraph(k)