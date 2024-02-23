var background = chrome.extension.getBackgroundPage();
var result1 = {
    "1":"Phishing",
    "-1":"Safe"
};
var colors = {
    "-1":"#58bc8a",
    "1":"#ff8b66"
};
var featureList = document.getElementById("features");

chrome.tabs.query({ currentWindow: true, active: true }, function(tabs){
    var result = background.results[tabs[0].id];
    var isPhish = background.isPhish[tabs[0].id];
    
var i=1;
    for(var key in result){
        var newFeature = document.createElement("li");
        console.log(key);
        var a= key
        a+=": "
        a+=result1[result[key]]
        newFeature.textContent = i;
        newFeature.textContent += ". "
        newFeature.textContent += a;
        //newFeature.textContent +=colors[result[key]];
        //newFeature.className = "rounded";
        //newFeature.style.background="#ff7b66";
        
        newFeature.style.color="black";
        newFeature.textContent += "\n\n";
        featureList.appendChild(newFeature);
        i+=1
    }
    
    var d="";
    if( result[key]==-1){
        d+="Safe";
    }
    else{
        d+="Phishing";
    }
    $("#site_score").css("color",colors[result[key]]);
    $("#site_score").text(d);
    
});

