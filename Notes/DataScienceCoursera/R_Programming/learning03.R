add2 <- function(x,y) {
  x+y
}

aboven <- function(x,n) {
  use <- x > n
  x[use]
}

(columnmean <- function(y) {
  nc <- ncol(y)
  means <- numeric(nc)
  for(i in 1:nc) {
    means[i] = mean(y [ ,i])
  }
  means
})