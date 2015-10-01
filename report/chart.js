function getStockSymbol() {
    var url = purl(location.search); 
    return url.param('stock_symbol') || '1101';
}

function makeTitleCommentText(period) {
    if (period === 'yearly') {
        return '(年)';
    } else if (period === 'quarterly') {
        return '(季)';
    } else {
        return '';
    }
}

function makeDivByPeriod(chartText, period) {
    var divPieces = [chartText, '_', period || 'yearly', '_', 'chart'];
    return divPieces.join('');
}

function makeDiv(chartText) {
    var divPieces = [chartText, '_', 'chart'];
    return divPieces.join('');
}

function makeDataPathByPeriod(chartText, stockSymbol, period) {
    var pathPieces = ['chart', '/', chartText, '/', period || 'yearly', '/', stockSymbol, '.json'];
    return pathPieces.join('');
}

function makeDataPath(chartText, stockSymbol) {
    var pathPieces = ['chart', '/', chartText, '/', stockSymbol, '.json'];
    return pathPieces.join('');
}

function makeCapitalIncreaseHistoryChart(stockSymbol) {
    var div = makeDiv('capital_increase_history');
    var config = {
        "type" : "serial",
        "dataLoader": {
            "url": makeDataPath('capital_increase_history', stockSymbol),
            "format": "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size": 15,
                "text": "股本形成過程及比例",
            },
        ],
        "numberFormatter" : {
            "precision" : 2, 
        },    
        "valueAxes" : [
            {
                "title" : "percent", // this line makes the chart "stacked"
                "stackType" : "100%",
            },
        ],
        "graphs" : [
            {
                "type" : "line", 
                "title" : "現金增資",
                "valueField" : "capital_increase_by_cash",
                "fillAlphas" : 0.6, 
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "type" : "line",
                "title" : "盈餘轉增資",
                "valueField" : "capital_increase_by_earnings",
                "fillAlphas" : 0.6,
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "type" : "line",
                "title" : "公積及其他",
                "valueField" : "capital_increase_by_surplus",
                "fillAlphas" : 0.6,
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
        ],
        "legend" : {
            "align" : "center",
            "valueText" : "[[value]] ([[percents]]%)",
            "valueAlign" : "left",
        },
        "chartCursor" : {
            "zoomable" : false, 
            "cursorPosition": "mouse",
        },
        "balloon": {
            "borderThickness": 1,
            "shadowAlpha": 0
        },
    };
    AmCharts.makeChart(div, config);
}

function makeCapitalStructureChart(stockSymbol, period) {
    var div = makeDivByPeriod('capital_structure', period);
    var config = {
        "type" : "serial",
        "dataLoader": {
            "url": makeDataPathByPeriod('capital_structure', stockSymbol, period),
            "format": "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size": 15,
                "text": "財務結構分析" + makeTitleCommentText(period),
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
            "zoomable" : false, 
            "cursorPosition": "mouse",
        },
        "balloon": {
            "borderThickness": 1,
            "shadowAlpha": 0
        },
    };
    AmCharts.makeChart(div, config);
}

function makeCashFlowChart(stockSymbol, period) {
    var div = makeDivByPeriod('cash_flow', period);
    var config = {
        "type" : "serial",
        "dataLoader": {
            "url": makeDataPathByPeriod('cash_flow', stockSymbol, period),
            "format": "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size": 15,
                "text": "現金流量表分析重點" + makeTitleCommentText(period),
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
            }, 
            {
                "id" : "minor_left_axis",
                "axisThickness" : 2,
                "gridAlpha" : 0,
                "offset" : 50,
                "axisAlpha" : 1,
                "position" : "left",
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
                "title" : "營運活動之現金流量",
                "valueField" : "cash_flow_from_operating_activities",
                "bullet" : "round",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "投資活動之現金流量",
                "valueField" : "cash_flow_from_investing_activities",
                "bullet" : "square",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "理財活動之現金流量",
                "valueField" : "cash_flow_from_financing_activities",
                "bullet" : "triangleUp",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "自由現金流量",
                "valueField" : "free_cash_flow",
                "bullet" : "triangleDown",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },    
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "累積自由現金流量",
                "valueField" : "accumulated_free_cash_flow",
                "bullet" : "diamond",
                "fillAlphas" : 0.2,
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
                "lineColor": "#04D215",
                "negativeLineColor": "#D1655D",
            },    
        ],
        "legend" : {
            "align" : "center",
            "valueAlign" : "left",
        },
        "chartCursor" : {
            "zoomable" : false,
            "cursorPosition": "mouse",
        },
        "balloon": {
            "borderThickness": 1,
            "shadowAlpha": 0
        },
    };
    AmCharts.makeChart(div, config);
}

