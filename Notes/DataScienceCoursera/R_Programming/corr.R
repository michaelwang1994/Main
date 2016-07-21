corr <- function(directory, threshold = 0) {
  data = c()
  list = complete(directory)
  files = list.files(directory, full.names = TRUE)
  id = which(list$nobs >= threshold)
  for (i in id) {
    read = read.csv(files[i])
    single = (read[(complete.cases(read)),])
    single_corr = cor(single$sulfate,single$nitrate)
    data <- c(data,single_corr)
  }
  data
}