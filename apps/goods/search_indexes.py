# 定义索引类
from haystack import indexes
# 导入要检索的模型类
from goods.models import GoodsSKU


# 指定对某个类的某些数据建立索引
# 索引类名格式：模型类名+Index
class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段 use_template=True指定根据表中哪些字段建立索引文件的说明放在一个文件中,即/template/search/indexes/goods/goodssku_text.txt
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 返回模型类
        return GoodsSKU

    # 建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()