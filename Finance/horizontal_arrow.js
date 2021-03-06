#!/usr/bin/env node --stack-size=65500
var request = require('request'),
syl = require('sylvester'),
cmb = require('cmb'),
moment = require('moment'),
cheerio = require('cheerio'),
jsonlite = require('./source/jsonlite.js'),
stock = encodeURI(process.argv[2]),
optURL = "https://www.google.com/finance/option_chain?q="+stock,
underlying = 0,
upState = 0,
downState = 0,
changes = [],
expiriesAhead = process.argv[3]?parseInt(process.argv[3]):0,
data = {},
probabilities = {},
results = {};
for(var i = 1; i<21; i++){
    changes.push(i/2);
}

console.log("Downloading data...");
request(optURL,parseID);

function standardDev(values){
    var avg = average(values);
    var squareDiffs = values.map(function(value){
        var diff = value - avg;
        var sqrDiff = diff * diff;
        return sqrDiff;
    });
    var avgSquareDiff = average(squareDiffs);
    var stdDev = Math.sqrt(avgSquareDiff);
    return stdDev;
};
 
function average(data){
    var sum = data.reduce(function(sum, value){
        return sum + value;
    }, 0);
    var avg = sum / data.length;
    return avg;
};

function parseID(e,r,b){
    var underlying_id = b.substr(b.indexOf('underlying_id:')+15,b.indexOf(',underlying_price:')-(b.indexOf('underlying_id:')+16)),
    chainURL = "https://www.google.com/finance/option_chain?cid="+underlying_id+"&output=json";
    request(chainURL,parseJSON);
};

function parseJSON(e,r,b){
    if(r){
        var json = jsonlite.parse(b),
        underlying_id = r.request.uri.query.substr(r.request.uri.query.indexOf("cid=")+4,r.request.uri.query.indexOf("&output=json")-(r.request.uri.query.indexOf("cid=")+4)),
        date = moment(json.expiry.y+" "+json.expiry.m+" "+json.expiry.d,"YYYY M D"),
        dateFor = date.format("MM/DD/YYYY");
        underlying = json.underlying_price;
        if(expiriesAhead==0){
            data[dateFor] = [];
            for(var i = 0; i < json.calls.length; i++){
                var call = json.calls[i];
                if(call.p!="-"){
                    var optObj = {};
                    optObj.call = 1;
                    optObj.strike = parseFloat(call.strike);
                    optObj.price = parseFloat(call.p);
                    data[dateFor].push(optObj);
                };
            };
            for(var i = 0; i < json.puts.length; i++){
                var put = json.puts[i];
                if(put.p!="-"){
                    var optObj = {};
                    optObj.call = 0;
                    optObj.strike = parseFloat(put.strike);
                    optObj.price = parseFloat(put.p);
                    data[dateFor].push(optObj);
                };
            };
        }else{
            var expiry = json.expirations[expiriesAhead],
            chainURL = "https://www.google.com/finance/option_chain?cid="+underlying_id+"&expd="+expiry.d+"&expm="+expiry.m+"&expy="+expiry.y+"&output=json";
            request(chainURL,parseChain);
        };
    };
};

function parseChain(e,r,b){
    var json = jsonlite.parse(b),
    date = moment(json.expiry.y+" "+json.expiry.m+" "+json.expiry.d,"YYYY M D"),
    dateFor = date.format("MM/DD/YYYY");
    data[dateFor] = [];
    for(var i = 0; i < json.calls.length; i++){
        var call = json.calls[i];
        if(call.p!="-"){
            var optObj = {};
            optObj.call = 1;
            optObj.strike = parseFloat(call.strike);
            optObj.price = parseFloat(call.p);
            data[dateFor].push(optObj);
        };
    };
    for(var i = 0; i < json.puts.length; i++){
        var put = json.puts[i];
        if(put.p!="-"){
            var optObj = {};
            optObj.call = 0;
            optObj.strike = parseFloat(put.strike);
            optObj.price = parseFloat(put.p);
            data[dateFor].push(optObj);
        };
    };
};

