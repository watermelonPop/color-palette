# color-pallete

Simple html/css/javascript project to work as a functional color pallete creator. 


## Getting Started

Running the files or going to https://watermelonpop.github.io/color-pallete/, should show a website with 3 color swatches, each with a shade selector, a lock button, and an x button. Below these swatches will be an add button and a generate button. Each swatch also displays the hex code and color name, along with a color wheel element. The add button adds another swatch to the pallete, and the generate button changes out the swatches for a new one. The shade selector allows you to filter the colors of a specified swatch(ie if you only want red shades, etc.) But it can be left at the default state of "all shades". The lock button allows you to save colors you want to keep in your pallete, while generating another color for the "unlocked" swatches. The x button allows you to get rid of a color swatch(ie you only want 2 swatches rather than 3). The color wheel element allows the user to change the shade to a specified hex code or rgb values. It also comes with a color bar and a transparency bar. This element allows the user to copy the hex code of each swatch.

## Usage

Uses bootstrap, coloris, and fontawesome as helpers for our website. Bootstrap for css purposes, coloris for the color wheel functionality, and fontawesome for the icons used in the project.

## Coding Checks
- On load, the website should show 3 random swatches.
- Clicking on the shade selector should have a dropdown menu of color options, which will filter the shades generated for the current swatch. 
- Clicking the add button should add another column with a randomized swatch.
- Clicking the generate buttons should change each unlocked swatch in the pallete. Should check if a filter has been chosen from the shade selector, and proceed accordingly.
- Clicking on the color wheel box should open the color wheel and allow the user to change the shade of the current swatch to a specified color.
- Clicking the lock icon should lock the current shade in the pallete, and clicking generate should NOT change the locked swatch.
- Clicking the x icon should delete the column and swatch inside it. 

## Global Variables
```javascript
var numColors = 0;
  // Keeps track of the number of swatches in the pallete.
  // Should be updated when adding or deleting swatches
var locked = [];
  // Array of true/false booleans of each swatch, and whether it's locked or not.
  // this must be updated when locking or unlocking a swatch
let colors = [[['RED', '#D0312D'], ['CHERRY RED', '#990F02'], ['ROSE', '#E3242B'],...]]]
  // Array of colors taken from the output of the python file inside the color-list folder, 'list.py'. 
      // list of txt color files copy and pasted from https://www.color-meanings.com/list-of-colors-names-hex-codes/
    // inner arrays are of the color name and the hex code
    // second inner arrays separate these innermost arrays into color(red, pink, etc.)
```
## Useful helper functions used: 
```javascript
function getRandomColor(x){
  // input is integer x, representing the which filter to place
  // if x=-1, this means any shade can be chosen
  // any other x means there's a color filter on the swatch
  //outputs an innermost array of global var colors, using  Math.Random()
}
function add(){
  // Adds a swatch to the pallete using innerHTML and getRandomColor()
}
function x(c){
  // deletes a swatch from the pallete using removeChild(){
  // then shifts the class name instances down (if deleting the first swatch, 
  // the second swatch should become the first swatch, take on its classname, etc.)
}
function shiftDivs(cn){
  // input is the integer number of the swatch to be deleted
  // For every swatch after the deleted one, shift the class names down
  //make sure to update numColors and locked
}
function lock(x){
  // changes the lock image to be "unlocked" or "locked"
  // updates global var locked
}
function randomThree(){
  // uses the add() function to display 3 random swatches on load
}
function changeColor(c, el){
  //  Changes the swatch color specified by the user in the color wheel element
  // no longer displays color name, just hex code
}
```
## Main Function - generate()
The function gets the elements that we want to write to, and the select elements from the shade select. Loops through every swatch, checks if it's locked. If unlocked, use getRandomColor() to get a new shade for each swatch. When getting random color, check the dropdown status of the swatch, and act accordingly. Then use innerHTML to change each swatch.

```javascript
function generate(){
        var dropdowns = document.getElementsByClassName("selectDrops");
        var toWrite = document.getElementsByClassName("outerCard");
        for(let i = 0; i < dropdowns.length; i++){
                if(locked[i] == false){
                        let randColor;
                        if(dropdowns[i].value == '0'){
                                randColor = getRandomColor(-1);
                        }else{
                                randColor = getRandomColor(parseInt(dropdowns[i].value)-1)
                        }
                        toWrite[i].innerHTML = '<div class="cardBack" style="background-color:' + randColor[1] + ';"><div class="card" id="firstColor"><div class="cardImg" style="background-color:' + randColor[1] + ';"></div><div class="card-body"><div class="clr-field card-title" style ="color: ' + randColor[1] + ';"><button class = "square" type="button" aria-labelledby="clr-open-label">::after</button><input type="text" class="coloris instance' + (i+1) + '" value="' + randColor[1] + '"></div><p class="card-text">' + randColor[0] + '</p><img src="unlocked.png" class="icon instance' + (i+1) + '" onclick="lock(' + (i+1) + ')"><br><br><button class="x instance' + numColors + '" onclick="x(this)">X</button></div></div></div>';
                }
        }
}
```
