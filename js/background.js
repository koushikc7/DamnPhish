var results = {};
var legitimatePercents = {};
var isPhish = {};


function fetchLive(callback) {
  $.getJSON("https://raw.githubusercontent.com/koushikc7/MajorProj/main/classifier.json", function(data) {
      chrome.storage.local.set({cache: data, cacheTime: Date.now()}, function() {
          callback(data);
      });
  });
}

function fetchCLF(callback) {
  chrome.storage.local.get(['cache', 'cacheTime'], function(items) {
      if (items.cache && items.cacheTime) {
          return callback(items.cache);
      }
      fetchLive(callback);
  });
}

function classify(tabId, result) {
  
  if(result.length != 0) {
    var X = [];
    X[0] = [];
    for(var key in result) {
        X[0].push(parseInt(result[key]));
    }
    console.log(result);
    console.log(X);
    fetchCLF(function(clf) {
      var rf = random_forest(clf);
      y = rf.predict(X);
      console.log(y[0]);
      if(y[0][0]) {
        isPhish[tabId] = true;
       
      } else {
        isPhish[tabId] = false;
      }
    });
  }

}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  results[sender.tab.id]=request;
  classify(sender.tab.id, request);
  sendResponse({received: "result"});
});