function analyze(){
    console.log("Data download complete.");
    for(var date in data){
        for(var j = 0; j<changes.length; j++){
            var change = changes[j];
            upState = underlying*(1+(change/100));
            downState = underlying*(1-(change/100));
            var options = data[date];
            if(options.length>2){
                var Farr = [],
                Parr = [];
                process.stdout.write("Analyzing "+options.length+" options for "+date+" using "+decodeURI('%C2%B1')+change+"%...");
                probabilities[change] = {"down":[],"neutral":[],"up":[]};
                for(var i = 0; i < options.length; i++){
                    var option = options[i],
                    strike = option.strike,
                    price = option.price,
                    call = option.call;
                    Parr.push(price);
                    if(call){
                        var upVal = Math.max(upState-strike,0),
                        neuVal = Math.max(underlying-strike,0),
                        downVal = Math.max(downState-strike,0);
                    }else{
                        var upVal = Math.max(strike-upState,0),
                        neuVal = Math.max(strike-underlying,0),
                        downVal = Math.max(strike-downState,0);
                    };
                    var row = [downVal,neuVal,upVal];
                    Farr.push(row);
                };
                var range = [];
                for(var i = 0; i < Farr.length; i++){range.push(i);};
                var com = new cmb(range,3);
                com.each(
                    function(val){
                        var F = $M([Farr[val[0]],Farr[val[1]],Farr[val[2]]]),
                        P = $M([Parr[val[0]],Parr[val[1]],Parr[val[2]]]);
                        if(F.inv()){
                            var arrowPrices = F.inv().x(P).toArray(),
                            arrowFlat = [];
                            arrowFlat = arrowFlat.concat.apply(arrowFlat,arrowPrices);
                            var arrowMax = Math.max.apply(Math, arrowFlat),
                            arrowMin = Math.min.apply(Math, arrowFlat),
                            arrowSum = arrowFlat.reduce(function(a,b){return a+b;});
                            if(arrowMin>=0 && arrowMax>0 && arrowMax<=1 && arrowSum<=1){
                                var inducedProb = arrowFlat.map(function(num){return num/arrowSum;});
                                probabilities[change].down.push(inducedProb[0]);
                                probabilities[change].neutral.push(inducedProb[1]);
                                probabilities[change].up.push(inducedProb[2]);
                            };
                        };
                    }
                );
                results[change] = {"down":{},"neutral":{},"up":{}};
                results[change].solutions = probabilities[change].down.length;
                if(probabilities[change].down.length>=2){
                    results[change].down.min = Math.min.apply(Math, probabilities[change].down);
                    results[change].down.max = Math.max.apply(Math, probabilities[change].down);
                    results[change].down.std = standardDev(probabilities[change].down);
                    results[change].down.avg = (probabilities[change].down.reduce(function(a,b){return a+b;})/probabilities[change].down.length);
                    results[change].down.len = probabilities[change].down.length;
                };
                if(probabilities[change].neutral.length>=2){
                    results[change].neutral.min = Math.min.apply(Math, probabilities[change].neutral);
                    results[change].neutral.max = Math.max.apply(Math, probabilities[change].neutral);
                    results[change].neutral.std = standardDev(probabilities[change].neutral);
                    results[change].neutral.avg = (probabilities[change].neutral.reduce(function(a,b){return a+b;})/probabilities[change].neutral.length);
                    results[change].neutral.len = probabilities[change].neutral.length;
                };
                if(probabilities[change].up.length>=2){
                    results[change].up.min = Math.min.apply(Math, probabilities[change].up);
                    results[change].up.max = Math.max.apply(Math, probabilities[change].up);
                    results[change].up.std = standardDev(probabilities[change].up);
                    results[change].up.avg = (probabilities[change].up.reduce(function(a,b){return a+b;})/probabilities[change].up.length);
                    results[change].up.len = probabilities[change].up.length;
                };
                process.stdout.write('Complete.');
                process.stdout.write('\n');
            };
        };
    };
};

function print(){
    process.stdout.write('\n');
    console.log("Plus/Minus Percent,Date,Solutions,Down State,Down Min,Down Max,Down SD,Down Avg,Neutral State,Neutral Min,Neutral Max,Neutral SD,Neutral Avg,Up State,Up Min,Up Max,Up SD,Up Avg");
    for(var i = 1; i<21; i++){
        var change = i/2,
        result = results[change];
        if(result){
            if(result.down.avg && result.neutral.avg && result.up.avg){
                console.log(change+","+Object.keys(data)[0]+","+result.solutions+","+underlying*(1-(change/100))+","+result.down.min+","+result.down.max+","+result.down.std+","+result.down.avg+","+underlying+","+result.neutral.min+","+result.neutral.max+","+result.neutral.std+","+result.neutral.avg+","+underlying*(1+(change/100))+","+result.up.min+","+result.up.max+","+result.up.std+","+result.up.avg)
            };
        };
    };
    console.log("Done.");
};

function exitHandler(options, err) {
    if (options.cleanup){
        analyze();
        print();
        process.exit();
    };
    if (err){console.log(err.stack)};
    if (options.exit){process.exit();};
};
process.on('exit', exitHandler.bind(null,{cleanup:true}));
process.on('SIGINT', exitHandler.bind(null, {exit:true}));
process.on('uncaughtException', exitHandler.bind(null, {exit:true}));