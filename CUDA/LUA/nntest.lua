require 'torch'
require 'nn'

-- Command line parameters
cmd = torch.CmdLine()
cmd:text()
cmd:text('Options for my NN')
cmd:option('-units',10,'units in the hidden layer')
cmd:option('-learningRate',0.01,'learning rate')
cmd:option('-trainingPerc',0.7,'training percentage')
cmd:option('-csv',"eth_dat.csv",'csv file')
cmd:option('-header',true,'csv has header')
-- etc...
cmd:text()
opt = cmd:parse(arg)


-- Fully connected feed-forward network container
mlp = nn.Sequential()

-- Data requirement: lua table with method size()
-- Method to read CSV
function string:splitAtCommas()
    local sep, values = ",", {}
    local pattern = string.format("([^%s]+)", sep)
    self:gsub(pattern, function(c) values[#values+1] = c end)
    return values
end

math.randomseed( os.time() )
function shuffleTable( t )
    assert( t, "shuffleTable() expected a table, got nil" )
    local copy = {}
    local iterations = #t
    local shuffleIdx = torch.randperm(iterations)
    local j
    
    for i = 1, iterations, 1 do
        j = shuffleIdx[i]
        copy[i] = t[j]
    end
    function copy:size() return t:size() end -- the requirement mentioned
    function copy:length() return t:length() end
    return copy
end

function subsetTable(t,startIndex,endIndex)
    assert( t, "subsetTable() expected a table, got nil" )
    local copy = {}
    local iterations = #t
    local j = 0
    
    for i = startIndex, endIndex, 1 do
            j = j + 1
        copy[j] = t[i]
    end
    function copy:size() return j end -- the requirement mentioned
    function copy:length() return t:length() end
    return copy
end

function loadData(dataFile,header)
    local dataset = {}
    local length = 0
    local i = 1
    for line in io.lines(dataFile) do
        if header == true then
            header = false
        else
            local values = line:splitAtCommas()
            local y = torch.Tensor(1)
            y[1] = values[#values] + 1 -- the target class is the last number in the line
            values[#values] = nil
            length = #values
            local x = torch.Tensor(values) -- the input data is all the other numbers
            dataset[i] = {x, y}
            i = i + 1
        end
    end
    function dataset:size() return (i - 1) end -- the requirement mentioned
    function dataset:length() return length end
    return dataset
end

dataset = loadData(opt.csv,opt.header)
randset = shuffleTable(dataset)
trainingCut = math.floor(dataset:size()*opt.trainingPerc)
trainingSet = subsetTable(randset,1,trainingCut)
testingSet = subsetTable(randset,trainingCut+1,randset:size())
print("Total obs: ",dataset:size())
print("Total vars: ",dataset:length())
print("Training obs: ",trainingSet:size())
print("Testing obs: ",testingSet:size())

-- Using tanh as transfer function for non-linearlity
inputSize = trainingSet:length()
hiddenLayer1Size = opt.units
hiddenLayer2Size = opt.units
hiddenLayer3Size = opt.units

mlp:add(nn.Linear(inputSize,hiddenLayer1Size))
mlp:add(nn.HardTanh())
mlp:add(nn.Linear(hiddenLayer1Size,hiddenLayer2Size))
mlp:add(nn.HardTanh())
--mlp:add(nn.Linear(hiddenLayer2Size,hiddenLayer3Size))
--mlp:add(nn.HardTanh())

-- outputs
nclasses = 2

mlp:add(nn.Linear(hiddenLayer2Size,nclasses))
mlp:add(nn.LogSoftMax())

-- Print
-- print(mlp)
-- out = mlp:forward(torch.randn(1,10))
-- print(out)

-- Training with SGD and negative log-likelihood criterion

criterion = nn.ClassNLLCriterion()
trainer = nn.StochasticGradient(mlp,criterion)
trainer.learningRate = opt.learningRate

-- Training!
trainer:train(trainingSet)

-- Prediction
-- x = torch.randn(43)
-- y = mlp:forward(x)
-- print(y)

-- Accuracy
function argmax(v)
  local maxvalue = torch.max(v)
  for i=1,v:size(1) do
    if v[i] == maxvalue then
      return i
    end
  end
end

tot = 0
pos = 0
for i = 1, testingSet:size(), 1 do
    local x = testingSet[i][1]
    local y = testingSet[i][2]
    local prediction = argmax(mlp:forward(x))
    if math.floor(prediction) == math.floor(y[1]) then
        pos = pos + 1
    end
    tot = tot + 1
end
print("Accuracy(%) is " .. pos/tot*100)

-- Save for later
torch.save('model.th', mlp)
-- mlp2 = torch.load('model.th')
