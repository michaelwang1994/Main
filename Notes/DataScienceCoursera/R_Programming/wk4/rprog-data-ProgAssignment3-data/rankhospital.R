rankhospital = function(state, outcome, num = "best") {
  dataset = read.csv("outcome-of-care-measures.csv", colClasses = "character")
  state_hospitals = dataset[(dataset$State == state), ]
  
  if (outcome == "heart attack") {
    condition = state_hospitals[c("Hospital.Name", "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack")]
  }
  else if (outcome == "heart failure") {
    condition = state_hospitals[c("Hospital.Name", "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure")]
  }
  else if (outcome == "pneumonia") {
    condition = state_hospitals[c("Hospital.Name", "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia")]
  }

  condition[, 2] = as.numeric(condition[, 2])
  rank_hospital = condition[order(condition[, 2], condition[, 1], na.last = NA), ]  
  
  if (num == "best") {
    rank_hospital[, 1][1]
  }
  
  else if (num == "worst") {
    rank_hospital[, 1][length(rank_hospital[, 1])]
  }
  else {
    rank_hospital[, 1][num]
  }
    
}