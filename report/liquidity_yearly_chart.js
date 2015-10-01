var chart = AmCharts.makeChart("liquidity_yearly_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "liquidity_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "償債能力",
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
            "title" : "流動比率 (%)",
            "valueField" : "current_ratio",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "速動比率 (%)",
            "valueField" : "quick_ratio",
            "bullet" : "square",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "right_axis",
            "type" : "line",
            "title" : "利息保障倍數",
            "valueField" : "interest_protection_multiples",
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
});
