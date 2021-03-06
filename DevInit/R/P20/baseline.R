library(WDI)
library(data.table)
library(zoo)
library(plyr)
library(ggplot2)

setwd("D:/Documents/Data/P20 baseline")

# indicators <- c(
#   "SH.STA.STNT.ZS"
#   ,"SP.REG.BRTH.ZS"
#   ,"SP.REG.DTHS.ZS"
#   ,"NY.GDP.PCAP.PP.KD"
#   ,"NY.GDP.MKTP.PP.KD"
#   ,"NY.GNP.PCAP.PP.KD"
#   ,"NY.GNP.MKTP.PP.KD"
#   ,"NY.GDP.PCAP.KD.ZG"
#   )
# 
# names(indicators) <- c(
#   "stunting"
#   ,"birth.registration"
#   ,"death.registration"
#   ,"gdp.pc.ppp.constant.2011"
#   ,"gdp.ppp.constant.2011"
#   ,"gni.pc.ppp.constant.2011"
#   ,"gnp.ppp.constant.2011"
#   ,"gdp.pc.growth"
#   )
# 
# dat <- WDI(country = "all", 
#            indicator = indicators, 
#            start = 1960, 
#            end = 2016,
#            extra = TRUE
# )
# 
# save(dat,file="wdi.RData")
load("wdi.RData")

pop <- read.csv("undesa.pop.csv")
cc <- read.csv("country-codes.csv")
cc <- cc[c("ISO3166.1.Alpha.3","ISO3166.1.numeric")]
names(cc) <- c("iso3c","LocID")
pop <- subset(pop,Variant=="Medium" & Sex=="Both" & AgeGrp=="0-4")
pop <- merge(pop,cc,by="LocID")
pop$under5.pop <- pop$Value*1000
setnames(pop,"Time","year")
pop <- pop[c("iso3c","year","under5.pop")]

dat <- merge(
  dat
  ,pop
  ,by=c("iso3c","year")
  )


#Stunting target is 40% global decrease by 2025
keep <- c("country","iso3c","year","SH.STA.STNT.ZS","under5.pop")
stunting <- dat[keep]
stunting <- stunting[order(stunting$iso3c,stunting$year),]
stunting <- stunting[complete.cases(stunting),]
stunting <- data.table(stunting)
stunting$latest <- rev(!duplicated(stunting[,list(rev(stunting$country),rev(stunting$iso3c))]))
penult.stunting <- subset(stunting,!latest)
penult.stunting$latest <- rev(!duplicated(penult.stunting[,list(rev(penult.stunting$country),rev(penult.stunting$iso3c))]))
penult.stunting <- subset(penult.stunting,latest)
setnames(penult.stunting,"latest","penult")
stunting <- subset(stunting,latest)
stunting.rate <- merge(
  stunting
  ,penult.stunting
  ,by=c("country","iso3c")
  ,suffixes = c(".latest", ".penult")
  )
stunting.rate$rate = (stunting.rate$SH.STA.STNT.ZS.latest-stunting.rate$SH.STA.STNT.ZS.penult)
stunting.rate$annualized.rate = stunting.rate$rate/(stunting.rate$year.latest-stunting.rate$year.penult)
keep <- c("iso3c","year.penult","annualized.rate")
stunting.rate <- data.frame(stunting.rate)
stunting.rate <- stunting.rate[keep]
stunting$years.to.target <- 2025-stunting$year
stunting$target <- 0.6*stunting$SH.STA.STNT.ZS
stunting$necessary.reduction <- stunting$SH.STA.STNT.ZS-stunting$target
stunting$annual.reduction <- stunting$necessary.reduction/stunting$years.to.target
stunting <- merge(
  stunting
  ,stunting.rate
  ,by="iso3c"
  ,all.x=TRUE
  )
write.csv(stunting,"stunting-rates.csv",na="",row.names=FALSE)

