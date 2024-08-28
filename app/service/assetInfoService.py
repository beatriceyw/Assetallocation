from app.utils import log_util
from app.dao import assetInfodao
from app.dto import assetInfoDto


def get_etf_detail(stock_name: str):
    response = assetInfodao.find_etf_detail(stock_name)

    return response
