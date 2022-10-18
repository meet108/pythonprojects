from base import db
from base.com.vo.category_vo import CategoryVO
from base.com.vo.product_vo import ProductVO
from base.com.vo.subcategory_vo import SubCategoryVO


class ProductDAO:
    def insert_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):
        product_vo_list = db.session.query(CategoryVO, SubCategoryVO,
                                           ProductVO).filter(
            CategoryVO.category_id == ProductVO.product_category_id).filter(
            SubCategoryVO.subcategory_id == ProductVO.product_subcategory_id).all()
        return product_vo_list