function makeCccChart(stockSymbol, period) {
    var div = makeDivByPeriod('ccc', period);
    var config = {
        "type" : "serial",
        "dataLoader" : {
            "url" : makeDataPathByPeriod('profitability', stockSymbol, period),
            "format" : "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size" : 15,
                "text" : "現金轉換循環" + makeTitleCommentText(period),
            },
        ],
        "numberFormatter" : {
            "precision" : 1, 
        },
        "valueAxes" : [
            {
                "id" : "left_axis",
                "axisThickness" : 2,
                "axisAlpha" : 1,
                "position" : "left",
                "title" : "Days",
            }, 
        ],
        "graphs" : [
            {
                "valueAxis" : "left_axis",
                "type" : "line", 
                "title" : "平均銷貨天數",
                "valueField" : "dio",
                "bullet" : "round",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "valueAxis" : "left_axis",
                "type" : "line",
                "title" : "平均應收帳款收現天數",
                "valueField" : "dso",
                "bullet" : "square",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "valueAxis": "left_axis",
                "type" : "line",
                "title" : "平均應付帳款付款天數",
                "valueField" : "dpo",
                "bullet" : "triangleUp",
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
            {
                "valueAxis" : "left_axis",
                "type" : "line",
                "title" : "現金轉換循環",
                "valueField" : "ccc",
                "bullet" : "diamond",
                "fillAlphas" : 0.1,
                "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            },
        ],
        "legend" : {
            "align" : "center",
            "valueAlign" : "left",
        },
        "chartCursor" : {
            "zoomable" : false, 
            "cursorPosition" : "mouse",
        },
        "balloon" : {
            "borderThickness" : 1,
            "shadowAlpha" : 0
        },
    };
    AmCharts.makeChart(div, config);
}

function makeDupontChart(stockSymbol, period) {
    var div = makeDivByPeriod('dupont', period);
    var config = {
        "type" : "serial",
        "dataLoader": {
            "url": makeDataPathByPeriod('dupont', stockSymbol, period),
            "format": "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size": 15,
                "text": "杜邦分析" + makeTitleCommentText(period),
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
            "zoomable" : false, 
            "cursorPosition": "mouse",
        },
        "balloon": {
            "borderThickness": 1,
            "shadowAlpha": 0
        },
    };
    AmCharts.makeChart(div, config);
}

function makeRevenueIndex(stockSymbol, period) {
    var div = makeDivByPeriod('revenue_index', period);
    var config = {
        "type" : "serial",
        "dataLoader": {
            "url": makeDataPathByPeriod('revenue_index', stockSymbol, period),
            "format": "json"
        },
        "categoryField" : "date",
        "titles" : [
            {
                "size": 15,
                "text": "五大盈餘指標" + makeTitleCommentText(period),
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
            "zoomable" : false,
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
makeCapitalStructureChart(stockSymbol, 'yearly');
makeCapitalStructureChart(stockSymbol, 'quarterly');
makeCapitalIncreaseHistoryChart(stockSymbol);
makeCashFlowChart(stockSymbol, 'yearly');
makeCashFlowChart(stockSymbol, 'quarterly');
makeCccChart(stockSymbol, 'yearly');
makeCccChart(stockSymbol, 'quarterly');
makeDupontChart(stockSymbol, 'yearly');
makeDupontChart(stockSymbol, 'quarterly');
makeRevenueIndex(stockSymbol, 'yearly');
makeRevenueIndex(stockSymbol, 'quarterly');
