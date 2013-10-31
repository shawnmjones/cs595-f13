library(igraph)
library(igraphdata)
library(Matrix)
library(lattice)

data(karate)

k <- karate

repeat {
  keb <- edge.betweenness(k)
  
  kebo <- order(keb, decreasing = TRUE)
  
  # for fun, pick off the ones with the lowest betweenness,
  # and watch the graph kick out one memeber at a time
  #kebo <- order(keb)
  
  s <- kebo[-1]
  
  v <- get.edge(k, s)
  
  k <- delete.edges(k, E(k, P = v))
  
  if ( clusters(k)$no == 15) break
}

plot.igraph(k)