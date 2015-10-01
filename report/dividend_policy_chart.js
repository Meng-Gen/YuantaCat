var chart = AmCharts.makeChart("dividend_policy_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "dividend_policy_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "股利政策",
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
            "id" : "right_axis",
            "axisThickness" : 2,
            "gridAlpha" : 0,
            "axisAlpha" : 1,
            "position" : "right",
            "title": "%",
        },
    ],
    "graphs" : [
        {
            "valueAxis": "left_axis",
            "type" : "line", 
            "title" : "現金股利",
            "valueField" : "cash_dividends",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "股票股利",
            "valueField" : "stock_dividends",
            "bullet" : "square",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "盈餘配股",
            "valueField" : "stock_dividends_from_retained_earnings",
            "bullet" : "triangleUp",
            "hidden" : true,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "公積配股",
            "valueField" : "stock_dividends_from_capital_reserve",
            "bullet" : "diamond",
            "hidden" : true,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "right_axis",
            "type" : "line",
            "title" : "員工配股率 (%)",
            "valueField" : "employee_stock_bonus_ratio",
            "type" : "column",
            "fillAlphas" : 0.1,
//"bullet" : "triangleDown",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
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
});
