import akshare as ak
from flask import Flask, jsonify, request

stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
print(stock_individual_info_em_df)



app = Flask(__name__)


# 定义一个 GET 路由
@app.route('/api/stock/individual', methods=['GET'])
def get_stock_individual():
    return jsonify({"code": 200, "data": stock_individual_info_em_df.to_dict()})


# 启动服务
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


