function getStockSymbol() {
    var url = purl(location.search); 
    return url.param('stock_symbol') || '1101';
}

function makeDiv(period) {
    var divPieces = ['dupont', '_', period || 'yearly', '_', 'chart'];
    return divPieces.join('');
}

function makeDupontDataPath(stockSymbol, period) {
    var pathPieces = ['chart/dupont/', period || 'yearly', '/', stockSymbol, '.json'];
    return pathPieces.join('');
}

function makeDupontChart(stockSymbol, period) {
    var div = makeDiv(period);
    var config = {
        "type" : "serial",
        "dataLoader": {
            "url": makeDupontDataPath(stockSymbol, period),
            "format": "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size": 15,
                "text": "杜邦分析",
            },
        ],
        "numberFormatter" : {
            "precision" : 2, 
        },
        "valueAxes" : [
            {
                "id" : "left_axis",
                "axisThickness" : 2,
                "axisAlpha" : 1,
                "position" : "left",
            }, 
            {
                "id" : "minor_left_axis",
                "axisThickness" : 2,
                "gridAlpha" : 0,
                "offset" : 50,
                "axisAlpha" : 1,
                "position" : "left",
                "title" : "%",
            },
            {
                "id" : "right_axis",
                "axisThickness" : 2,
                "gridAlpha" : 0,
                "axisAlpha" : 1,
                "position" : "right",
            },
        ],
        "graphs" : [
            {
                "valueAxis": "left_axis",
                "type" : "line", 
                "title" : "ROE (%)",
                "valueField" : "roe",
                "bullet" : "round",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
            },
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "ROA (%)",
                "valueField" : "roa",
                "bullet" : "square",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
            },
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "純益率 (%)",
                "valueField" : "ros",
                "bullet" : "triangleUp",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
            },
            {
                "valueAxis": "minor_left_axis",
                "type" : "line",
                "title" : "總資產週轉率 (%)",
                "valueField" : "ato",
                "bullet" : "triangleDown",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
            },        
            {
                "valueAxis": "right_axis",
                "type" : "line",
                "title" : "權益乘數",
                "valueField" : "equity_multiplier",
                "bullet" : "diamond",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
        ],
        "legend" : {
            "align" : "center",
            "valueAlign" : "left",
        },
        "chartCursor" : {
            "zoomable" : false, // as the chart displayes not too many values, we disabled zooming
            "cursorPosition": "mouse",
        },
        "balloon": {
            "borderThickness": 1,
            "shadowAlpha": 0
        },
    };
    AmCharts.makeChart(div, config);
}

var stockSymbol = getStockSymbol();
makeDupontChart(stockSymbol, 'yearly');
makeDupontChart(stockSymbol, 'quarterly');

//var dataPathPiece = ['./yuantacat/data/report/capital_structure/yearly/', stockSymbol, '.json'];
//console.log(dataPathPiece.join(''));