#CRVS target is 100%
keep <- c("country","iso3c","year","SP.REG.BRTH.ZS","under5.pop")
crvs <- dat[keep]
crvs <- crvs[order(crvs$iso3c,crvs$year),]
crvs <- crvs[complete.cases(crvs),]
crvs <- data.table(crvs)
crvs$latest <- rev(!duplicated(crvs[,list(rev(crvs$country),rev(crvs$iso3c))]))
penult.crvs <- subset(crvs,!latest)
penult.crvs$latest <- rev(!duplicated(penult.crvs[,list(rev(penult.crvs$country),rev(penult.crvs$iso3c))]))
penult.crvs <- subset(penult.crvs,latest)
setnames(penult.crvs,"latest","penult")
crvs <- subset(crvs,latest)
crvs.rate <- merge(
  crvs
  ,penult.crvs
  ,by=c("country","iso3c")
  ,suffixes = c(".latest", ".penult")
)
crvs.rate$rate = (crvs.rate$SP.REG.BRTH.ZS.latest-crvs.rate$SP.REG.BRTH.ZS.penult)
crvs.rate$annualized.rate = crvs.rate$rate/(crvs.rate$year.latest-crvs.rate$year.penult)
keep <- c("iso3c","year.penult","annualized.rate")
crvs.rate <- data.frame(crvs.rate)
crvs.rate <- crvs.rate[keep]
crvs$years.to.target <- 2030-crvs$year
crvs$target <- 100
crvs$necessary.increase <- crvs$target-crvs$SP.REG.BRTH.ZS
crvs$annual.increase <- crvs$necessary.increase/crvs$years.to.target
crvs <- merge(
  crvs
  ,crvs.rate
  ,by="iso3c"
  ,all.x=TRUE
)
write.csv(crvs,"crvs-rates.csv",na="",row.names=FALSE)

#Income target is at least 7% GDP growth per annum in least developed
keep <- c("country","iso3c","year","NY.GDP.PCAP.KD.ZG","under5.pop")
gdp.growth <- dat[keep]
gdp.growth <- gdp.growth[order(gdp.growth$iso3c,gdp.growth$year),]
gdp.growth <- gdp.growth[complete.cases(gdp.growth),]
gdp.growth <- data.table(gdp.growth)
gdp.growth$latest <- rev(!duplicated(gdp.growth[,list(rev(gdp.growth$country),rev(gdp.growth$iso3c))]))
penult.gdp.growth <- subset(gdp.growth,!latest)
penult.gdp.growth$latest <- rev(!duplicated(penult.gdp.growth[,list(rev(penult.gdp.growth$country),rev(penult.gdp.growth$iso3c))]))
penult.gdp.growth <- subset(penult.gdp.growth,latest)
setnames(penult.gdp.growth,"latest","penult")
gdp.growth <- subset(gdp.growth,latest)
gdp.growth.rate <- merge(
  gdp.growth
  ,penult.gdp.growth
  ,by=c("country","iso3c")
  ,suffixes = c(".latest", ".penult")
)
gdp.growth.rate$rate = (gdp.growth.rate$NY.GDP.PCAP.KD.ZG.latest-gdp.growth.rate$NY.GDP.PCAP.KD.ZG.penult)
gdp.growth.rate$annualized.rate = gdp.growth.rate$rate/(gdp.growth.rate$year.latest-gdp.growth.rate$year.penult)
keep <- c("iso3c","year.penult","annualized.rate")
gdp.growth.rate <- data.frame(gdp.growth.rate)
gdp.growth.rate <- gdp.growth.rate[keep]
gdp.growth$years.to.target <- 2030-gdp.growth$year
gdp.growth$target <- 7
gdp.growth$necessary.increase <- gdp.growth$target-gdp.growth$NY.GDP.PCAP.KD.ZG
gdp.growth$annual.increase <- gdp.growth$necessary.increase/gdp.growth$years.to.target
gdp.growth <- merge(
  gdp.growth
  ,gdp.growth.rate
  ,by="iso3c"
  ,all.x=TRUE
)
write.csv(gdp.growth,"gdp.growth-rates.csv",na="",row.names=FALSE)

write.csv(dat,"baseline_wdi.csv",na="",row.names=FALSE)

#Stunting over time
stunt.ot <- dat[order(dat$iso3c,dat$year),]
stunt.ot <- stunt.ot[c("iso3c","year","SH.STA.STNT.ZS","under5.pop")]
colname <- "SH.STA.STNT.ZS"
stunt.ot <- ddply(stunt.ot,.(iso3c),function(x)
{
  naLen <- nrow(x[which(is.na(x[,colname])),])
  allLen <- nrow(x)
  valueLen <- allLen-naLen
  ival <- x[,colname]
  x[,paste("original",colname,sep="-")] <- ival 
  if(valueLen>=2)
  {
    ival <- na.approx(x[,colname],rule=2)
#     interpVals <- na.approx(x[,colname])
#     xIndex = 1
#     while(is.na(x[,colname][xIndex])){xIndex<-xIndex+1}
#     for(i in 1:length(interpVals))
#     {
#       ival[xIndex] <- interpVals[i]
#       xIndex<-xIndex+1
#     }
  }
  else if(valueLen==1){
    ival <- rep(sum(x[,colname],na.rm=TRUE),allLen)
  }
  x[,colname] <- ival 
  return(x)
})

