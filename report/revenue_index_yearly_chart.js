var chart = AmCharts.makeChart("revenue_index_yearly_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "revenue_index_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "五大盈餘指標",
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
    ],
    "graphs" : [
        {
            "valueAxis": "left_axis",
            "type" : "column", 
            "title" : "存貨指標",
            "valueField" : "inventory_index",
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "column",
            "title" : "應收帳款指標",
            "valueField" : "accounts_receivable_index",
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "column",
            "title" : "營業毛利指標",
            "valueField" : "gross_profit_index",
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "column",
            "title" : "銷管費用指標",
            "valueField" : "selling_and_administrative_expenses_index",
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "column",
            "title" : "應付帳款指標",
            "valueField" : "accounts_payable_index",
            "fillAlphas" : 0.6,
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
