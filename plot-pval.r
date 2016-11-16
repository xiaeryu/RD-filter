# Read data, change input file name accordingly
data <- read.table("final_output")

# Save to a png file
png("Summary.plot.png", height=960, width=2000)

# Plot figure
plot(data[,1]~seq(1,nrow(data)),ylab="-log10P",las=1,pch=20)

# Close plot handle
dev.off()
