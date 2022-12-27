
var calcString;

function set () {
    
    document.getElementById("inputBox").value = "Blop";

}

function updatedString(id){

    if (id != "undefined"){
        calcString = calcString + id;
        settInputText(calcString);
    }
    

}

function settInputText(value){
    document.getElementById("inputBox").value = value;
}
 
function resetting(){

    calcString = '';
    settInputText('')


}