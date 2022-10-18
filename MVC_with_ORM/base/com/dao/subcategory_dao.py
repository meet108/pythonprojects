from base import db
from  base.com.vo.category_vo import CategoryVO
from base.com.vo.subcategory_vo import SubCategoryVO


class SubcategoryDAO:
    def insert_subcategory(self, subcatgory_vo):
        db.session.add(subcatgory_vo)
        db.session.commit()

    def view_subcategory(self):
        subcategory_vo_list = db.session.query(SubCategoryVO, CategoryVO).join(
            CategoryVO,
            SubCategoryVO.subcategory_category_id == CategoryVO.category_id).all()
        return subcategory_vo_list

    def delete_subcategory(self, subcategory_vo):
        subcategory_vo_obj = subcategory_vo.query.get(
            subcategory_vo.subcategory_id)
        db.session.delete(subcategory_vo_obj)
        db.session.commit()

    def edit_subcategory(self, subcategory_vo):
        subcategory_vo_list = SubCategoryVO.query.filter_by(
            subcategory_id=subcategory_vo.subcategory_id).all()
        return subcategory_vo_list

    def update_subcategory(self, subcategory_vo):
        db.session.merge(subcategory_vo)
        db.session.commit()

    def view_ajax_subcategory_product(self, subcategory_vo):
        subcategory_vo_list = SubCategoryVO.query.filter_by(
            subcategory_category_id=subcategory_vo.subcategory_category_id
        ).all()
        return subcategory_vo_list
