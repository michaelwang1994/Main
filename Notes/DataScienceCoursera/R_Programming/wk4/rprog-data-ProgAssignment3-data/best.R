best = function(state, outcome) {
  dataset = read.csv("outcome-of-care-measures.csv", colClasses = "character", na.strings = "Not Available", stringsAsFactors = FALSE)
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

  best_hospital = condition[order(condition[, 2], na.last = TRUE), ][1, ]$Hospital.Name
  best_hospital
}