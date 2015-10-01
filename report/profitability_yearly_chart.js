var chart = AmCharts.makeChart("profitability_yearly_chart", {
    "type" : "serial",
    "dataLoader": {
        "url": "profitability_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "獲利能力",
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
    ],
    "graphs" : [
        {
            "valueAxis": "left_axis",
            "type" : "line", 
            "title" : "毛利率 (%)",
            "valueField" : "gross_profit_margin",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "營業利益率 (%)",
            "valueField" : "operating_profit_margin",
            "bullet" : "square",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "稅前純益率 (%)",
            "valueField" : "net_profit_before_tax_margin",
            "bullet" : "triangleUp",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "稅後純益率 (%)",
            "valueField" : "net_profit_margin",
            "bullet" : "diamond",
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
