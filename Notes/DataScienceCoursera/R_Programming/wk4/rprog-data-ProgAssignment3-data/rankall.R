rankall = function(outcome, num = "best") {
  dataset = read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  if (outcome == "heart attack") {
    condition = dataset[c("Hospital.Name", "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack", "State")]
  }
  else if (outcome == "heart failure") {
    condition = state_hospitals[c("Hospital.Name", "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure", "State")]
  }
  else if (outcome == "pneumonia") {
    condition = state_hospitals[c("Hospital.Name", "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia", "State")]

  }

  condition[, 2] = as.numeric(condition[, 2])
  condition = condition[order(condition[, 2], condition[, 1], na.last = NA), ]
    
  data_split = split(condition, condition$State)
  
  if (num == "best") {
    data_split = unlist(lapply(data_split, head, 1))
    data_split
  }
  
  else if (num == "worst") {
    lapply(data_split, tail, 1)
  }
  else {
    lapply(data_split, head, num)
  }
  
}