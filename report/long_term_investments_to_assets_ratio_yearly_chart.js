var chart = AmCharts.makeChart("long_term_investments_to_assets_ratio_yearly_chart", {
    "type" : "serial",
    "dataLoader": {
        "url": "cash_flow_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "長期投資占總資產比率",
        },
    ],
    "numberFormatter" : {
        "precision" : 0, 
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
            "title" : "長期投資占總資產比率 (%)",
            "valueField" : "long_term_investments_to_assets_ratio",
            "bullet" : "round",
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
