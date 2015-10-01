var chart = AmCharts.makeChart("capital_structure_yearly_chart", {
    "type" : "serial",
    "dataLoader": {
        "url": "capital_structure_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "財務結構分析",
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
            "title" : "自有資本比率 (%)",
            "valueField" : "equity_ratio",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "負債比率 (%)",
            "valueField" : "liabilities_ratio",
            "bullet" : "square",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "實質負債比 (%)",
            "valueField" : "true_liabilities_ratio",
            "bullet" : "triangleUp",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]%</b></span>",
        },
        {
            "valueAxis": "right_axis",
            "type" : "line",
            "title" : "長期資金占固定資產比率",
            "valueField" : "long_term_capital_to_fixed_assets_ratio",
            "bullet" : "triangleDown",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
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
