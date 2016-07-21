x = matrix(1:6,2,3)

for (i in seq_len(nrow(x))) {
	for(j in seq_len(ncol(x))) {
		print (x [i, j])
	}
}

count = 0
while(count < 10) {
	print(count)
	count = count + 1
}

z = 5
while(z >= 3 && z <= 10) {
	print(z)
	coin <- rbinom(1,1,0.5)
	
	if (coint == 1){
		z = z + 1
		} else{
			z = z - 1
	}
}

x0 <- 1
tol <- 1e-8

repreat { #these will run 5ever, until convergence
	x1 = computeEstimate()  #so convergense is SUPER important
	
	if(abs(x1 - x0) < tol) {
		break
		} else{
			x0 <- x1
	}
}

for(i in 1:100) {
	if(i <= 20) {
		## skip first 20 iterations
		next
	}
	do something here
}

