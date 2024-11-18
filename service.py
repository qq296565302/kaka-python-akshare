# pip install PyExecJS

import akshare as ak
from flask import Flask, jsonify, request




app = Flask(__name__)


# 个股信息查询
@app.route('/api/stock/individual', methods=['GET'])
def get_stock_individual():
    symbol = request.args.get('symbol')
    if symbol is None:
        return jsonify({"code": 500, "message": "Missing symbol parameter"})

    stock_individual_info_em_df = ak.stock_individual_info_em(symbol=symbol)
    return jsonify({"code": 200, "data": stock_individual_info_em_df.to_dict(), "message": "success"})

# 行情报价
@app.route('/api/stock/quote', methods=['GET'])
def get_stock_quote():
    symbol = request.args.get('symbol')
    if symbol is None:
        return jsonify({"code": 500, "message": "Missing symbol parameter"})

    stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol=symbol)
    return jsonify({"code": 200, "data": stock_bid_ask_em_df.to_dict(), "message": "success"})

# 启动服务
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)