stunt.ot$stunted <- stunt.ot$under5.pop*(stunt.ot$SH.STA.STNT.ZS/100)
stunt.ot <- data.table(stunt.ot)
stunt.ot <- stunt.ot[,.(total.stunted = sum(stunted,na.rm=TRUE),total.under5 = sum(under5.pop,na.rm=TRUE)),by=.(year)]
p <- ggplot(stunt.ot, aes(y=total.stunted,x=year)) + geom_line()
p
write.csv(stunt.ot,"stunting-over-time.csv",na="",row.names=FALSE)

#CRVS over time
library(rCharts)
birthreg.ot <- dat[order(dat$iso3c,dat$year),]
birthreg.ot <- birthreg.ot[c("country","iso3c","year","SP.REG.BRTH.ZS","under5.pop")]
birthreg.ot <- birthreg.ot[complete.cases(birthreg.ot),]
birthreg.ot <- birthreg.ot[order(birthreg.ot$year),]
colname <- "SP.REG.BRTH.ZS"
# birthreg.ot <- ddply(birthreg.ot,.(iso3c),function(x)
# {
#   naLen <- nrow(x[which(is.na(x[,colname])),])
#   allLen <- nrow(x)
#   valueLen <- allLen-naLen
#   ival <- x[,colname]
#   x[,paste("original",colname,sep="-")] <- ival 
#   if(valueLen>=2)
#   {
#     ival <- na.approx(x[,colname],rule=2)
#     #     interpVals <- na.approx(x[,colname])
#     #     xIndex = 1
#     #     while(is.na(x[,colname][xIndex])){xIndex<-xIndex+1}
#     #     for(i in 1:length(interpVals))
#     #     {
#     #       ival[xIndex] <- interpVals[i]
#     #       xIndex<-xIndex+1
#     #     }
#   }
#   else if(valueLen==1){
#     ival <- rep(sum(x[,colname],na.rm=TRUE),allLen)
#   }
#   x[,colname] <- ival 
#   return(x)
# })
birthreg.ot$unreged <- birthreg.ot$under5.pop*(1-(birthreg.ot$SP.REG.BRTH.ZS/100))
# setnames(birthreg.ot,"SP.REG.BRTH.ZS","Percent registered")
# setnames(birthreg.ot,"unreged","Unregistered children")
# setnames(birthreg.ot,"year","Year")
# setnames(birthreg.ot,"country","Country")
# d <- dPlot(
#   y = "Percent registered",
#   x = "Year",
#   groups = c("Country"),
#   data = birthreg.ot,
#   type = "line",
#   bounds = list(x = 50, y = 50, height = 600, width = 700),
#   height = 750,
#   width = 800
# )
# d$xAxis( type = "addCategoryAxis")
# d$yAxis( type = "addMeasureAxis")
# d$setTemplate(afterScript = "
#               <script>
#               myChart.draw()
#               myChart.axes[0].titleShape.text('Year')
#               myChart.axes[1].titleShape.text('Percent registered')
#               myChart.svg.append('text')
#               .attr('x', 250)
#               .attr('y', 20)
#               .text('Birth registration over time')
#               .style('text-anchor','beginning')
#               .style('font-size', '100%')
#               .style('font-family','sans-serif')
#               </script>               
#               ")
# d
# d$save('reg_line.html', cdn = TRUE)
# setnames(birthreg.ot,"Percent registered","Birth.registration")
# Year <- c(2000,2010,2030)
# Birth.registration <- c(58,65,100)
# world <- data.frame(Year,Birth.registration)
# p <- ggplot() +
#   stat_bin2d(data=birthreg.ot, aes(y=Birth.registration,x=Year)) +
#   geom_line(data=world, aes(y=Birth.registration,x=Year))
# p
# birthreg.ot <- data.table(birthreg.ot)
# birthreg.ot <- birthreg.ot[,.(total.unreged = sum(unreged,na.rm=TRUE),total.under5 = sum(under5.pop,na.rm=TRUE)),by=.(year)]
write.csv(birthreg.ot,"birthreg-over-time.csv",na="",row.names=FALSE)

world.pop <- data.table(pop)
world.pop <- data.table(subset(pop,year>=2015))
world.pop <- world.pop[order(world.pop$iso3c,world.pop$year),]
world.pop <- world.pop[,.(under5.pop=sum(under5.pop)),by=.(year)]
plot(under5.pop~year,data=world.pop,type="l")
write.csv(world.pop,"D:/Documents/Data/P20 baseline/world pop.csv",row.names=FALSE,na="")
