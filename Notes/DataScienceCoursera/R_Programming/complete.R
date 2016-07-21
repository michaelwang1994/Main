complete <- function(directory, id = 1:332) {
  data = data.frame()
  files <- list.files(directory, full.names = TRUE)
  
  for (i in id) {
    read = read.csv(files[i])
    nobs = nrow(read[(complete.cases(read)),])
    data = rbind(data,c(i, nobs))
  }
  names(data) = c('id','nobs')
  data
}