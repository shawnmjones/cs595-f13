library(igraph) # for graph functions
library(igraphdata) # for karate club data

data(karate)

club <- karate
threshold <- 5

# graph prior to the breakup
plot.igraph(club, 
  vertex.color="#339900",
  vertex.frame.color="#000000",
  vertex.shape="circle",
  vertex.size=11,
  vertex.label.color="#ffffff",
  edge.color="black",
  main="Karate Club Graph Prior to Breakup",
  vertex.label.font=2,
  layout=layout.kamada.kawai,
  vertex.label.cex=1.2
)

# Algorithm below graciously provided by Corren McCoy
# also described by University of Michigan
while( clusters(club) $no < threshold ) {
  # calculate betweenness of all edges
  club.edge.betweenness <- edge.betweenness(club)
  
  # remove edge with highest betweenness
  decreasing.betweenness <- order(club.edge.betweenness, decreasing = TRUE)
  
  # for fun, pick off the ones with the lowest betweenness,
  # and watch the club kick out one memeber at a time
  #decreasing.betweenness <- order(decreasing.betweenness)
  
  # get the one with the highest edge betweenness
  highest.betweenness <- decreasing.betweenness[-1]
  
  # acquire the edge to delete
  edge.to.delete <- get.edge(club, highest.betweenness)
  
  # get rid of it
  club <- delete.edges(club, E(club, P = edge.to.delete))
}

plot.igraph(club, 
  vertex.color="#ff0000",
  vertex.frame.color="#000000",
  vertex.shape="circle",
  vertex.size=11,
  vertex.label.color="#ffffff",
  edge.color="black",
  main="Karate Club Split, Predicted by Girvan-Newman Betweenness Clustering",
  vertex.label.font=2,
  layout=layout.kamada.kawai,
  vertex.label.cex=1.2
  )