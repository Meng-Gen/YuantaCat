var chart = AmCharts.makeChart("dupont_yearly_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "dupont_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "杜邦分析",
        },
    ],
    "categoryAxis" : {
        "gridAlpha" : 0.07,
        "axisColor" : "#DADADA",
        "startOnAxis" : true,
    },
    "numberFormatter" : {
        "precision" : 2, 
    },
    "valueAxes" : [
        {
            "id" : "left_axis",
            "axisThickness" : 2,
            "gridAlpha" : 0,
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
            "title": "%",
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
});
