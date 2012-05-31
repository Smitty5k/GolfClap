//The maximum allowed score value
var MAX_SCORE_VALUE=10;
//The minimum allowed score value
var MIN_SCORE_VALUE=0;

/**
 * Start watching the table once the document loads.
 */
$(document).ready(function() {
    $('#table-design').bind('input', function() {
        $("#total-1").html(sumOfColumns("table-design", 3, true));
        $("#total-2").html(sumOfColumns("table-design", 4, true));
        $("#total-3").html(sumOfColumns("table-design", 5, true));
        $("#total-4").html(sumOfColumns("table-design", 6, true));
    });
});

/**
 * Ensures the input is an int and within range
 * @param inputValue the input value
 * @return {*} the valid
 */
function scrubInput(inputValue){
    //if it's not an int return 0
    if(!/^\d{0,2}$/.test(inputValue)){
        return 0;
    }
    //if it's an int and it's greater than max allowed
    //return max allowed
    if(inputValue > MAX_SCORE_VALUE){
        return MAX_SCORE_VALUE;
    }
    //if it's an int and less than min allowed
    //return min allowed.
    if(inputValue < MIN_SCORE_VALUE){
        return MIN_SCORE_VALUE;
    }
    return inputValue;
}

/**
 * Sum the columns in the table and index provided.
 * @param tableID the id of the table to process
 * @param columnIndex the index of the column to process
 * @param hasHeader flag to indicate that the column has a header or not
 * @return {Number} the sum of the column.
 */
function sumOfColumns(tableID, columnIndex, hasHeader) {
    //the total to be returned.
    var tot = 0;
    //the current value.
    var myVal = 0;
    //the id of the current value
    var idValue="";
    //for the provided table get specified column from each row
    $("#" + tableID + " tr" + (hasHeader ? ":gt(1)" : ""))
        .children("td:nth-child(" + columnIndex + ")")
        .each(function() {
            //get the ID value for this row
            idValue = $(this).children("input").attr("id");
            //get the input value for this row
            myVal = $(this).children("input").val();
            //scrub the input from row/column
            myVal=scrubInput(myVal);
            //don't add the total column to the total
            if(!(typeof idValue === "undefined"))
            {
                //set the new value in the field
                $(this).children("input").val(myVal);
                tot += parseInt(myVal);
            }
        });
    return tot;
}

