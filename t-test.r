args <- commandArgs(TRUE)

## args[1] : first coverage summary file
## args[2] : second coverage summary file
## args[3] : output file

cov <- read.table(args[1], row.names=1)
cov <- as.matrix(cov)
scaled <- cov[,-1]
cum <- cov[,1]
scaled.1 <- sweep(scaled,1,cum,`/`)

cov <- read.table(args[2], row.names=1)
cov <- as.matrix(cov)
scaled <- cov[,-1]
cum <- cov[,1]
scaled.2 <- sweep(scaled,1,cum,`/`)

rm(cov)

first <- seq(1,nrow(scaled.1))
input <- rbind(scaled.1, scaled.2)
rm(scaled.1)
rm(scaled.2)

outmat <- apply(input, 2, function(dat){t.test(dat[first],dat[-first], alternative="two.sided")$p.value})

write.table(outmat, args[3], quote=FALSE, row.names=FALSE, col.names = FALSE)
