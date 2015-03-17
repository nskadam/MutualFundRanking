#------------------------------------------------------------------------------#
# Analyse MF Data 
#------------------------------------------------------------------------------#


# Load Packages ----------------------------------------------------------------
library(doSNOW)
library(RCurl)
library(XML)
library(doSNOW)
library(foreach)
options(java.parameters = "-Xmx4000m")
library(xlsx)  
library(stringr)
library(xts)
library(PerformanceAnalytics)
library(reshape2)
library(stringdist)
library(ggplot2)
library(data.table)

# Clear Workspace & Load Functions ---------------------------------------------
if('cl' %in% ls()){
  stopCluster(cl)  
}
rm(list=ls());gc()


work.dir<-'D:\\0. Nilesh Files\\7.1. Personal\\15.4 MF Ranking\\Mutual Fund Ranking\\'
dir.data <- 'Data'
dir.result <- 'Result
'
# source r functions
source('D:\\0. Nilesh Files\\Dropbox\\SkyDrive\\2. Projects\\7. Perosonal\\37. R Functions\\3. Scripts\\a_r_functions.r')

SetWorkDirDataProcessing()

# start parallel backend
#cl<-makeCluster(12) 
#registerDoSNOW(cl)






# User inputs ------------------------------------------------------------------

file = 'D:\\0. Nilesh Files\\7.1. Personal\\15.4 MF Ranking\\Mutual Fund Ranking\\Data\\mf_data_parsed.csv'
dat <- fread(file)
colnames(dat) <- make.names(str_split('Row Number;scheme.code;scheme.name;nav;Repurchase Price;Sale Price;date', ';')[[1]])
dat <- as.data.frame(dat)

dat <- dat[,c('scheme.code', 'scheme.name', 'nav', 'date')]
dat.all <- dat

mf.numbers <- '102000
101762
101161
100377
108466
101144'

mf.numbers <- str_split(mf.numbers, '\n')[[1]]

dat <- dat.all[ dat$scheme.code %in% mf.numbers,]
dat$date <- as.Date(dat$date, '%d-%b-%Y')
dat$nav <- as.numeric(dat$nav)


PlotMFSchemes <- function(dat,scheme.codes = unique(dat$scheme.code)){
  dat.ts <- dcast(dat, date ~ scheme.name , value.var = 'nav')
  dat.ts.date <- dat.ts$date
  dat.ts$date <- NULL
  dat.ts <- na.locf(dat.ts)
  dat.ts <- dat.ts[ complete.cases(dat.ts),]
  
  dat.ts <- zoo(dat.ts,dat.ts.date)
  
  dat.ret <- Return.calculate(dat.ts)
  
  
  colnames(dat.ret)
  charts.PerformanceSummary(dat.ret)
}


PlotMFSchemes(dat)

