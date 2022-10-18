from flask import render_template, request, redirect

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO
from base.com.dao.subcategory_dao import SubcategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO


@app.route('/admin/load_subcategory')
def load_subcategory():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('admin/addSubCategory.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("ADD SUBCATEGORY EXCEPTION")
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/insert_subcategory', methods=['POST'])
def insert_subcategory():
    try:
        subcategory_id = request.form.get('subcategoryCategoryId')
        subcategory_name = request.form.get('subcategoryName')
        subcategory_description = request.form.get('subcategoryDescription')

        subcategory_dao = SubcategoryDAO()
        subcategory_vo = SubCategoryVO()

        subcategory_vo.subcategory_category_id = subcategory_id
        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description

        subcategory_dao.insert_subcategory(subcategory_vo)
        return redirect('/admin/load_subcategory')

    except Exception as ex:
        print("Insert Subcategory Exception")
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/view_subcategory', methods=['GET'])
def admin_view_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_dao.view_subcategory()
        return render_template("admin/viewSubCategory.html",
                               subcategory_vo_list=subcategory_dao.view_subcategory())
    except Exception as ex:
        print("View SubCategory Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/delete_subcategory', methods=['GET'])
def admin_delete_subcategory():
    try:
        subcategory_id = request.args.get('subcategoryId')
        subcategory_vo = SubCategoryVO()
        # subcategory_vo.subcategory_id = subcategory_id

        subcategory_dao = SubcategoryDAO()

        subcategory_vo.subcategory_id = subcategory_id
        subcategory_dao.delete_subcategory(subcategory_vo)
        return redirect('/admin/view_subcategory')

    except Exception as ex:
        print("Delete SubCategory Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/edit_subcategory', methods=['GET'])
def admin_edit_subcategory():
    try:
        subcategory_id = request.args.get('subcategoryId')
        subcategory_vo = SubCategoryVO()
        subcategory_vo.subcategory_id = subcategory_id

        subcategory_dao = SubcategoryDAO()
        subcategory_vo_list = subcategory_dao.edit_subcategory(subcategory_vo)
        return render_template("admin/editSubCategory.html",
                               data=subcategory_vo_list)
    except Exception as ex:
        print("Edit SubCategory Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/update_subcategory', methods=['POST'])
def admin_update_subcategory():
    try:
        category_id = request.form.get('categoryId')
        subcategory_id = request.form.get('subcategoryId')
        SubCategoryName = request.form.get('subcategoryName')
        SubCategoryDescription = request.form.get('subcategoryDescription')
        category_vo = CategoryVO()
        category_vo.category_id = category_id
        subcategory_vo = SubCategoryVO()
        subcategory_vo.subcategory_id = subcategory_id
        subcategory_vo.subcategory_name = SubCategoryName
        subcategory_vo.subcategory_description = SubCategoryDescription
        subcategory_dao = SubcategoryDAO()
        subcategory_dao.update_subcategory(subcategory_vo)
        return redirect('/admin/view_subcategory')

    except Exception as ex:
        print("Update SubCategory Exception", ex)
        return render_template('admin/error.html', ex=ex)
