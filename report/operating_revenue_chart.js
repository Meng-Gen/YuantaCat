var chart = AmCharts.makeChart("operating_revenue_chart", {
    "type" : "serial",
    "dataLoader": {
        "url": "operating_revenue_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "每月營業收入分析",
        },
    ],
    "numberFormatter" : {
        "precision" : 0, 
    },
    "valueAxes" : [
        {
            "id" : "left_axis",
            "axisThickness" : 2,
            "maximum" : 20,
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
            "valueAxis": "right_axis",
            "type" : "column", 
            "title" : "每月營收",
            "valueField" : "operating_revenue",
            "fillAlphas" : 0.1,
            "hidden" : true,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "累積營收年增率 (%)",
            "valueField" : "accumulated_operating_revenue_yoy",
            "fillAlphas" : 0.5,
            "bullet" : "triangleUp",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "right_axis",
            "type" : "line",
            "title" : "長期平均線 (12ma)",
            "valueField" : "long_term_average",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "right_axis",
            "type" : "line",
            "title" : "短期平均線 (3ma)",
            "valueField" : "short_term_average",
            "bullet" : "square",
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
